# -*- coding: utf-8 -*-
# Rende i .ptj Protobject come i BLOCCHI, con le ETICHETTE UFFICIALI in spagnolo.
#
# Fonte delle stringhe: protobject/_locale/es/ (file dell'editor Protobject):
#   - blockly_standard.js : Blockly.Msg["KEY"] = "..."  (blocchi standard: bucle/si/variables/math)
#   - custom_blocks.js    : locutions.blocks.*           (mainLoop, on start, retraso, suoni, note, batteria)
#   - es_devices.js       : locutions.<dispositivo>.*    (DibujoLED, Inclinación, ReproductorSonido, ...)
# Questi 3 file danno le PAROLE; l'ORDINE/struttura dei blocchi-dispositivo è ricostruito
# con regole dedotte da quei file e dall'editor (es. suffisso "en <Dispositivo>", getter
# "<prop> in <Dispositivo>", variante play vs playNumber a seconda dell'input).
#
# Riproducibile: legge equivalent-<code>.ptj (i file ufficiali) e ricostruisce; se le
# attività cambiano, basta ri-eseguire.  Output: decoded/<slug>.blocks.txt
import os, re, sys, json
import xml.etree.ElementTree as ET
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

BASE = os.path.dirname(os.path.abspath(__file__))
LOC = os.path.join(BASE, "_locale", "es")
DEC = os.path.join(BASE, "decoded"); os.makedirs(DEC, exist_ok=True)

ACTS = {"02.1-xylophone":"xilofono-inclinacion","02.2-music-visualizer":"luci-discoteca-ruido",
 "03.1-led-xylophone":"xilofono-inclinacion-con-nota-led","04.1-heart-beat":"corazon-forever-loop",
 "14.1-ticklish-robot":"robot-risa-simpatica-al-ruido","14.2-my-robot-friend-heart":"corazon-variables-eventos",
 "16.1-cookie-thief-alarm":"alarma-caja-galletas","16.2-sunflower-alarm-clock":"despertador-por-la-manana",
 "16.3-bat-in-the-dark":"luces-de-fiesta-al-oscurecer","16.4-robot-activation-challenge":"juego-toques",
 "16.5-magic-clap-switch":"luz-encendida-al-ruido","17.1-magic-birthday-candle":"flama-vela-con-soplo",
 "19.1-digital-hot-potato":"papas-caliente-juego","21.1-cinematic-power-on":"luz-encendida-ruido-animacion",
 "22.1-dj-metronome":"metronomo-con-inclinacion","22.2-applause-battle":"aplausometro-tiempo-aplausos",
 "22.3-dont-spill-liquid-game":"nivel-con-ruido"}

# ---------- parser puro-Python dei file locale ----------
def load_msg(path):
    out = {}
    for m in re.finditer(r'Blockly\.Msg\["([^"]+)"\]\s*=\s*"((?:\\.|[^"\\])*)"', open(path, encoding="utf-8").read()):
        v = re.sub(r"\\u([0-9a-fA-F]{4})", lambda x: chr(int(x.group(1), 16)), m.group(2))
        out[m.group(1)] = v.replace('\\"', '"').replace("\\\\", "\\").replace("\\n", "\n")
    return out

def load_locutions(path):
    s = open(path, encoding="utf-8").read()
    i = s.index("{", s.index("locutions"))
    def ws(i):
        while i < len(s):
            if s[i] in " \t\r\n,": i += 1
            elif s[i:i+2] == "//":
                while i < len(s) and s[i] != "\n": i += 1
            else: break
        return i
    def string(i):
        q = s[i]; i += 1; out = []
        while s[i] != q:
            if s[i] == "\\":
                n = s[i+1]
                if n == "u": out.append(chr(int(s[i+2:i+6], 16))); i += 6
                else: out.append({"n":"\n","t":"\t","r":"\r"}.get(n, n)); i += 2
            else: out.append(s[i]); i += 1
        return "".join(out), i+1
    def obj(i):                       # s[i] == '{'
        o = {}; i += 1
        while True:
            i = ws(i)
            if s[i] == "}": return o, i+1
            j = i
            while s[j] not in ":" and s[j] not in " \t\r\n": j += 1
            key = s[i:j].strip().strip("\"'"); i = ws(j)
            assert s[i] == ":"; i = ws(i+1)
            if s[i] == "{": val, i = obj(i)
            elif s[i] in "\"'": val, i = string(i)
            else:
                j = i
                while s[j] not in ",}\n": j += 1
                val = s[i:j].strip(); i = j
            o[key] = val
    return obj(i)[0]

MSG = load_msg(os.path.join(LOC, "blockly_standard.js"))
CUST = load_locutions(os.path.join(LOC, "custom_blocks.js"))["blocks"]
DEV = load_locutions(os.path.join(LOC, "es_devices.js"))

# componente -> categoria dispositivo (in es_devices)
CAT = {"DibujoLED":"matrixDraw","Inclinación":"smartphoneOrientation","ReproductorSonido":"audioPlayer",
 "BateríaMusical":"playDrum","NivelRuido":"noiseLevel","TecladoMusical":"playKeyboard",
 "IntensidadLuz":"lightIntensity","BotónTáctil":"touchButton","DibujarEscribir":"interactiveTurtleDraw"}
def midi_note(n):
    try: n = int(n)
    except Exception: return str(n)
    names = ["do","do#","re","re#","mi","fa","fa#","sol","sol#","la","la#","si"]
    return "%s%d" % (names[n % 12], n // 12 - 1)

# ---------- .ptj -> XML ----------
def ptj_xml(path):
    raw = open(path, encoding="utf-8").read().strip()
    s = json.loads(raw[raw.index("(")+1: raw.rindex(")")])
    return s[s.index("\n")+1:]

# ---------- parsing Blockly ----------
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
def _matrix(csv):
    vals = csv.split(",")
    if len(vals) != 49: return ["[matriz %d]" % len(vals)]
    return ["".join("#" if vals[r*7+c] not in ("0", "") else "." for c in range(7)) for r in range(7)]
def _par(x):                          # avvolge in () evitando doppie parentesi
    return x if x.startswith("(") and x.endswith(")") else "(%s)" % x
def _dev(t):
    rest = t[len("protobject_"):]; parts = rest.split("_")
    comp = parts[0]; base = re.sub(r"\d+$", "", comp)
    if rest.endswith("_get"): return comp, base, "get", "get"
    if rest.endswith("_change"): return comp, base, "change", "change"
    return comp, base, (parts[1] if len(parts) > 1 else ""), "set"

def _expr(el):
    if el is None: return "?"
    t = el.get("type"); f, v, s, n, c = _parts(el)
    if t == "math_number": return f.get("NUM", "?")
    if t == "logic_boolean": return MSG.get("LOGIC_BOOLEAN_TRUE", "true") if f.get("BOOL") == "TRUE" else MSG.get("LOGIC_BOOLEAN_FALSE", "false")
    if t == "text": return '"%s"' % f.get("TEXT", "")
    if t == "variables_get": return f.get("VAR", "?")
    if t == "math_arithmetic":
        return "(%s %s %s)" % (_expr(v.get("A")), {"ADD":"+","MINUS":"−","MULTIPLY":"×","DIVIDE":"÷","POWER":"^"}.get(f.get("OP"), f.get("OP")), _expr(v.get("B")))
    if t == "logic_compare":
        return "(%s %s %s)" % (_expr(v.get("A")), {"EQ":"=","NEQ":"≠","LT":"<","LTE":"≤","GT":">","GTE":"≥"}.get(f.get("OP"), f.get("OP")), _expr(v.get("B")))
    if t == "logic_operation":
        op = MSG.get("LOGIC_OPERATION_AND", "y") if f.get("OP") == "AND" else MSG.get("LOGIC_OPERATION_OR", "o")
        return "(%s %s %s)" % (_expr(v.get("A")), op, _expr(v.get("B")))
    if t == "logic_negate": return MSG.get("LOGIC_NEGATE_TITLE", "no %1").replace("%1", _par(_expr(v.get("BOOL"))))
    if t == "math_round":
        key = {"ROUND":"MATH_ROUND_OPERATOR_ROUND","ROUNDUP":"MATH_ROUND_OPERATOR_ROUNDUP","ROUNDDOWN":"MATH_ROUND_OPERATOR_ROUNDDOWN"}.get(f.get("OP"), "MATH_ROUND_OPERATOR_ROUND")
        return "%s%s" % (MSG.get(key, "redondear"), _par(_expr(v.get("NUM"))))
    if t == "math_random_int":
        return MSG.get("MATH_RANDOM_INT_TITLE", "%1..%2").replace("%1", _expr(v.get("FROM"))).replace("%2", _expr(v.get("TO")))
    if t == "math_constrain":
        return MSG.get("MATH_CONSTRAIN_TITLE", "limitar %1 %2 %3").replace("%1", _expr(v.get("VALUE"))).replace("%2", _expr(v.get("LOW"))).replace("%3", _expr(v.get("HIGH")))
    if t == "color_light": return "%s %s" % (CUST["color"]["clarityAt"], _expr(v.get("LEVEL")))
    if t == "colour_picker": return f.get("COLOUR", "color")
    if t == "sounds_list":
        sid = f.get("VAR", "").split(".")[0]; return "'%s'" % CUST["sounds"].get(sid, sid)
    if t == "protobject_milliseconds": return CUST["timing"]["milliseconds"]   # reporter tempo corrente (etichetta da confermare)
    if t == "control_note": return midi_note(f.get("VAR", "?"))
    if t == "control_drum":
        return {"0":CUST["music"]["drumBass"],"1":CUST["music"]["drumTom"],"2":CUST["music"]["drumHi"]}.get(f.get("VAR"), "tambor %s" % f.get("VAR"))
    if t.startswith("protobject_") and t.endswith("_get"):          # getter: "<prop> in <Disp>"
        comp, base, action, kind = _dev(t); loc = DEV.get(CAT.get(base), {}); prop = f.get("property", "")
        pk = {"lightIntensity":"light"}.get(prop, prop)   # IntensidadLuz: property 'lightIntensity' -> palabra 'light'
        word = loc.get(pk) or loc.get(prop) or prop
        return "%s in %s" % (word, comp)
    return t

def _devbody(comp, base, action, fields, values):
    cat = CAT.get(base); d = DEV.get(cat, {})
    def E(k): return _expr(values.get(k))
    enC = "%s %s" % (d.get("onTxt") or d.get("inTxt") or "en", comp)   # suffisso "en <Dispositivo>"
    if cat == "matrixDraw":
        if action == "drawOnXY": return "%s %s %s %s %s %s %s" % (d["drawOn"], E("VAR"), d["yTxt"], E("VAR2"), d["withColour"], E("VAR3"), enC)
        if action == "draw":     return ("%s %s %s %s" % (d["draw"], d["withColour"], E("VAR2"), enC), values.get("VAR"))
        if action == "clear":    return "%s %s" % (d["clear"], enC)
        if action == "background": return "%s %s %s" % (d["setBg"], E("VAR"), enC)
    if cat == "audioPlayer":
        if action == "play": return "%s %s %s" % (d["play"], E("VAR"), enC)
        if action == "stop": return "%s %s" % (d["stop"], comp)
    if cat in ("playKeyboard", "playDrum"):
        if action == "play":                                          # variante dedotta dall'input
            var = values.get("VAR"); picker = var is not None and var.get("type") in ("control_note", "control_drum")
            return "%s %s %s" % (d["play"] if picker else d["playNumber"], E("VAR"), enC)
        if action == "stop": return "%s %s" % (d["stop"], enC)
    if cat == "interactiveTurtleDraw":
        if action == "setSize": return "%s %s %s" % (d["setSize"], E("VAR"), enC)
        if action == "writeText": return "%s %s %s" % (d["write"], E("VAR"), enC)
        if action == "clear": return "%s %s" % (d["clear"], enC)
    return "%s %s %s" % (action, " ".join(E(k) for k in values), enC)

def _render(block, indent, out):
    pad = "  " * indent
    while block is not None:
        t = block.get("type"); f, v, s, n, c = _parts(block); matrix = None
        if t == "main_loop": head = CUST["loops"]["mainLoop"]
        elif t == "on_start": head = CUST["playPressed"]
        elif t == "protobject_sleep":
            unit = CUST["timing"]["milliseconds"] if f.get("timingType") == "ms" else CUST["timing"]["seconds"]
            head = "%s %s %s" % (CUST["timing"]["delayOf"], _expr(v.get("VAR")), unit)
        elif t == "controls_repeat_ext": head = MSG.get("CONTROLS_REPEAT_TITLE", "repetir %1").replace("%1", _expr(v.get("TIMES")))
        elif t == "controls_for":
            head = MSG.get("CONTROLS_FOR_TITLE", "contar %1 %2 %3 %4").replace("%1", f.get("VAR", "i")).replace("%2", _expr(v.get("FROM"))).replace("%3", _expr(v.get("TO"))).replace("%4", _expr(v.get("BY")))
        elif t == "controls_whileUntil":
            op = MSG.get("CONTROLS_WHILEUNTIL_OPERATOR_WHILE", "repetir mientras") if f.get("MODE") == "WHILE" else MSG.get("CONTROLS_WHILEUNTIL_OPERATOR_UNTIL", "repetir hasta")
            head = "%s %s" % (op, _expr(v.get("BOOL")))
        elif t == "variables_set": head = MSG.get("VARIABLES_SET", "establecer %1 a %2").replace("%1", f.get("VAR", "?")).replace("%2", _expr(v.get("VALUE")))
        elif t == "math_change": head = MSG.get("MATH_CHANGE_TITLE", "añadir %2 a %1").replace("%1", f.get("VAR", "?")).replace("%2", _expr(v.get("DELTA")))
        elif t == "controls_if":
            i = 0; first = True
            while ("IF%d" % i) in v or ("DO%d" % i) in s:
                cond = _expr(v.get("IF%d" % i)) if ("IF%d" % i) in v else "?"
                kw = MSG.get("CONTROLS_IF_MSG_IF", "si") if first else MSG.get("CONTROLS_IF_MSG_ELSEIF", "sino si")
                line = pad + "%s %s:" % (kw, cond)
                if first and c: line += "   // " + c.replace("\n", " ")   # comentario en línea, sobre el bloque
                out.append(line); first = False
                if s.get("DO%d" % i) is not None: _render(s.get("DO%d" % i), indent+1, out)
                i += 1
            if s.get("ELSE") is not None: out.append(pad + MSG.get("CONTROLS_IF_MSG_ELSE", "sino") + ":"); _render(s.get("ELSE"), indent+1, out)
            block = n; continue
        elif t.startswith("protobject_") and t.endswith("_change"):    # evento: "cuando <Disp> <evento>"
            comp, base, action, kind = _dev(t); prop = f.get("property", "")
            ev = DEV.get(CAT.get(base), {}).get(prop + "Ev", prop)
            head = "%s %s %s" % (CUST["events"]["on"], comp, ev)
        elif t.startswith("protobject_"):                             # azione dispositivo
            comp, base, action, kind = _dev(t); r = _devbody(comp, base, action, f, v)
            if isinstance(r, tuple): head, matrix = r
            else: head = r
        else: head = "(%s)" % t
        bodies = [b for b in s.values() if b is not None]
        line = pad + head + (":" if bodies or matrix is not None else "")
        if c: line += "   // " + c.replace("\n", " ")               # comentario en línea, sobre el bloque
        out.append(line)
        if matrix is not None:
            mf = _parts(matrix)[0]
            for row in _matrix(mf.get("btmMatrix", "")): out.append(pad + "    " + row)
        for b in bodies: _render(b, indent+1, out)
        block = n

def render(xml, slug):
    root = ET.fromstring(xml); out = ["ACTIVIDAD: %s" % slug, "FUENTE: Protobject (bloques, etiquetas oficiales es)", ""]
    for ch in root:
        if _strip(ch.tag) in ("block", "shadow"): _render(ch, 0, out); out.append("")
    return "\n".join(out)

if __name__ == "__main__":
    only = sys.argv[1:] or list(ACTS)
    for slug in ACTS:
        if slug not in only: continue
        try:
            xml = ptj_xml(os.path.join(BASE, "equivalent-%s.ptj" % ACTS[slug]))
            open(os.path.join(DEC, slug + ".blocks.txt"), "w", encoding="utf-8").write(render(xml, slug))
            print("OK  %s" % slug)
        except Exception as e:
            print("ERR %s: %s" % (slug, e))
