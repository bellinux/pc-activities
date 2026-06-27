# -*- coding: utf-8 -*-
# Estrae il sorgente MakeCode dai .hex di micro:bit e lo rende come i BLOCCHI,
# usando le ETICHETTE UFFICIALI in spagnolo dell'editor (NON traduzioni inventate).
#
# Le stringhe ufficiali vengono da cdn.makecode.com (lingua es-ES), salvate in
# microbit/_locales/es/{core,music,microphone}-strings.json. Per aggiornarle:
#   curl "https://cdn.makecode.com/api/translations?lang=es-ES&filename=microbit%2Fcore-strings.json&approved=true&cdn=AAAAMMGG" -o microbit/_locales/es/core-strings.json
#   (idem music-strings.json, microphone-strings.json)
# I blocchi Blockly (repeat/for/while/if/set/change/on start) usano le stringhe
# ufficiali del file strings.json (incluse qui sotto come costanti).
#
# Formato .hex: Universal Hex; il sorgente sta nei record 0x0E -> MAGIC pxt ->
# header(metaLen u16, textLen u32, +2) -> META JSON -> TEXT (LZMA) -> <header><files>.
# files: main.blocks (XML Blockly) + main.ts (TypeScript).
import json, os, sys, lzma, re
import xml.etree.ElementTree as ET
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

ACTS = [
    ("02.1-xylophone", "xilofono-inclinacion"), ("02.2-music-visualizer", "luci-discoteca-ruido"),
    ("03.1-led-xylophone", "xilofono-inclinacion-con-nota-led"), ("04.1-heart-beat", "corazon-forever-loop"),
    ("14.1-ticklish-robot", "robot-risa-simpatica-al-ruido"), ("14.2-my-robot-friend-heart", "corazon-variables-eventos"),
    ("16.1-cookie-thief-alarm", "alarma-caja-galletas"), ("16.2-sunflower-alarm-clock", "despertador-por-la-manana"),
    ("16.3-bat-in-the-dark", "luces-de-fiesta-al-oscurecer"), ("16.4-robot-activation-challenge", "juego-toques"),
    ("16.5-magic-clap-switch", "luz-encendida-al-ruido"), ("17.1-magic-birthday-candle", "flama-vela-con-soplo"),
    ("19.1-digital-hot-potato", "papas-caliente-juego"), ("21.1-cinematic-power-on", "luz-encendida-ruido-animacion"),
    ("22.1-dj-metronome", "metronomo-con-inclinacion"), ("22.2-applause-battle", "aplausometro-tiempo-aplausos"),
    ("22.3-dont-spill-liquid-game", "nivel-con-ruido"),
]
BASE = os.path.dirname(os.path.abspath(__file__))
DEC = os.path.join(BASE, "decoded"); os.makedirs(DEC, exist_ok=True)
MAGIC = bytes([0x41, 0x14, 0x0E, 0x2F, 0xB8, 0x2F, 0xA2, 0xBB])

# ---- stringhe ufficiali dei blocchi micro:bit (caricate dai file locale) ----
STR = {}
for _f in ("core-strings.json", "music-strings.json", "microphone-strings.json"):
    try: STR.update(json.load(open(os.path.join(BASE, "_locales", "es", _f), encoding="utf-8")))
    except Exception: pass

# blockId (tipo nel XML) -> simbolo pxt (per cercare "<simbolo>|block")
SYM = {
    "device_forever":"basic.forever", "device_show_leds":"basic.showLeds", "device_show_number":"basic.showNumber",
    "device_pause":"basic.pause", "device_clear_display":"basic.clearScreen",
    "device_plot":"led.plot", "device_unplot":"led.unplot", "device_set_brightness":"led.setBrightness",
    "device_acceleration":"input.acceleration", "device_get_light_level":"input.lightLevel",
    "device_get_sound_level":"input.soundLevel", "device_get_running_time":"input.runningTime",
    "input_on_sound":"input.onSound", "device_gesture_event":"input.onGesture", "input_logo_event":"input.onLogoEvent",
    "music_playable_play":"music.play", "music_playable_play_default_bkg":"music._playDefaultBackground",
    "music_tone_playable":"music.tonePlayable", "device_beat":"music.beat",
    "device_builtin_melody_playable":"music.builtInMelody",
    "soundExpression_builtinPlayableSoundEffect":"music.builtinPlayableSoundEffect",
    "music_stop_all_sounds":"music.stopAllSounds", "device_ring":"music.ringTone", "device_stop_melody":"music.stopMelody",
    "device_random":"Math.randomRange", "math_constrain_value":"Math.constrain", "serial_writevalue":"serial.writeValue",
}
# blocchi Blockly built-in (stringhe ufficiali da strings.json es-ES)
BK = {"on_start":"al iniciar", "repeat":"repetir {0} veces", "for":"para {0} de 0 a {1}",
      "while":"mientras {0}", "set":"fijar {0} a {1}", "change":"cambiar {0} por {1}",
      "if":"si {0} entonces", "elseif":"si no, si {0} entonces", "else":"si no"}
# device_note salva una frequenza; MakeCode la mostra in solfeo (Do/Re/Mi…), ottava media senza numero
NOTE = {131:"Do3",139:"Do#3",147:"Re3",156:"Re#3",165:"Mi3",175:"Fa3",185:"Fa#3",196:"Sol3",208:"Sol#3",220:"La3",233:"La#3",247:"Si3",
        262:"Do",277:"Do#",294:"Re",311:"Re#",330:"Mi",349:"Fa",370:"Fa#",392:"Sol",415:"Sol#",440:"La",466:"La#",494:"Si",
        523:"Do5",554:"Do#5",587:"Re5",622:"Re#5",659:"Mi5",698:"Fa5",740:"Fa#5",784:"Sol5",831:"Sol#5",880:"La5",932:"La#5",988:"Si5"}

# ---- estrazione dal .hex ----
def hex_data(path):
    out = bytearray()
    for line in open(path):
        line = line.strip()
        if line.startswith(":"):
            b = bytes.fromhex(line[1:])
            if b[3] in (0x00, 0x0D, 0x0E): out += b[4:4 + b[0]]
    return bytes(out)

def lzma_raw(text):
    props = text[0]; lc = props % 9; lp = (props // 9) % 5; pb = (props // 9) // 5
    filt = [{"id": lzma.FILTER_LZMA1, "dict_size": max(4096, int.from_bytes(text[1:5], "little")), "lc": lc, "lp": lp, "pb": pb}]
    return lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=filt).decompress(text[13:])

def extract(path):
    blob = hex_data(path); p = blob.find(MAGIC)
    if p < 0: raise ValueError("MAGIC pxt non trovato")
    p += 8; meta_len = int.from_bytes(blob[p:p+2], "little"); text_len = int.from_bytes(blob[p+2:p+6], "little"); p += 8
    meta = json.loads(blob[p:p+meta_len].decode("utf-8")); p += meta_len
    raw = lzma_raw(blob[p:p+text_len]).decode("utf-8")
    dec = json.JSONDecoder(); header, i = dec.raw_decode(raw); files, _ = dec.raw_decode(raw, i)
    return meta, header, files

# ---- parsing Blockly ----
def _strip(t): return t.split("}", 1)[1] if "}" in t else t
def _first(el):
    sh = None
    for ch in el:
        tg = _strip(ch.tag)
        if tg == "block": return ch
        if tg == "shadow" and sh is None: sh = ch
    return sh
def _parts(el):
    f, v, s, nx, c = {}, {}, {}, None, None
    for ch in el:
        tg = _strip(ch.tag)
        if tg == "field": f[ch.get("name")] = (ch.text or "").strip()
        elif tg == "value": v[ch.get("name")] = _first(ch)
        elif tg == "statement": s[ch.get("name")] = _first(ch)
        elif tg == "next": nx = _first(ch)
        elif tg == "comment": c = (ch.text or "").strip()
    return f, v, s, nx, c
def _leds(s):
    return [ln.strip() for ln in s.replace("`", "").split("\n") if ln.strip() and set(ln.strip()) <= set("#. ")]

def _enum_es(val):                                   # "Gesture.Shake" -> "agitado"
    if val is None: return "?"
    s = STR.get(val + "|block") or STR.get(val) or val.split(".")[-1]
    return re.sub(r"^\{[^}]*\}", "", s).strip()

def pxt_fill(block):                                 # riempie il template ufficiale "<sym>|block"
    t = block.get("type"); f, v, s, n, c = _parts(block)
    sym = SYM.get(t)
    tmpl = STR.get(sym + "|block") if sym else None
    if not tmpl: return None
    tmpl = tmpl.split("||")[0]
    def rep(m):
        name = m.group(1)
        if name in v and v[name] is not None: return _expr(v[name])
        if name in f: return _enum_es(f[name])
        return ""
    out = re.sub(r"[%$](\w+)(?:=\w+)?", rep, tmpl).replace("|", " ")
    return re.sub(r"\s+", " ", out).strip()

def _expr(el):
    if el is None: return "?"
    t = el.get("type"); f, v, s, n, c = _parts(el)
    if t in ("math_number", "math_whole_number"): return f.get("NUM", "?")
    if t == "math_number_minmax": return f.get("SLIDER", "?")
    if t == "timePicker": return f.get("ms", "?")
    if t == "logic_boolean": return "verdadero" if f.get("BOOL") == "TRUE" else "falso"
    if t == "text": return '"%s"' % f.get("TEXT", "")
    if t in ("variables_get", "variables_get_reporter"): return f.get("VAR", "?")
    if t == "math_arithmetic":
        return "(%s %s %s)" % (_expr(v.get("A")), {"ADD":"+","MINUS":"−","MULTIPLY":"×","DIVIDE":"÷","POWER":"^"}.get(f.get("OP"), f.get("OP")), _expr(v.get("B")))
    if t == "logic_compare":
        return "(%s %s %s)" % (_expr(v.get("A")), {"EQ":"=","NEQ":"≠","LT":"<","LTE":"≤","GT":">","GTE":"≥"}.get(f.get("OP"), f.get("OP")), _expr(v.get("B")))
    if t == "logic_operation":
        return "(%s %s %s)" % (_expr(v.get("A")), {"AND":"y","OR":"o"}.get(f.get("OP"), f.get("OP")), _expr(v.get("B")))
    if t == "logic_negate": return "no(%s)" % _expr(v.get("BOOL"))
    if t == "math_js_round": return "redondeo(%s)" % _expr(v.get("ARG0"))
    if t == "device_note":
        nm = f.get("name", "?")
        try: return NOTE.get(int(nm), "%s Hz" % nm)
        except Exception: return "%s Hz" % nm
    pf = pxt_fill(el)
    return pf if pf is not None else t

def _render(block, indent, out):
    pad = "  " * indent
    while block is not None:
        t = block.get("type"); f, v, s, n, c = _parts(block)
        if t == "controls_if":
            i = 0; first = True
            while ("IF%d" % i) in v or ("DO%d" % i) in s:
                cond = _expr(v.get("IF%d" % i)) if ("IF%d" % i) in v else "?"
                line = pad + (BK["if"] if first else BK["elseif"]).format(cond) + ":"
                if first and c: line += "   // " + c.replace("\n", " ")   # comentario en línea, sobre el bloque
                out.append(line); first = False
                if s.get("DO%d" % i) is not None: _render(s.get("DO%d" % i), indent + 1, out)
                i += 1
            if s.get("ELSE") is not None: out.append(pad + BK["else"] + ":"); _render(s.get("ELSE"), indent + 1, out)
            block = n; continue
        if t == "device_show_leds":
            out.append(pad + (pxt_fill(block) or "mostrar LEDs") + ":" + ("   // " + c.replace("\n", " ") if c else ""))
            for row in _leds(f.get("LEDS", "")): out.append(pad + "    " + row)
            block = n; continue
        if t == "pxt-on-start":            head = BK["on_start"]
        elif t == "controls_repeat_ext":   head = BK["repeat"].format(_expr(v.get("TIMES")))
        elif t == "pxt_controls_for":      head = BK["for"].format(_expr(v.get("VAR")), _expr(v.get("TO")))
        elif t == "device_while":          head = BK["while"].format(_expr(v.get("COND")))
        elif t == "variables_set":         head = BK["set"].format(f.get("VAR", "?"), _expr(v.get("VALUE")))
        elif t == "variables_change":      head = BK["change"].format(f.get("VAR", "?"), _expr(v.get("VALUE")))
        else:
            head = pxt_fill(block) or ("(%s)" % t)
        bodies = [b for b in s.values() if b is not None]
        line = pad + head + (":" if bodies else "")
        if c: line += "   // " + c.replace("\n", " ")               # comentario en línea, sobre el bloque
        out.append(line)
        for b in bodies: _render(b, indent + 1, out)
        block = n

def render_blocks(xml, slug, meta):
    root = ET.fromstring(xml)
    out = ["ACTIVIDAD: %s" % slug, "FUENTE: micro:bit / MakeCode %s — \"%s\"  (etiquetas oficiales es-ES)" % (meta.get("eVER", "?"), meta.get("name", "?")), ""]
    for ch in root:
        if _strip(ch.tag) in ("block", "shadow"): _render(ch, 0, out); out.append("")
    return "\n".join(out)

if __name__ == "__main__":
    if not STR:
        print("ATTENZIONE: stringhe locale non trovate in microbit/_locales/es/ (scaricale da cdn.makecode.com)")
    only = sys.argv[1:] or [s for s, _ in ACTS]
    for slug, code in ACTS:
        if slug not in only: continue
        path = os.path.join(BASE, code + ".hex")
        try:
            meta, header, files = extract(path)
            ts = files.get("main.ts", ""); bx = files.get("main.blocks", "")
            open(os.path.join(DEC, slug + ".ts"), "w", encoding="utf-8").write(ts)
            if bx:
                open(os.path.join(DEC, slug + ".blocks.xml"), "w", encoding="utf-8").write(bx)
                txt = render_blocks(bx, slug, meta)
                open(os.path.join(DEC, slug + ".blocks.txt"), "w", encoding="utf-8").write(txt)
            print("OK  %-34s [%s]  (MakeCode %s)" % (slug, meta.get("name", "?"), meta.get("eVER", "?")))
        except FileNotFoundError: print("ERR %-34s file non trovato: %s.hex" % (slug, code))
        except Exception as e: print("ERR %-34s %s" % (slug, e))
