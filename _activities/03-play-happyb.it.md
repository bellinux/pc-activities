---
layout: activity
title: "Suona una Canzone"
image: src/03-playing-happy-birthday/03.tocando-melodia.svg
video: src/videos/03_happy_birthday.mp4
video_title: "Cosa faremo?"
description: "Trasforma il tuo dispositivo in uno strumento musicale! Impara a sequenziare le note e a controllarne la durata per suonare una melodia familiare."
lang: it
permalink: /it/attivita/suona-una-canzone/
ref: activity_playing_happy_birthday

# ACTIVITY INFO
level: 1
computational_topics:
  - "Fondamenti di Programmazione"
  - "Temporizzazione ed Eventi"
general_topics:
  - "Arte e Musica"

tags: [Note Musicali, Sequenziamento, Temporizzazione, Suono, Altoparlante]

introduction: |
  È ora di diventare un musicista digitale! Questa attività trasformerà il tuo dispositivo in uno strumento. Imparerai a programmare una sequenza di **note musicali** e a usare la **temporizzazione** per controllarne il ritmo, componendo la classica canzone 'Tanti Auguri' un blocco alla volta.
  
teacher: |
  ### **Corsi**
  * Classi 3-12

  ### **Materiali**
  * Smartphone, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere i concetti di sequenziamento dei passaggi.
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello degli altri.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - La Scienza del Suono**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a creare un prototipo di un giocattolo musicale."**
  2.  Stimola la loro curiosità con una domanda: **"Come pensate che il vostro telefono o le vostre cuffie producano il suono?"**
  3.  Dopo una breve discussione, è tempo di demistificare la tecnologia. Esploriamo come un semplice altoparlante può trasformare segnali elettrici silenziosi nella musica e nei suoni che sentiamo ogni giorno.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Composizione della Melodia**
  1.  Ora che tutti comprendono le basi del suono digitale, iniziamo a comporre! La missione è ricreare la canzone "Tanti Auguri" programmando la sequenza corretta di note e ritardi.
  2.  Guida i tuoi studenti attraverso **le istruzioni passo-passo per costruire la melodia**, che sono dettagliate nella sezione pratica qui sotto.
  3.  La sequenza di note richiesta è: **Do4, Do4, Sol4, Sol4, La4, La4, Sol4, Fa4, Fa4, Mi4, Mi4, Re4, Re4, Do4**. Assicurati che dispongano i blocchi in questo ordine preciso.

  ### **Chiusura (5-10 minuti) - Riflessione e Remix**
  1.  Una volta che gli studenti hanno una canzone funzionante, sfidali a pensare come produttori musicali. Come potrebbero cambiare il tempo?
  2.  Poni la sfida: **"E se volessimo suonare la canzone più velocemente o più lentamente?"** Usa questa domanda per avviare una discussione su come cambiare ogni singolo valore di ritardo possa essere noioso, preparando il terreno per concetti più avanzati come le variabili. Usa la sezione finale per guidare la conversazione.

  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Come producono il suono i dispositivi?"
    type: "learn"
    icon: "book-reader"
    content: |
      Ti sei mai chiesto come il tuo telefono possa far esplodere le tue canzoni preferite? La magia avviene in un piccolo componente chiamato **altoparlante**. Pensalo come un dispositivo che converte i segnali elettrici in onde sonore. Un magnete e una bobina all'interno si muovono quando l'elettricità li attraversa, facendo vibrare un cono. Queste vibrazioni creano le onde sonore che viaggiano attraverso l'aria fino alle nostre orecchie.
      Il nostro cervello interpreta queste onde come musica, voci o effetti sonori, permettendoci di goderci un film o cantare una canzone.
    media: "src/03-playing-happy-birthday/a-speaker.svg"

  - title: "Gli altoparlanti sono ovunque!"
    type: "learn"
    content: |
      Puoi trovare altoparlanti in tutti i tipi di dispositivi! Sono nella tua TV, dentro le tue cuffie e, naturalmente, nel tuo smartphone. Se hai mai guardato un video o ascoltato musica sul tuo telefono, hai sentito i suoi altoparlanti in azione.
    media:
      - "src/03-playing-happy-birthday/a-tv.svg"
      - "src/03-playing-happy-birthday/a-headphones.svg"
      - "src/03-playing-happy-birthday/a-smartphone.svg"

  - id: "create"
    title: "Suoniamo una Canzone"
    type: "create"
    icon: "cogs"
    heading_text: "Creeremo un prototipo che suona 'Tanti Auguri' sul telefono. Per prima cosa, colleghiamo il nostro dispositivo."
    steps:
      - "Clicca su <addbutton>Aggiungi dispositivo</addbutton> nella barra laterale sinistra."
      - "Seleziona il componente <comp>TastieraMusicale</comp> per suonare le note sullo smartphone."
      - "Scansiona il codice <qr> con il tuo smartphone o premi <openwindow>Apri in questa finestra</openwindow>."

  - title: "Trascina le note!"
    type: "create"
    content: |
      Per costruire una melodia, devi trascinare i blocchi delle note nell'area di lavoro nella sequenza corretta.
    media: "src/03-playing-happy-birthday/a-dragnote.it.svg"
    
  - title: "Come controllare la durata di una nota?"
    type: "create"
    content: |
      ### Usiamo i ritardi!

      Una melodia non è fatta solo di note; è anche ritmo. Per controllare per quanto tempo una nota viene suonata, devi aggiungere una pausa prima che inizi la successiva.
      
      Ad esempio:
      * suona una nota
      * **aspetta 400 millisecondi**
      * suona la nota successiva
      * **aspetta 200 millisecondi**
      * … e così via.
    right_content:
      - text: |
          **Suggerimento Pro:** I blocchi di **ritardo** che controllano queste pause si trovano nella categoria <category>Temporizzazione</category>. Sono essenziali per creare il ritmo della tua canzone!

  - title: "Qual è la sequenza di note e ritardi?"
    type: "create"
    content: |
      La parte principale di “Tanti Auguri” ha questa sequenza di note con i rispettivi ritardi, misurati in millisecondi (ms).
    media: "src/03-playing-happy-birthday/a-noteduration.es.it.svg"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
    media: "[700]https://app.protobject.com/generate?a03-melody&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai programmato una canzone, ma se volessi un remix?"
    content: |
      Per cambiare il tempo, devi regolare i ritardi. In questo momento, la tua canzone usa pause di 200, 400 e 600 millisecondi.

      E se volessi suonarla due volte più velocemente? Dovresti tornare indietro e cambiare *ogni singolo blocco di ritardo* a mano. Sembra un sacco di lavoro! C'è un modo più intelligente ed efficiente per controllare la velocità?
---