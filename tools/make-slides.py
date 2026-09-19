"""Genera la presentación que el docente proyecta, una por actividad.

Copia autónoma del generador del sitio de Protobject (`new-static-site/tools/make-slides.py`,
importada el 19-09-2026). Desde entonces nuestras actividades y las del sitio siguen caminos
distintos: estas son las versiones para la equivalencia con micro:bit. El cuerpo es el del
sitio; cambia solo lo que se lee y dónde se escribe:

- lee las 17 actividades de `activities.json`, en ese orden: `_activities/<slug>.es.md`
  (nunca otros archivos de `_activities/`);
- los medios se nombran `src/<actividad>/<archivo>` y en disco están en ese mismo lugar;
- escribe `ppt/<slug>.es.pptx`; la caché de medios va en `tools/media-cache/` (no se versiona).

    python tools/make-slides.py                    # las que faltan
    python tools/make-slides.py 02.1 16.7          # solo estas, por fragmento del nombre
    python tools/make-slides.py --force 02.1       # regenerarla aunque exista

La diapositiva del programa es una captura de `app.protobject.com/generate?equivalent-…`,
que carga el `.ptj` PUBLICADO en fond.protobject.com: si un programa cambia, primero se
publica y después se regenera su presentación (con `--force`).

Necesita python-pptx, PyYAML, Playwright (Chromium), `rsvg-convert` para los dibujos y
`ffmpeg` para el fotograma de portada de los videos; las rutas de los dos últimos se
cambian con PROTOBJECT_RSVG / PROTOBJECT_FFMPEG.
"""

import json
import yaml
import os
import sys
import glob
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE_TYPE, PP_PLACEHOLDER
from pptx.enum.text import MSO_AUTO_SIZE
from pptx.dml.color import RGBColor
from urllib import request
import re
import subprocess
import hashlib
from playwright.sync_api import sync_playwright

# --- WHERE THINGS ARE ---
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FOLDER = os.path.join(PROJECT_ROOT, '_activities')
ACTIVITIES_INDEX = os.path.join(PROJECT_ROOT, 'activities.json')
TEMPLATE_PPTX = os.path.join(PROJECT_ROOT, 'tools', 'template-simple.pptx')
OUTPUT_FOLDER = os.path.join(PROJECT_ROOT, 'ppt')

# The stills and animations these decks are built from, which are working
# material and not content: they are converted once, embedded in the decks, and
# never served to anybody. They used to be cached inside `assets/ppt/images`,
# which is inside the folder the site publishes wholesale — half a gigabyte of
# GIFs shipped to readers who had no way of even asking for them.
MEDIA_CACHE = os.path.join(PROJECT_ROOT, 'tools', 'media-cache')

RSVG_CONVERT_PATH = os.environ.get('PROTOBJECT_RSVG', "C:/msys64/mingw64/bin/rsvg-convert.exe")
FFMPEG_PATH = os.environ.get('PROTOBJECT_FFMPEG', "C:/ffmpeg-7.0-essentials_build/bin/ffmpeg.exe")


def asset_path(reference):
    """`src/16.4-robot-activation-challenge/a-memory.svg` como archivo: aquí la URL publicada y la ruta coinciden."""
    return os.path.join(PROJECT_ROOT, reference.replace('/', os.sep))


# --- FUNZIONI HELPER ---

def parse_front_matter(file_path):
    """Estrae e analizza il front matter YAML da un file markdown."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'^---\s*\n(.*?)\n^---\s*$', content, re.DOTALL | re.MULTILINE)
    return yaml.safe_load(match.group(1)) if match else None

def delete_shape_if_empty(shape):
    """Controlla se una forma ha una cornice di testo vuota e, in tal caso, la elimina."""
    if shape and shape.has_text_frame and not shape.text_frame.text.strip():
        sp = shape._sp
        sp.getparent().remove(sp)

def _populate_paragraph_with_markdown(p, text):
    """Popola un paragrafo applicando una formattazione markdown (grassetto, elenchi puntati/numerati)."""
    p.clear()
    clean_text = text.strip()
    is_heading = False
    
    if clean_text.startswith('#'):
        heading_match = re.match(r'^(#{1,4})\s', clean_text)
        if heading_match:
            is_heading = True
            clean_text = clean_text[len(heading_match.group(1)):].lstrip()
            
    bullet_match = re.match(r'^\*\s+', clean_text)
    numbered_match = re.match(r'^\d+\.\s+', clean_text)

    if bullet_match:
        p.level = 0
        clean_text = "" + clean_text[len(bullet_match.group(0)):].lstrip()
    elif numbered_match:
        p.level = 0
        
    parts = re.split(r'(\*\*.*?\*\*)', clean_text)
    for part in parts:
        run = p.add_run()
        is_bold_run = False
        if part.startswith('**') and part.endswith('**'):
            run.text = part[2:-2]
            is_bold_run = True
        else:
            run.text = part

        # Sizes are a starting ratio, not a decision: `fit_text_to_box` scales
        # them to the room the layout actually gives this text. They were fixed
        # at fourteen points, which overflowed a dense paragraph and left two
        # lines marooned in the middle of an empty slide.
        if is_heading:
            run.font.bold = True
            run.font.size = Pt(BASE_HEADING_PT)
        else:
            run.font.size = Pt(BASE_BODY_PT)
            if is_bold_run:
                run.font.bold = True

BASE_BODY_PT = 14
BASE_HEADING_PT = 16

EMU_PER_POINT = 12700
# What a placeholder keeps for itself: PowerPoint's default inset is a tenth of
# an inch each way, and text drawn to the very edge reads as a mistake anyway.
INSET_POINTS = 16


def fit_text_to_box(text_frame, width, height, smallest=11, largest=30):
    """Sizes the text to the room it has — down when it would spill, up when it rattles.

    An estimate, not a measurement: PowerPoint does the real layout and this file
    is written without it. A proportional face averages about half its point size
    per character, and a line takes about a fifth more than its size in height;
    those two numbers put the answer within a point or two, which is all this
    needs to stop text falling off a slide or sitting in the middle of an empty
    one.

    `TEXT_TO_FIT_SHAPE` is set as well, so PowerPoint shrinks it further if the
    estimate was generous. That alone was not enough: a reader that does not
    recompute autofit — and several do not — would show the overflow.
    """
    lines = [p.text for p in text_frame.paragraphs if p.text.strip()]
    if not lines:
        return

    usable_width = width / EMU_PER_POINT - INSET_POINTS * 2
    usable_height = height / EMU_PER_POINT - INSET_POINTS * 2
    if usable_width <= 0 or usable_height <= 0:
        return

    def fits(size):
        per_line = max(1, int(usable_width / (size * 0.5)))
        rows = sum(max(1, -(-len(line) // per_line)) for line in lines)
        # A little air between paragraphs, as the template's own spacing gives.
        return rows * size * 1.22 + (len(lines) - 1) * size * 0.35 <= usable_height

    size = smallest
    for candidate in range(largest, smallest - 1, -1):
        if fits(candidate):
            size = candidate
            break

    for paragraph in text_frame.paragraphs:
        for run in paragraph.runs:
            was = run.font.size.pt if run.font.size else BASE_BODY_PT
            run.font.size = Pt(size + (BASE_HEADING_PT - BASE_BODY_PT if was > BASE_BODY_PT else 0))

    text_frame.word_wrap = True
    try:
        text_frame.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
    except Exception:
        pass


def split_for_strip(text, placeholder):
    """What fits the caption strip, and whether the rest has to go to the notes.

    The code slide gives its explanation a band four fifths of an inch tall, which
    is right for a caption and hopeless for the six hundred words some activities
    write there: no size makes that fit, so it used to run off the bottom of the
    slide with nothing to say it had. The opening sentences stay where a class can
    read them and the whole passage goes to the notes, which is where a script for
    the teacher belongs anyway.
    """
    # A section that writes its caption as a list has nothing to trim: it goes
    # through whole, and `add_markdown_text` gives each entry its own paragraph.
    if not isinstance(text, str) or fits_in(text, placeholder):
        return text, False
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    kept = ''
    for sentence in sentences:
        candidate = (kept + ' ' + sentence).strip()
        if kept and not fits_in(candidate, placeholder):
            break
        kept = candidate
    return (kept or sentences[0]), True


def fits_in(text, placeholder, size=11):
    """Whether that much text would sit inside the box at a readable size."""
    usable_width = placeholder.width / EMU_PER_POINT - INSET_POINTS * 2
    usable_height = placeholder.height / EMU_PER_POINT - INSET_POINTS * 2
    if usable_width <= 0 or usable_height <= 0:
        return True
    per_line = max(1, int(usable_width / (size * 0.5)))
    rows = max(1, -(-len(text) // per_line))
    return rows * size * 1.22 <= usable_height


def fit_placeholder_text(placeholder):
    """`fit_text_to_box` for a placeholder, which knows its own size."""
    if placeholder is not None and placeholder.has_text_frame:
        fit_text_to_box(placeholder.text_frame, placeholder.width, placeholder.height)


def insert_whole_picture(placeholder, image_path):
    """The whole picture inside the box, rather than the box filled by part of it.

    `insert_picture` crops to fill: a program taller than its placeholder lost its
    top and its bottom, which is why the code slides showed a piece of a program
    and no sign that anything was missing. Undoing the crop and fitting the
    picture inside shows all of it — smaller, and complete, which is the trade
    worth making for something a reader can open full size from the link beside
    it.
    """
    box = (placeholder.left, placeholder.top, placeholder.width, placeholder.height)
    picture = placeholder.insert_picture(image_path)
    picture.crop_left = picture.crop_right = picture.crop_top = picture.crop_bottom = 0
    try:
        native_width, native_height = picture.image.size
        aspect = native_width / native_height
    except Exception:
        aspect = box[2] / box[3]
    picture.left, picture.top, picture.width, picture.height = fit_inside(box, aspect)
    return picture


# The tags an activity writes around the things a learner has to find on screen.
# They were being unwrapped to plain text; a component's name is the one word in
# a step that has to be spotted from the back of a room, so it is set in bold.
TAGGED = re.compile(
    r'<(?P<tag>addbutton|comp|openwindow|category|runbutton)>(?P<label>.*?)</(?P=tag)>|<qr>')


def strip_bold(text):
    """Markdown emphasis removed, for the notes, which carry no formatting."""
    return re.sub(r'[*][*](.+?)[*][*]', lambda m: m.group(1), str(text))


def unwrap_tags(text):
    """Unwraps the tags, and hands back whatever shape it was given.

    Several sections write their content as a list — the reflection questions are
    one per entry — and a version of this that stringified everything turned that
    list into its own printed form on the slide, brackets, quotes and all.
    """
    if isinstance(text, list):
        return [unwrap_tags(item) for item in text]
    if not isinstance(text, str):
        return text
    return TAGGED.sub(lambda m: f"**{m.group('label')}**" if m.group('label') is not None else 'QR', text)


def add_markdown_text(text_frame, markdown_text):
    """Svuota una cornice di testo e la popola con testo formattato in markdown."""
    text_frame.clear() 
    if text_frame.paragraphs:
        p = text_frame.paragraphs[0]
        p.clear()
        for i in range(len(text_frame.paragraphs) - 1, 0, -1):
            text_frame._txBody.remove(text_frame.paragraphs[i]._p)
    
    if not markdown_text:
        return
        
    source_lines = markdown_text if isinstance(markdown_text, list) else str(markdown_text).strip().split('\n')
    lines = [line.strip() for line in source_lines if line.strip()]
    
    if not lines:
        return
        
    _populate_paragraph_with_markdown(text_frame.paragraphs[0], lines[0])
    for line_text in lines[1:]:
        p = text_frame.add_paragraph()
        _populate_paragraph_with_markdown(p, line_text)

def reveal_hidden_blocks(url):
    """Il docente ha bisogno del programma intero.

    Un'attivita' puo' marcare dei blocchi come la risposta che l'alunno deve
    trovare da solo, e generate li disegna coperti. Nella slide del docente
    mancherebbe proprio il pezzo di cui parla la lezione, quindi qui si chiede
    la versione scoperta.
    """
    if '/generate' not in url or '&show' in url:
        return url
    return url + '&show'

# Bumped when the way a shot is taken changes, so the cache below stops handing
# back pictures taken the old way. The screenshots of the code slide were cached
# in August, while `app.protobject.com` still served the previous build, and every
# deck therefore showed an empty canvas: two starter blocks and a lot of white.
# Nothing short of changing this key would have refreshed them.
SHOT_VERSION = 2

# Twice the pixels, because these are projected. A program that reads on a laptop
# is unreadable from the back of a classroom.
SHOT_SCALE = 2

# Con `--force` la foto del programa se vuelve a tomar: la caché está indexada por URL,
# y la URL de un programa no cambia cuando se publica una versión nueva.
RETAKE_SHOTS = '--force' in sys.argv[1:]


def take_website_screenshot(url, image_folder):
    """A picture of one program, cropped to the program.

    The page it shoots is `generate`, which draws the blocks on a transparent
    ground and leaves the rest of the window empty. Photographing the window gave
    a small program adrift in white; measuring what was actually drawn and
    cropping to it gives the blocks and nothing else.
    """
    try:
        url = reveal_hidden_blocks(url)
        url_hash = hashlib.md5(f"{SHOT_VERSION}|{url}".encode()).hexdigest()
        screenshot_path = os.path.join(image_folder, f"screenshot_{url_hash}.png")
        if os.path.exists(screenshot_path) and not RETAKE_SHOTS:
            return screenshot_path

        print(f"  -> Catturando screenshot di {url}...")
        with sync_playwright() as p:
            browser = p.chromium.launch()
            # Roomy on purpose: the program is fitted to the width it is given,
            # and a cramped window would draw it small before it is cropped.
            page = browser.new_page(
                viewport={"width": 1600, "height": 1000},
                device_scale_factor=SHOT_SCALE,
            )
            page.goto(url, wait_until='networkidle', timeout=60000)
            page.wait_for_timeout(2500)

            # Both canvases: a comment bubble is drawn on its own, above the
            # blocks, and measuring only the blocks would cut one in half.
            box = page.evaluate("""() => {
              const blocks = document.querySelector('.blocklyBlockCanvas');
              if (!blocks) return null;
              const a = blocks.getBoundingClientRect();
              if (!a.width || !a.height) return null;
              const bubbles = document.querySelector('.blocklyBubbleCanvas');
              const b = bubbles && bubbles.getBoundingClientRect();
              const left = b && b.height ? Math.min(a.left, b.left) : a.left;
              const top = b && b.height ? Math.min(a.top, b.top) : a.top;
              const right = b && b.height ? Math.max(a.right, b.right) : a.right;
              const bottom = b && b.height ? Math.max(a.bottom, b.bottom) : a.bottom;
              const pad = 24;
              return { x: left - pad, y: top - pad,
                       width: right - left + pad * 2, height: bottom - top + pad * 2 };
            }""")

            if box and box['width'] > 0 and box['height'] > 0:
                page.screenshot(path=screenshot_path, clip=box)
            else:
                # A program that would not draw is still worth a picture of
                # whatever did: better a wrong slide than a missing one.
                print("  -> ATTENZIONE: non trovo i blocchi, scatto la finestra intera")
                page.screenshot(path=screenshot_path)

            browser.close()
        return screenshot_path
    except Exception as e:
        print(f"  -> ERRORE durante la cattura dello screenshot per {url}: {e}")
        return None


# The notice the template opens with, written out in all three languages. A deck
# has one language, so the other two are two paragraphs of somebody else's
# alphabet on the first thing a class sees.
NOTICE_HEADINGS = {'en': 'English', 'es': 'Español', 'it': 'Italiano'}


def keep_notice_language(prs, lang):
    """Leaves the opening notice standing, in this deck's language only.

    Paragraphs are deleted rather than the text rewritten, so what survives keeps
    the size, weight and colour the template gave it. The language heading goes
    too: it labelled a choice that no longer has to be made.
    """
    heading = NOTICE_HEADINGS.get(lang)
    if heading is None or len(prs.slides) == 0:
        return
    for shape in prs.slides[0].shapes:
        if not shape.has_text_frame or 'automatically generated' not in shape.text_frame.text:
            continue
        paragraphs = list(shape.text_frame.paragraphs)
        keep, current = [], None
        for paragraph in paragraphs:
            line = paragraph.text.strip()
            if line in NOTICE_HEADINGS.values():
                current = line
                continue
            if current == heading and line:
                keep.append(paragraph)
        if not keep:
            return
        for paragraph in paragraphs:
            if paragraph not in keep:
                paragraph._p.getparent().remove(paragraph._p)
        return


def poster_frame(video_path, image_folder):
    """One frame of a video, for PowerPoint to show before anybody presses play.

    Without it an embedded video is a black rectangle on the slide, which reads
    as a broken deck rather than as a video. Taken half a second in, because the
    very first frame of these recordings is often still fading up.
    """
    poster = os.path.join(image_folder, os.path.splitext(os.path.basename(video_path))[0] + '.poster.png')
    if os.path.exists(poster):
        return poster
    try:
        subprocess.run(
            [FFMPEG_PATH, '-ss', '00:00:00.5', '-i', video_path, '-frames:v', '1', '-y', poster],
            check=True, capture_output=True, text=True,
        )
        return poster if os.path.exists(poster) else None
    except Exception as e:
        print(f"  -> Non sono riuscito a estrarre il fotogramma di copertina: {e}")
        return None


def fit_inside(box, aspect):
    """A rectangle of the given shape, centred in the box it is given."""
    left, top, width, height = box
    if aspect <= 0:
        return box
    if width / height > aspect:
        drawn_width = int(height * aspect)
        return (left + (width - drawn_width) // 2, top, drawn_width, height)
    drawn_height = int(width / aspect)
    return (left, top + (height - drawn_height) // 2, width, drawn_height)


def place_video(slide, placeholder, video_path, image_folder):
    """Puts the video itself on the slide, where the picture would have gone.

    These were being turned into GIFs — 360 pixels wide, ten frames a second,
    sixty-four colours — because a deck full of raw video was assumed to be
    enormous. Measured against their own GIFs the videos come to 53 MB against
    52: the same, for full colour, sound, and a pause button. python-pptx has
    embedded them since 0.6, so nothing outside Python was ever needed.
    """
    poster = poster_frame(video_path, image_folder)
    aspect = 16 / 9
    if poster:
        try:
            from PIL import Image
            with Image.open(poster) as frame:
                aspect = frame.width / frame.height
        except Exception:
            pass

    left, top, width, height = fit_inside(
        (placeholder.left, placeholder.top, placeholder.width, placeholder.height), aspect
    )
    placeholder._element.getparent().remove(placeholder._element)
    slide.shapes.add_movie(
        video_path, left, top, width, height,
        poster_frame_image=poster, mime_type='video/mp4',
    )


def download_and_convert_media(media_urls, image_folder):
    """Scarica (se web) e converte media (immagini, video in GIF, SVG in PNG)."""
    image_paths = []
    if not isinstance(media_urls, list):
        media_urls = [media_urls]
        
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    for url in media_urls:
        if not isinstance(url, str):
            continue
        clean_url = re.sub(r'^\[\d+\]', '', url)
        
        try:
            is_web_url = clean_url.startswith('http')
            
            if is_web_url:
                filename = os.path.basename(clean_url.split("?")[0])
                local_path = os.path.join(image_folder, filename)
                if not os.path.exists(local_path):
                    print(f"  -> Scaricando {clean_url}...")
                    req = request.Request(clean_url, headers=headers)
                    with request.urlopen(req) as response, open(local_path, 'wb') as out_file:
                        out_file.write(response.read())
            else:
                local_path = asset_path(clean_url)
                if not os.path.exists(local_path):
                    print(f"  -> ATTENZIONE: File locale non trovato: {local_path}")
                    continue

            if local_path.lower().endswith('.mp4'):
                # Beside the deck, not beside the source: `assets/` is content,
                # and a build artefact dropped in it comes back as a diff.
                gif_path = os.path.join(image_folder, os.path.splitext(os.path.basename(local_path))[0] + '.gif')
                if not os.path.exists(gif_path):
                    print(f"  -> Generando GIF di alta qualità per: {local_path}")
                    
                    # 360px and ten frames a second, from a 64-colour
                    # palette, with dithering off. A GIF stores every frame
                    # whole, so each of those knobs is worth multiples rather
                    # than percentages: this activity's animation went from
                    # 57.6 MB to under 4, and the deck it sits in with it.
                    # Dithering costs the most of all — the noise it adds is
                    # precisely what the frame-to-frame compression cannot pack.
                    scale_filter = "scale=w=min(360\,iw):h=-1:flags=lanczos"
                    frame_rate = 10
                    
                    palette_path = os.path.join(image_folder, f'palette_{os.path.basename(gif_path)}.png')
                    palette_command = [
                        FFMPEG_PATH, 
                        '-i', local_path,
                        '-vf', f'fps={frame_rate},{scale_filter},palettegen=max_colors=64',
                        '-y', palette_path
                    ]
                    subprocess.run(palette_command, check=True, capture_output=True, text=True)

                    gif_command = [
                        FFMPEG_PATH,
                        '-i', local_path,
                        '-i', palette_path,
                        '-lavfi', f'fps={frame_rate},{scale_filter} [x]; [x][1:v] paletteuse=dither=none',
                        '-y', gif_path
                    ]
                    subprocess.run(gif_command, check=True, capture_output=True, text=True)
                image_paths.append(gif_path)
            elif local_path.lower().endswith('.svg'):
                png_path = os.path.join(image_folder, re.sub(r'[\/]', '_', os.path.splitext(clean_url)[0]) + '.png')
                if not os.path.exists(png_path):
                    subprocess.run([RSVG_CONVERT_PATH, "-f", "png", "-o", png_path, local_path], check=True)
                image_paths.append(png_path)
            elif re.search(r'\.(png|jpg|jpeg)$', local_path, re.IGNORECASE):
                image_paths.append(local_path)
            elif not is_web_url:
                 print(f"  -> ATTENZIONE: Tipo di file locale non gestito: {local_path}")
            else:
                screenshot_path = take_website_screenshot(clean_url, image_folder)
                if screenshot_path:
                    image_paths.append(screenshot_path)
        except Exception as e:
            print(f"  -> Errore durante il processamento di {url}: {e}")
    return image_paths

SEE_THE_PROGRAM = {
    'en': 'See the complete program',
    'es': 'Ver el programa completo',
    'it': 'Vedi il programma completo',
}


def read_challenge(section):
    """The challenge an activity closes on, as text and pictures.

    Written as `right_content`: a list whose entries carry either a `text` or a
    `media`, in the order they are shown beside the reflection questions.
    """
    entries = section.get('right_content')
    if not isinstance(entries, list):
        legacy = str(section.get('challenge_content', '')).strip()
        return unwrap_tags(legacy), []
    text = ' '.join(str(e['text']).strip() for e in entries if isinstance(e, dict) and e.get('text'))
    media = [str(e['media']) for e in entries if isinstance(e, dict) and e.get('media')]
    # Unwrapped here, at the one place the challenge is read, so both the column
    # beside the questions and the slide of its own get it.
    return unwrap_tags(text.strip()), media


def add_challenge_slide(prs, text, media, image_folder):
    """The challenge on a slide of its own, titled with its own word.

    The title is the label the activity already writes in bold — "Sfida",
    "Desafío", "Challenge" — so nothing here has to be translated, and a lesson
    that words it differently keeps its own wording.
    """
    label = re.match(r'\s*\*\*(.+?)\*\*\s*:?\s*', text)
    heading = label.group(1).strip().rstrip(':') if label else ''
    body = text[label.end():] if label else text

    images = download_and_convert_media(media, image_folder)
    layout = get_slide_layout(prs, 'one-img' if images else 'create-step')
    slide = prs.slides.add_slide(layout)

    try:
        title_shape = slide.shapes.title
    except AttributeError:
        title_shape = None
    if title_shape:
        title_shape.text = heading
        delete_shape_if_empty(title_shape)

    body_ph = next((sh for sh in slide.placeholders
                    if hasattr(sh, 'placeholder_format')
                    and sh.placeholder_format.type in (PP_PLACEHOLDER.BODY, PP_PLACEHOLDER.OBJECT)), None)
    if body_ph is None:
        body_ph = next((sh for sh in slide.placeholders
                        if hasattr(sh, 'placeholder_format') and sh.placeholder_format.idx == 1), None)
    if body_ph:
        add_markdown_text(body_ph.text_frame, body)
        fit_placeholder_text(body_ph)
        delete_shape_if_empty(body_ph)

    if images:
        pic_ph = next((sh for sh in slide.placeholders
                       if hasattr(sh, 'placeholder_format')
                       and sh.placeholder_format.type == PP_PLACEHOLDER.PICTURE), None)
        if pic_ph:
            try:
                insert_whole_picture(pic_ph, images[0])
            except Exception as e:
                print(f"  -> Non sono riuscito a inserire il disegno della sfida: {e}")


def get_slide_layout(prs, name):
    """Recupera un layout di diapositiva per nome dalla presentazione."""
    for layout in prs.slide_layouts:
        if layout.name == name:
            return layout
    print(f"  -> ATTENZIONE: Layout '{name}' non trovato. Uso 'Title and Content'.")
    return prs.slide_layouts[5]

def main():
    wanted = [a for a in sys.argv[1:] if not a.startswith('--')]
    force = '--force' in sys.argv[1:]
    print("Starting PowerPoint generation...")
    output_folder_abs = OUTPUT_FOLDER
    image_folder_abs = MEDIA_CACHE
    if not os.path.exists(output_folder_abs):
        os.makedirs(output_folder_abs)
    if not os.path.exists(image_folder_abs):
        os.makedirs(image_folder_abs)

    # Solo las 17 de `activities.json`, en su orden: en `_activities/` hay otros
    # archivos que no son de este proyecto.
    with open(ACTIVITIES_INDEX, encoding='utf-8') as index:
        slugs = json.load(index)['activities']
    activity_files = [os.path.join(INPUT_FOLDER, slug + '.es.md') for slug in slugs]
    missing = [f for f in activity_files if not os.path.exists(f)]
    if missing:
        sys.exit('Faltan actividades: ' + ', '.join(missing))

    # The two switches the help text at the top has always promised and nobody
    # had wired up: a name to work on one activity, and `--force` to rebuild a
    # deck that already exists. Without them every run rebuilt all hundred and
    # twenty-five, which is a long time to wait to look at one slide.
    if wanted:
        activity_files = [f for f in activity_files
                          if any(w in os.path.basename(f) for w in wanted)]
    if not force:
        activity_files = [
            f for f in activity_files
            if not os.path.exists(os.path.join(
                OUTPUT_FOLDER, os.path.splitext(os.path.basename(f))[0] + '.pptx'))
        ]

    print(f"Trovati {len(activity_files)} file da processare...")

    for file_path in activity_files:
        print(f"\nProcessing {file_path}...")
        prs = Presentation(TEMPLATE_PPTX)
        data = parse_front_matter(file_path)
        if not data:
            continue

        lang = str(data.get('lang', 'en'))
        keep_notice_language(prs, lang)

        # --- SLIDE 1: COPERTINA ---
        cover_layout = get_slide_layout(prs, 'Title Slide')
        slide = prs.slides.add_slide(cover_layout)
        
        try:
            title_shape = slide.shapes.title
        except AttributeError:
            title_shape = None

        if title_shape:
            title_shape.text = data.get('title', 'Senza Titolo')
            delete_shape_if_empty(title_shape)
            
        subtitle_shape = slide.placeholders[1] if len(slide.placeholders) > 1 else None
        if subtitle_shape:
            subtitle_shape.text = data.get('description', '')
            delete_shape_if_empty(subtitle_shape)

        # The introduction, where it is of use: in the notes.
        #
        # It is written to be read aloud at the start of a lesson — six hundred
        # characters of it — so the slide is the wrong place for it twice over:
        # it would not fit the subtitle box, and a paragraph nobody can read from
        # the back of the room is furniture. In the notes it reaches the one
        # person it was written for.
        introduction = str(data.get('introduction', '')).strip()
        if introduction:
            plain = re.sub(r'\*\*(.+?)\*\*', r'\1', introduction)
            slide.notes_slide.notes_text_frame.text = plain
            
        cover_image_paths = download_and_convert_media([data.get('image', '')], image_folder_abs)
        if cover_image_paths:
            pic_placeholder = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.type == PP_PLACEHOLDER.PICTURE), None)
            if pic_placeholder:
                try:
                    insert_whole_picture(pic_placeholder, cover_image_paths[0])
                except Exception as e:
                    print(f"Errore nell'inserire l'immagine di copertina: {e}")
        
        # --- SLIDE 2: "COSA FAREMO?" ---
        if data.get('video') and data.get('video_title'):
            print("  -> Aggiungo la slide 'Cosa Faremo'...")
            what_to_do_layout = get_slide_layout(prs, 'what-to-do')
            slide = prs.slides.add_slide(what_to_do_layout)
            
            try:
                title_shape = slide.shapes.title
            except AttributeError:
                title_shape = None

            if title_shape:
                title_shape.text = data.get('video_title')
                delete_shape_if_empty(title_shape)
                
            pic_placeholder = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.type == PP_PLACEHOLDER.PICTURE), None)
            video_file = asset_path(str(data.get('video')))
            if pic_placeholder and os.path.exists(video_file):
                print("  -> Incorporo il video...")
                place_video(slide, pic_placeholder, video_file, image_folder_abs)
            else:
                # A video that is somewhere else, or is not a file we hold: the
                # old road, which still ends in a picture on the slide.
                video_gif_paths = download_and_convert_media([data.get('video')], image_folder_abs)
                if video_gif_paths and pic_placeholder:
                    insert_whole_picture(pic_placeholder, video_gif_paths[0])

        # --- SLIDES DI CONTENUTO ---
        for section in data.get('content_sections', []):
            if section.get('type') == 'final':
                continue

            section_type = section.get('type')
            slide = None

            # --- [GESTIONE] PER 'create' CON STEPS ---
            if section_type == 'create' and 'steps' in section and section['steps']:
                print(f"  -> Gestione slide 'create' con steps: {section.get('title')}")
                slide_layout = get_slide_layout(prs, 'create-step')
                slide = prs.slides.add_slide(slide_layout)
                
                try:
                    title_shape = slide.shapes.title
                except AttributeError:
                    title_shape = None
                
                if title_shape:
                    title_shape.text = section.get('title', '')
                    delete_shape_if_empty(title_shape)
                
                heading_ph = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.type == PP_PLACEHOLDER.CHART), None)
                if heading_ph:
                    add_markdown_text(heading_ph.text_frame, section.get('heading_text', ''))
                    fit_placeholder_text(heading_ph)
                    delete_shape_if_empty(heading_ph)
                
                body_ph = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.type == PP_PLACEHOLDER.BODY), None)
                if not body_ph:
                    body_ph = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.idx == 1), None)

                if body_ph:
                    steps = section.get('steps', [])
                    formatted_steps = "\n".join(steps)
                    cleaned_steps = unwrap_tags(formatted_steps)
                    add_markdown_text(body_ph.text_frame, cleaned_steps)
                    fit_placeholder_text(body_ph)
                    delete_shape_if_empty(body_ph)

            # --- [GESTIONE] PER 'reflect' ---
            elif section_type == 'reflect':
                print(f"  -> Gestione slide 'reflect': {section.get('title')}")
                slide_layout = get_slide_layout(prs, 'reflect-box')
                slide = prs.slides.add_slide(slide_layout)

                try:
                    title_shape = slide.shapes.title
                except AttributeError:
                    title_shape = None
                
                if title_shape:
                    title_shape.text = section.get('title', '')
                    delete_shape_if_empty(title_shape)

                body_ph = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.type == PP_PLACEHOLDER.BODY), None)
                if not body_ph:
                    body_ph = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.idx == 1), None)

                if body_ph:
                    add_markdown_text(body_ph.text_frame, unwrap_tags(section.get('content', '')))
                    fit_placeholder_text(body_ph)
                    delete_shape_if_empty(body_ph)
                
                # The closing challenge — "could the alarm switch itself off?" —
                # is written as `right_content`, a list of text and pictures, and
                # the deck was looking for a `challenge_content` that no activity
                # has. So the last thing a lesson says was being dropped from
                # every deck.
                challenge_text, challenge_media = read_challenge(section)

                challenge_ph = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.type == PP_PLACEHOLDER.CHART), None)
                if challenge_ph:
                    # Beside the questions when it is only words — which is the
                    # arrangement the activity page itself uses. With a diagram it
                    # gets a slide of its own rather than a column four inches
                    # wide holding both.
                    add_markdown_text(challenge_ph.text_frame, '' if challenge_media else challenge_text)
                    fit_placeholder_text(challenge_ph)
                    delete_shape_if_empty(challenge_ph)

                if challenge_media and challenge_text:
                    add_challenge_slide(prs, challenge_text, challenge_media, image_folder_abs)

            # --- [GESTIONE] PER 'code-composition' ---
            elif section_type == 'code-composition':
                print(f"  -> Gestione slide 'code-composition': {section.get('title')}")
                slide_layout = get_slide_layout(prs, 'code-composition')
                slide = prs.slides.add_slide(slide_layout)
                
                try:
                    title_shape = slide.shapes.title
                except AttributeError:
                    title_shape = None
                
                if title_shape:
                    title_shape.text = section.get('title', '')
                    delete_shape_if_empty(title_shape)
                
                body_ph = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.type == PP_PLACEHOLDER.BODY), None)
                if not body_ph:
                    body_ph = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.idx == 1), None)

                if body_ph:
                    cleaned_content = unwrap_tags(section.get('content', ''))
                    on_slide, in_notes = split_for_strip(cleaned_content, body_ph)
                    add_markdown_text(body_ph.text_frame, on_slide)
                    fit_placeholder_text(body_ph)
                    delete_shape_if_empty(body_ph)
                    if in_notes:
                        slide.notes_slide.notes_text_frame.text = strip_bold(cleaned_content)

                media_url = section.get('media')
                image_paths = download_and_convert_media(media_url, image_folder_abs)
                
                pic_ph = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.type == PP_PLACEHOLDER.PICTURE), None)
                if pic_ph and image_paths:
                    insert_whole_picture(pic_ph, image_paths[0])
                
                link_ph = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.type == PP_PLACEHOLDER.CHART), None)
                if link_ph:
                    url_text = media_url if isinstance(media_url, str) else (media_url[0] if isinstance(media_url, list) and media_url else '')
                    if url_text:
                        clean_url_text = re.sub(r'^\[\d+\]\s*', '', url_text).strip()
                        
                        p = link_ph.text_frame.paragraphs[0]
                        p.clear()
                        run = p.add_run()
                        run.text = SEE_THE_PROGRAM.get(lang, SEE_THE_PROGRAM['en'])
                        run.hyperlink.address = clean_url_text
                        font = run.font
                        font.color.rgb = RGBColor(0, 0, 255)
                        font.underline = True
                    delete_shape_if_empty(link_ph)

            # --- GESTIONE STANDARD (PER 'learn', 'create' senza steps, etc.) ---
            else:
                image_paths = download_and_convert_media(section.get('media', []), image_folder_abs)
                layout_name_map = {1: 'one-img', 2: 'two-img', 3: 'three-img', 4: 'four-img'}
                layout_name = layout_name_map.get(len(image_paths))
                slide_layout = get_slide_layout(prs, layout_name if layout_name else 'Title and Content')
                slide = prs.slides.add_slide(slide_layout)

                try:
                    title_shape = slide.shapes.title
                except AttributeError:
                    title_shape = None
                
                if title_shape:
                    title_shape.text = section.get('title', '')
                    delete_shape_if_empty(title_shape)
                
                body_ph = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.type == PP_PLACEHOLDER.BODY), None)
                if not body_ph:
                    body_ph = next((sh for sh in slide.placeholders if hasattr(sh, 'placeholder_format') and sh.placeholder_format.idx == 1), None)

                # The `learn` sections come through here, and they name components
                # and buttons exactly as the `create` steps do.
                slide_content = section.get('content', '')
                if isinstance(slide_content, list):
                    slide_content = [unwrap_tags(line) for line in slide_content]
                else:
                    slide_content = unwrap_tags(slide_content)

                if body_ph:
                    add_markdown_text(body_ph.text_frame, slide_content)
                    fit_placeholder_text(body_ph)
                    delete_shape_if_empty(body_ph)
                elif isinstance(slide_content, str) and slide_content.strip():
                    slide.notes_slide.notes_text_frame.text = strip_bold(slide_content)

                if layout_name:
                    pic_placeholders = [ph for ph in slide.placeholders if hasattr(ph, 'placeholder_format') and ph.placeholder_format.type == PP_PLACEHOLDER.PICTURE]
                    for i, img_path in enumerate(image_paths):
                        if i < len(pic_placeholders):
                            insert_whole_picture(pic_placeholders[i], img_path)
            
        base_name = os.path.basename(file_path)
        file_name_without_ext = os.path.splitext(base_name)[0]
        output_path = os.path.join(output_folder_abs, f"{file_name_without_ext}.pptx")
        prs.save(output_path)
        print(f"Presentation saved successfully: {output_path}")

    print("\nBatch processing complete.")

if __name__ == '__main__':
    main()