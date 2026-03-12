---
layout: activity
title: "Costruisci il Tuo Cronometro"
image: src/07-stopwatch/stopwatch-cover.svg
video: src/videos/07_stopwatch.mp4
video_title: "Cosa faremo?"
description: "Padroneggia l'uso di variabili e loop per costruire un cronometro funzionale che conta i secondi sullo schermo."
lang: it
permalink: /it/attivita/costruisci-il-tuo-cronometro/
ref: activity_stopwatch

# ACTIVITY INFO
level: 1
computational_topics:
  - "Loop"
  - "Variabili e Dati"
  - "Temporizzazione ed Eventi"
general_topics:
  - "Matematica e Logica"

tags: [Variabili, Contatore, Loop, Loop Principale, Temporizzazione, Cronometro]

introduction: |
  Ti sei mai chiesto come un gioco tiene il punteggio o un orologio conta i secondi? Si tratta di ricordare e aggiornare un numero. In questa missione, sbloccherai quel segreto combinando **loop** e **variabili** per costruire un cronometro perfettamente funzionante. Preparati a imparare come far contare, ricordare e visualizzare informazioni che cambiano nel tempo al tuo programma.

teacher: |
  ### **Corsi**
  * Classi dalla 3 alla 12
  
  ### **Materiali**
  * Telefono cellulare, tablet o computer
  * Connessione a Internet
  
  ### **Descrizione**
  In questa attività, gli studenti combineranno loop e variabili per creare un'applicazione pratica: un cronometro. Impareranno come inizializzare, incrementare e visualizzare il valore di una variabile nel tempo, rafforzando questi concetti fondamentali dell'informatica.
  
  ### **Obiettivi Educativi**
  * Comprendere il concetto di una variabile come contatore.
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e l'ambiente.
  * Valutare il proprio lavoro e quello degli altri.
  * Partecipare a discussioni e riflessioni per proporre miglioramenti.
  
  ### **Inizio (10 minuti) - La Sfida del Conteggio**
  1.  Dai il benvenuto alla classe e presenta l'attività: **"Oggi impareremo a costruire un cronometro che conta i secondi da zero."**
  2.  Stimola la curiosità con una domanda: **"Come pensate che un computer 'ricordi' a che numero è arrivato mentre conta?"**
  3.  Dopo una breve discussione, spiega che i computer, proprio come noi, possono 'dimenticare' se non hanno un posto dove conservare le informazioni. Questa è l'occasione perfetta per introdurre il concetto di variabile come 'scatola di memoria' per il nostro programma. Esploriamo come funziona.

  {{learn}}
  
  ### **Sviluppo (20-30 minuti) - Costruzione del Contatore**
  1.  Ora che la teoria è solida, è tempo di costruire il cronometro e vedere questi concetti in azione. Questo progetto è un fantastico esempio di come loop e variabili lavorano insieme.
  2.  Guida gli studenti attraverso **le istruzioni per impostare la variabile e creare il loop di conteggio**, come dettagliato nella sezione pratica qui sotto.
  3.  **Nota per l'insegnante:** Sperimenta con l'attività prima della lezione per anticipare le domande.

  ### **Chiusura (5-10 minuti) - Riflessione e Aggiornamenti**
  1.  Una volta che tutti hanno un cronometro funzionante, è tempo di riflettere sul potente strumento che hanno appena usato e pensare a come rendere il loro progetto ancora migliore.
  2.  Usa la sezione finale per guidare una discussione su altri usi delle variabili e per introdurre una nuova e stimolante funzionalità per il loro cronometro: l'aggiunta dei minuti!
  
  {{reflect}}
  
  #### **Informazioni aggiuntive per l'insegnante**
  La soluzione alla sfida proposta nella sezione di riflessione è disponibile a [questo link](https://app.protobject.com/generate?cronometro-desafio). Usala come riferimento per guidare gli studenti che potrebbero avere difficoltà.

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Come funziona un cronometro?"
    type: "learn"
    icon: "book-reader"
    content: |
      Un cronometro ha un compito semplice: contare i secondi che passano. Ogni secondo, essenzialmente dice: "**Ehi, è passato un altro secondo. Aggiungerò 1 al numero totale di secondi che ho già contato.**"
      Quindi, se il cronometro è a 9 secondi, dopo un altro secondo, calcola 9 + 1 = 10 secondi. Questo processo si ripete più e più volte... **È un lavoro perfetto per un loop!**
    media: "src/07-stopwatch/a-count.svg"
  
  - title: "E se perdiamo il conto?"
    type: "learn"
    content: |
      Ti è mai capitato di contare qualcosa e dimenticare l'ultimo numero a cui eri arrivato? Devi ricominciare tutto da capo! **Un computer può avere lo stesso problema.**
      Per evitarlo, probabilmente scriveresti il numero. Poi, per continuare a contare, guarderesti il numero, aggiungeresti 1 e scriveresti il nuovo totale. Stai memorizzando un valore che cambia nel tempo!
    media: "src/07-stopwatch/a-count-lost.svg"

  - title: "Come fa il computer a 'scriverlo'?"
    type: "learn"
    content: |
      Per risolvere questo problema di memoria, usiamo uno strumento di programmazione fondamentale: una **Variabile**.
      Pensa a una variabile come a una piccola scatola nella memoria del computer dove puoi conservare qualcosa. Per mantenere le cose organizzate e ricordare cosa c'è dentro, dai un nome alla scatola.
      Usando una variabile, possiamo far sì che il nostro computer tenga il conto senza mai dimenticare a che numero è arrivato.
    media: "src/07-stopwatch/a-num-var.it.svg"

  - title: "Come la usiamo?"
    type: "learn"
    content: |
      Per prima cosa, dobbiamo creare la nostra variabile e darle un nome in modo da sapere a cosa serve. In questo caso, chiamiamola "**tempo**".
      Successivamente, dobbiamo darle un valore iniziale. Poiché un cronometro inizia a contare da 0, all'inizio del nostro programma, imposteremo la variabile "**tempo**" uguale a 0.
    media: "src/07-stopwatch/a-num-var-time.it.svg"

  - title: "Le variabili... Variano!"
    type: "learn"
    content: |
      Come suggerisce il nome, il valore all'interno di una variabile può cambiare, o "variare". Possiamo estrarre il valore, cambiarlo e poi salvare il nuovo valore nella stessa variabile.
      Per il nostro cronometro, ogni volta che il nostro loop principale viene eseguito, diremo al programma di aggiungere 1 al valore della variabile "**tempo**". **E così, stiamo contando!**
    media: "src/07-stopwatch/a-var-change.it.svg"

  - title: "Mettiamoci al lavoro!"
    type: "learn"
    content: |
      Per costruire il nostro cronometro, inizieremo creando una variabile chiamata "tempo" e impostando il suo valore iniziale a 0. Quindi, creeremo un loop che si ripete più e più volte. All'interno del loop, aumenteremo il valore della nostra variabile "tempo" di 1 e poi aspetteremo un secondo.
    media: "src/a.working.svg"

  - id: "create"
    title: "Crea"
    type: "create"
    icon: "cogs"
    heading_text: "Ora costruiremo il nostro cronometro."
    ready_message: "Ora siamo pronti per scrivere il codice."
    steps:
      - "Premi <addbutton>Aggiungi dispositivo</addbutton> e seleziona il componente <comp>ScriviDisegna</comp>. Chiamiamolo **Cronometro** in modo da poter scrivere i numeri sullo schermo."
      - "Scansiona il codice <qr>."
      - "Ricorda che se non hai uno smartphone per scansionare i codici **QR**, puoi premere <openwindow>Apri in questa finestra</openwindow> per aprire i componenti sullo stesso computer."

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sul simbolo del punto interrogativo per aprire i commenti che spiegano il codice.
      Le variabili sono gestite nella categoria <category>Variabili</category>.
    media: "https://app.protobject.com/generate?a07-stopwatch&it&dynamic&-1"


  - id: "reflect"
    title: "Cos'altro possiamo inventare?"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Rispondiamo alle seguenti domande:"
    content: |
      * Oltre ai numeri, quali altri tipi di informazioni potremmo memorizzare in una variabile?
      * Quali altri prototipi potresti costruire ora che sai come creare un contatore?
      * Come potremmo far contare al nostro cronometro anche i minuti oltre ai secondi?
    right_content:
      - text: |
          **Sfida**: Aggiorniamo il nostro cronometro per includere i minuti!
      - text: |
          **Suggerimento**: Quanti secondi ci sono in un minuto? Potresti aver bisogno di una seconda variabile per tenere traccia dei minuti. Un loop *all'interno* del tuo loop principale potrebbe aiutarti a contare i secondi fino a 60 prima di aggiungere uno al tuo contatore dei minuti?
---