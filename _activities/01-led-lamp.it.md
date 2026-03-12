---
layout: activity
title: "Accendi un LED"
image: src/01-led-lamp/01.lampara-led.svg
video: src/videos/01_led_lamp.mp4
video_title: "Cosa faremo?"
description: "Fai il tuo primo passo nel mondo della programmazione imparando la magia della programmazione a blocchi."
lang: it
permalink: /it/attivita/accendi-un-led/
ref: activity_led_lamp

# ACTIVITY INFO
level: 1
computational_topics:
  - "Fondamenti di Programmazione"
general_topics:
  - "Scienza e Tecnologia"

tags: [Programmazione a Blocchi, Prima Attività, Lampada LED, Comandi di Base]

introduction: |
  Ti sei mai chiesto come funzionano i tuoi giochi o le tue app preferite? Tutto inizia con una singola istruzione. Preparati a inviare il tuo primo comando e a dare vita a una lampada LED virtuale. In questa missione, scoprirai la magia della **programmazione** imparando a dire a un dispositivo esattamente cosa fare, usando semplici **blocchi** visivi.
  
teacher: |
  ### **Corsi**
  * Classi 3-12
  
  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet
  
  ### **Descrizione**
  In questa attività, gli studenti possono sperimentare in modo introduttivo con Protobject, imparando la programmazione visiva e l'informatica in modo sicuro e giocoso utilizzando un dispositivo.
  
  ### **Obiettivi Educativi**
  * Comprendere i concetti di "programmazione a blocchi" e "prototipo".
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello degli altri, sia individualmente che in team.
  * Partecipare a dialoghi e riflessioni per proporre miglioramenti.
  
  ### **Inizio (10 minuti) - Scintilla l'Idea**
  1.  Dai il benvenuto alla classe e presenta l'attività: **"Oggi impareremo a prototipare con Protobject e accenderemo la nostra prima lampada LED."**
  2.  Stimola la loro curiosità con una domanda: **"Sapete cos'è la programmazione?"**
  3.  Dopo una breve discussione per raccogliere le loro idee, è il momento perfetto per introdurre i concetti fondamentali. Spiega che la programmazione è semplicemente un modo per dare istruzioni super specifiche a un computer e che useremo blocchi visivi divertenti invece di testo complicato. Esploriamo queste idee insieme.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione del Prototipo**
  1.  Ora che i concetti chiave sono chiari, è tempo di mettersi all'opera e dare vita a quella lampada! Prepara gli studenti per la fase pratica.
  2.  Assicurati che ogni studente abbia un dispositivo pronto e guidali attraverso **il processo passo-passo per creare il loro primo prototipo**, come descritto di seguito.
  3.  **Nota per l'insegnante:** Sperimenta con l'attività prima della lezione per anticipare eventuali domande.

  ### **Chiusura (5-10 minuti) - Riflessione e Sfida Finale**
  1.  Ottimo lavoro! Una volta che gli studenti hanno acceso con successo le loro lampade, è tempo di stimolare ulteriormente la loro curiosità e riflettere su quanto appena accaduto.
  2.  Inizia la discussione con una semplice domanda: **"Ottimo lavoro! L'avete accesa, ma come la spegnereste?"** Lasciali sperimentare con il blocco **SPEGNI**. Questo è un ottimo momento per spiegare perché non sembra funzionare (a causa della velocità di esecuzione del computer) e per preparare il terreno per la prossima avventura con la temporizzazione. Usa le seguenti domande per guidare la conversazione.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Cos'è la Programmazione?"
    type: "learn"
    icon: "book-reader"
    content: |
      La programmazione consiste nel dare a un computer una serie di istruzioni specifiche per completare un'attività. In questo modo, il computer sa esattamente cosa fare seguendo i passaggi che hai stabilito.
      I programmatori usano un linguaggio speciale che i computer possono capire. Lo chiamiamo **linguaggio di programmazione**, e può essere basato su testo o su blocchi.
    media: "src/01-led-lamp/a-programming.svg"

  - title: "Testo vs. Blocchi: Due Modi per Programmare"
    type: "learn"
    content: 
      - |
        La **programmazione testuale** è come scrivere una ricetta da zero, usando linguaggi come Python, Java o C++. Può essere difficile per i principianti.
      - |
        La **programmazione a blocchi**, d'altra parte, è come costruire con i mattoncini LEGO®. Ogni blocco è un pezzo di codice pre-fatto che puoi semplicemente trascinare e incastrare con altri, senza bisogno di digitare.
        Questo è esattamente il tipo di programmazione che usiamo in Protobject!
    media: ["src/01-led-lamp/b-text-programming.svg","src/01-led-lamp/c-block-programming.svg"]

  - title: "Benvenuto in Protobject!"
    type: "learn"
    content: |
      Protobject ti permette di programmare il tuo smartphone e farlo interagire con il mondo che ti circonda.
      Come? È semplice! Colleghi un dispositivo, costruisci il tuo codice trascinando i blocchi nell'area di lavoro e poi attivi il tuo prototipo!
    media: "src/01-led-lamp/d-introb-protobject.it.svg"

  - title: "Attiva il Tuo Prototipo"
    type: "learn"
    content: |
      Quando i tuoi blocchi di codice sono pronti, puoi dare vita al tuo prototipo premendo il **pulsante rosso**.
      Siamo pronti per iniziare a sperimentare! Segui le istruzioni qui sotto e crea la tua prima invenzione.
    media: "src/01-led-lamp/e-intro2b-protobject.it.svg"

  - id: "create"
    title: "Crea"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo una lampada sul nostro smartphone e accendiamola con Protobject."
    ready_message: "Ora siamo pronti per scrivere il codice."
    steps:
      - "Premi <addbutton>Aggiungi dispositivo</addbutton> e seleziona il componente <comp>Lampada</comp>."
      - "Scansiona il codice <qr> con il tuo smartphone."
      - "Ricorda che se non hai uno smartphone per scansionare i codici **QR**, puoi premere <openwindow>Apri in questa finestra</openwindow> per aprire i componenti sullo stesso computer."

  - title: "Trascina il blocco ACCENDI"
    type: "create"
    content: |
      Fantastico! Accendiamo la nostra lampada LED!
      
      Ogni blocco rappresenta un'**azione**. Inizieremo usando solo un blocco che ci permetterà di **accendere la nostra lampada LED**.
      
      Per farlo, **trascina il blocco ACCENDI** nell'area di lavoro.
    content_class: "space-y-2"
    media: "src/01-led-lamp/f-intro3b-protobject.it.svg"

  - title: "Ora attiva il prototipo!"
    type: "create"
    content: |
      La tua **lampada LED** dovrebbe **accendersi**!
    content_class: "text-center text-xl"
    media: "src/01-led-lamp/g-intro4c-protobject.it.svg"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    content: 
      - |
        Hai imparato ad accendere la lampada. Qual è il prossimo passo logico? Come la spegneresti?
      - |
        Hai provato ad aggiungere il blocco **SPEGNI** subito dopo il primo?
      
    media: ["src/01-led-lamp/h-light-on-to-off.svg", "https://app.protobject.com/generate?encenderApagar&it&static&-1"]
    right_content:
      - text: |
          **Pensa**: Hai considerato la **velocità** con cui un computer segue le istruzioni? È così incredibilmente veloce che la lampada si accende e si spegne prima che i tuoi occhi possano notarlo! Per controllare cose come questa, dovremo imparare a gestire il tempo.

    
---