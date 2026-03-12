---
layout: activity
title: "Il Puntatore Digitale"
image: src/22-presentation-pointer/22.puntero-presentaciones.svg
video: src/videos/22_laser_pointer.mp4
video_title: "Cosa faremo?"
description: "Combina l'accelerometro, il giroscopio e il magnetometro del tuo telefono per creare un puntatore che puoi controllare con il movimento."
lang: it
permalink: /it/attivita/il-puntatore-digitale/
ref: activity_presentation_pointer

# ACTIVITY INFO
level: 3
computational_topics:
  - "Sensori e Input"
  - "Grafica e Disegno"
  - "Loop"
general_topics:
  - "Scienza e Tecnologia"

tags: [Fusione di Sensori, Accelerometro, Giroscopio, Magnetometro, Eventi, Loop Principale, Disegno, Coordinate]

introduction: |
  Come fa il tuo telefono a sapere di ruotare lo schermo quando lo giri di lato? O come fa un visore VR a tracciare ogni tuo movimento? Il segreto è una tecnica potente chiamata **Fusione di Sensori**. In questa missione avanzata di Livello 3, imparerai come il tuo telefono combina il suo accelerometro, giroscopio e magnetometro per individuare la sua esatta orientazione nello spazio 3D. Preparati a sfruttare questi dati per costruire un puntatore digitale controllato dal movimento, proprio come un puntatore laser ad alta tecnologia!
teacher: |
  ### **Corsi**
  * Classi 9-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere cosa sono i sensori di movimento del telefono e come lavorano insieme (Fusione di Sensori).
  * Essere in grado di posizionare elementi su un piano cartesiano.
  * Comprendere il concetto di una funzione computabile.
  * Valutare il proprio lavoro e quello degli altri.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - Il Sesto Senso del Telefono**
  1.  Introduci l'attività: **"Oggi impareremo a prototipare un puntatore per presentazioni controllato dal movimento, usando alcuni dei sensori più avanzati del vostro telefono."**
  2.  Inizia questa lezione avanzata con una domanda intrigante: **"Il vostro telefono è solo un blocco di vetro e metallo. Come fa a sapere qual è l'alto, il basso, la sinistra e la destra nel mondo reale?"**
  3.  Spiega che non è uno, ma un team di sensori che lavorano insieme. Introduci brevemente i tre attori principali: l'accelerometro (per il movimento), il giroscopio (per la rotazione) e il magnetometro (come una bussola). Poi, introduci il concetto principale: la **Fusione di Sensori**, il processo di combinare tutti questi dati per ottenere un risultato super accurato.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Programmazione con Dati Fusi**
  1.  Ora che gli studenti hanno una comprensione concettuale della Fusione di Sensori, è tempo di usare quei dati fusi per controllare un oggetto sullo schermo.
  2.  Guidali attraverso **le istruzioni per creare il puntatore e programmare la logica di controllo del movimento**, come dettagliato nella sezione pratica qui sotto. Questa è una costruzione complessa, quindi presta molta attenzione a come gli output X e Y del sensore vengono utilizzati per aggiornare le coordinate del puntatore.

  ### **Chiusura (5-10 minuti) - Il Team dei Sensori**
  1.  Una volta che tutti hanno il loro puntatore controllato dal movimento funzionante, è tempo di riflettere sulla tecnologia avanzata che hanno appena implementato.
  2.  Usa la sezione finale per guidare una discussione che rafforzi la loro comprensione dei diversi sensori e dei loro ruoli, e per sfidarli con una versione multiplayer del progetto.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Come fa il telefono a conoscere la sua orientazione?"
    type: "learn"
    icon: "book-reader"
    content: |
      Immagina di essere in una stanza buia e vuota con gli occhi bendati. Probabilmente potresti ancora indicare 'su' e 'giù' perché puoi sentire la gravità. Il tuo telefono fa qualcosa di simile, ma è molto più avanzato. Per conoscere la sua esatta orientazione nello spazio 3D, utilizza un team di sensori specializzati.
    media: "src/22-presentation-pointer/a-orientation.svg"

  - title: "Incontra il Team dei Sensori"
    type: "learn"
    content: |
      Il senso dell'orientamento del tuo telefono proviene da tre specialisti principali:
      * **Accelerometro**: Il 'Rilevatore di Movimento'. Percepisce l'accelerazione lineare — muovendosi avanti/indietro, sinistra/destra e su/giù.
      * **Giroscopio**: Lo 'Specialista della Rotazione'. Rileva torsioni e giri, misurando i cambiamenti nell'angolo del telefono.
      * **Magnetometro**: Il 'Navigatore'. È una bussola digitale che rileva i campi magnetici, sapendo sempre da che parte è il Nord.
    media: 
      - "src/22-presentation-pointer/z-accelerometer.svg"
      - "src/22-presentation-pointer/b-gyroscope-orientation.svg"
      - "src/22-presentation-pointer/c-magnetometer.svg"

  - title: "Lavorare Insieme: Fusione di Sensori"
    type: "learn"
    content: |
      Nessuno di questi sensori è perfetto da solo. L'accelerometro può essere instabile e il giroscopio può 'andare alla deriva' nel tempo. Ma quando lavorano insieme, i loro punti di forza coprono le debolezze reciproche. Questa collaborazione è chiamata **Fusione di Sensori**. Il software del telefono 'fonde' intelligentemente i dati di tutti e tre i sensori per ottenere una singola lettura altamente accurata della sua orientazione. È il lavoro di squadra definitivo!
    media: "src/22-presentation-pointer/d-fusion.it.svg"
  
  - title: "Dalla Fusione alle Coordinate"
    type: "learn"
    content: |
      Il risultato della Fusione di Sensori è un flusso di dati numerici. Il nostro lavoro come programmatori è dare un significato a quei dati. Quando muoviamo il telefono, i valori per gli assi di rotazione X e Y cambiano. Leggendo questi valori, possiamo mappare il movimento fisico del telefono alle coordinate X e Y di un puntatore sulla nostra tela digitale.
    media: "src/22-presentation-pointer/e-coordenates.svg"

  - id: "create"
    title: "Crea il Puntatore per Presentazioni"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo il prototipo: avremo bisogno di uno smartphone e di un computer/tablet."
    steps:
      - "Sullo stesso smartphone, aggiungi i componenti <comp>Direzione</comp> e <comp>BottoneTouch</comp>."
      - "Aggiungi il dispositivo <comp>ScriviDisegna</comp> aprendolo sul tuo computer/tablet cliccando su <openwindow>Apri in questa finestra</openwindow>."
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
    media: "[600]https://app.protobject.com/generate?a22-pointermap&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai appena sfruttato una funzionalità avanzata dello smartphone! Rivediamo il team dei sensori:"
    content: |
      * Quale sensore agisce come una bussola, rilevando il nord magnetico?
      * Quale sensore è il migliore per rilevare inclinazioni e rotazioni?
      * Qual è lo scopo del pulsante 'reset' in questo progetto? Cosa succede se non lo usi?
    right_content:
      - text: |
          **Sfida**: Programmiamo due puntatori contemporaneamente in modo che due persone possano indicare indipendentemente aree diverse dello schermo con i propri telefoni!
---