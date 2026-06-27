# PROMPT / Runbook — Rieseguire la pipeline di equivalenza

> **Quando l'utente dice** cose tipo *"ho cambiato alcune attività, rifai la pipeline e ricalcola l'equivalenza"*, *"rigenera AST/PDG/metriche"*, *"aggiorna la tabla ontologica"* → **segui ESATTAMENTE questo runbook.** È auto-contenuto: descrive principio, ordine, regole, comandi e verifica.

---

## 0. Principio (3 tipi di passo)

| Passo | Tipo | Chi lo fa |
|---|---|---|
| Estrazione codice → testo | **DETERMINISTICO** | `node` (decoder JS dai `.ptj`/`.hex`). Riproducibile, niente immagini, niente LLM. |
| Astrazione semantica: **AST → Tabla IR canonica → PDG** | **LLM (= io/agenti)** | workflow multi-agente, schema = `vela-analisis/vela/`. |
| Grafi SVG + metriche (GED, isomorfismo) | **DETERMINISTICO** | Python (`networkx` + `graphviz`), env conda `pdg-vela`. |

**Regole non negoziabili dell'astrazione:**
1. **Ordine: AST → Tabla IR (ontologia canonica comune) → PDG.** Il `kind` di ogni nodo PDG **È** un `canonical_node` della tabla. Quindi l'ontologia esiste *prima* del grafo.
2. **Una sola tabla di equivalenza:** `reporte/tabla_ontologica.json` (comune a tutte le 17). NON si scrivono più `tabla_ir.json` per-attività (deprecati; la vista per-attività evidenzia l'ontologia comune).
3. **Fedeltà:** ogni programma è rappresentato com'è. Operazioni semanticamente equivalenti → stesso `canonical_node`; ma se i due programmi differiscono, i grafi differiscono (la metrica lo rivela). **Mai forzare l'equivalenza.**
4. **Stabilità dei nomi:** ri-eseguendo, l'ontologia si **estende** partendo da quella vigente; non rinominare i `canonical_node` esistenti salvo errore palese.

**Hard rules di normalizzazione — l'equivalenza è «a meno del plumbing di piattaforma» (NON dimenticarle ai re-run):**
- **AST · albero pulito (scomposto, SENZA ripetizione):** ogni nodo mostra SOLO la propria operazione, con il marcatore `◻` dove va ogni figlio; **mai** ripetere il testo appiattito di un figlio nel padre. Diventano nodi figlio solo le **operazioni** (`Operator` = aritmetica/confronto/logica; `Sensor` = lettura sensore/getter); gli **atomi** (numeri, variabili, colori, note) restano **inline**. L'AST è *fedele* (colore, assi x/y reali, Hz/nota come sono); la normalizzazione è SOLO nel PDG.
- **PDG · 4 regole:**
  - **(A) Scartare** senza analogo: il **colore** della matrice LED (micro:bit non ce l'ha) → ignorato.
  - **(B) Alpha-rename** dei recursi fisici (assi sensore x/y; istanze dispositivo `DibujoLED1/2`, `Inclinación1/2`, `TecladoMusical1/2`…): l'etichetta non conta, conta l'**identità**. Indice canonico `resId` per ordine di apparizione per tipo di recurso; si butta l'etichetta letterale (x/y, numero del dispositivo). Stesso asse/dispositivo sempre (resId 1) ≡ altro sempre (resId 1) → equivalenti; **2 distinti** (resId 1,2) ≠ 1 solo.
  - **(C) Unificare** l'encoding: frequency (Hz) ≡ nota (MIDI) → kind `PlayTone`.
  - **(D) Aritmetica = opzione B:** operatore **SÌ** (campo `op` ∈ `+ − × ÷ round constrain`), costante **NO**. Quindi `+1000` ≡ `+60`; ma `×` ≠ `+`.
  - Il motore `pdg_engine.py` confronta i nodi su **`kind` + `op` + `resId`** (`node_match`). Le **aristi `data`** hanno la `var` **canonicalizzata in modo deterministico** (`normalize_pdg`, applicata da `run_all.py` che riscrive i `.json` puliti): valore di un sensore → `tilt_1`/`sound_1`/`light_1`/`time` (con `resId`; `tilt_2` se 2° asse distinto), altezza di un tono → `pitch` (non frequency/nota), intermedi → `value`, variabile utente → nome minuscolo. Poi viene **confrontata** (è riproducibile). Su `control` (`true`/`false`) e `side_effect` (`display`/`sound`) la `var` si conserva.

---

## 1. Pre-requisiti
- **Sorgenti aggiornate:** i file modificati devono stare in `protobject/equivalent-<code>.ptj` e `microbit/<code>.hex` (root del progetto).
- Se è cambiato l'**insieme/ordine/titoli** delle attività: aggiorna `activities.json` (root) e poi `node gen-actividades-json.js`.
- **Env:** `node` (root) e conda **`pdg-vela`** (ha `dot`/graphviz). Il binario: `C:\Users\Ale\miniconda3\Scripts\conda.exe`.
- **Schema gold di riferimento:** `pipeline-equivalence/vela-analisis/vela/` (ast/pdg/tabla d'esempio). Non sta in `reporte/actividades/` apposta (non è una delle 17).

---

## 2. Procedura (eseguila in quest'ordine)

### Passo A — Estrazione testo (DETERMINISTICO)
Dalla **root del progetto**:
```bash
node gen-text-json.js
```
Rigenera `reporte/actividades/<code>/text_{protobject,makecode}.json` per tutte le 17 (modo "solo struttura": niente commenti, LED collassati). Verifica che riflettano le modifiche.

### Passo B — Astrazione semantica (LLM, workflow)
Lancia il workflow con lo strumento **Workflow**:
```
Workflow({ scriptPath: "pipeline-equivalence/reporte/scripts/pipeline_llm.js" })
```
- **Tutte le 17** (default): nessun `args`.
- **Solo alcune** (re-run mirato): `Workflow({ scriptPath: "...", args: { codes: ["juego-toques","nivel-con-ruido"] } })`. In modalità parziale l'ontologia **NON** viene ricostruita: si carica quella vigente (`tabla_ontologica.json`) e si rigenerano solo AST+PDG delle attività indicate. Se hai aggiunto operazioni nuove non coperte dall'ontologia, fai un re-run **completo**.

Il workflow fa, in quest'ordine: **17 agenti AST** → **costruisce/aggiorna l'ontologia comune** (seed = `tabla_ontologica.json` vigente) con **verifica avversariale in loop** (3 lenti: completezza/consistenza/fedeltà, fino a consenso, max 4 round) → la scrive in `reporte/tabla_ontologica.json` → **17 agenti PDG** (`pdg_{makecode,protobject}.json`, `kind` dalla ontologia). Gli agenti **scrivono i file** e leggono lo schema da `vela-analisis/vela/`.

> Nota su "consenso=false": è normale e accettabile se le 2-3 issue residue sono **divergenze reali documentate** (es. metronomo calcola intervalli diversi; gesto screen-up vs side). Il loop va in plateau; non insistere oltre — sono differenze vere tra le piattaforme, non errori.

### Passo C — Calcolo (DETERMINISTICO, Python)
```bash
"C:\Users\Ale\miniconda3\Scripts\conda.exe" run -n pdg-vela python "pipeline-equivalence/reporte/scripts/run_all.py"
```
Per ogni attività: legge `pdg_*.json`, costruisce i grafi (networkx), renderizza `pdg_{makecode,protobject}.svg` (graphviz `dot`), calcola **GED + isomorfismo (VF2)**, scrive `metricas.json`. Robusto: un errore per-attività non blocca le altre. Atteso: `N/N OK`.

### Passo D — Verifica
- Apri `pipeline-equivalence/index.html` (server su 8080, o via preview servendo la root del progetto → `/pipeline-equivalence/index.html`).
- Controlla: le 17 attività mostrano **metriche** e **grafi** (niente "Pendiente"), il link **ontologia comune** in cima funziona, e "Ver código + AST" / "Tabla IR" / "PDG" per-attività aprono.
- **Rivedi le metriche** per anomalie: un GED alto con stesse dimensioni nodi può indicare (a) divergenza d'ordine di statement indipendenti — limite noto della metrica PDG, fedele — o (b) incoerenza di astrazione: in tal caso ispeziona i due `pdg_*.json` e i `text_*.json`. Segnala all'utente; **non auto-correggere** astrazioni dubbie.

---

## 3. Schema dei JSON (replica esatta da `vela-analisis/vela/`)

**AST** (`ast_{makecode,protobject}.json`):
```json
{ "platform": "MakeCode|Protobject",
  "ast": { "blocks": [ { "type": "Event", "label": "...", "children": [ { "type":"Action","label":"...","children":[] } ] } ] } }
```
`type`: Event · Event_Interrupt · Loop · Conditional · Branch_True · Branch_False · Assignment · State_Toggle · Action.

**Ontologia** (`reporte/tabla_ontologica.json`, UNICA, comune):
```json
{ "descripcion": "...", "nodes": [ { "canonical_node":"DrawImage", "makecode_block":"show leds", "protobject_block":"draw [image] ... on DibujoLED", "category":"display", "note":"..." } ] }
```

**PDG** (`pdg_{makecode,protobject}.json`):
```json
{ "platform":"MakeCode|Protobject",
  "nodes": [ { "id":"n1", "kind":"<canonical_node>", "seq":1, "in_loop":false } ],
  "edges": [ { "source":"n1", "target":"n2", "type":"control|data|side_effect", "var":"" } ] }
```

---

## 4. File coinvolti (riferimento rapido)
- Estrazione: `blocks-decoder.js`, `decode.js`, `gen-text-json.js`, `lib/lzma_worker.min.js` (root).
- Indice dashboard: `gen-actividades-json.js` → `pipeline-equivalence/actividades.json`.
- Workflow LLM: `pipeline-equivalence/reporte/scripts/pipeline_llm.js`.
- Calcolo: `pipeline-equivalence/reporte/scripts/{run_all.py, run_pipeline.py, pdg_engine.py}`.
- Output per-attività: `reporte/actividades/<code>/{ast,pdg}_*.json`, `metricas.json`, `pdg_*.svg`.
- Ontologia unica: `reporte/tabla_ontologica.json`. Schema gold: `vela-analisis/vela/`.
- Viewer: `reporte/visores/{visor_ast,visor_tabla,visor_ontologia,visor_pdg}.html`. Il dashboard `index.html` è **dinamico** (legge `actividades.json`) — niente HTML da copiare.
