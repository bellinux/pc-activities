/* ============================================================================
 * pipeline_llm.js — WORKFLOW (multi-agente) de abstracción semántica del
 * pipeline de equivalencia. Se invoca con la herramienta Workflow.
 *
 * Hace los pasos LLM: AST (17) -> ontología canónica COMÚN (verificada
 * adversarialmente) -> PDG (17). NO hace la extracción (eso es determinístico:
 * `node gen-text-json.js`) ni el cálculo (eso es Python: `run_all.py`).
 *
 * Esquema de referencia: pipeline-equivalence/vela-analisis/vela/ (ejemplo gold).
 * Semilla de ontología: la ontología vigente reporte/tabla_ontologica.json
 * (mantiene estables los canonical_node entre re-ejecuciones).
 *
 * Ver el runbook completo en pipeline-equivalence/prompt.md
 * ========================================================================== */
export const meta = {
  name: 'equivalence-pipeline-llm',
  description: 'AST (17) -> ontología canónica común (verificada) -> PDG (17). Microbit vs Protobject.',
  phases: [
    { title: 'AST', detail: '17 agentes: text_*.json -> ast_*.json + inventario de operaciones' },
    { title: 'Ontología', detail: 'tabla canónica común (seed = ontología vigente) + verificación adversarial hasta consenso' },
    { title: 'PDG', detail: '17 agentes: ast + ontología -> pdg_*.json (kind = canonical_node)' },
  ],
}

const ACTS = [
  { num: 1, code: 'xilofono-inclinacion', title: 'El Xilófono Mágico Inclinable' },
  { num: 2, code: 'luci-discoteca-ruido', title: 'El Visualizador de Música' },
  { num: 3, code: 'xilofono-inclinacion-con-nota-led', title: 'El Xilófono del Futuro (con LEDs)' },
  { num: 4, code: 'corazon-forever-loop', title: 'El Llavero de Corazón Luminoso' },
  { num: 5, code: 'robot-risa-simpatica-al-ruido', title: 'El Robot Cosquilloso' },
  { num: 6, code: 'corazon-variables-eventos', title: 'El Corazón de Mi Robot Amigo' },
  { num: 7, code: 'alarma-caja-galletas', title: '¡Alarma: El Ladrón de Galletas!' },
  { num: 8, code: 'despertador-por-la-manana', title: 'El Despertador de Girasol' },
  { num: 9, code: 'luces-de-fiesta-al-oscurecer', title: 'El Vuelo del Murciélago Nocturno' },
  { num: 10, code: 'juego-toques', title: '¡El Desafío de Activación del Robot!' },
  { num: 11, code: 'luz-encendida-al-ruido', title: 'El Interruptor Mágico de Aplausos' },
  { num: 12, code: 'flama-vela-con-soplo', title: 'La Vela Mágica de Cumpleaños' },
  { num: 13, code: 'papas-caliente-juego', title: 'La Papa Explosiva Digital' },
  { num: 14, code: 'luz-encendida-ruido-animacion', title: 'El Encendido Cinematográfico' },
  { num: 15, code: 'metronomo-con-inclinacion', title: 'El Metrónomo de DJ' },
  { num: 16, code: 'aplausometro-tiempo-aplausos', title: 'La Batalla de Aplausos' },
  { num: 17, code: 'nivel-con-ruido', title: '¡No Derrames el Líquido! - El Juego de Pulso' },
]
// args.codes (opcional) = subconjunto de codes a procesar; por defecto las 17.
const TARGET = (args && Array.isArray(args.codes) && args.codes.length) ? ACTS.filter(a => args.codes.includes(a.code)) : ACTS
const IS_FULL = TARGET.length === ACTS.length   // re-run completo vs parcial (subconjunto)
const DIR = c => `pipeline-equivalence/reporte/actividades/${c}`
const REF = 'pipeline-equivalence/vela-analisis/vela'   // esquema gold de referencia
const ONT_PATH = 'pipeline-equivalence/reporte/tabla_ontologica.json'

// Reglas de equivalencia (curadas, fuente de verdad). Se escriben SIEMPRE en la
// ontología (sobreviven a los re-runs). Si cambian las reglas, edítalas aquí.
const REGLAS = {
  veredicto: "Dos actividades son equivalentes si lo son sus PROGRAMAS «a menos del plumbing de plataforma»: se comparan los grafos de dependencias (PDG) normalizados, coincidiendo el kind canónico, el operador aritmético, la identidad del recurso físico y la topología (def→uso).",
  reglas: [
    { clave: "El COLOR se ignora", detalle: "La matriz LED de Protobject tiene color; micro:bit no. Sin análogo → se descarta." },
    { clave: "Los NOMBRES de dispositivo no importan", detalle: "DibujoLED1/2, TecladoMusical1, Inclinación2… son instancias: cuenta la FUNCIÓN, no el nombre (micro:bit tiene una sola de cada tipo)." },
    { clave: "Los EJES x/y son indiferentes", detalle: "Leer la inclinación en x o en y es la misma operación física; se renombran por orden de aparición (tilt_1, tilt_2…). PERO usar 2 ejes distintos ≠ usar 1 solo (eso sí es una diferencia real). Igual para 2 dispositivos distintos del mismo tipo." },
    { clave: "Hz y nota = mismo pitch", detalle: "frequency (Hz) y nota (MIDI) son dos codificaciones de la misma altura; no distinguen." },
    { clave: "Sonido por INTENCIÓN", detalle: "PlayTone = pitch controlado/variable (xilófono); EmitSound = sonido genérico a evento (latido, bip, percusión; el «drum» va aquí); PlaySound = clip/melodía con nombre. No se distingue por timbre ni dispositivo." },
    { clave: "Aritmética: operador sí, constante no", detalle: "Cuenta la operación (+, −, ×, ÷, round), no el número. Así «+1000» ≡ «+60» (ajuste de escala), pero «×» ≠ «+» (sensibilidad distinta)." }
  ]
}

const AST_SCHEMA = { type: 'object', additionalProperties: false, required: ['code', 'written', 'operations'],
  properties: { code: { type: 'string' }, written: { type: 'boolean' },
    operations: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['meaning', 'makecode_label', 'protobject_label'],
      properties: { meaning: { type: 'string' }, makecode_label: { type: 'string' }, protobject_label: { type: 'string' }, suggested_kind: { type: 'string' } } } } } }
const ONTOLOGY_SCHEMA = { type: 'object', additionalProperties: false, required: ['nodes'],
  properties: { nodes: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['canonical_node', 'makecode_block', 'protobject_block', 'category'],
    properties: { canonical_node: { type: 'string' }, makecode_block: { type: 'string' }, protobject_block: { type: 'string' }, category: { type: 'string' }, note: { type: 'string' } } } } } }
const REVIEW_SCHEMA = { type: 'object', additionalProperties: false, required: ['approved', 'issues'],
  properties: { approved: { type: 'boolean' }, issues: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['severity', 'problem', 'suggestion'],
    properties: { severity: { type: 'string' }, canonical_node: { type: 'string' }, problem: { type: 'string' }, suggestion: { type: 'string' } } } } } }
const PDG_SCHEMA = { type: 'object', additionalProperties: false, required: ['code', 'written', 'nodes_mb', 'nodes_pb', 'kinds_used'],
  properties: { code: { type: 'string' }, written: { type: 'boolean' }, nodes_mb: { type: 'number' }, nodes_pb: { type: 'number' }, kinds_used: { type: 'array', items: { type: 'string' } }, note: { type: 'string' } } }

const astPrompt = a => `Eres un agente del pipeline de equivalencia (Microbit vs Protobject), actividad "${a.code}" (${a.title}). cwd = raíz del proyecto.
PRIMERO lee el ESQUEMA de ejemplo (replícalo EXACTO): ${REF}/ast_protobject.json y ${REF}/ast_makecode.json
ENTRADA (léelas): ${DIR(a.code)}/text_protobject.json y ${DIR(a.code)}/text_makecode.json (cada una = { platform, extracted_text:[líneas indentadas, 2 espacios por nivel] }).
TAREA: genera y ESCRIBE el AST de ambas plataformas: ${DIR(a.code)}/ast_protobject.json y ${DIR(a.code)}/ast_makecode.json
Esquema: { "platform":"...", "ast": { "blocks": [ {"type","label","children":[...]} ] } } (JSON válido, indent 4).
"type": Event (al iniciar/on start), Event_Interrupt (eventos disparados: tocar logo, sonido, botón…), Loop (repetir/forever), Conditional (si/if), Branch_True/Branch_False, Assignment (fijar/establecer var), State_Toggle (negar var), Action (acción de dispositivo: dibujar, plot, pausa, sonido, nota…), Operator (aritmética/comparación/lógica), Sensor (lectura de sensor o getter de dispositivo).
REGLA DURA · ÁRBOL LIMPIO (descompuesto, SIN repetición):
- children = anidamiento real: tanto el FLUJO DE CONTROL (cuerpo de loop, ramas de un if) como las SUB-EXPRESIONES que sean OPERACIONES.
- Se vuelven nodos HIJO solo las OPERACIONES: aritmética/comparación/lógica (Operator), lecturas de sensor y getters (Sensor), y operaciones con argumentos. Los ÁTOMOS (números, variables, colores literales, notas) quedan INLINE en la label del padre, NO son nodos.
- Cada nodo muestra en label SOLO su propia operación, con el marcador ◻ donde va cada hijo. NUNCA repitas el texto aplanado de un hijo en el padre (el error a evitar: que "aceleración x" aparezca en el padre y otra vez en los hijos).
- Ejemplo micro:bit de "tono de timbre (Hz) (aceleración (mg) x + 1000)":
  {"type":"Action","label":"tono de timbre (Hz) de ◻","children":[
    {"type":"Operator","label":"◻ + 1000","children":[
      {"type":"Sensor","label":"aceleración (mg) x","children":[]} ]} ]}
  (la lectura de sensor es hoja; la constante 1000 va inline; nada se repite).
FIDELIDAD: el AST refleja cada programa TAL CUAL (con su color, sus ejes x/y reales, frequency o nota como esté). La normalización para la equivalencia NO se hace aquí: se hace en el PDG.
DEVUELVE: { code:"${a.code}", written:true, operations:[ {meaning, makecode_label, protobject_label, suggested_kind} ] } alineando, dentro de esta actividad, cada operación distinta (eventos, variables, condicionales, loops, acciones) con su forma en makecode y en protobject.`

const ontologyBuildPrompt = inv => `Eres el CONSTRUCTOR/ACTUALIZADOR de la ONTOLOGÍA CANÓNICA COMÚN (común a las 17 actividades). cwd = raíz del proyecto.
SEMILLA: lee la ontología vigente ${ONT_PATH} (si existe) y MANTÉN ESTABLES sus canonical_node; si no existe, usa ${REF}/tabla_ir.json como semilla. EXTIÉNDELA/ajústala para cubrir TODAS las operaciones del inventario actual (agrega nodos para operaciones nuevas, no renombres los existentes salvo error claro).
INVENTARIO agregado de operaciones reales (alineaciones makecode↔protobject por actividad):
${JSON.stringify(inv)}
Reglas: misma operación semántica => UN solo canonical_node (PascalCase, estable). makecode_block/protobject_block = forma representativa genérica; si una plataforma no tiene equivalente, anótalo en "note". category = event/variable/control/display/sound/sensor/math/timing/debug. Documenta divergencias reales en "note" (no fuerces equivalencias falsas).
Los canonical_node son AGNÓSTICOS al eje (ReadTilt, no ReadTiltX/Y), a la instancia de dispositivo (DrawImage, no DrawImageLED2) y al encoding del pitch (Hz y nota MIDI son el mismo concepto). La aritmética es UN solo nodo "Arithmetic" (el operador concreto va en el atributo "op" del PDG, no en el canonical_node).
SONIDO — CAMBIO DELIBERADO (aplícalo AUNQUE rompa la estabilidad; elimina "PlayDrum"): distingue el sonido POR INTENCIÓN, y escribe en cada nodo una NOTA clara del "cuándo":
 • "PlayTone" — SOLO cuando la ALTURA (pitch) es el punto: controlada/variable (p.ej. xilófono, el pitch sale de la inclinación). note: "Usar cuando la altura del sonido ES el objetivo (pitch controlado/variable); Hz y nota MIDI son el mismo concepto. NO para sonidos genéricos."
 • "EmitSound" — sonido GENÉRICO a evento, con timbre/altura INCIDENTALES (un latido, un bip, una percusión, o un tono de altura FIJA usado como señal). Aquí colapsa el antiguo PlayDrum. note: "Usar cuando solo importa que SUENE algo en un evento (latido/bip/percusión/feedback); la altura y el timbre son incidentales. En micro:bit no existe 'drum': usa un tono — da igual."
 • "PlaySound" — clip/melodía PREGRABADO con nombre (alarma, risa, 'celebración final'); se mantiene. note: "Sonido/melodía con nombre, pregrabado."
 Criterio PlayTone vs EmitSound: pitch CALCULADO/VARIABLE → PlayTone; pitch FIJO o incidental → EmitSound.
DEVUELVE: { nodes:[ {canonical_node, makecode_block, protobject_block, category, note?} ] } cubriendo TODO el inventario. NO escribas archivos aún.`

const reviewPrompt = (ont, inv, lens) => `Eres REVISOR ADVERSARIAL (lente "${lens}") de la ontología canónica común. Por defecto BUSCA problemas; aprueba solo si está bien.
ONTOLOGÍA: ${JSON.stringify(ont)}
INVENTARIO: ${JSON.stringify(inv)}
- completitud: ¿cubre TODA operación del inventario? ¿falta algún canonical_node?
- consistencia: ¿cada operación = un único canonical_node? ¿duplicados/solapamientos/nombres incoherentes?
- fidelidad: ¿los makecode_block/protobject_block son DE VERDAD el mismo concepto? ¿alguna alineación falsa (equivalencia forzada)?
DEVUELVE: { approved:bool, issues:[ {severity:"alta|media|baja", canonical_node?, problem, suggestion} ] }. approved=true SOLO si no hay alta/media.`

const revisePrompt = (ont, issues, inv) => `Mejora la ontología canónica común resolviendo estos issues, manteniendo el esquema { nodes:[{canonical_node, makecode_block, protobject_block, category, note?}] } y cubriendo TODO el inventario. Mantén estables los canonical_node existentes.
ONTOLOGÍA: ${JSON.stringify(ont)}
ISSUES: ${JSON.stringify(issues)}
INVENTARIO: ${JSON.stringify(inv)}
DEVUELVE la ontología corregida COMPLETA ({ nodes:[...] }).`

const writeOntologyPrompt = ont => `Escribe (cwd = raíz del proyecto) el archivo ${ONT_PATH} con contenido EXACTO (JSON, indent 4):
${JSON.stringify({ descripcion: 'Ontología canónica común a las 17 actividades. El campo kind de cada nodo PDG es uno de estos canonical_node.', reglas_de_equivalencia: REGLAS, nodes: ont.nodes }, null, 4)}
Confirma que quedó escrito.`

const pdgPrompt = (a, ont) => `Eres el agente PDG del pipeline de equivalencia, actividad "${a.code}" (${a.title}). cwd = raíz del proyecto.
PRIMERO lee los ESQUEMAS de ejemplo (replícalos EXACTO): ${REF}/pdg_protobject.json, ${REF}/pdg_makecode.json, ${REF}/tabla_ir.json
ENTRADA (léelos): ${DIR(a.code)}/ast_protobject.json y ${DIR(a.code)}/ast_makecode.json
ONTOLOGÍA CANÓNICA COMÚN (el "kind" de cada nodo DEBE ser uno de estos canonical_node):
${JSON.stringify(ont.nodes.map(n => ({ canonical_node: n.canonical_node, makecode_block: n.makecode_block, protobject_block: n.protobject_block })))}
TAREA: ESCRIBE 2 archivos en ${DIR(a.code)}/ (JSON indent 4): pdg_makecode.json y pdg_protobject.json = { "platform":"MakeCode|Protobject", "nodes":[...], "edges":[...] }.
- nodes: { id:"n1".., kind:<canonical_node>, seq:<orden de ejecución>, in_loop:<bool>, op?:<operador aritmético>, resId?:<índice de recurso físico> }.
- edges: { source, target, type, var }: "control" (evento->primer hijo; secuencia; conditional->cada nodo de su rama con var="true"/"false"; el loop NO es nodo, in_loop marca pertenencia), "data" (definición de variable -> uso, var=nombre; productor de valor -> consumidor, var=parámetro), "side_effect" (efectos ordenados sobre recurso compartido, var="display"/"sound"...).
- "kind" SOLO de la ontología. Misma operación => mismo kind en ambas plataformas.
REGLAS DURAS DE NORMALIZACIÓN (el PDG compara "módulo plumbing de plataforma" — NO las olvides):
  (A) DESCARTAR sin analogo: el COLOR de la matriz LED se IGNORA (micro:bit no tiene color) — no generes nodos/edges por el color.
  (B) ALPHA-RENOMBRAR recursos físicos (la etiqueta no importa, la IDENTIDAD sí): para cada TIPO de recurso (eje de sensor x/y; instancia de dispositivo DibujoLED1/2, Inclinación1/2, TecladoMusical1/2, NivelRuido1/2…) enumera los DISTINTOS que usa ESTE programa y asígnales un índice por orden de aparición (1,2,3…); pon ese índice en "resId" del nodo que toca el recurso, y TIRA la etiqueta literal (x/y, el número del dispositivo). Consecuencia buscada: usar SIEMPRE el mismo eje/dispositivo (resId 1) ≡ usar siempre otro (también resId 1) → equivalentes; usar 2 ejes/dispositivos DISTINTOS (resId 1 y 2) ≠ usar 1 solo.
  (C) UNIFICAR encoding: frequency (Hz) y nota (MIDI) son el MISMO concepto → kind "PlayTone" en ambas plataformas; el encoding es plumbing.
  (D) ARITMÉTICA = opción B (operador SÍ, constante NO): cada operación aritmética/redondeo es un nodo kind "Arithmetic" con campo "op" ∈ {"+","-","×","÷","round","constrain"}; las CONSTANTES numéricas se DESCARTAN (no son nodos ni operandos). Así "+1000" ≡ "+60" (ambos op="+") pero "×" ≠ "+".
  (E) La "var" de las aristas "data" se canonicaliza después automáticamente (valor de sensor → "tilt_1"/"sound_1"… con su resId; altura de tono → "pitch", no frequency/nota; intermedio → "value"; variable de usuario → su nombre). Puedes poner nombres razonables; el motor (normalize_pdg) los normaliza igual.
  (F) SONIDO por INTENCIÓN (no por dispositivo ni timbre): kind "PlayTone" SOLO si el pitch es controlado/variable (xilófono); "EmitSound" si es un sonido genérico a evento (latido/bip/percusión/tono de altura fija como señal — el antiguo "drum" va AQUÍ); "PlaySound" si es un clip/melodía con nombre. Criterio: pitch calculado/variable → PlayTone; pitch fijo o incidental → EmitSound. NO uses "PlayDrum".
FIDELIDAD: tras la normalización, si los programas siguen difiriendo, los grafos DEBEN diferir (no fuerces isomorfismo).
- NOTA: la tabla de equivalencia per-actividad ya NO se escribe (tabla_ir.json quedó deprecado); la vista por actividad resalta la ontología común. NO escribas tabla_ir.json.
DEVUELVE: { code:"${a.code}", written:true, nodes_mb, nodes_pb, kinds_used:[...] }.`

// ===================== EJECUCIÓN =====================
phase('AST')
const astResults = (await parallel(TARGET.map(a => () =>
  agent(astPrompt(a), { label: `ast:${a.code}`, phase: 'AST', agentType: 'general-purpose', schema: AST_SCHEMA })
))).filter(Boolean)
log(`AST generados: ${astResults.length}/${TARGET.length}`)

phase('Ontología')
const inventory = astResults.map(r => ({ code: r.code, operations: r.operations }))
let ontology, round = 0, approved = false
if (IS_FULL) {
  // Re-run COMPLETO: (re)construir la ontología común y verificarla adversarialmente.
  ontology = await agent(ontologyBuildPrompt(inventory), { label: 'ontology:build', phase: 'Ontología', agentType: 'general-purpose', schema: ONTOLOGY_SCHEMA })
  while (!approved && round < 4 && ontology) {
    round++
    const reviews = (await parallel(['completitud', 'consistencia', 'fidelidad'].map(lens => () =>
      agent(reviewPrompt(ontology, inventory, lens), { label: `verify:${lens}:r${round}`, phase: 'Ontología', schema: REVIEW_SCHEMA })
    ))).filter(Boolean)
    const blocking = reviews.filter(r => !r.approved).flatMap(r => r.issues || []).filter(i => i.severity === 'alta' || i.severity === 'media')
    log(`Ontología ronda ${round}: ${ontology.nodes.length} nodos, ${reviews.filter(r => r.approved).length}/3 aprueban, ${blocking.length} bloqueantes`)
    if (!blocking.length) { approved = true; break }
    ontology = await agent(revisePrompt(ontology, blocking, inventory), { label: `ontology:revise:r${round}`, phase: 'Ontología', agentType: 'general-purpose', schema: ONTOLOGY_SCHEMA })
  }
  await agent(writeOntologyPrompt(ontology), { label: 'ontology:write', phase: 'Ontología', agentType: 'general-purpose' })
  log(`Ontología final: ${ontology.nodes.length} nodos, consenso=${approved} (rondas=${round})`)
} else {
  // Re-run PARCIAL: usar la ontología vigente SIN reconstruirla (no se sobreescribe).
  ontology = await agent(`Lee el archivo ${ONT_PATH} (cwd = raíz del proyecto) y devuélvelo TAL CUAL como { nodes:[ {canonical_node, makecode_block, protobject_block, category, note} ] }. NO modifiques, NO reconstruyas, NO escribas nada.`, { label: 'ontology:load', phase: 'Ontología', agentType: 'general-purpose', schema: ONTOLOGY_SCHEMA })
  approved = true
  log(`Ontología vigente cargada sin reconstruir (re-run parcial): ${ontology ? ontology.nodes.length : 0} nodos`)
}

phase('PDG')
const pdgResults = (await parallel(TARGET.map(a => () =>
  agent(pdgPrompt(a, ontology), { label: `pdg:${a.code}`, phase: 'PDG', agentType: 'general-purpose', schema: PDG_SCHEMA })
))).filter(Boolean)
log(`PDG generados: ${pdgResults.length}/${TARGET.length}`)

return {
  procesadas: TARGET.map(a => a.code), asts: astResults.length, ontology_nodes: ontology.nodes.length,
  ontology_consensus: approved, ontology_rounds: round, pdgs: pdgResults.length,
  pdg_summary: pdgResults.map(r => ({ code: r.code, nodes_mb: r.nodes_mb, nodes_pb: r.nodes_pb })),
}
