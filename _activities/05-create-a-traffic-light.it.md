---
layout: activity
title: "Il Semaforo"
image: src/05-creating-a-traffic-light/05.semaforo.svg
video: src/videos/05_traffic_light.mp4
video_title: "Cosa faremo?"
description: "Dì addio al codice ripetitivo! Impara a usare i cicli infiniti per automatizzare la classica sequenza di un semaforo."
lang: it
permalink: /it/attivita/il-semaforo/
ref: activity_create_a_traffic_light

# ACTIVITY INFO
level: 1
computational_topics:
  - "Loop"
  - "Temporizzazione ed Eventi"
general_topics:
  - "Vita Quotidiana"

tags: [Cicli, Ciclo Principale, Ripeti per sempre, Automazione, Temporizzazione, Semaforo]

introduction: |
  Come si fa a far funzionare un programma da solo, per sempre? Se dovessi programmare un semaforo per un'intera giornata copiando e incollando comandi, il tuo programma sarebbe lungo milioni di righe! In questa missione, imparerai il segreto dei programmatori per l'automazione: il **ciclo** infinito. Preparati a costruire un semaforo intelligente e completamente automatizzato che non si ferma mai.
  

teacher: |
  ### **Corsi**
  * Classi dalla 3ª elementare alla 5ª superiore

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a internet

  ### **Obiettivi Educativi**
  * Comprendere il concetto di "ripeti per sempre" (Ciclo Principale).
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e l'ambiente circostante.
  * Valutare il proprio lavoro e quello degli altri, sia individualmente che in squadra.
  * Partecipare a dialoghi e riflessioni per proporre miglioramenti.

  ### **Inizio (10 minuti) - Il Problema della Ripetizione**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a prototipare un semaforo automatizzato."**
  2.  Inizia ripassando il concetto di sequenza. Chiedi alla classe: **"Sappiamo come accendere una luce per qualche secondo. Ma come creeremmo una sequenza, come una luce verde, poi una gialla e poi una rossa?"**
  3.  Dopo il loro brainstorming, presenta la sfida più grande: **"Ok, ma se avessimo bisogno che quel semaforo funzioni per un'ora intera, o tutto il giorno? Copiare e incollare quella sequenza centinaia di volte sarebbe impossibile!"** Questo imposta il problema perfetto per cui i cicli sono la soluzione.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione del Sistema Automatizzato**
  1.  Ora che gli studenti hanno compreso il potere dei cicli per l'automazione, è il momento di costruire il semaforo.
  2.  Guidali attraverso **le istruzioni per creare la sequenza di luci e inserirla all'interno del ciclo infinito**, come dettagliato nella sezione pratica qui sotto. Questo è il loro primo assaggio della creazione di un programma che funziona da solo.

  ### **Chiusura (5-10 minuti) - Dal Codice al Mondo Reale**
  1.  Una volta che il semaforo di tutti funziona ininterrottamente, è il momento di collegare la loro creazione digitale al mondo che li circonda.
  2.  Usa la sezione finale per avviare una discussione su come funzionano i semafori nelle nostre città e perché sono così importanti per la sicurezza e l'ordine. Questo li aiuta a vedere l'applicazione nel mondo reale dei concetti di programmazione che hanno appena imparato.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Cosa possiamo fare con una lampada a LED?"
    type: "learn"
    icon: "book-reader"
    content: |
      Se programmiamo una lampada a LED per passare dal verde, al giallo e poi al rosso in una sequenza temporizzata... abbiamo creato un semaforo!
      Per farlo, dobbiamo solo programmare la **temporizzazione** giusta e i **colori** giusti.
    media: "src/05-creating-a-traffic-light/a.trafficlight.svg"

  - title: "Il Problema: Il Codice si Ferma!"
    type: "learn"
    content: |
      Se programmi solo un ciclo — verde, giallo, rosso — il programma lo eseguirà una volta e poi si fermerà. Per farlo ripetere, potresti copiare e incollare i blocchi più e più volte.
      Ma se volessi che il semaforo funzionasse per un'ora? **Ti ritroveresti con un'enorme quantità di codice ripetuto!** È inefficiente e impossibile da gestire.
    media: "src/05-creating-a-traffic-light/a.trafficlight-seq.svg"

  - title: "La Soluzione: Il Ciclo 'Ripeti per Sempre'"
    type: "learn"
    content: |
      ### Come facciamo a farlo ripetere da solo? Usiamo un ciclo!

      Il blocco **"ripeti per sempre"** è uno strumento fondamentale nella programmazione. Questo concetto, noto anche come **Ciclo Principale**, dice al computer di ripetere tutto il codice al suo interno più e più volte, finché l'utente non ferma manualmente il programma.
      Inserendo la nostra sequenza del semaforo all'interno di questo ciclo, possiamo farlo funzionare all'infinito!
    media: "src/05-creating-a-traffic-light/a.trafficlight-seq2.it.svg"
  
  - title: "Mettiamoci al lavoro!"
    type: "learn"
    content: |
      Creeremo il nostro prototipo di semaforo inserendo il codice dei colori e della temporizzazione all'interno del ciclo **“ripeti per sempre”**. Programmeremo la luce in modo che sia verde per 6 secondi, gialla for 1 secondo e rossa per 6 secondi, creando un ciclo realistico.
    media: "src/a.working.svg"

  - id: "create"
    title: "Crea il nostro Semaforo!"
    type: "create"
    icon: "cogs"
    heading_text: "Costruiamo il nostro semaforo!"
    steps:
      - "Premi <addbutton>Aggiungi Dispositivo</addbutton> e seleziona <comp>Lampada</comp>."
      - "Scansiona il codice <qr>."
      - "Ricorda che se non hai uno smartphone, puoi premere <openwindow>Apri in questa finestra</openwindow> per aprire i componenti sullo stesso computer."
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.

      Il blocco "ripeti per sempre" si trova nella categoria <category>Base</category>.
    media: "[700]https://app.protobject.com/generate?a05-trafficlight&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai costruito un semaforo funzionante! Ora, pensiamo al mondo reale."
    content: |
      * Come funzionano i semafori veri? Sono tutti da soli o lavorano in squadra?
      * Quanti semafori sono solitamente necessari per controllare un singolo incrocio?
      * Qual è lo scopo più importante di un semaforo nelle nostre comunità?
---