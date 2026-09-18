# -*- coding: utf-8 -*-
"""Importa a este repo los .ptj de la app con los comentarios reescritos.

Fuente: app.protobject.com/public/ptj/eq-<code>.ptj (la copia de catalogo de
la app, donde el autor mejoro los comentarios en agosto de 2026). Destino:
protobject/equivalent-<code>.ptj, los archivos oficiales de este trabajo, que
fond.protobject.com sirve a las vistas incrustadas.

Revisado el 18-09-2026, actividad por actividad y con un segundo revisor
esceptico por lote:
  - el PROGRAMA es identico en las 17 (mismos bloques, misma lista de
    componentes); solo cambian los comentarios;
  - los comentarios son trilingues ([it]...[it][en]...[en][es]...[es]) y la
    app muestra solo el idioma de la pagina;
  - 16 de las 17 mejoran; la papa (papas-caliente-juego) tiene el mismo
    comentario y no se importa;
  - 26 problemas en el ESPANOL, corregidos aqui en 21 comentarios (los otros
    dos comentarios afectados son los del xilofono que reescribe
    xilofono_a_hz.py): bloques nombrados con una etiqueta que el estudiante no
    ve («esperar» es «retraso de», «si ... entonces» es «si ... hacer»),
    «teléfono» por «celular», y algunos datos inexactos.

Cada correccion comprueba el texto espanol que reemplaza antes de tocarlo. Las
partes en italiano e ingles no se tocan.

    python importar_de_la_app.py          (desde protobject/)
"""
import io
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
# protobject/ -> activities-equivalence -> Fondccyt -> Work-in-progress -> Protobject
APP = os.path.normpath(os.path.join(BASE, "..", "..", "..", "..", "app.protobject.com", "public", "ptj"))

IMPORT = [
    "corazon-forever-loop", "xilofono-inclinacion", "xilofono-inclinacion-con-nota-led",
    "luci-discoteca-ruido", "robot-risa-simpatica-al-ruido", "alarma-caja-galletas",
    "despertador-por-la-manana", "luces-de-fiesta-al-oscurecer", "juego-toques",
    "corazon-variables-eventos", "flama-vela-con-soplo", "nivel-con-ruido",
    "luz-encendida-al-ruido", "luz-encendida-ruido-animacion", "metronomo-con-inclinacion",
    "gritometro-tiempo-gritos",
]

# (code, n.º de comentario en orden de documento, espanol actual, espanol corregido)
FIXES = [
    ("corazon-forever-loop", 2,
     "El bloque 'esperar' hace una pausa del tiempo que tú elijas antes de pasar a la orden siguiente.",
     "El bloque 'retraso de' hace una pausa del tiempo que tú elijas antes de pasar a la orden siguiente."),

    ("xilofono-inclinacion", 4,
     "Entrega cuánto está inclinado el teléfono en el eje y.",
     "Entrega cuánto está inclinado el celular en el eje y."),
    ("xilofono-inclinacion", 5,
     "El bloque 'esperar' hace una pausa de 0.1 segundos, así puedes tocar muchos sonidos distintos en poco tiempo.",
     "El bloque 'retraso de' hace una pausa de 100 milisegundos (0,1 segundos), así puedes tocar muchos sonidos "
     "distintos en poco tiempo."),
    # los comentarios 2 y 3 del xilofono los reescribe xilofono_a_hz.py, en hercios

    ("xilofono-inclinacion-con-nota-led", 1,
     "Dibuja un punto según la inclinación: mientras más inclinas el teléfono, más cerca de los bordes aparece el punto.",
     "Dibuja un punto según la inclinación: mientras más inclinas el celular, más cerca de los bordes aparece el "
     "punto; si lo inclinas demasiado, se sale de la pantalla y no se ve."),
    ("xilofono-inclinacion-con-nota-led", 2,
     "Convierte la inclinación del teléfono en la posición del punto, usando los ejes x e y.",
     "Convierte la inclinación del celular en la posición del punto en el eje y (el eje x queda fijo en 4)."),

    ("luci-discoteca-ruido", 1,
     "Borra la pantalla antes de dibujar otra vez, para que la barra nueva no se encime con la anterior.",
     "Borra la pantalla antes de dibujar otra vez, para que la luz anterior no quede encendida."),
] + [
    ("luci-discoteca-ruido", k,
     "Dibuja en la columna X una barra tan alta como el ruido; el valor se divide para que quepa en la matriz de LEDs.",
     "Dibuja en la columna X una luz, más arriba cuanto más ruido hay; el valor se divide para que quepa en la "
     "matriz de LEDs.")
    for k in (2, 3, 4)
] + [
    ("robot-risa-simpatica-al-ruido", 1,
     "Cuando el micrófono oye un sonido fuerte, se ejecuta todo lo que está dentro de este bloque.",
     "Cuando el ruido sube de golpe (por ejemplo, con un aplauso), se ejecuta todo lo que está dentro de este bloque."),
    ("robot-risa-simpatica-al-ruido", 3,
     "Corta el sonido por si todavía está sonando, para que no suene cuando no debe.",
     "Corta la risa; sin este bloque, el sonido se repetiría sin parar."),

    ("alarma-caja-galletas", 1,
     "El bloque 'si … entonces' mira la inclinación: cuando pasa del valor elegido, se ejecuta todo lo que está "
     "dentro del bloque.",
     "El bloque 'si … hacer' mira la inclinación: cuando pasa del valor elegido, se ejecuta todo lo que está "
     "dentro del bloque; si no, se lo salta."),

    ("luces-de-fiesta-al-oscurecer", 1,
     "Bloque 'si … entonces … si no' con dos caminos: si hay oscuridad se ejecuta la animación de luz, y si hay "
     "claridad los LEDs se quedan apagados.",
     "Bloque 'si … hacer … sino' con dos caminos: si hay oscuridad se ejecuta la animación de luz, y si hay "
     "claridad los LEDs se quedan apagados."),

    ("corazon-variables-eventos", 1,
     "El bloque 'esperar' aguarda los milisegundos que guarda la variable 'pausaLarga': cambia esa variable y el "
     "corazón grande late más rápido o más lento.",
     "El bloque 'retraso de' espera los milisegundos que guarda la variable 'pausaLarga': cambia esa variable y el "
     "corazón grande late más rápido o más lento."),
    ("corazon-variables-eventos", 2,
     "El bloque 'esperar' aguarda los milisegundos que guarda la variable 'pausaCorta': así de rápido late el "
     "corazón chico.",
     "El bloque 'retraso de' espera los milisegundos que guarda la variable 'pausaCorta': así de rápido late el "
     "corazón chico."),

    ("nivel-con-ruido", 2,
     "Convertimos la inclinación del celular, ya desplazada en 'xDesplazado', en un número del 1 al 8 y lo "
     "guardamos en la variable 'ledX': es la posición del LED que se encenderá.",
     "Convertimos la inclinación del celular, ya desplazada en 'xDesplazado', en un número del 1 al 7 y lo "
     "guardamos en la variable 'ledX': es la posición del LED que se encenderá."),
    ("nivel-con-ruido", 3,
     "Este 'si … entonces' pregunta si 'centradoX' y 'centradoY' son verdaderas a la vez: si es así, el celular "
     "está nivelado.",
     "Este bloque 'si' pregunta si 'centradoX' y 'centradoY' son verdaderas a la vez: si es así, el celular "
     "está nivelado."),

    ("luz-encendida-al-ruido", 1,
     "El bloque 'no' da vuelta el valor de la variable 'estado': si era verdadero lo pone falso, y si era falso lo "
     "pone verdadero, con cada ruido fuerte.",
     "El bloque 'no' entrega lo contrario de 'estado' y 'establecer estado a' lo guarda: si era verdadero queda "
     "falso, y si era falso queda verdadero, con cada ruido fuerte."),

    ("gritometro-tiempo-gritos", 2,
     "Encendemos un LED rojo en la columna y la fila de ahora: cuanto más largo es el grito, más LEDs se encienden.",
     "Encendemos un LED rojo en la columna y la fila de ahora: cuanto más largo es el grito, más LEDs se encienden, "
     "hasta llenar la matriz."),
    ("gritometro-tiempo-gritos", 3,
     "'esperar' medio segundo antes del siguiente LED, así cada LED encendido vale medio segundo de grito.",
     "'retraso de 500 milisegundos' espera medio segundo antes del siguiente LED, así cada LED encendido vale "
     "medio segundo de grito."),
    ("gritometro-tiempo-gritos", 6,
     "'cuando el ruido cambia de golpe' avisa que alguien ha empezado a gritar, y entonces ponemos "
     "'partidaEnCurso' en verdadero.",
     "'cuando NivelRuido2 detecta aumento repentino' avisa que alguien ha empezado a gritar, y entonces ponemos "
     "'partidaEnCurso' en verdadero."),
]

COMMENT = re.compile(r"(<comment[^>]*>)(.*?)(</comment>)", re.S)
ES = re.compile(r"\[es\](.*?)\[es\]", re.S)


def load(path):
    raw = io.open(path, encoding="utf-8").read().strip()
    m = re.match(r'^oPTJ\((".*")\)\s*;?\s*$', raw, re.S)
    if not m:
        sys.exit("formato inesperado: %s" % path)
    return raw, json.loads(m.group(1))


def dump(inner):
    return "oPTJ(%s)" % json.dumps(inner, ensure_ascii=False)


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def unesc(t):
    return t.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


def fix_comment(inner, n, old, new, code):
    matches = list(COMMENT.finditer(inner))
    if n > len(matches):
        sys.exit("%s: no hay comentario %d" % (code, n))
    m = matches[n - 1]
    body = m.group(2)
    e = ES.search(body)
    if not e:
        sys.exit("%s #%d: el comentario no tiene parte [es]" % (code, n))
    current = re.sub(r"\s+", " ", unesc(e.group(1))).strip()
    if current != old:
        sys.exit("%s #%d: el espanol no es el revisado\n  esperado: %s\n  hallado:  %s" % (code, n, old, current))
    body = body[:e.start(1)] + esc(new) + body[e.end(1):]
    return inner[:m.start(2)] + body + inner[m.end(2):]


def main():
    fixes_by_code = {}
    for code, n, old, new in FIXES:
        fixes_by_code.setdefault(code, []).append((n, old, new))

    for code in IMPORT:
        src = os.path.join(APP, "eq-%s.ptj" % code)
        dst = os.path.join(BASE, "equivalent-%s.ptj" % code)
        raw, inner = load(src)
        if dump(inner) != raw:
            sys.exit("%s: el archivo de la app no sobrevive a leer y escribir sin cambios" % code)
        for n, old, new in fixes_by_code.get(code, []):
            inner = fix_comment(inner, n, old, new, code)
        io.open(dst, "w", encoding="utf-8", newline="").write(dump(inner))
        print("  importado %-36s correcciones: %d" % (code, len(fixes_by_code.get(code, []))))
    left = set(fixes_by_code) - set(IMPORT)
    if left:
        sys.exit("correcciones para actividades no importadas: %s" % sorted(left))
    print("importadas: %d  correcciones: %d" % (len(IMPORT), len(FIXES)))


if __name__ == "__main__":
    main()
