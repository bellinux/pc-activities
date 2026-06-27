"""Ejecuta el pipeline algorítmico (SVG + métricas) para TODAS las actividades.
Uso (en el env conda con graphviz):
    conda run -n pdg-vela python run_all.py
Lee pdg_makecode.json / pdg_protobject.json de cada carpeta, renderiza los SVG y
guarda metricas.json. Robusto: errores por actividad no detienen el resto."""
import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdg_engine import build_graph_from_json, render_pdg, compare_pdgs, normalize_pdg

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../reporte
ACTS_DIR = os.path.join(BASE, 'actividades')

CODES = [
    'xilofono-inclinacion', 'luci-discoteca-ruido', 'xilofono-inclinacion-con-nota-led',
    'corazon-forever-loop', 'robot-risa-simpatica-al-ruido', 'corazon-variables-eventos',
    'alarma-caja-galletas', 'despertador-por-la-manana', 'luces-de-fiesta-al-oscurecer',
    'juego-toques', 'luz-encendida-al-ruido', 'flama-vela-con-soplo', 'papas-caliente-juego',
    'luz-encendida-ruido-animacion', 'metronomo-con-inclinacion', 'aplausometro-tiempo-aplausos',
    'nivel-con-ruido',
]


def run_one(code):
    d = os.path.join(ACTS_DIR, code)
    pa = os.path.join(d, 'pdg_makecode.json')
    pb = os.path.join(d, 'pdg_protobject.json')
    if not (os.path.exists(pa) and os.path.exists(pb)):
        return (code, 'SKIP', 'faltan pdg_*.json')
    with open(pa, 'r', encoding='utf-8') as f:
        ja = json.load(f)
    with open(pb, 'r', encoding='utf-8') as f:
        jb = json.load(f)
    # canonicalizar la var de las aristas de datos (determinista) y reescribir,
    # para que los .json queden limpios y reproducibles (tilt_1 / pitch / value)
    normalize_pdg(ja)
    normalize_pdg(jb)
    with open(pa, 'w', encoding='utf-8') as f:
        json.dump(ja, f, indent=4, ensure_ascii=False)
    with open(pb, 'w', encoding='utf-8') as f:
        json.dump(jb, f, indent=4, ensure_ascii=False)
    Ga = build_graph_from_json(ja)
    Gb = build_graph_from_json(jb)
    render_pdg(Ga, os.path.join(d, 'pdg_makecode'))
    render_pdg(Gb, os.path.join(d, 'pdg_protobject'))
    metrics = compare_pdgs(Ga, Gb)
    with open(os.path.join(d, 'metricas.json'), 'w', encoding='utf-8') as f:
        json.dump(metrics, f, indent=4)
    return (code, 'OK', "iso=%s ged=%s N=%s/%s E=%s/%s" % (
        metrics['isomorphic'], metrics['graph_edit_distance'],
        metrics['nodes_G1'], metrics['nodes_G2'], metrics['edges_G1'], metrics['edges_G2']))


if __name__ == '__main__':
    results = []
    for code in CODES:
        try:
            results.append(run_one(code))
        except Exception as e:
            results.append((code, 'ERROR', repr(e)))
        c, st, info = results[-1]
        print("[%-5s] %-34s %s" % (st, c, info), flush=True)
    ok = sum(1 for _, s, _ in results if s == 'OK')
    print("\n=== %d/%d OK ===" % (ok, len(CODES)))
