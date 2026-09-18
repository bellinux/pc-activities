# -*- coding: utf-8 -*-
"""Los dos xilofonos pasan de «tocar nota numero» a «tocar frecuencia (Hz)».

Desde el 18-09-2026 el Teclado Musical de Protobject tiene el bloque
«tocar frecuencia N Hz en TecladoMusicalN», que en el archivo se guarda como
`protobject_TecladoMusicalN_frequency_set_4`. Con el, Protobject toca en
hercios como el «tono de timbre (Hz)» del micro:bit, y la diferencia de unidad
entre las dos versiones del xilofono desaparece.

Cambios, y solo estos, en cada archivo:
  1. el bloque de nota pasa a ser el de frecuencia (tipo e id);
  2. el valor por defecto oculto de su entrada pasa de 60 a 440, el del bloque
     nuevo en la aplicacion;
  3. la constante de la suma pasa de 60 (el Do central como numero de nota) a
     262 (el Do central en hercios, el mismo «Do medio» de MakeCode);
  4. en 02.2, los comentarios de esos dos bloques se reescriben en los tres
     idiomas que guarda el archivo, para que digan lo que el programa hace.

Por que 262: la inclinacion de Protobject da m/s2 x 10, entre -98 y 98 al
inclinar el celular. Con 262, la frecuencia queda entre 164 y 360 Hz: siempre
positiva, el reposo sigue en el Do central, y el barrido completo es algo mas
de una octava.

    python xilofono_a_hz.py            (desde protobject/)

Idempotente: si un archivo ya esta en hercios, no lo toca.
"""
import io
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = {
    "xilofono-inclinacion": True,                 # con comentarios que reescribir
    "xilofono-inclinacion-con-nota-led": False,   # sin comentarios en esos bloques
}

OLD_TYPE = "protobject_TecladoMusical1_play_set_2"
NEW_TYPE = "protobject_TecladoMusical1_frequency_set_4"
BASE_HZ = "262"

COMMENT_PLAY = (
    "[it]Questo blocco suona alla frequenza che gli dai, in hertz (Hz): più il numero è piccolo più il suono "
    "è grave, più è grande più è acuto. Con 0 o un numero negativo non suona niente.[it]"
    "[en]This block plays a sound at the frequency you give it, in hertz (Hz): the smaller the number, the "
    "lower the sound; the bigger, the higher. With 0 or a negative number it plays nothing.[en]"
    "[es]Este bloque toca un sonido de la frecuencia que le des, en hercios (Hz): cuanto más pequeño el "
    "número, más grave; cuanto más grande, más agudo. Con 0 o un número negativo no suena nada.[es]"
)
COMMENT_SUM = (
    "[it]Somma 262 all'inclinazione: 262 Hz è il Do centrale, il suono che senti con il telefono orizzontale. "
    "Inclinando il telefono, l'inclinazione va da −98 a 98, quindi la frequenza resta tra 164 e 360 Hz: "
    "sempre positiva.[it]"
    "[en]Adds 262 to the tilt: 262 Hz is middle C, the sound you hear with the phone flat. When you tilt the "
    "phone, the tilt goes from −98 to 98, so the frequency stays between 164 and 360 Hz: always "
    "positive.[en]"
    "[es]Suma 262 a la inclinación: 262 Hz es el Do central, el sonido que escuchas con el celular "
    "horizontal. Al inclinar el celular, la inclinación va de −98 a 98, así que la frecuencia queda entre "
    "164 y 360 Hz: siempre positiva.[es]"
)


def load(path):
    raw = io.open(path, encoding="utf-8").read().strip()
    m = re.match(r'^oPTJ\((".*")\)\s*;?\s*$', raw, re.S)
    if not m:
        sys.exit("formato inesperado: %s" % path)
    return json.loads(m.group(1))


def save(path, inner):
    io.open(path, "w", encoding="utf-8", newline="").write("oPTJ(%s)" % json.dumps(inner, ensure_ascii=False))


def set_comment(xml, block_open, text):
    """Pone `text` como comentario del bloque que empieza en `block_open`.

    El comentario de un bloque es su primer hijo <comment>, justo tras la
    etiqueta de apertura. Si no hay, se crea con el tamano de los demas.
    """
    i = xml.index(block_open) + len(block_open)
    esc = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    m = re.match(r'<comment([^>]*)>(.*?)</comment>', xml[i:], re.S)
    if m:
        return xml[:i] + '<comment%s>%s</comment>' % (m.group(1), esc) + xml[i + m.end():]
    return xml[:i] + '<comment pinned="false" h="116" w="320">%s</comment>' % esc + xml[i:]


def convert(code, rewrite_comments):
    path = os.path.join(BASE, "equivalent-%s.ptj" % code)
    inner = load(path)
    if NEW_TYPE in inner:
        print("  %s: ya toca en hercios, sin cambios" % code)
        return False
    if inner.count(OLD_TYPE) != 2:        # el tipo y el id del mismo bloque
        sys.exit("%s: esperaba un solo bloque de nota, encontre %d menciones" % (code, inner.count(OLD_TYPE)))

    comps, _, rest = inner.partition("\n")
    i = rest.find("<xml")
    head, xml = rest[:i], rest[i:]

    open_old = '<block type="%s" id="%s">' % (OLD_TYPE, OLD_TYPE)
    open_new = '<block type="%s" id="%s">' % (NEW_TYPE, NEW_TYPE)
    assert xml.count(open_old) == 1, code
    xml = xml.replace(open_old, open_new)

    # la entrada del bloque: su sombra por defecto (60 -> 440) y la suma
    j = xml.index(open_new)
    k = xml.index('<value name="VAR">', j)
    shadow = re.compile(r'(<shadow type="math_number" id="[^"]*"><field name="NUM">)60(</field></shadow>)')
    m = shadow.match(xml, k + len('<value name="VAR">'))
    assert m, "%s: no encuentro la sombra de la entrada" % code
    xml = xml[:m.start()] + m.group(1) + "440" + m.group(2) + xml[m.end():]

    # la suma: su entrada A es la constante
    a = xml.index('<block type="math_arithmetic"', k)
    add_open = xml[a:xml.index(">", a) + 1]
    va = xml.index('<value name="A">', a)
    m = shadow.match(xml, va + len('<value name="A">'))
    assert m, "%s: la constante de la suma no es 60" % code
    xml = xml[:m.start()] + m.group(1) + BASE_HZ + m.group(2) + xml[m.end():]

    if rewrite_comments:
        xml = set_comment(xml, open_new, COMMENT_PLAY)
        xml = set_comment(xml, add_open, COMMENT_SUM)

    save(path, comps + "\n" + head + xml)
    print("  %s: tocar frecuencia (%s + inclinación) Hz" % (code, BASE_HZ))
    return True


if __name__ == "__main__":
    for c, rw in FILES.items():
        convert(c, rw)
