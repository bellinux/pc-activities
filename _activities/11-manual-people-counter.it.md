---
layout: activity
title: "Crea un Contapersone"
image: src/11-manual-people-counter/11.contador-personas.svg
video: src/videos/11_people_counter.mp4
video_title: "Cosa faremo?"
description: "Usa eventi e variabili per costruire uno strumento pratico per contare le persone, proprio come a un vero concerto o in un negozio."
lang: it
permalink: /it/attivita/crea-un-contapersone/
ref: activity_manual_people_counter

# ACTIVITY INFO
level: 1
computational_topics:
  - "Temporizzazione ed Eventi"
  - "Variabili e Dati"
  - "Condizionali e Logica"
general_topics:
  - "Matematica e Logica"

tags: [Eventi, Variabili, Contatore, Input Utente, Dati]

introduction: |
  Sei mai stato a un grande evento o in un negozio affollato e hai visto qualcuno alla porta con un contatore, che conta tutti quelli che entrano? Costruiamone una versione digitale! In questa missione, combinerai due dei concetti più potenti della programmazione — **eventi** e **variabili** — per creare un pratico contapersone. Preparati a costruire uno strumento reale che ascolta l'input e tiene traccia dei dati.

teacher: |
  ### **Corsi**
  * Classi 3-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere i concetti di "evento" e "dati numerici".
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo che li circonda.
  * Valutare il proprio lavoro e quello degli altri.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - La Logica di un Contatore**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a prototipare un contapersone digitale."**
  2.  Chiedi alla classe: **"Cos'è un dispositivo di conteggio e dove ne avete visto uno in uso?"** (es. negozi, concerti, trasporti).
  3.  Dopo aver discusso i suoi usi nel mondo reale, spiega la logica che c'è dietro. Abbiamo bisogno di un posto dove 'memorizzare' il conteggio attuale e di un modo per 'sapere' quando aggiungere un'altra persona. Questo è lo scenario perfetto per mostrare come le **variabili** (per memorizzare i dati) e gli **eventi** (per attivare le azioni) lavorano insieme per creare uno strumento utile.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione del Dispositivo**
  1.  Ora che gli studenti comprendono la logica di usare una variabile come contatore e un evento come attivatore, è tempo di costruire il dispositivo.
  2.  Guidali attraverso **le istruzioni per creare l'interfaccia utente e programmare la logica di conteggio**, come dettagliato nella sezione pratica qui sotto. Questo progetto è una fantastica applicazione reale dei concetti che hanno imparato.

  ### **Chiusura (5-10 minuti) - Riflessione e Aggiornamenti**
  1.  Una volta che tutti hanno un contatore funzionante, è tempo di un esercizio di pensiero critico. Un evento è l'*unico* modo per costruirlo? E come possiamo renderlo ancora più utile?
  2.  Usa le sezioni finali per guidare una discussione che confronta l'efficienza degli eventi rispetto ai loop, e poi sfidali ad aggiornare il loro contatore con una nuova importante funzionalità: la sottrazione.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Cos'è un dispositivo di conteggio?"
    type: "learn"
    icon: "book-reader"
    content: |
      Un dispositivo di conteggio, o "clicker", è uno strumento semplice usato per **tenere traccia di una quantità**. Potrebbe essere usato per contare prodotti in un magazzino, giri in una gara o, nel nostro caso, persone che entrano in un locale.
      Ogni volta che qualcuno entra, si **preme un pulsante** e il **contatore sul display aumenta di uno**. È un modo semplice ed efficace per tenere un conteggio accurato.
    media: "src/11-manual-people-counter/a.lcd-counter.svg"

  - title: "Qual è lo scopo di un contapersone?"
    type: "learn"
    content: |
      I contapersone sono sorprendentemente utili in molte situazioni. I negozi li usano per monitorare il flusso di clienti, gli organizzatori di eventi li usano per controllare la capienza dei locali per motivi di sicurezza e i trasporti pubblici possono usare i dati per migliorare il servizio. È uno strumento semplice che aiuta a rendere i sistemi più sicuri ed efficienti.
    media:
      - "src/11-manual-people-counter/b.shop_.example.svg"
      - "src/11-manual-people-counter/b.event_.example.svg"
      - "src/11-manual-people-counter/b.bus_.example.svg"

  - title: "Usiamo una variabile per tenere traccia"
    type: "learn"
    content: |
      Ricordi le **variabili**? Sono come scatole etichettate per conservare informazioni. Per il nostro contapersone, una variabile è lo strumento perfetto per fungere da tabellone digitale. Creeremo una variabile per memorizzare il conteggio attuale e potremo aggiornare il valore al suo interno ogni volta che entra una nuova persona.
    media: "src/11-manual-people-counter/c.variable-use.it.svg"

  - title: "E come sappiamo quando contare?"
    type: "learn"
    content: |
      Come sappiamo *quando* aggiornare la nostra variabile? Usiamo un **evento**!
      Invece di chiedere costantemente "Il pulsante è premuto?", il programma si limita ad ascoltare. Quando premi il pulsante, invia un segnale — un evento — al nostro codice. Quell'evento è l'attivatore che dice al nostro programma: 'Ok, è ora di aggiungere 1 alla variabile contatore!' È un modo efficiente e intelligente di programmare.
    media: "src/11-manual-people-counter/evento-icon.es.it.svg"

  - id: "create"
    title: "Costruiamo il contatore"
    type: "create"
    icon: "cogs"
    heading_text: "Creeremo un prototipo che ci permette di contare le persone che entrano in un luogo."
    content: |
      Per prima cosa, dobbiamo aggiungere due componenti: uno per (1) visualizzare il numero di persone e un secondo per (2) fungere da pulsante "aggiungi".
    steps:
      - "Premi <addbutton>Aggiungi dispositivo</addbutton> e seleziona <comp>ScriviDisegna</comp>, il dispositivo dove visualizzeremo il numero."
      - "Premi di nuovo <addbutton>Aggiungi dispositivo</addbutton> e seleziona <comp>BottoneTouch</comp> per creare il pulsante."
      - "Ricorda che se non hai uno smartphone, puoi premere <openwindow>Apri in questa finestra</openwindow>."
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
    media: "[700]https://app.protobject.com/generate?a11-peoplecounter&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "E se usassimo un loop principale invece di un evento?"
    content: |
      Hai costruito questo contatore usando un evento, che è super efficiente. Ma potresti costruirlo con un loop principale? Dai un'occhiata al codice qui sotto. Qual è la differenza principale? Cosa pensi che succederebbe se tenessi premuto il pulsante nella versione con il loop rispetto alla versione con l'evento?
    media: "[450]https://app.protobject.com/generate?contarpersonaswhile&it&dynamic&-1"

  - title: "Sfida"
    icon: "trophy"
    type: "reflect"
    heading_text: "Il tuo contatore può solo aumentare. Ma cosa succede se le persone escono?"
    content: |
      Un vero contatore ha bisogno di un modo per sottrarre! La tua sfida è aggiungere un secondo pulsante al tuo prototipo che **diminuisce** il conteggio di uno ogni volta che viene premuto.
    media: "src/videos/counter_challenge.mp4"
    right_content:
      - text: |
          **Suggerimento:** Avrai bisogno di aggiungere un secondo componente <comp>BottoneTouch</comp>. Come programmeresti un *secondo* evento per gestire la sottrazione?
---