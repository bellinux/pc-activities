---
layout: activity
title: "La Cassaforte a Due Chiavi"
image: src/21-safe-box-with-alarm/21.caja-seguridad.svg
video: src/videos/21_safe_box.mp4
video_title: "Cosa faremo?"
description: "Esplora i concetti di cybersecurity e gli operatori logici ('AND') per costruire un allarme ad alta sicurezza che richiede la pressione simultanea di due pulsanti."
lang: it
permalink: /it/attivita/la-cassaforte-a-due-chiavi/
ref: activity_safe_box_with_alarm

# ACTIVITY INFO
level: 2
computational_topics:
  - "Condizionali e Logica"
  - "Sensori e Input"
general_topics:
  - "Vita Quotidiana"

tags: [Operatori Logici (AND), Condizionali Annidati, Cybersecurity, Autenticazione a Due Fattori, Multi-dispositivo, Sensore di Inclinazione]

introduction: |
  Come fanno le banche e i tuoi giochi preferiti a proteggere il tuo account dagli hacker? Spesso, usano più di una semplice password. In questa missione, ti tufferai nel mondo della **cybersecurity** e degli operatori logici. Imparerai come funziona l'**operatore 'AND'** costruendo una cassaforte ad alta sicurezza che si disattiva solo se due chiavi diverse (pulsanti) vengono premute esattamente nello stesso momento — proprio come un vero sistema di autenticazione a due fattori!

teacher: |
  ### **Corsi**
  * Classi 6-12

  ### **Materiali**
  * 3 cellulari, tablet o computer
  * Connessione a Internet
  * Una scatola (come una scatola da scarpe o una scatola della pizza) che funga da cassaforte fisica
  * Un oggetto che sia il "tesoro" all'interno

  ### **Obiettivi Educativi**
  * Comprendere il concetto dell'operatore logico AND e dei condizionali annidati.
  * Creare un oggetto tecnologico (prototipo) utilizzando più dispositivi.
  * Identificare le relazioni tra tecnologia, sicurezza e il mondo circostante.
  * Valutare il proprio lavoro e quello dei pari.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - La Serratura e la Chiave Digitale**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi creeremo una cassaforte ad alta sicurezza con uno speciale allarme a due chiavi."**
  2.  Inizia la lezione con una domanda di grande interesse: **"Avete mai sentito parlare di Cybersecurity? Cosa pensate che sia?"**
  3.  Usa questa discussione per introdurre concetti come la protezione dei dati e le password complesse. Poi, introduci l'**Autenticazione a Due Fattori (2FA)** come un ulteriore livello di sicurezza. Spiega che la nostra cassaforte userà questo stesso principio, richiedendo l'uso contemporaneo di due 'chiavi'. Questo è il momento perfetto per introdurre l'operatore logico **AND**.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione della Cassaforte ad Alta Sicurezza**
  1.  Ora che gli studenti comprendono la logica dell'operatore 'AND' e la sua connessione con la cybersecurity, è tempo di costruire la cassaforte.
  2.  Guidali attraverso **le istruzioni per configurare i tre dispositivi e programmare la logica di sicurezza**, come dettagliato nella sezione pratica qui sotto. Questa è un'ottima opportunità per il lavoro di squadra, con studenti diversi che gestiscono la cassaforte e ciascuna delle due "chiavi".

  ### **Chiusura (5-10 minuti) - Pensare come un Esperto di Sicurezza**
  1.  Una volta che le casseforti sono costruite e testate, è tempo di riflettere sull'importanza reale dei concetti che hanno appena usato.
  2.  Usa la sezione finale per guidare una discussione sulla cybersecurity come campo e per incoraggiarli a pensare ad altri modi per proteggere le informazioni digitali.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Cos'è la Cybersecurity?"
    type: "learn"
    icon: "book-reader"
    content: |
      La cybersecurity è come uno scudo digitale. È la pratica di proteggere computer, telefoni e dati importanti da persone malintenzionate online che vogliono rubarli o danneggiarli. Proprio come potresti avere una serratura sul tuo diario o sulla tua stanza, anche i tuoi account online hanno bisogno di protezione.
    media: "src/21-safe-box-with-alarm/a-cybersecurity.svg"

  - title: "White Hat vs. Black Hat"
    type: "learn"
    content: |
      Su Internet, ci sono i "Black Hat" — hacker malintenzionati che usano virus informatici e trucchi per rubare informazioni. Ma ci sono anche i "White Hat" — esperti di cybersecurity che lavorano per costruire difese e proteggere dati e sistemi da questi attacchi. Sono i supereroi digitali.
    media: 
      - "src/21-safe-box-with-alarm/b-hackers.svg"
      - "src/21-safe-box-with-alarm/b-securityexpert.svg"

  - title: "La Tua Prima Linea di Difesa: le Password"
    type: "learn"
    content: |
      Uno dei modi migliori per proteggersi è usare password complesse e uniche. Una password complessa è una che nessuno può indovinare facilmente. Se la tua password è troppo semplice, come "123456" o "password", qualcuno potrebbe facilmente entrare nella tua "cassaforte digitale" senza il tuo permesso.
    media: "src/21-safe-box-with-alarm/c-strongpassword.svg"

  - title: "E se la tua password viene rubata?"
    type: "learn"
    content: |
      Anche con una password complessa, hai bisogno di un piano di riserva. È qui che entra in gioco l'**Autenticazione a Due Fattori (2FA)**. È come aver bisogno di una seconda chiave segreta. Ad esempio, dopo aver inserito la password, un sito potrebbe inviarti un codice speciale sul telefono che devi inserire anche tu. Senza quel secondo codice, nessuno può entrare, anche se conosce la tua password.
    media: "src/21-safe-box-with-alarm/d-two-factor.svg"
  
  - title: "La Nostra Cassaforte a Due Fattori!"
    type: "learn"
    content: |
      La cassaforte che stiamo costruendo oggi usa lo stesso principio della 2FA. Per spegnere l'allarme, hai bisogno di due chiavi (i nostri due pulsanti) premute contemporaneamente. Se un ladro ruba il pulsante di Martin, non può comunque disattivare l'allarme senza avere anche il pulsante di Juan. Questo rende il tesoro molto più sicuro!
    media: "src/21-safe-box-with-alarm/e-onebutton.svg"

  - title: "Booleani e l'Operatore AND"
    type: "learn"
    content: |
      Ricorda che i **Booleani** sono un tipo di dati semplice con solo due valori possibili: **VERO** o **FALSO**. Quando un pulsante viene premuto, il suo stato potrebbe essere VERO. Quando non è premuto, il suo stato è FALSO.
      L'operatore logico **AND** è come un buttafuori severo che ha bisogno di vedere due documenti d'identità. Restituisce **VERO** solo se *tutte* le condizioni che controlla sono vere. Se anche una sola è falsa, l'intero risultato è falso.
    media: "src/21-safe-box-with-alarm/f-boolean.it.svg"

  - title: "Come AND Protegge la Nostra Scatola"
    type: "learn"
    content: |
      Ecco come funziona la logica per la nostra cassaforte:
      * Se il Pulsante 1 è premuto (VERO) **E** il Pulsante 2 è premuto (VERO) --> Il risultato è **VERO** e l'allarme è spento.
      * Se il Pulsante 1 è premuto (VERO) **E** il Pulsante 2 NON è premuto (FALSO) --> Il risultato è **FALSO** e l'allarme è attivo.
      * Se nessuno dei due è premuto, il risultato è anche **FALSO**. Entrambe le chiavi sono richieste contemporaneamente!
    media: 
      - "src/21-safe-box-with-alarm/l-box-false-false.it.svg"
      - "src/21-safe-box-with-alarm/m-box-true-false.it.svg"
      - "src/21-safe-box-with-alarm/n-box-true-true.it.svg"

  - id: "create"
    title: "Crea la Cassaforte"
    type: "create"
    icon: "cogs"
    heading_text: "Per questa attività, abbiamo bisogno di 3 dispositivi."
    steps:
      - "Sul primo dispositivo (la cassaforte stessa), aggiungi <comp>ScriviDisegna</comp>, <comp>Inclinazione</comp> e <comp>RiproduttoreSuoni</comp>."
      - "Sul secondo dispositivo, aggiungi un <comp>BottoneTouch</comp> (questa è la chiave di Martin)."
      - "Sul terzo dispositivo, aggiungi un altro <comp>BottoneTouch</comp> (questa è la chiave di Juan)."
    right_content:
      - text: |
          **Suggerimento**: Puoi aggiungere più componenti allo stesso smartphone premendo di nuovo il pulsante *SCAN* dopo aver aggiunto il primo.
      - media: "src/general-scan-button.svg"
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
    media: "[700]https://app.protobject.com/generate?a21-alarmbuttons&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai appena usato un principio fondamentale della cybersecurity!"
    content: |
      * Hai trovato interessante questo argomento? La cybersecurity è uno dei campi in più rapida crescita e più importanti della tecnologia. È qualcosa che potresti vederti fare in futuro?
      * Quali altri metodi conosci per proteggere i tuoi account e dati online?
    right_content:
      - text: |
          Ricorda sempre l'importanza della **cybersecurity** nel nostro mondo digitale!
---