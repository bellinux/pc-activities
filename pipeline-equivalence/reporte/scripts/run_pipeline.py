import sys
import os
import json
from pdg_engine import build_graph_from_json, render_pdg, compare_pdgs

def run(activity_name: str):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    activity_dir = os.path.join(base_dir, 'actividades', activity_name)
    
    if not os.path.isdir(activity_dir):
        print(f"Error: La carpeta de la actividad '{activity_name}' no existe en {activity_dir}")
        sys.exit(1)

    print(f"--- Iniciando Pipeline para la actividad: {activity_name} ---")

    # Rutas de entrada JSON
    pdg_a_path = os.path.join(activity_dir, 'pdg_makecode.json')
    pdg_b_path = os.path.join(activity_dir, 'pdg_protobject.json')

    if not os.path.exists(pdg_a_path) or not os.path.exists(pdg_b_path):
        print("Faltan archivos pdg_*.json en la carpeta.")
        sys.exit(1)

    # Cargar JSON
    with open(pdg_a_path, 'r', encoding='utf-8') as f:
        json_a = json.load(f)
    with open(pdg_b_path, 'r', encoding='utf-8') as f:
        json_b = json.load(f)

    # 1. Construir Grafos Matemáticamente
    print("Construyendo grafos en networkx...")
    G_a = build_graph_from_json(json_a)
    G_b = build_graph_from_json(json_b)

    # 2. Renderizar SIEMPRE dos SVG independientes
    print("Renderizando SVG a través de graphviz...")
    svg_a_out = os.path.join(activity_dir, 'pdg_makecode')
    svg_b_out = os.path.join(activity_dir, 'pdg_protobject')
    
    render_pdg(G_a, svg_a_out)
    render_pdg(G_b, svg_b_out)

    # 3. Calcular Métricas Algorítmicas
    print("Calculando GED e Isomorfismo...")
    metrics = compare_pdgs(G_a, G_b)
    metrics_out = os.path.join(activity_dir, 'metricas.json')
    with open(metrics_out, 'w', encoding='utf-8') as f:
        json.dump(metrics, f, indent=4)

    print(f"Pipeline ejecutado exitosamente. Archivos generados en {activity_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python run_pipeline.py <nombre_actividad>")
        sys.exit(1)
    
    activity = sys.argv[1]
    run(activity)
