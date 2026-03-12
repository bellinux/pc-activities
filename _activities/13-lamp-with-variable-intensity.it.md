---
layout: activity
title: "Controlla l'Intensità della Luce"
image: src/13-lamp-with-variable-intensity/13.lampara-intensidad-variable.svg
video: src/videos/13_light_intensity.mp4
video_title: "Cosa faremo?"
description: "Esplora il mondo del colore e della luce usando una manopola per cambiare gradualmente la luminosità di una lampada dal nero al bianco."
lang: it
permalink: /it/attivita/controlla-lintensita-della-luce/
ref: activity_lamp_with_variable_intensity

# ACTIVITY INFO
level: 1
computational_topics:
  - "Sensori e Input"
  - "Temporizzazione ed Eventi"
general_topics:
  - "Scienza e Tecnologia"

tags: [Potenziometro, Eventi, Input Analogico, Colore, Scala di Grigi, Intensità Luminosa]

introduction: |
  Abbiamo usato una manopola per controllare il volume; ora usiamo lo stesso potere analogico per controllare la luce! In questa missione, ti tufferai nella scienza del colore digitale (RGB) e imparerai come il tuo schermo crea ogni sfumatura dal nero puro al bianco brillante. Costruirai quindi il tuo interruttore dimmer, usando un **potenziometro** per controllare fluidamente l'intensità di una lampada virtuale.

teacher: |
  ### **Corsi**
  * Classi 3-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere i concetti di eventi e potenziometri.
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello degli altri.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - La Scienza del Colore dello Schermo**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a prototipare una lampada con intensità variabile, un interruttore dimmer."**
  2.  Poni una domanda guida: **"Avete mai notato che i colori in una rivista stampata sembrano diversi dalla stessa immagine su uno schermo? Perché pensate che sia così?"**
  3.  Questa domanda è il gateway perfetto per spiegare la differenza tra **colore sottrattivo** (inchiostro/pittura) e **colore additivo** (luce/schermi). Spiega che gli schermi usano il modello additivo RGB (Rosso, Verde, Blu). Poi, introduci lo strumento per il controllo graduale: il **potenziometro**, che fungerà da nostro dimmer.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione del Dimmer**
  1.  Ora che gli studenti comprendono la teoria del colore additivo e come un potenziometro può controllarlo, è tempo di costruire l'interruttore dimmer.
  2.  Guidali attraverso **le istruzioni per creare la lampada e programmare il controllo dell'intensità**, come dettagliato nella sezione pratica qui sotto. Assicurati che vedano come il singolo valore della manopola viene immesso in tutti e tre i canali di colore (R, G e B) per creare un effetto in scala di grigi.

  ### **Chiusura (5-10 minuti) - Riflessione su Colore e Controllo**
  1.  Una volta che tutti hanno un interruttore dimmer funzionante, è tempo di riflettere sulla teoria del colore che hanno appena messo in pratica.
  2.  Usa la sezione finale per guidare una discussione sul controllo dei singoli colori (un ottimo teaser per la prossima attività) e per sfidarli a combinare luce e suono nel loro progetto.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Colori Stampa vs. Schermo"
    type: "learn"
    icon: "book-reader"
    content: |
      Il **colore sottrattivo** (come l'inchiostro su carta) inizia con una superficie bianca e *sottrae* luce. Mescolando tutti i colori primari dell'inchiostro (Ciano, Magenta, Giallo) si ottiene il nero.
      Il **colore additivo** (come uno schermo del telefono) inizia con una superficie nera e *aggiunge* luce. I colori primari sono Rosso, Verde e Blu (RGB). Mescolando tutti e tre alla massima intensità si crea una luce bianca pura. Questo è il modello che usiamo in Protobject!
    media: "src/13-lamp-with-variable-intensity/a-additive-substactive.it.svg"

  - title: "Colore Additivo e Sfumature di Grigio"
    type: "learn"
    content: |
      Nel modello additivo RGB, possiamo creare diverse sfumature di grigio mescolando **quantità uguali** di luce rossa, verde e blu.
      * Una **bassa intensità** di tutti e tre i colori si traduce in un **grigio scuro**.
      * Un'**alta intensità** di tutti e tre si traduce in un **grigio chiaro**.
      * Il **nero** è la totale assenza di luce (tutti i colori spenti), mentre il **bianco** è tutti e tre i colori alla loro massima intensità.
    media: "src/13-lamp-with-variable-intensity/b-opacity.svg"

  - title: "Usare un Potenziometro per Controllare l'Intensità"
    type: "learn"
    content: |
      Per controllare la luminosità della nostra luce, abbiamo bisogno di un input analogico. Il **potenziometro** è lo strumento perfetto per questo! È un componente, solitamente controllato con una manopola, che fornisce una gamma fluida di valori.
      Possiamo usare il valore del potenziometro per impostare la luminosità per i pixel rossi, verdi e blu sullo schermo tutti insieme. Girando la manopola, possiamo far visualizzare allo schermo qualsiasi sfumatura dal nero fino al bianco.
    media: "src/13-lamp-with-variable-intensity/b-opacity-knob.svg"
  
  - title: "Mettiamoci al lavoro!"
    type: "learn"
    content: |
      Useremo il potenziometro per modificare l'intensità della nostra lampada. Mentre giriamo la manopola, il nostro programma leggerà il suo valore e lo convertirà in un livello di luminosità per la lampada, regolandolo in tempo reale.
    media: "src/a.working.svg"

  - id: "create"
    title: "Crea la Lampada Variabile"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo il prototipo per controllare l'intensità della luce."
    content: |
      Per prima cosa, aggiungeremo due componenti: uno che funga da lampada e un altro che sia la nostra manopola dimmer.
    steps:
      - "Premi <addbutton>Aggiungi Dispositivo</addbutton>, seleziona <comp>Lampada</comp> e premi <openwindow>Apri in questa finestra</openwindow>."
      - "Premi di nuovo <addbutton>Aggiungi Dispositivo</addbutton>, seleziona <comp>Manopola</comp> e scansiona il codice <qr> con il tuo smartphone."
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
      I blocchi di colore si trovano nella categoria <category>Colore</category>.
      **Ricorda**: Puoi costruirlo usando un **evento** (più efficiente) o un **loop principale**.
    media: "[700]https://app.protobject.com/generate?a13.knobluz&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai controllato l'intensità della luce bianca!"
    content: |
      Lo hai fatto inviando lo *stesso* valore dalla manopola ai canali Rosso, Verde e Blu.
      *Ma se inviassi valori *diversi*? Come programmeresti la manopola per regolare solo l'intensità della luce rossa, mentre il verde e il blu rimangono spenti?*
    right_content:
      - text: |
          **Sfida**: Modifica il progetto in modo che quando l'intensità della luce (il valore della manopola) supera 80, inizi a suonare una canzone.
      - text: |
          **Suggerimento**: Avrai bisogno del componente <comp>RiproduttoreSuoni</comp>. All'interno del tuo evento o loop, puoi usare un condizionale: **SE** il valore della manopola è maggiore di 80, **ALLORA** riproduci la canzone, **ALTRIMENTI** ferma la canzone.
---