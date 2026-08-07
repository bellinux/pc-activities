import networkx as nx
from networkx.algorithms import isomorphism
import graphviz
import json
from collections import defaultdict

COLORS = {
    'background': '#FBF6EB', 'ink': '#1A1612', 'ink_soft': '#4A3F33',
    'burgundy':   '#8B2418', 'ochre': '#B8843A', 'moss': '#5A6B3B',
    'slate':      '#34495e',
    'paper':      '#FBF6EB',
}
NODE_STYLES = {
    'ProgramStartEvent': {'fillcolor': COLORS['slate'], 'fontcolor': COLORS['paper']},
    'SuddenNoiseEvent':  {'fillcolor': COLORS['slate'], 'fontcolor': COLORS['paper']},
    'SetVariable':       {'fillcolor': COLORS['burgundy'], 'fontcolor': COLORS['paper']},
    'ToggleVariable':    {'fillcolor': COLORS['burgundy'], 'fontcolor': COLORS['paper']},
    'ConditionalBranch': {'fillcolor': COLORS['ochre'], 'fontcolor': COLORS['paper']},
    'DrawImage':         {'fillcolor': COLORS['moss'],  'fontcolor': COLORS['paper']},
    'RandomInteger':     {'fillcolor': COLORS['moss'],  'fontcolor': COLORS['paper']},
    'PlotPoint':         {'fillcolor': COLORS['moss'],  'fontcolor': COLORS['paper']},
    'Delay':             {'fillcolor': COLORS['ink_soft'], 'fontcolor': COLORS['paper']},
}
DEFAULT_NODE_STYLE = {'fillcolor': COLORS['paper'], 'fontcolor': COLORS['ink']}

def build_graph_from_json(json_data: dict) -> nx.MultiDiGraph:
    G = nx.MultiDiGraph(name=f"PDG_{json_data.get('platform', 'Unknown')}")
    
    for node in json_data.get('nodes', []):
        G.add_node(node['id'], kind=node['kind'], seq=node['seq'], in_loop=node['in_loop'],
                   op=node.get('op'), resId=node.get('resId'))
        
    for edge in json_data.get('edges', []):
        G.add_edge(edge['source'], edge['target'], type=edge['type'], var=edge['var'])

    return G


# --- Canonicalización determinista de la 'var' de las aristas de DATOS --------
# La var es plumbing: el eje (x/y), el encoding del pitch (frequency/nota) y los
# nombres intermedios (value/a/b) no deben distinguir plataformas. Se reescribe a
# una forma canónica reproducible:
#   valor de un sensor  -> "<sensor>_<resId>"  (p.ej. "tilt_1"; "tilt_2" si hay un 2º eje distinto)
#   altura de un tono   -> "pitch"             (no "frequency"/"nota")
#   intermedio genérico -> "value"
#   variable de usuario -> su nombre en minúsculas
SENSOR_CANON = {'ReadTilt': 'tilt', 'ReadSoundLevel': 'sound',
                'ReadLightLevel': 'light', 'ReadRuntimeMillis': 'time'}
PITCH_LABELS = {'frequency', 'freq', 'hz', 'nota', 'note', 'tono', 'tone', 'pitch'}
GENERIC_LABELS = {'x', 'y', 'z', 'eje', 'axis', 'value', 'val', 'a', 'b', 'c',
                  'result', 'res', 'n', 'num', 'index', 'i', 'arg', 'operand', ''}


def normalize_pdg(pdg: dict) -> dict:
    nodes = {n['id']: n for n in pdg.get('nodes', [])}
    for e in pdg.get('edges', []):
        if e.get('type') != 'data':
            continue
        src = nodes.get(e.get('source'), {})
        raw = (e.get('var') or '').strip().lower()
        if src.get('kind') in SENSOR_CANON:
            e['var'] = "%s_%s" % (SENSOR_CANON[src['kind']], src.get('resId') or 1)
        elif raw in PITCH_LABELS:
            e['var'] = 'pitch'
        elif raw in GENERIC_LABELS:
            e['var'] = 'value'
        else:
            e['var'] = raw
    return pdg

def render_pdg(G: nx.MultiDiGraph, output_path: str) -> str:
    dot = graphviz.Digraph(name=G.graph['name'])
    dot.attr(rankdir='TB', bgcolor=COLORS['background'],
             pad='0.3', nodesep='0.45', ranksep='0.55')
    dot.attr('node', shape='box', style='rounded,filled',
             fontname='Arial', fontsize='11',
             color=COLORS['ink'], penwidth='1.5', margin='0.16,0.09')
    dot.attr('edge', fontname='Arial', fontsize='10',
             color=COLORS['ink_soft'], penwidth='1.3',
             fontcolor=COLORS['burgundy'])

    out_loop = [(n, a) for n, a in G.nodes(data=True) if not a.get('in_loop', True)]
    for node_id, attrs in out_loop:
        style = NODE_STYLES.get(attrs['kind'], DEFAULT_NODE_STYLE)
        label = f"{attrs.get('seq', '')}   {attrs['kind']}" + (f" [{attrs['op']}]" if attrs.get('op') else "") + (f" #{attrs['resId']}" if attrs.get('resId') else "")
        dot.node(node_id, label=label, **style)

    in_loop = [(n, a) for n, a in G.nodes(data=True) if a.get('in_loop', True)]
    with dot.subgraph(name='cluster_loop') as c:
        c.attr(
            label='<<b >loop</b><br/><font color="#8B2418" point-size="9">alcance de control</font>>',
            labeljust='l', labelloc='t',
            fontname='Arial', fontsize='11',
            style='dashed,rounded', color=COLORS['burgundy'],
            penwidth='1.8', bgcolor=COLORS['paper'], margin='18'
        )
        for node_id, attrs in in_loop:
            style = NODE_STYLES.get(attrs['kind'], DEFAULT_NODE_STYLE)
            label = f"{attrs.get('seq', '')}   {attrs['kind']}" + (f" [{attrs['op']}]" if attrs.get('op') else "") + (f" #{attrs['resId']}" if attrs.get('resId') else "")
            c.node(node_id, label=label, **style)

    for u, v, edge_attrs in G.edges(data=True):
        if edge_attrs['type'] == 'data':
            dot.edge(u, v, label=f" {edge_attrs['var']} ", color=COLORS['ink_soft'])
        elif edge_attrs['type'] == 'side_effect':
            dot.edge(u, v, label=f" {edge_attrs['var']} ", color=COLORS['moss'], fontcolor=COLORS['moss'], style='dashed', constraint='false')
        elif edge_attrs['type'] == 'control':
            label_text = f" {edge_attrs['var']} " if edge_attrs.get('var') else ""
            dot.edge(u, v, label=label_text, color=COLORS['burgundy'], style='solid', penwidth='2.0')

    return dot.render(output_path, format='svg', cleanup=True)

def node_match(node_a, node_b):
    # Equivalencia "módulo plumbing": además del kind canónico, comparamos el
    # operador aritmético (op: "+","-","×","÷","round"… — la CONSTANTE se ignora) y
    # la identidad canónica del recurso físico (resId: índice del eje/dispositivo
    # distinto, por orden de aparición — la etiqueta x/y o el nombre se ignoran).
    return (node_a['kind'] == node_b['kind']
            and node_a.get('op') == node_b.get('op')
            and node_a.get('resId') == node_b.get('resId'))

def _edge_signature(attrs):
    # La 'var' ya viene canonicalizada por normalize_pdg (tilt_1 / pitch / value /
    # nombre-de-variable), así que es reproducible y se puede comparar tal cual.
    return (attrs['type'], attrs.get('var', ''))

def edge_match_multi(edges_a, edges_b):
    sig_a = sorted(_edge_signature(d) for d in edges_a.values())
    sig_b = sorted(_edge_signature(d) for d in edges_b.values())
    return sig_a == sig_b

def edge_match_single(attrs_a, attrs_b):
    return _edge_signature(attrs_a) == _edge_signature(attrs_b)

# --- PDG canónico: la dependencia de control es de DOMINANCIA, no de secuencia --
# Los agentes escriben el control encadenado (Evento -> s1 -> s2 -> s3), lo que
# convierte el ORDEN en estructura. En un PDG, todas las sentencias de un bloque
# dependen del MISMO nodo de control (Evento -> s1, Evento -> s2, Evento -> s3):
# el orden entre sentencias independientes desaparece, que es justo lo que debe
# pasar. El orden que SÍ importa lo siguen fijando las aristas 'side_effect'
# (efectos sobre el mismo recurso) y 'data' (def -> uso), que no se tocan.
CONTROL_CATEGORIES = ('event', 'control')
_CTRL_KINDS_CACHE = None

def _control_kinds() -> set:
    """canonical_node de categoría event/control, leídos de la ontología."""
    global _CTRL_KINDS_CACHE
    if _CTRL_KINDS_CACHE is None:
        import os
        ont = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tabla_ontologica.json')
        try:
            with open(ont, encoding='utf-8') as f:
                data = json.load(f)
            _CTRL_KINDS_CACHE = {n['canonical_node'] for n in data['nodes']
                                 if n.get('category') in CONTROL_CATEGORIES}
        except Exception:      # sin ontología: respaldo con los nodos de control conocidos
            _CTRL_KINDS_CACHE = {'ProgramStartEvent', 'SuddenNoiseEvent', 'OnTouchEvent',
                                 'OnTiltGestureEvent', 'ConditionalBranch', 'LoopForever',
                                 'RepeatN', 'ForRange', 'WhileLoop'}
    return _CTRL_KINDS_CACHE


def to_pure_pdg(G: nx.MultiDiGraph) -> nx.MultiDiGraph:
    """Reescribe la cadena secuencial como abanico de dominancia."""
    ctrl = _control_kinds()
    H = nx.MultiDiGraph(name=G.graph.get('name', ''))
    for n, attrs in G.nodes(data=True):
        H.add_node(n, **attrs)

    ctrl_edges = [(u, v, d) for u, v, d in G.edges(data=True) if d.get('type') == 'control']
    parent = {}                                   # sentencia -> (nodo de control que la domina, var)
    for u, v, d in ctrl_edges:                    # 1) hijas directas de un nodo de control
        if G.nodes[u].get('kind') in ctrl:
            parent[v] = (u, d.get('var', ''))
    for _ in range(len(ctrl_edges) + 1):          # 2) propagar por la cadena hasta punto fijo
        cambio = False
        for u, v, d in ctrl_edges:
            if G.nodes[u].get('kind') not in ctrl and u in parent and v not in parent:
                parent[v] = parent[u]
                cambio = True
        if not cambio:
            break

    for u, v, d in G.edges(data=True):            # 3) data y side_effect intactos
        if d.get('type') != 'control':
            H.add_edge(u, v, **d)
    for v, (u, var) in parent.items():            # 4) control en abanico
        H.add_edge(u, v, type='control', var=var)
    return H


# El GED es NP-duro: con branch-and-bound, si la búsqueda TERMINA el valor es el
# óptimo exacto; si la corta el timeout, es solo una cota superior. Se registra
# cuál de los dos casos ocurrió en 'ged_exact'.
GED_TIMEOUT = 60

def _ged(G1, G2):
    import time
    t0 = time.time()
    val = nx.graph_edit_distance(G1, G2, node_match=node_match,
                                 edge_match=edge_match_single, timeout=GED_TIMEOUT)
    return val, (time.time() - t0) < GED_TIMEOUT * 0.95


def compare_pdgs(G1: nx.MultiDiGraph, G2: nx.MultiDiGraph) -> dict:
    # Veredicto sobre el PDG canónico (sin el orden entre sentencias independientes).
    P1, P2 = to_pure_pdg(G1), to_pure_pdg(G2)
    is_iso = isomorphism.MultiDiGraphMatcher(P1, P2, node_match=node_match,
                                             edge_match=edge_match_multi).is_isomorphic()
    ged, exact = _ged(P1, P2)

    # Segundo pase sobre el grafo con el orden: solo sirve para saber si hay que
    # sugerir alinear la secuencia. No produce veredicto ni puntaje visible.
    orden_iso = isomorphism.MultiDiGraphMatcher(G1, G2, node_match=node_match,
                                                edge_match=edge_match_multi).is_isomorphic()

    return {
        'isomorphic': is_iso,
        'graph_edit_distance': ged,
        'ged_exact': exact,
        'nodes_G1': G1.number_of_nodes(),
        'nodes_G2': G2.number_of_nodes(),
        'edges_G1': G1.number_of_edges(),
        'edges_G2': G2.number_of_edges(),
        # equivalentes, pero las sentencias independientes van en distinto orden:
        # conviene alinearlas para que las dos versiones se lean igual.
        'order_hint': bool(is_iso and not orden_iso),
    }
