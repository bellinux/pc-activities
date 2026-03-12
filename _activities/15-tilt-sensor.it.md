---
layout: activity
title: "La Livella a Bolla: È Dritta?"
image: src/15-tilt-sensor/15.sensor-inclinacion.svg
video: src/videos/15_tilt_sensor.mp4
video_title: "Cosa faremo?"
description: "Usa il sensore di inclinazione del tuo telefono e i condizionali avanzati ('Altrimenti Se') per costruire uno strumento che ti dice se qualcosa è perfettamente a livello."
lang: it
permalink: /it/attivita/la-livella-a-bolla-e-dritta/
ref: activity_tilt_sensor

# ACTIVITY INFO
level: 1
computational_topics:
  - "Condizionali e Logica"
  - "Sensori e Input"
  - "Loop"
general_topics:
  - "Scienza e Tecnologia"

tags: [Condizionali, Altrimenti Se, Multi-Condizione, Sensore di Inclinazione, Accelerometro, Loop Principale]

introduction: |
  I nostri programmi possono già fare scelte semplici: SE questo, ALLORA quello, ALTRIMENTI fai qualcos'altro. Ma la vita è solitamente più complicata di due sole opzioni! In questa missione, imparerai a gestire condizioni multiple usando il potente comando **'ALTRIMENTI SE'**. Preparati a usare l'**accelerometro** del tuo telefono per costruire una livella a bolla digitale che cambia colore in base a quanto è inclinata.

teacher: |
  ### **Corsi**
  * Classi 3-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere i concetti di “altrimenti se” (elif) e il “piano cartesiano”.
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello degli altri in compiti individuali o di squadra.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - Decisioni con Molti Percorsi**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a prototipare un rilevatore di inclinazione digitale, proprio come la livella a bolla di un falegname."**
  2.  Inizia riepilogando brevemente il condizionale 'SE/ALTRIMENTI' per due opzioni (come ACCESO/SPENTO). Poi, introduci un problema più complesso: **"Un blocco SE/ALTRIMENTI è ottimo per due scelte. Ma se hai *quattro* scelte? Ad esempio, vuoi un programma che suggerisca un pasto in base all'ora del giorno."**
  3.  Usa questa analogia per mostrare perché abbiamo bisogno di più di un semplice 'ALTRIMENTI'. Questa è la configurazione perfetta per introdurre la struttura **'ALTRIMENTI SE'** come un modo per concatenare più controlli per prendere decisioni più complesse.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione della Livella a Bolla**
  1.  Ora che gli studenti comprendono come costruire una decisione a più percorsi con 'ALTRIMENTI SE', è tempo di applicare quella logica a un sensore reale.
  2.  Guidali attraverso **le istruzioni per costruire la livella a bolla e programmare la logica multi-condizionale**, come dettagliato nella sezione pratica qui sotto. Assicurati che capiscano come ogni blocco 'ALTRIMENTI SE' controlla un diverso intervallo di valori di inclinazione, creando i diversi avvisi colorati.

  ### **Chiusura (5-10 minuti) - Riflessione su Sensori e Logica**
  1.  Una volta che la livella a bolla di tutti cambia colore correttamente, è tempo di riflettere sul sensore e sulla potente logica che hanno usato.
  2.  Usa la sezione finale per guidare una discussione sulle altre capacità dell'accelerometro e per sfidarli a creare un nuovo prototipo che combina inclinazione e suono.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Più di Due Opzioni?"
    type: "learn"
    icon: "book-reader"
    content: |
      Hai visto come i condizionali possono funzionare con due opzioni: **SE** una condizione è vera, fai qualcosa, **ALTRIMENTI** fai qualcosa di diverso. Questo è perfetto per un semplice interruttore on/off.
      Ma se hai bisogno di controllare più condizioni diverse?
    media: "src/15-tilt-sensor/a-ifsimple.it.svg"

  - title: "Introduzione a 'Altrimenti Se'"
    type: "learn"
    content: |
      La struttura **“altrimenti se”** ti permette di concatenare più controlli in un unico blocco ordinato. Puoi pensarla come un arbitro in una partita di calcio:
      * **SE** il fallo è molto grave, **ALLORA** mostra un cartellino rosso.
      * **ALTRIMENTI SE** il fallo è solo un avvertimento, **ALLORA** mostra un cartellino giallo.
      * **ALTRIMENTI** (se nessuna delle precedenti è vera), **ALLORA** è solo un semplice fallo.
      Il programma controlla ogni condizione in ordine finché non ne trova una vera.
    media: "src/15-tilt-sensor/multiple-if.it.svg"

  - title: "ALTRIMENTI SE: 4 Opzioni per la nostra Livella a Bolla"
    type: "learn"
    content: |
      Useremo questa logica a più percorsi per programmare un rilevatore di inclinazione che ci aiuti ad appendere quadri perfettamente dritti.
      Lo schermo si illuminerà con colori diversi in base al valore di inclinazione: verde per livello, giallo per leggermente fuori, arancione per più inclinato e rosso per molto inclinato.
    media: "src/15-tilt-sensor/y-multiple-inclination.svg"
  
  - title: "Come fa il telefono a rilevare l'inclinazione?"
    type: "learn"
    content: |
      Per rilevare l'inclinazione di un telefono, usiamo un piccolo sensore integrato chiamato **accelerometro**. Questo sensore può misurare forze come la gravità, indicando al telefono la sua orientazione nello spazio. Misura l'inclinazione su tre assi diversi: X (sinistra-destra), Y (avanti-indietro) e Z (su-giù). Ciò consente al telefono di sapere se è inclinato da un lato, in posizione verticale o sdraiato.
    media: "src/15-tilt-sensor/z-accelerometer.svg"

  - id: "create"
    title: "Crea il Sensore di Inclinazione"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo un prototipo che ci aiuti a rilevare se una cornice è inclinata."
    content: |
      Per prima cosa, aggiungeremo due componenti: uno per rilevare l'inclinazione del telefono e un altro per visualizzare la luce colorata.
    steps:
      - "Clicca su <addbutton>Aggiungi dispositivo</addbutton> e seleziona <comp>Inclinazione</comp>."
      - "Clicca di nuovo su <addbutton>Aggiungi dispositivo</addbutton> e seleziona <comp>Lampada</comp>."
      - "**Aggiungi entrambi i dispositivi allo stesso smartphone per questo progetto.**"
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
      Il blocco "assoluto" (che rende un numero positivo) si trova nella categoria <category>Matematica</category>, all'interno del menu a discesa del blocco "radice quadrata".
    media: "[700]https://app.protobject.com/generate?a15-inclination&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai costruito un programma che può prendere decisioni complesse!"
    content: |
      Questa catena 'SE / ALTRIMENTI SE / ALTRIMENTI' è uno strumento super potente.
      * La nostra livella a bolla ha usato l'asse Y (inclinazione avanti-indietro). Cosa pensi che succederebbe se cambiassi il codice per leggere invece l'asse X (inclinazione sinistra-destra)?
      * Quale altro strumento o gioco del mondo reale potresti costruire usando il sensore di inclinazione del tuo telefono?
    right_content:
      - text: |
          **Sfida**: Crea un lettore musicale in cui puoi regolare il volume inclinando lo smartphone su e giù.
      - text: |
          **Suggerimento**: Avrai bisogno del componente <comp>RiproduttoreSuoni</comp>. All'interno del tuo loop principale, puoi impostare il volume in base al valore che ottieni dal sensore di inclinazione.
---