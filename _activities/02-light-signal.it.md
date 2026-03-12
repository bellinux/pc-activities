---
layout: activity
title: "Crea un Segnale Luminoso Lampeggiante"
image: src/02-light-signals/cover.svg
video: src/videos/02_beacon.mp4
video_title: "Cosa faremo?"
description: "Scopri come controllare la velocità del tuo codice programmando una sequenza di luci lampeggianti."
lang: it
permalink: /it/attivita/crea-un-segnale-luminoso-lampeggiante/
ref: activity_light_signals

# ACTIVITY INFO
level: 1
computational_topics:
  - "Fondamenti di Programmazione"
  - "Temporizzazione ed Eventi"
general_topics:
  - "Scienza e Tecnologia"

tags: [Temporizzazione, Blocco di Ritardo, Sequenziamento, Segnale Luminoso, Effetto Lampeggiante]

introduction: |
  Hai mai visto le luci lampeggianti su una torre o un veicolo di emergenza e ti sei chiesto come vengono controllate? Quel lampeggiare non è casuale, è programmato con un senso del **tempo**. In questa missione, diventerai il maestro del tempo, imparando a usare i **ritardi** per creare da zero il tuo segnale luminoso lampeggiante.
  
teacher: |
  ### **Corsi**
  * Classi 3-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Descrizione**
  In questa attività, gli studenti impareranno il concetto fondamentale di programmazione della "temporizzazione". Useranno i blocchi di ritardo per controllare la sequenza di una lampada virtuale, creando un classico effetto di segnale luminoso lampeggiante e comprendendo perché le pause sono cruciali nella programmazione.

  ### **Obiettivi Educativi**
  * Comprendere i concetti di "LED" e "temporizzazione".
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello degli altri, sia individualmente che in team.
  * Discutere e riflettere su idee di miglioramento.

  ### **Inizio (10 minuti) - Introduzione al Concetto di Tempo**
  1.  Dai il benvenuto agli studenti e presenta l'attività: **"Oggi impareremo a prototipare un segnale luminoso che si accende e si spegne."**
  2.  Per stimolare la discussione, inizia con una domanda: **"Sapete cosa fa illuminare lo schermo del vostro cellulare?"**
  3.  Dopo che avranno condiviso le loro idee, spiega che lo schermo è fatto di piccole luci chiamate LED. Poi, poni un esperimento mentale: **"Immaginate di scrivere un programma che dice a una lampada di accendersi e, nella riga successiva, di spegnersi. Cosa pensate che vedreste effettivamente?"** Lasciali discutere. La risposta è... niente! Questo è il momento perfetto per spiegare che i computer sono incredibilmente veloci e perché dobbiamo programmare delle pause, introducendo il concetto di "Temporizzazione".

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione del Segnale Luminoso**
  1.  Con la teoria della temporizzazione coperta, è tempo di metterla in pratica e costruire il segnale luminoso lampeggiante.
  2.  Guida i tuoi studenti attraverso **le istruzioni per collegare il dispositivo e programmare la sequenza di luci** dettagliate nella sezione pratica qui sotto. Incoraggiali a sperimentare con diversi tempi di ritardo per vedere come influisce sulla velocità del lampeggio.

  ### **Chiusura (5-10 minuti) - Riflessione e Applicazioni Future**
  1.  Eccellente! Una volta che tutti hanno un segnale luminoso funzionante, passa a una discussione finale per consolidare la loro comprensione e sfidarli a pensare in grande.
  2.  Inizia la riflessione ponendo la domanda chiave dell'attività: **"In quali altre situazioni potremmo usare la temporizzazione?"** Usa le seguenti domande per guidare una conversazione su come la temporizzazione viene utilizzata nella tecnologia di tutti i giorni.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Cos'è un LED?"
    type: "learn"
    icon: "book-reader"
    content: |
      Hai mai guardato da vicino lo schermo della tua TV o del tuo smartphone? È composto da milioni di piccole e potenti luci chiamate **LED**.
      I LED sono ovunque intorno a noi, da quelli grandi che illuminano una stanza a quelli piccoli che lavorano insieme per creare le immagini che vedi su uno schermo.
    media: "src/02-light-signals/a-examples1.svg"

  - title: "E lo schermo del cellulare?"
    type: "learn"
    content_class: "space-y-2 text-xl"
    content: |
      Lo schermo del tuo cellulare è pieno di migliaia di questi piccoli LED. Quando guardi un video o una foto, sono queste le luci che si accendono e si spengono per formare l'immagine.
      Quando prototipiamo con Protobject, sono proprio questi i LED che controlliamo con il nostro codice!
    media: "src/02-light-signals/b-led-smartphone.svg"

  - title: "Il Problema della Velocità"
    type: "learn"
    content: |
      Ecco un indovinello: immagina di dire al tuo prototipo di accendere una lampada **ON** e poi, nell'istruzione successiva, di spegnerla **OFF**. Ti aspetteresti di vedere un rapido flash, giusto? Ma in realtà non vedresti niente!
      Perché? **Le macchine sono incredibilmente veloci!** La lampada si accende, ma si spegne così rapidamente che i nostri occhi umani non riescono nemmeno a percepirlo.
    media: "src/02-light-signals/c-no-time.svg"
  
  - title: "Le Istruzioni Devono Essere Precise!"
    type: "learn"
    content: |
      I computer non possono indovinare cosa vogliamo. Se le nostre istruzioni sono ambigue, il programma non funzionerà come previsto.
      Nel nostro indovinello della luce lampeggiante, il pezzo mancante era dire al computer **quanto tempo aspettare** tra l'accensione e lo spegnimento della luce. Questa azione di fare una pausa per una durata specifica si chiama **Temporizzazione**.
    media: "src/02-light-signals/d-time.svg"

  - title: "Cosa significa 'temporizzazione'?"
    type: "learn"
    content: |
      Per far lampeggiare una luce come un segnale luminoso, dobbiamo creare una sequenza che includa **tempi di attesa**, o ritardi, tra i comandi ON e OFF.
      Nella programmazione, possiamo misurare il tempo in diverse unità. In Protobject, possiamo usare **secondi** o **millisecondi** (1000 millisecondi = 1 secondo) per controllare perfettamente la nostra temporizzazione.
    media: "src/02-light-signals/e-sequence.svg"

  - id: "create"
    title: "Crea un Segnale Luminoso"
    type: "create"
    icon: "cogs"
    heading_text: "Creeremo un prototipo di un segnale luminoso."

    steps:
      - "Premi <addbutton>Aggiungi dispositivo</addbutton> e seleziona il componente <comp>Lampada</comp>."
      - "Scansiona il codice <qr> con il tuo smartphone."
      - "Se non hai uno smartphone, puoi premere <openwindow>Apri in questa finestra</openwindow> per aprire la lampada sullo stesso computer."

  - title: "Dove si trovano i blocchi di ritardo?"
    type: "create"
    content_class: "text-center text-xl"
    content: |
      Per prima cosa, troviamo i blocchi che controllano il tempo. Apri la categoria <category>Temporizzazione</category>.
    media: "src/02-light-signals/f-delay-a.it.svg"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sul punto interrogativo per aprire i commenti che spiegano il codice.
      
      *Ricorda*: i blocchi di ritardo si trovano nella categoria <category>Temporizzazione</category>.
    media: "[600]https://app.protobject.com/generate?a02-timing&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai imparato a controllare un segnale luminoso. Ora, pensa in grande!"
    content: |
      * In quali altre situazioni del mondo reale potresti usare la temporizzazione e i ritardi? Pensa a giochi, animazioni o anche a strumenti che usi tutti i giorni.
    right_content:
      - text: |
          **Ricorda:** la programmazione consiste nel creare una sequenza chiara di passaggi per raggiungere un obiettivo.
          Aggiungendo ritardi, hai trasformato una semplice luce in un segnale luminoso funzionale!
---