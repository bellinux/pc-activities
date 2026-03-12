---
layout: activity
title: "Il Misuratore di Rumore"
image: src/17-noise-visualizer/17.visualizador-ruido.svg
video: src/videos/17_noise_visualizer.mp4
video_title: "Cosa faremo?"
description: "Impara le basi del disegno su una tela digitale creando una linea che cresce e si restringe con il volume del rumore circostante."
lang: it
permalink: /it/attivita/il-misuratore-di-rumore/
ref: activity_noise_visualizer

# ACTIVITY INFO
level: 2
computational_topics:
  - "Grafica e Disegno"
  - "Sensori e Input"
  - "Loop"
general_topics:
  - "Matematica e Logica"
  - "Arte e Musica"

tags: [Piano Cartesiano, Disegno, Coordinate, Sensore di Rumore, Loop Principale, Visualizzazione Dati]

introduction: |
  Come puoi trasformare il suono in un'immagine? In questa missione di Livello 2, ci tufferemo nel mondo della grafica digitale! Imparerai come i programmatori usano il **Piano Cartesiano** (coordinate X e Y) per disegnare forme e linee su uno schermo. Preparati a costruire un visualizzatore di rumore in tempo reale che utilizza l'input del tuo microfono per controllare un display grafico dinamico.
  
teacher: |
  ### **Corsi**
  * Classi 6-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere i concetti del piano cartesiano e del disegno su schermo.
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello degli altri.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - La Tela è una Mappa**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a prototipare un visualizzatore di rumore, trasformando il suono in grafica."**
  2.  Inizia la lezione con una domanda che si collega alle loro lezioni di matematica: **"Avete mai sentito parlare del piano cartesiano in matematica? A cosa serve?"**
  3.  Collega le loro risposte al mondo della programmazione. Spiega che ogni schermo — dal loro telefono a un videogioco — è una griglia. I programmatori usano le coordinate X e Y per posizionare ogni singolo elemento visivo. Oggi diventeranno artisti digitali, usando questo sistema per disegnare una linea la cui lunghezza è controllata dal suono.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Disegnare con i Dati**
  1.  Ora che gli studenti comprendono i fondamenti del disegno su un piano di coordinate, è tempo di costruire il loro visualizzatore di suoni.
  2.  Guidali attraverso **le istruzioni per creare la tela da disegno e programmare la logica di visualizzazione**, come dettagliato nella sezione pratica qui sotto. Presta molta attenzione al blocco `disegna linea` e a come il livello di rumore dal sensore viene utilizzato per determinare la lunghezza della linea in tempo reale.

  ### **Chiusura (5-10 minuti) - L'Artista Digitale**
  1.  Una volta che tutti hanno un visualizzatore funzionante che reagisce alla loro voce, è tempo di riflettere sui nuovi poteri grafici che hanno sbloccato.
  2.  Usa la sezione finale per sfidare la loro comprensione del sistema di coordinate e per introdurre una sfida di visualizzazione più complessa che coinvolge forme e testo.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Cos'è il Piano Cartesiano?"
    type: "learn"
    icon: "book-reader"
    content: |
      Pensa a uno schermo non come a una superficie piana, ma come a un foglio di carta millimetrata. Per dire al computer dove disegnare qualcosa, devi dargli un "indirizzo", proprio come una posizione su una mappa. Questa mappa è chiamata **Piano Cartesiano**. È un sistema di coordinate composto da due assi perpendicolari: la linea orizzontale è chiamata **asse X** e la linea verticale è chiamata **asse Y**. Il punto in cui si incontrano è l'"origine" (0,0).
    media: "src/17-noise-visualizer/a-cartesian.svg"

  - title: "Come funzionano gli assi X e Y?"
    type: "learn"
    content: |
      L'**asse X** (orizzontale) funziona proprio come una linea numerica: i numeri più piccoli sono a sinistra e i numeri più grandi sono a destra. L'**asse Y** (verticale) posiziona i numeri più piccoli in basso e quelli più grandi in alto. Combinando un valore X e un valore Y, possiamo definire la posizione precisa di qualsiasi punto sullo schermo.
    media: 
      - "src/17-noise-visualizer/b-cartesianx.svg"
      - "src/17-noise-visualizer/c-cartesiany.svg"

  - title: "Il Primo Quadrante"
    type: "learn"
    content: |
      Il piano cartesiano è diviso in quattro quadranti. In Protobject, per mantenere le cose semplici, usiamo principalmente il **primo quadrante**, dove sia i valori X che Y sono numeri positivi. Il punto di origine (0,0) corrisponde all'angolo in basso a sinistra della nostra tela da disegno.
    media: "src/17-noise-visualizer/d-quadrants.svg"

  - title: "Come Disegnare una Linea"
    type: "learn"
    content: |
      Per disegnare una linea, devi solo dare al computer tre istruzioni: un punto di partenza (una coordinata X, Y), la direzione in cui viaggiare (un angolo) e quanto lontano andare (una lunghezza).
      Per una barra verticale, inizieremo dal fondo dello schermo, punteremo dritto verso l'alto (un angolo di 90 gradi) e faremo cambiare la lunghezza in base al livello di rumore!
    media: "src/17-noise-visualizer/f-drawlin.svg"

  - title: "Perché visualizzare il rumore?"
    type: "learn"
    content: |
      Visualizzare l'intensità del suono non è solo per divertimento; è utile! In ambienti rumorosi come le fabbriche, un misuratore di rumore può aiutare a proteggere l'udito dei lavoratori. In un'aula o in una biblioteca, può essere un ottimo spunto visivo per aiutare tutti a essere più consapevoli dei livelli di rumore, creando un ambiente migliore per l'apprendimento e la concentrazione.
    media: 
      - "src/17-noise-visualizer/g-mechanical.svg"
      - "src/17-noise-visualizer/h-classrooml.svg"

  - id: "create"
    title: "Crea il Visualizzatore di Rumore"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo il prototipo che visualizza il livello di rumore in tempo reale."
    content: |
      Per prima cosa, dobbiamo aggiungere due componenti: uno per (1) rilevare il rumore con il microfono e un altro per (2) fungere da nostra tela da disegno.
    steps:
      - "Premi <addbutton>Aggiungi Dispositivo</addbutton>, seleziona <comp>LivelloRumore</comp> e scansiona il codice <qr> con il tuo smartphone."
      - "Clicca su <addbutton>Aggiungi Dispositivo</addbutton>, seleziona <comp>ScriviDisegna</comp> e premi <openwindow>Apri in questa finestra</openwindow> per generare una superficie di disegno sul computer."
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice. Nota che dobbiamo pulire lo schermo in ogni ciclo del loop per cancellare la vecchia linea prima di disegnare quella nuova!
    media: "[600]https://app.protobject.com/generate?a17-noisevisualizer&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai appena disegnato con i dati! Ora, diventiamo creativi."
    content: |
      * Il nostro codice disegna una linea verticale. Come cambieresti i parametri del blocco "disegna linea" per renderla invece una linea **orizzontale**?
      * Oltre a una linea, in quali altri modi potresti visualizzare il rumore? Un cerchio che cresce? Un colore che cambia da verde a rosso?
    right_content:
      - text: |
          **Sfida**: Creiamo un visualizzatore di rumore per un'aula. Vogliamo che mostri un cerchio che cresce all'aumentare del livello di rumore. Inoltre, se il livello di rumore diventa troppo alto (supera un valore specifico), dovrebbe visualizzare la parola **SILENZIO!** sullo schermo.
      - text: |
          **Suggerimento**: Puoi usare il blocco "disegna un punto a" per disegnare il cerchio e impostare la sua dimensione in base al livello di rumore. Avrai bisogno di un condizionale (blocco SE) per controllare il livello di rumore e decidere quando scrivere il testo.
    media: "src/videos/silent_challenge.mp4"
---