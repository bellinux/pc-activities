# CLAUDE.md — Actividades de Pensamiento Computacional (Protobject ↔ micro:bit)

> Contesto del progetto per riprendere il lavoro. Progetto **Fondecyt · PUC Chile**.
> Lingua di lavoro con l'utente: **italiano**. Lingua del prodotto (sito, attività): **spagnolo del Cile**.

---

## 1. Cos'è

Sito statico che presenta una **progressione didattica di 17 attività** di physical computing
(programmazione a **blocchi Blockly** da cellulare con **Protobject**, pensate per studenti in Cile),
più un sistema per verificare scientificamente l'**equivalenza** tra la versione Protobject e quella micro:bit/MakeCode.

Repo originariamente clonato da `github.com/bellinux/pc-activities` e poi riorganizzato in questa cartella.

---

## 2. ⚠️ REGOLE / VINCOLI non negoziabili (l'utente ci tiene molto)

1. **SOLO le 17 attività in spagnolo.** Le varianti **trilingui NON esistono** per questo lavoro:
   **MAI** citarle, confrontarle o usarle come riferimento. Punto.
2. **Spagnolo del Cile.** Termini obbligatori: `celular` (non móvil/teléfono/smartphone), `computador`,
   `ampolleta` (non bombilla), `papa` (non patata), `rompecabezas` (non puzzle).
3. **Nessuna attività deve citarne un'altra** ("como en la actividad anterior", "la próxima misión",
   nomi di altri progetti, "desafío final", ecc.). La progressione sta nell'**ORDINE**, non nei rimandi testuali.
4. **Difficoltà valutata a BLOCCHI Blockly, non a codice testuale** (es. `repetir N` ≠ `contar con`/`for`).
5. **L'ordine pedagogico è un'iterazione continua**: né l'ordine numerico né quello pedagogico "vincono";
   se cambia un'attività cambia anche l'ordine. Co-evolvono.
6. **Il report è per studenti.** NON correggere di propria iniziativa: l'utente decide cosa aggiustare.
   Trova/verifica con prova verbatim → verifica avversariale scettica (default: respingere).

---

## 3. Struttura del progetto

| Path | Ruolo |
|---|---|
| `index.html` | **Landing/home**: spiega il progetto + organizzazione, 4 card di navigazione. |
| `engine.html` | **IL VISORE** delle attività. 100% spagnolo. Vedi §5. |
| `planificacion.html` | **Rationale** della progressione: HTML AUTONOMO (5 fasi, 17 progetti, algoritmi). Documento vivo. |
| `report.html` | **Report di qualità** (es-CL), sezioni §A–§G; ogni codice attività linka a `engine.html#a=`. |
| `activities.json` | **Indice ordinato** dei 17 slug. L'ordine = ordine e numeri 1..17 nel visore. **Riordinare = editare questo file.** |
| `_activities/` | I `.md` delle attività: 17 `.es.md` solo-spagnolo (le ufficiali) + 22 base trilingui (`.es/.en/.it`, **ORFANE**, non referenziate). Tutti CRLF. |
| `src/` · `microbit/` | Immagini/video per attività · firmware `.hex` per micro:bit. |
| `protobject/` | Codice Blockly reale. `equivalent-<code>.ptj` (root, ufficiali) + `decode_ptj.py`; `raw/` solo `.xml`; `decoded/` `.txt`. Vedi §6. |
| `pipeline-equivalence/` | Sistema di analisi equivalenza Protobject↔micro:bit via **AST + PDG + metriche** (Python). **ANCORA in italiano**, lavoro **rinviato**. |
| `readme.txt` | Del clone originale. |

---

## 4. Le 17 attività (ordine attuale = `activities.json`)

> Lo `slug` è l'id stabile (lo usano deep-link e report). Il `code` nomina i file Protobject:
> `protobject/equivalent-<code>.ptj` e `protobject/raw/<code>.xml`. Il `.txt` decodificato è `decoded/<slug>.txt`.

| # | slug | code (Protobject) | título real (dal `.md`) |
|--:|---|---|---|
| 1 | `02.1-xylophone` | `xilofono-inclinacion` | El Xilófono Mágico Inclinable |
| 2 | `02.2-music-visualizer` | `luci-discoteca-ruido` | El Visualizador de Música |
| 3 | `03.1-led-xylophone` | `xilofono-inclinacion-con-nota-led` | El Xilófono del Futuro (con LEDs) |
| 4 | `04.1-heart-beat` | `corazon-forever-loop` | El Llavero de Corazón Luminoso |
| 5 | `14.1-ticklish-robot` | `robot-risa-simpatica-al-ruido` | El Robot Cosquilloso |
| 6 | `14.2-my-robot-friend-heart` | `corazon-variables-eventos` | El Corazón de Mi Robot Amigo |
| 7 | `16.1-cookie-thief-alarm` | `alarma-caja-galletas` | ¡Alarma: El Ladrón de Galletas! |
| 8 | `16.2-sunflower-alarm-clock` | `despertador-por-la-manana` | El Despertador de Girasol |
| 9 | `16.3-bat-in-the-dark` | `luces-de-fiesta-al-oscurecer` | El Vuelo del Murciélago Nocturno |
| 10 | `16.4-robot-activation-challenge` | `juego-toques` | ¡El Desafío de Activación del Robot! |
| 11 | `16.5-magic-clap-switch` | `luz-encendida-al-ruido` | El Interruptor Mágico de Aplausos |
| 12 | `17.1-magic-birthday-candle` | `flama-vela-con-soplo` | La Vela Mágica de Cumpleaños |
| 13 | `19.1-digital-hot-potato` | `papas-caliente-juego` | La Papa Explosiva Digital |
| 14 | `21.1-cinematic-power-on` | `luz-encendida-ruido-animacion` | El Encendido Cinematográfico |
| 15 | `22.1-dj-metronome` | `metronomo-con-inclinacion` | El Metrónomo de DJ |
| 16 | `22.2-applause-battle` | `aplausometro-tiempo-aplausos` | La Batalla de Aplausos |
| 17 | `22.3-dont-spill-liquid-game` | `nivel-con-ruido` | ¡No Derrames el Líquido! - El Juego de Pulso |

**Logica di entrata (insight dell'autore):** `04.1-heart-beat` era progettata come PRIMA lezione (un solo output,
costruisce la logica base in ~10 min); oggi è 4ª. Documentato in §C del report e in `planificacion.html`.
NON riordinare senza che l'utente lo chieda.

---

## 5. Come servire / eseguire

```bash
# Sito (dalla ROOT del progetto)
python -m http.server 8000      # → http://localhost:8000/

# Decoder Protobject (offline, dalla cartella protobject/)
python decode_ptj.py            # tutti i 17
python decode_ptj.py 02.1-xylophone   # solo alcuni (per slug)
```

- La `pipeline-equivalence/` usa un proprio env miniconda (`pdg-vela`, porta 8080) per i suoi script Python.
- Download utente dal visore: vanno all'URL **live** di Protobject (`app.protobject.com/main?app/<code>`,
  `codetutorials.protobject.com/<code>.ptj`), NON ai file locali.

---

## 6. Dettagli tecnici (gotchas)

- **CRLF nei `.md`**: tutti i file attività hanno fine-riga Windows. Qualsiasi parser frontmatter va reso
  CRLF-tolerant — normalizzare `\r\n`→`\n` (e togliere il BOM) PRIMA della regex `^---\n`. L'engine lo fa.
- **`engine.html` (il visore):**
  - Lingua fissa `es` (tolti selettore lingua e barra filtri — erano residui multilingua).
  - Indice = `activities.json`; i **numeri 1..17** derivano dalla posizione.
  - Il menu mostra il **titolo REALE** estratto dal frontmatter `title:` di ogni `.md` (`loadIndex`/`extractTitle`).
  - All'apertura di un'attività compare un **badge `_activities/<slug>.es.md`** sotto il titolo.
  - **Deep-link + evidenziazione**: legge l'hash `#a=<slug>&q=<testo>`; cerca il testo nella vista studente,
    poi nella guida docente (modale), e se è in un commento dei blocchi mostra un avviso "está en el código".
    `report.html` genera questi link (mappa TAG2SLUG).
- **Formato `.ptj`**: `oPTJ("<json-string>")` dove la stringa = JSON dei componenti + `\n` + XML Blockly
  (con commenti in spagnolo). Parsing Blockly: preferire `<block>` a `<shadow>`; rendere il corpo
  `statement` dei cicli (non solo dei condizionali).
- **`decode_ptj.py`**: mappa `code↔slug`. Legge `equivalent-<code>.ptj` dalla ROOT (file UFFICIALI),
  scrive `<code>.xml` in `raw/` e `<slug>.txt` in `decoded/`. **NON scarica più nulla** (offline;
  `FileNotFoundError` se un `.ptj` manca; `PTJ_PREFIX="equivalent-"`).

---

## 7. Stato attuale (fatto e verificato)

- ✅ **Engine ripulito**: solo i 17, niente lingua/filtri, titoli reali, badge file, deep-link. **100% spagnolo**
  (UI + errori sentence-case + commenti del codice; `<html lang="es">`). Verificato: `node --check` OK, scan italiano LIMPIO.
- ✅ **Redazione es-CL** applicata ai `.md` (~22 correzioni: patata→papa, bombilla→ampolleta, Puzzle→Rompecabezas,
  celular uniforme, tildi/segni ¡¿). I `.md` parsano ancora (yaml.safe_load).
- ✅ **Report** verificato in modo avversariale (§A errori testo↔código, §B difetti codice, §C sequenza,
  §D scartati, §E coerenza, §F redazione, §G riferimenti incrociati).
- ✅ **`planificacion.html`** = HTML autonomo (niente più `.md` sorgente; cartella `planificacion-actividad/` eliminata).
- ✅ **`protobject/`** riorganizzato: 17 `equivalent-*.ptj` in root, `raw/` solo xml, `decoded/` txt; decoder offline.
- ✅ `motor.html` (vecchia copia orfana italiana) **eliminato**.

---

## 8. TODO / decisioni aperte

- **`pipeline-equivalence/`**: tradurre IT→ES e portare avanti il lavoro scientifico (equivalenza AST+PDG). Rinviato.
- **Decisioni di redazione NON auto-applicate** (l'utente è indeciso, non toccare senza ok): `16.1` "Sino" (nome blocco),
  `16.4` energía/toques, `17.1` flama/llama, `22.1` ultimoLatido, terminologia `for`/`while` → `contar con`/`repetir mientras`.
- **§F**: ~12 correzioni che stanno nei **commenti del CODICE** (blocchi), da fare a mano in Protobject (l'utente).
- **Bug noti non risolti** (scelta dell'utente): teacher-modal `PLACEHOLDER_0` (marked converte `__PLACEHOLDER_0__`
  in grassetto rompendo l'iniezione di `{{learn}}` in `openTeacherModal`).
- Anteprima browser via MCP (`Claude_Preview`) talvolta disconnessa → verifiche fatte via HTTP + `node --check`.

---

## 9. Memoria persistente

Esiste una memoria auto-caricata in
`~/.claude/projects/<questo-progetto>/memory/` con: `pc-activities-project.md` (dettaglio), `mai-citare-trilingui.md`,
`valuta-difficolta-a-blocchi.md`, e l'indice `MEMORY.md`. Tenere CLAUDE.md e memoria allineati quando lo stato cambia.
