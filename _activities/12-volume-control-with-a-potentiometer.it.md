---
layout: activity
title: "Il Controllo del Volume"
image: src/12-volume-control-with-a-potentiometer/12.control-volumen.svg
video: src/videos/12_music_volume.mp4
video_title: "Cosa faremo?"
description: "Impara a leggere l'input continuo da una manopola virtuale (potenziometro) per controllare il volume di una canzone in tempo reale."
lang: it
permalink: /it/attivita/il-controllo-del-volume/
ref: activity_volume_control_with_a_potentiometer

# ACTIVITY INFO
level: 1
computational_topics:
  - "Sensori e Input"
  - "Loop"
general_topics:
  - "Arte e Musica"
  - "Scienza e Tecnologia"

tags: [Input Analogico, Potenziometro, Manopola, Loop Principale, Controllo Volume]

introduction: |
  Finora, i nostri pulsanti sono stati o ACCESI o SPENTI. Ma che dire di tutti i controlli intermedi? Pensa a una manopola del volume, un dimmer per la luce o un joystick. Questi richiedono un controllo fluido e graduale. In questa missione, esplorerai il mondo dell'**input analogico** programmando una manopola virtuale, nota anche come **potenziometro**. Preparati a imparare come leggere un valore che cambia continuamente per controllare il volume del tuo progetto in tempo reale.

teacher: |
  ### **Corsi**
  * Classi 3-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere il concetto di potenziometro.
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello degli altri.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - Oltre Acceso e Spento**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a creare una manopola del volume che ci dia un controllo fluido e graduale."**
  2.  Poni una domanda guida: **"Pensate a una manopola del volume su uno stereo o a un interruttore dimmer per una luce. In cosa è diverso da un semplice pulsante on/off?"**
  3.  Guida la discussione verso l'idea di valori 'graduali' o 'intermedi'. Spiega che questo si chiama **controllo analogico** e il componente che ci permette di farlo è un potenziometro. Approfondiamo come funziona e come possiamo programmarlo.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione del Controller del Volume**
  1.  Ora che gli studenti comprendono il concetto di potenziometro e come leggere il suo valore, è tempo di costruire un controller del volume in tempo reale.
  2.  Guidali attraverso **le istruzioni per collegare i componenti e programmare la logica di controllo del volume**, come dettagliato nella sezione pratica qui sotto. Incoraggiali a vedere come il valore della manopola influisce direttamente sul volume del lettore audio mentre la girano.

  ### **Chiusura (5-10 minuti) - Il Mondo dell'Analogico**
  1.  Una volta che tutti hanno una manopola del volume funzionante, è tempo di fare un brainstorming su altri usi di questo potente input analogico.
  2.  Usa la sezione finale per stimolare una discussione creativa su altre cose che possono essere controllate gradualmente e per sfidarli a visualizzare i dati del loro nuovo sensore.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Cos'è un potenziometro?"
    type: "learn"
    icon: "book-reader"
    content: |
      Hai mai regolato il volume di una radio? O cambiato la luminosità di una lampada usando un dimmer? Se sì, probabilmente hai usato un potenziometro.
      È la tecnologia dietro ogni controllo che non è solo acceso o spento, ma permette una gamma fluida di valori intermedi. Di solito, lo controlli con una **manopola**!
    media: "src/12-volume-control-with-a-potentiometer/a.main-knob.svg"

  - title: "Come funziona?"
    type: "learn"
    content: |
      Un potenziometro funziona cambiando la sua resistenza elettrica mentre lo giri. Pensalo come un rubinetto per l'elettricità. Girando la manopola, puoi cambiare **gradualmente** quanta corrente elettrica scorre attraverso di esso.
      Nel caso di un altoparlante, regolare la corrente ti permette di **aumentare o diminuire il volume** in modo fluido.
    media: "src/12-volume-control-with-a-potentiometer/b.knob-music-anim.svg"

  - title: "Come lo programmiamo?"
    type: "learn"
    content: |
      Per far funzionare la nostra manopola del volume, il nostro programma deve conoscere la sua posizione attuale. Abbiamo due ottimi modi per farlo:
      * **Il Loop Principale:** Possiamo inserire il nostro codice in un loop "ripeti per sempre". Il programma controllerà costantemente il valore della manopola e aggiornerà il volume, più e più volte.
      * **Eventi:** Un modo più efficiente! Possiamo usare un evento che si attiva *solo quando la manopola viene girata*. Il programma attende in silenzio finché non riceve un segnale, poi aggiorna il volume.
      Nella programmazione, ci sono spesso soluzioni diverse per lo stesso problema!
    media: "src/12-volume-control-with-a-potentiometer/c.loop-or-event.it.svg"

  - id: "create"
    title: "Mettiamoci al lavoro!"
    type: "create"
    icon: "cogs"
    heading_text: "Creeremo un prototipo che ci permette di controllare il volume di una canzone con un potenziometro."
    content: |
      Per prima cosa, aggiungeremo due componenti: uno per (1) riprodurre la musica e un secondo per (2) fungere da nostra manopola di controllo.
    steps:
      - "Premi <addbutton>Aggiungi Dispositivo</addbutton> e seleziona <comp>Manopola</comp>."
      - "Premi di nuovo <addbutton>Aggiungi Dispositivo</addbutton> e seleziona <comp>RiproduttoreSuoni</comp>."
      - "Ricorda che se non hai uno smartphone per scansionare i codici <qr>, puoi premere <openwindow>Apri in questa finestra</openwindow>."
    right_content:
      - text: |
          **Suggerimento**: In Protobject, puoi aggiungere più componenti sullo stesso smartphone premendo il pulsante *SCAN* tante volte quante ne hai bisogno.
      - media: "src/general-scan-button.svg"
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
      **Ricorda**: Puoi costruirlo usando un **loop principale** o, per un approccio più efficiente, usare l'**evento** che si attiva **quando la manopola viene girata**.
    media: "[700]https://app.protobject.com/generate?a12-knobvolume&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai appena sbloccato il potere del controllo analogico!"
    content: |
      Semplice ACCESO/SPENTO va bene, ma il controllo graduale apre un mondo completamente nuovo di possibilità.
      *Quali altre cose in un gioco o in un'app vorresti controllare in modo fluido con una manopola o uno slider? (Pensa alla velocità del personaggio, alla luminosità dello schermo o alla dimensione del pennello in un'app di disegno).* 
    right_content:
      - text: |
          **Sfida**: Creiamo un visualizzatore che mostri il volume attuale come un numero sullo schermo.
      - text: |
          **Suggerimento**: Avrai bisogno del componente <comp>ScriviDisegna</comp>. All'interno del tuo loop o evento, come puoi prendere il valore dalla manopola e dire al componente WriteDraw di visualizzarlo come testo?
---