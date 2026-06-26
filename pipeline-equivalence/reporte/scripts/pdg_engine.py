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
        G.add_node(node['id'], kind=node['kind'], seq=node['seq'], in_loop=node['in_loop'])
        
    for edge in json_data.get('edges', []):
        G.add_edge(edge['source'], edge['target'], type=edge['type'], var=edge['var'])
        
    return G

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
        label = f"{attrs.get('seq', '')}   {attrs['kind']}"
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
            label = f"{attrs.get('seq', '')}   {attrs['kind']}"
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
    return node_a['kind'] == node_b['kind']

def _edge_signature(attrs):
    return (attrs['type'], attrs.get('var', ''))

def edge_match_multi(edges_a, edges_b):
    sig_a = sorted(_edge_signature(d) for d in edges_a.values())
    sig_b = sorted(_edge_signature(d) for d in edges_b.values())
    return sig_a == sig_b

def edge_match_single(attrs_a, attrs_b):
    return _edge_signature(attrs_a) == _edge_signature(attrs_b)

def compare_pdgs(G1: nx.MultiDiGraph, G2: nx.MultiDiGraph) -> dict:
    matcher = isomorphism.MultiDiGraphMatcher(G1, G2, node_match=node_match, edge_match=edge_match_multi)
    is_iso = matcher.is_isomorphic()
    ged = nx.graph_edit_distance(G1, G2, node_match=node_match, edge_match=edge_match_single, timeout=10)
    
    return {
        'isomorphic': is_iso,
        'graph_edit_distance': ged,
        'nodes_G1': G1.number_of_nodes(),
        'nodes_G2': G2.number_of_nodes(),
        'edges_G1': G1.number_of_edges(),
        'edges_G2': G2.number_of_edges(),
    }
