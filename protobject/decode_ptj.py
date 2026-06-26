# -*- coding: utf-8 -*-
import json, re, os, sys
import xml.etree.ElementTree as ET

# (slug, code) nell'ordine della sequenza didattica
ACTS = [
    ("02.1-xylophone", "xilofono-inclinacion"),
    ("02.2-music-visualizer", "luci-discoteca-ruido"),
    ("03.1-led-xylophone", "xilofono-inclinacion-con-nota-led"),
    ("04.1-heart-beat", "corazon-forever-loop"),
    ("14.1-ticklish-robot", "robot-risa-simpatica-al-ruido"),
    ("14.2-my-robot-friend-heart", "corazon-variables-eventos"),
    ("16.1-cookie-thief-alarm", "alarma-caja-galletas"),
    ("16.2-sunflower-alarm-clock", "despertador-por-la-manana"),
    ("16.3-bat-in-the-dark", "luces-de-fiesta-al-oscurecer"),
    ("16.4-robot-activation-challenge", "juego-toques"),
    ("16.5-magic-clap-switch", "luz-encendida-al-ruido"),
    ("17.1-magic-birthday-candle", "flama-vela-con-soplo"),
    ("19.1-digital-hot-potato", "papas-caliente-juego"),
    ("21.1-cinematic-power-on", "luz-encendida-ruido-animacion"),
    ("22.1-dj-metronome", "metronomo-con-inclinacion"),
    ("22.2-applause-battle", "aplausometro-tiempo-aplausos"),
    ("22.3-dont-spill-liquid-game", "nivel-con-ruido"),
]

BASE = os.path.dirname(os.path.abspath(__file__))
PTJ = BASE                            # i .ptj stanno nella ROOT di protobject/
PTJ_PREFIX = "equivalent-"            # i file locali .ptj hanno questo prefisso (il code remoto NO)
RAW = os.path.join(BASE, "raw");      os.makedirs(RAW, exist_ok=True)   # solo .xml (Blockly estratto)
DEC = os.path.join(BASE, "decoded");  os.makedirs(DEC, exist_ok=True)   # .txt (pseudocodice)

def fetch(code):
    # I .ptj locali (equivalent-<code>.ptj) sono i file UFFICIALI: si leggono, NON si scaricano più.
    path = os.path.join(PTJ, PTJ_PREFIX + code + ".ptj")
    if not os.path.exists(path):
        raise FileNotFoundError("Falta el .ptj oficial: %s" % os.path.basename(path))
    return open(path, encoding="utf-8").read().strip()

def split_ptj(raw):
    inner = raw[raw.index("(")+1: raw.rindex(")")]
    s = json.loads(inner)
    nl = s.index("\n")
    comps = json.loads(s[:nl])
    xml = s[nl+1:]
    return comps, xml

def strip_ns(t):
    return t.split("}", 1)[1] if "}" in t else t

def matrix_art(csv):
    # 49 valori -> griglia 7x7 con # / .
    v = csv.split(",")
    if len(v) != 49:
        return "matriz(%d valores)" % len(v)
    rows = ["".join("#" if v[r*7+c] not in ("0","") else "." for c in range(7)) for r in range(7)]
    return "\n".join("        " + r for r in rows)

def child_blocks(el):
    # ritorna dict: fields, values, statements, next, comment, per un <block>/<shadow>
    fields, values, stmts, nxt, comment = {}, {}, {}, None, None
    for ch in el:
        tag = strip_ns(ch.tag)
        if tag == "field":
            fields[ch.get("name")] = (ch.text or "").strip()
        elif tag == "value":
            b = first_block(ch)
            if b is not None: values[ch.get("name")] = b
        elif tag == "statement":
            b = first_block(ch)
            if b is not None: stmts[ch.get("name")] = b
        elif tag == "next":
            nxt = first_block(ch)
        elif tag == "comment":
            comment = (ch.text or "").strip()
    return fields, values, stmts, nxt, comment

def first_block(el):
    # preferisci <block> (valore reale) a <shadow> (default)
    shadow = None
    for ch in el:
        tag = strip_ns(ch.tag)
        if tag == "block":
            return ch
        if tag == "shadow" and shadow is None:
            shadow = ch
    return shadow

def expr(el):
    # rende un blocco-valore (espressione) in una sola riga
    if el is None:
        return "?"
    t = el.get("type")
    f, v, s, n, c = child_blocks(el)
    if t == "math_number":
        return f.get("NUM", "?")
    if t == "logic_boolean":
        return f.get("BOOL", "?")
    if t == "text":
        return '"%s"' % f.get("TEXT", "")
    if t == "math_arithmetic":
        op = {"ADD":"+","MINUS":"-","MULTIPLY":"*","DIVIDE":"/","POWER":"^"}.get(f.get("OP"), f.get("OP"))
        return "(%s %s %s)" % (expr(v.get("A")), op, expr(v.get("B")))
    if t == "logic_compare":
        op = {"EQ":"==","NEQ":"!=","LT":"<","LTE":"<=","GT":">","GTE":">="}.get(f.get("OP"), f.get("OP"))
        return "(%s %s %s)" % (expr(v.get("A")), op, expr(v.get("B")))
    if t == "logic_operation":
        op = f.get("OP", "?")
        return "(%s %s %s)" % (expr(v.get("A")), op, expr(v.get("B")))
    if t == "logic_negate":
        return "no(%s)" % expr(v.get("BOOL"))
    if t == "math_random_int":
        return "aleatorio(%s..%s)" % (expr(v.get("FROM")), expr(v.get("TO")))
    if t == "variables_get":
        return "var:%s" % f.get("VAR", "?")
    if t and t.endswith("_get") and t.startswith("protobject_"):
        comp = t[len("protobject_"):-len("_get")]
        return "%s.leer(%s)" % (comp, f.get("property", ""))
    if t == "protobject_get_time":
        return "tiempoActual()"
    # fallback generico
    extra = " ".join("%s=%s" % (k, val) for k, val in f.items())
    if v:
        extra += " " + " ".join("%s=%s" % (k, expr(b)) for k, b in v.items())
    return "%s(%s)" % (t, extra.strip())

def clean_stmt_type(t, f, v):
    if t == "main_loop": return "REPETIR PARA SIEMPRE (bucle principal)"
    if t == "on_start" or t == "protobject_on_start": return "AL INICIAR"
    if t == "controls_repeat_ext": return "REPETIR %s VECES" % expr(v.get("TIMES"))
    if t == "controls_repeat": return "REPETIR %s VECES" % f.get("TIMES","?")
    if t == "controls_whileUntil":
        return "MIENTRAS (%s) %s" % (f.get("MODE",""), expr(v.get("BOOL")))
    if t == "controls_for":
        return "CONTAR CON %s DE %s A %s PASO %s" % (f.get("VAR","i"), expr(v.get("FROM")), expr(v.get("TO")), expr(v.get("BY")))
    if t == "controls_if": return "SI"
    if t == "variables_set": return "ESTABLECER var:%s = %s" % (f.get("VAR","?"), expr(v.get("VALUE")))
    if t == "math_change": return "AÑADIR %s A var:%s" % (expr(v.get("DELTA")), f.get("VAR","?"))
    if t == "protobject_sleep": return "ESPERAR %s %s" % (expr(v.get("time")) if "time" in v else f.get("NUM",""), f.get("timingType",""))
    if t and t.startswith("protobject_") and ("_play_" in t or "_draw_" in t or "_set" in t):
        comp = t[len("protobject_"):]
        return "%s" % comp
    return t

EVENT_HINT = ("event", "when", "cuando", "_on_", "touch", "tocado", "shake", "sound", "ruido", "tilt")

def render(block, indent, out):
    while block is not None:
        t = block.get("type")
        f, v, s, n, c = child_blocks(block)
        head = clean_stmt_type(t, f, v)
        # argomenti valore non già consumati
        line = "  "*indent + head
        # campi rilevanti non strutturali
        shown = set()
        for k, val in f.items():
            if k in ("timingType","VAR","TIMES","OP","MODE") : continue
            if k == "btmMatrix":
                line += "  [matriz]"
            elif k == "COLOUR":
                line += "  color=%s" % val
            else:
                line += "  %s=%s" % (k, val)
        # valori inline (es. play(...))
        for k, b in v.items():
            if k in ("TIMES","BOOL","FROM","TO","BY","DELTA","VALUE","A","B","time") or k.startswith("IF"): continue
            line += "  %s=%s" % (k, expr(b))
        out.append(line)
        if c:
            out.append("  "*indent + "    ; // " + c.replace("\n"," "))
        if t == "controls_if":
            # IF/DO0/ELSE
            i = 0
            while ("IF%d"%i) in v or ("DO%d"%i) in s:
                if ("IF%d"%i) in v:
                    out.append("  "*indent + "  [si %s]" % expr(v.get("IF%d"%i)))
                if ("DO%d"%i) in s:
                    render(s.get("DO%d"%i), indent+1, out)
                i += 1
            if "ELSE" in s:
                out.append("  "*indent + "  [sino]")
                render(s.get("ELSE"), indent+1, out)
        if "btmMatrix" in f:
            out.append(matrix_art(f["btmMatrix"]))
        # corpo dei blocchi non-condizionali (loop/eventi/al iniciar): rendi tutti gli statement
        if t != "controls_if":
            for name, b in s.items():
                render(b, indent+1, out)
        block = n

def decode_one(slug, code):
    comps, xml = split_ptj(fetch(code))
    open(os.path.join(RAW, code + ".xml"), "w", encoding="utf-8").write(xml)
    root = ET.fromstring(xml)
    out = []
    out.append("ACTIVIDAD: %s" % slug)
    out.append("CODE: %s" % code)
    out.append("COMPONENTES: " + ", ".join("%s=%s" % (c["name"], c["type"]) for c in comps))
    out.append("")
    for ch in root:
        if strip_ns(ch.tag) in ("block","shadow"):
            render(ch, 0, out)
            out.append("")
    txt = "\n".join(out)
    open(os.path.join(DEC, slug + ".txt"), "w", encoding="utf-8").write(txt)
    return comps, xml, txt

if __name__ == "__main__":
    only = sys.argv[1:] or [s for s, _ in ACTS]
    for slug, code in ACTS:
        if slug not in only:
            continue
        try:
            comps, xml, txt = decode_one(slug, code)
            print("OK  %-34s %4d char xml  %d componentes" % (slug, len(xml), len(comps)))
        except Exception as e:
            print("ERR %-34s %s" % (slug, e))
