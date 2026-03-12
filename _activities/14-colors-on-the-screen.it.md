---
layout: activity
title: "Mescolare i Colori RGB"
image: src/14-colors-on-the-screen/14.colores-pantalla2.svg
video: src/videos/14_color_mix.mp4
video_title: "Cosa faremo?"
description: "Diventa un artista digitale! Usa tre manopole per controllare i canali Rosso, Verde e Blu e mescola qualsiasi colore tu possa immaginare."
lang: it
permalink: /it/attivita/mescolare-i-colori-rgb/
ref: activity_colors_on_the_screen

# ACTIVITY INFO
level: 1
computational_topics:
  - "Sensori e Input"
  - "Loop"
general_topics:
  - "Arte e Musica"
  - "Scienza e Tecnologia"

tags: [Teoria del Colore, RGB, Potenziometro, Loop Principale, Input Analogico, Mescolanza di Colori]

introduction: |
  Come fa lo schermo del tuo telefono o della tua TV a creare milioni di colori diversi quando usa solo tre tipi di piccole luci? Mescolandoli! In questa missione, diventerai un artista digitale e uno scienziato del colore. Prenderai il controllo dei tre colori primari della luce — **Rosso**, **Verde** e **Blu (RGB)** — usando tre manopole separate per mescolare qualsiasi colore tu possa immaginare e padroneggiare l'arcobaleno digitale.

teacher: |
  ### **Corsi**
  * Classi 3-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere il concetto di colore e come viene rappresentato digitalmente (RGB).
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello degli altri individualmente o in team.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - La Scienza del Colore**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo come gli schermi creano ogni colore che abbiate mai visto."**
  2.  Poni una domanda guida: **"Come pensate che i vostri occhi vedano il colore di una mela? E in che modo è diverso da come uno schermo *crea* il colore?"**
  3.  Questa discussione porterà naturalmente all'idea di luce riflessa contro luce emessa. Spiega che gli schermi funzionano *aggiungendo* luce insieme, che è il momento perfetto per introdurre i due principali modelli di colore: Additivo (per gli schermi) e Sottrattivo (per la stampa).

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Mescolare l'Arcobaleno**
  1.  Ora che gli studenti hanno una solida comprensione della teoria del colore RGB, è tempo di metterla in pratica e diventare dei miscelatori di colori digitali.
  2.  Guidali attraverso **le istruzioni per configurare il loro controller a tre manopole e programmare la logica di miscelazione dei colori**, come dettagliato nella sezione pratica qui sotto. Questo è un ottimo esercizio per gestire più input in tempo reale contemporaneamente.

  ### **Chiusura (5-10 minuti) - Diventare un Esperto di Colori**
  1.  Una volta che tutti stanno sperimentando la creazione di colori diversi, riunisci il gruppo per una riflessione finale su ciò che hanno imparato.
  2.  Usa la sezione finale per rafforzare i concetti fondamentali della teoria del colore e per sfidarli a creare una lampada che cambia colore automaticamente, senza alcuna manopola.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Come vediamo i colori?"
    type: "learn"
    icon: "book-reader"
    content: |
      Quando la luce colpisce un oggetto, come una mela, la superficie dell'oggetto assorbe la maggior parte della luce ma ne riflette una parte. I nostri occhi vedono questa luce riflessa.
      Se vediamo una mela **rossa**, significa che la sua buccia sta assorbendo tutti i colori *tranne* il rosso. La luce rossa rimbalza, raggiunge i nostri occhi e il nostro cervello dice: "Quello è rosso!"
    media: "src/14-colors-on-the-screen/a.reflection2.svg"

  - title: "Come mescoliamo i colori?"
    type: "learn"
    content: |
      Per creare colori con la luce, dobbiamo mescolare diversi **raggi di luce**. Se mescoliamo **tutti** i colori della luce insieme, otteniamo una **luce bianca** pura. La totale assenza di luce è il **nero**.
      Puoi vederlo in natura! Dopo che piove, piccole gocce d'acqua nell'aria possono agire come prismi e **separare** la luce solare bianca in tutti i suoi colori componenti, creando un **arcobaleno**!
    media: "src/14-colors-on-the-screen/b.color_.freedom2.svg"

  - title: "Sintesi Sottrattiva (Pittura e Inchiostro)"
    type: "learn"
    content: |
      In questo modello, il colore di un oggetto dipende dalla luce che **riflette**. I colori primari sono Ciano, Magenta e Giallo. Poiché questo modello funziona *sottraendo* (assorbendo) la luce, mescolando tutti e tre i colori si ottiene il **Nero**. Questo modello è usato per cose che non emettono la propria luce, come la stampa fotografica, i coloranti e le vernici.
    media: "src/14-colors-on-the-screen/c-sustractive.it.svg"
  
  - title: "Sintesi Additiva (Schermi e Luce)"
    type: "learn"
    content: |
      In questo modello, il colore viene creato **aggiungendo** diverse luci insieme. I colori primari sono **Rosso, Verde e Blu (RGB)**.
      - **Rosso + Verde** = **Giallo**
      - **Verde + Blu** = **Ciano**
      - **Rosso + Blu** = **Magenta**
      Poiché stiamo mescolando luce pura, combinando tutti e tre alla massima intensità si ottiene la **Luce Bianca**. Questo modello è usato per tutti gli schermi, come TV, telefoni e monitor di computer.
    media: "src/14-colors-on-the-screen/d-additive.it.svg"

  - title: "Come usa un monitor l'RGB?"
    type: "learn"
    content: |
      Il tuo schermo è composto da milioni di piccoli punti chiamati pixel. Ogni pixel è in realtà un team di tre LED ancora più piccoli: uno **R**osso, uno **V**erde e uno **B**lu.
      Per creare un colore specifico per quel singolo pixel — diciamo, viola — lo schermo dice ai LED rossi e blu di accendersi brillantemente e a quello verde di rimanere debole. Moltiplica questo processo per milioni di pixel e otterrai un'immagine completa e ricca!
    media: "src/14-colors-on-the-screen/e-pixels.svg"

  - id: "create"
    title: "Giochiamo con i Colori!"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo un prototipo che ci permetta di mescolare e creare qualsiasi colore di luce."
    content: |
      Avremo bisogno di 4 componenti: 1 lampada per mostrare il colore e 3 manopole per controllare ogni colore primario (Rosso, Verde e Blu).
    steps:
      - "Premi <addbutton>Aggiungi dispositivo</addbutton>, seleziona <comp>Lampada</comp> e premi <openwindow>Apri in questa finestra</openwindow>."
      - "Premi <addbutton>Aggiungi dispositivo</addbutton>, seleziona <comp>Manopola</comp> e scansiona il codice <qr> con uno smartphone per controllare il colore **rosso**."
      - "Aggiungi altri due componenti <comp>Manopola</comp> su altri due smartphone per controllare i colori **verde** e **blu**."
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
    media: "[700]https://app.protobject.com/generate?a14-colors&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Ora sei un maestro dell'arcobaleno digitale!"
    content: |
      * Quali sono le 'ricette' RGB per alcuni dei tuoi colori preferiti, come l'arancione, il rosa o il verde acqua? Sperimenta e scoprilo!
      * Quando modifichi una foto su un'app, stai usando il modello di colore Additivo o Sottrattivo? E quando mescoli la vernice per un progetto artistico?
    right_content:
      - text: |
          **Sfida**: Creiamo una lampada che cicla gradualmente attraverso tutti i colori dell'arcobaleno da sola, senza essere controllata da manopole!
      - text: |
          **Suggerimento**: Potresti usare loop e variabili per aumentare e diminuire lentamente i valori di Rosso, Verde e Blu nel tempo.
---