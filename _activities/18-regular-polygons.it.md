---
layout: activity
title: "Arte Geometrica: Disegnare Poligoni"
image: src/18-regular-polygons/18.poligonos-regulares.svg
video: src/videos/18_regular_polygons.mp4
video_title: "Cosa faremo?"
description: "Esplora la potenza dei loop 'While' per disegnare programmaticamente forme geometriche perfette, dai triangoli agli ettagoni."
lang: it
permalink: /it/attivita/arte-geometrica-disegnare-poligoni/
ref: activity_regular_polygons

# ACTIVITY INFO
level: 2
computational_topics:
  - "Loop"
  - "Grafica e Disegno"
  - "Variabili e Dati"
general_topics:
  - "Matematica e Logica"
  - "Arte e Musica"

tags: [Loop, Loop While, Disegno, Piano Cartesiano, Geometria, Variabili]

introduction: |
  Perché disegnare un triangolo a mano quando puoi programmare un programma per disegnare un ettagono a 100 lati in pochi secondi? In questa missione, combinerai geometria e programmazione per creare un potente generatore di poligoni. Imparerai a usare il **loop 'Ripeti Mentre'** — un loop che viene eseguito finché una condizione è vera — per disegnare qualsiasi forma geometrica perfetta tu possa immaginare.

teacher: |
  ### **Corsi**
  * Classi 6-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere il concetto di un loop "while" nella programmazione.
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello dei pari.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - Il Loop Condizionale**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a disegnare forme geometriche complesse usando il codice."**
  2.  Introduci un nuovo tipo di loop. Chiedi alla classe: **"Abbiamo visto un loop che funziona per sempre. Ma se volessimo un loop che funzioni solo *mentre* una certa condizione è vera, e poi si fermi?"**
  3.  Spiega che questo è ciò che fa un loop "while". Poi, collegalo a un compito reale: disegnare un poligono. Chiedi: **"Come disegneremmo un quadrato? Disegniamo un lato, giriamo di 90 gradi, disegniamo un altro lato... ripetiamo l'azione 'disegna e gira' *mentre* abbiamo ancora lati da disegnare."** Questa è l'introduzione perfetta alla logica che costruiranno.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Il Generatore di Poligoni**
  1.  Ora che gli studenti comprendono la logica dell'uso di un loop 'while' e la semplice matematica dietro i poligoni, è tempo di costruire il loro generatore di forme.
  2.  Guidali attraverso **le istruzioni per creare il programma che disegna poligoni in base all'input della manopola**, come dettagliato nella sezione pratica qui sotto. Presta molta attenzione alla condizione del loop `while` (ad es. `while contatore < lati`) e a come viene calcolato l'angolo di rotazione.

  ### **Chiusura (5-10 minuti) - Codifica Creativa**
  1.  Una volta che tutti hanno un generatore di poligoni interattivo, è tempo di sperimentare e giocare il ruolo di un programmatore creativo.
  2.  Usa la sezione finale per sfidarli a modificare le variabili del programma. Questo li incoraggia a vedere come piccoli cambiamenti nel codice possono portare a grandi cambiamenti nell'output visivo, che è un concetto fondamentale nell'arte generativa.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Il Loop 'Ripeti Mentre'"
    type: "learn"
    icon: "book-reader"
    content: |
      Un loop **‘ripeti mentre’** è come una guardia persistente. Prima controlla una condizione. **Mentre** quella condizione è vera, esegue un blocco di codice più e più volte. Nel momento in cui la condizione diventa falsa, il loop si ferma.
      Questo è perfetto per situazioni in cui non si conosce il numero esatto di ripetizioni in anticipo, ma si conosce l'obiettivo che si sta cercando di raggiungere.
    media: "[600]https://app.protobject.com/generate?mientras&it&static&-1"

  - title: "Cos'è un poligono regolare?"
    type: "learn"
    content: |
      Un poligono regolare è una forma in cui tutti i lati hanno la stessa lunghezza e tutti gli angoli interni sono uguali. Conosci quelli semplici: un triangolo equilatero (3 lati), un quadrato (4 lati), un pentagono (5 lati).
      Ma che dire di un decagono (10 lati) o di un icosagono (20 lati)? Disegnarli a mano sarebbe molto noioso!
    media: "src/18-regular-polygons/a.polyexample.svg"

  - title: "Il Segreto della Geometria: 360 Gradi"
    type: "learn"
    content: |
      Ecco un trucco geometrico interessante: la somma degli angoli esterni di *qualsiasi* poligono regolare è sempre **360°**.
      Quindi, per capire di quanto la nostra "penna" deve girare ad ogni angolo, basta dividere 360 per il numero di lati!
      - **Triangolo**: 360 / 3 = 120° di rotazione
      - **Quadrato**: 360 / 4 = 90° di rotazione
      - **Pentagono**: 360 / 5 = 72° di rotazione
    media: "src/18-regular-polygons/b.angleexample.svg"

  - title: "Combiniamo loop e geometria!"
    type: "learn"
    content: |
      Nota lo schema che si ripete per disegnare qualsiasi poligono: **disegna una linea**, poi **ruota**. Ripetiamo questo processo finché non abbiamo disegnato tutti i lati.
      Questo è un lavoro perfetto per un loop `ripeti mentre`! Possiamo dire al programma: **MENTRE** il numero di lati che abbiamo disegnato è inferiore al numero totale di lati che vogliamo, **FAI** l'azione "disegna e ruota".
    media: "src/18-regular-polygons/z-square-anim2.svg"

  - id: "create"
    title: "Crea il Disegnatore di Poligoni"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo il prototipo. Avremo bisogno di uno smartphone e di un computer/tablet."
    steps:
      - "Aggiungi il dispositivo <comp>Manopola</comp> per controllare il numero di lati."
      - "Aggiungi il dispositivo <comp>ScriviDisegna</comp> aprendolo sullo stesso computer/tablet cliccando su <openwindow>Apri in questa finestra</openwindow>."
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
    media: "[600]https://app.protobject.com/generate?a18-polygons&it&dynamic&-1"

  - id: "reflect"
    title: "Sfida: Modifiche Creative al Codice"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Ora che hai implementato il generatore di poligoni, giochiamo con il codice!"
    content: |
      * **Mod #1: Controllo del Perimetro.** Come modificheresti il codice per rendere il poligono più grande o più piccolo?
      * **Mod #2: Direzione di Rotazione.** Cosa succede se ruoti a destra invece che a sinistra?
      * **Mod #3: Colore Dinamico.** Come possiamo cambiare il colore delle linee in base al numero di lati del poligono?
---