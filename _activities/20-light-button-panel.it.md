---
layout: activity
title: "Codice Intelligente: Usare le Funzioni"
image: src/20-light-button-panel/20.botonera-luces.svg
video: src/videos/20_light_button_panel.mp4
video_title: "Cosa faremo?"
description: "Impara a scrivere codice più pulito e riutilizzabile creando funzioni con parametri per un gioco di luci a due pulsanti."
lang: it
permalink: /it/attivita/codice-intelligente-usare-le-funzioni/
ref: activity_light_button_panel

# ACTIVITY INFO
level: 2
computational_topics:
  - "Funzioni"
  - "Temporizzazione ed Eventi"
general_topics:
  - "Matematica e Logica"

tags: [Funzioni, Parametri, Codice Riutilizzabile, Eventi, Input Utente]

introduction: |
  Stanco di copiare e incollare gli stessi blocchi più e più volte? Man mano che i tuoi programmi diventano più complessi, hai bisogno di un modo per rimanere organizzato ed efficiente. Il segreto definitivo dei programmatori professionisti per questo è la **Funzione**! In questa missione, imparerai a raggruppare il tuo codice in blocchi intelligenti e riutilizzabili che possono essere chiamati in qualsiasi momento. Preparati a costruire una singola funzione di schema luminoso che può essere attivata da pulsanti diversi per creare risultati diversi.

teacher: |
  ### **Corsi**
  * Classi 6-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere il concetto di funzioni e parametri.
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello degli altri.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - Il Problema della Ripetizione**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a scrivere codice più intelligente ed efficiente usando le funzioni."**
  2.  Inizia la lezione chiedendo: **"Immaginate di scrivere un programma e di dover usare gli stessi 10 blocchi di codice in cinque punti diversi. Qual è il problema di copiarli e incollarli semplicemente?"** (Guidali a problemi di dimensioni, disordine e difficoltà nel fare modifiche: dovresti correggere un bug in 5 punti!).
  3.  Spiega che i programmatori hanno una soluzione potente per questo: le **Funzioni**. Usa l'analogia di una ricetta: invece di scrivere i passaggi ogni volta, fai semplicemente riferimento al nome della ricetta. Questo è il punto di partenza perfetto per spiegare come le funzioni ci aiutano a scrivere codice riutilizzabile.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione di una Funzione Riutilizzabile**
  1.  Ora che gli studenti comprendono il potere di creare blocchi di codice riutilizzabili, è tempo di costruire la loro prima funzione.
  2.  Guidali attraverso **le istruzioni per creare la loro funzione `sequenza_luci` e poi chiamarla da due diversi eventi di pulsanti**, come dettagliato nella sezione pratica qui sotto. Questa è la loro prima volta a definire un blocco personalizzato e poi usarlo nel loro programma, che è un passo importante.

  ### **Chiusura (5-10 minuti) - Il Potere dei Parametri**
  1.  Una volta che tutti hanno il loro pannello luminoso a due pulsanti funzionante da una singola funzione, è tempo di riflettere sulla potenza e l'eleganza di questo nuovo strumento.
  2.  Usa la sezione finale per incoraggiare la sperimentazione con i parametri della funzione e per sfidarli a costruire una seconda funzione diversa per un altro compito.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Cosa sono le funzioni?"
    type: "learn"
    icon: "book-reader"
    content: |
      Le funzioni sono gruppi di codice riutilizzabili che puoi nominare e poi "chiamare" ogni volta che ne hai bisogno.
      Immagina di avere una ricetta preferita con cinque passaggi per preparare la cena. Invece di scrivere quei cinque passaggi ogni singola volta, puoi creare una singola "scheda ricetta" chiamata "CENA". Ora, devi solo chiamare quella singola funzione e il programma esegue tutti e cinque i passaggi. Questa è una funzione **senza parametri** perché fa la stessa identica cosa ogni volta.
    media: "src/20-light-button-panel/a-dinner.svg"

  - title: "Funzioni con Parametri"
    type: "learn"
    content: |
      Ma se volessi preparare la stessa ricetta con ingredienti principali diversi? Possiamo rendere la nostra funzione più intelligente dandole dei **parametri** — input che possono cambiare il risultato.
      Pensa di nuovo alla funzione CENA. Possiamo aggiungere un parametro per l'ingrediente principale. Ora, chiamare `CENA(tagliatelle)` darà un risultato diverso da `CENA(riso)`. I passaggi sono gli stessi, ma l'input cambia il risultato.
      Nella nostra attività, creeremo una funzione `sequenza_luci` con un parametro **colore**. La funzione eseguirà sempre lo stesso schema lampeggiante, ma il colore della luce cambierà in base al parametro che forniamo quando la chiamiamo.
    media: "src/20-light-button-panel/b-green-red.svg"

  - id: "create"
    title: "Crea il Pannello Luminoso"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo il prototipo. Avremo bisogno di 3 dispositivi (o aprirli nella stessa finestra)."
    steps:
      - "Sul primo dispositivo, aggiungi il componente <comp>Lampada</comp>."
      - "Sul secondo dispositivo, aggiungi il primo <comp>BottoneTouch</comp>."
      - "Sul terzo dispositivo, aggiungi il secondo <comp>BottoneTouch</comp>. Ricorda, puoi usare <openwindow>Apri in questa finestra</openwindow> per aprire i componenti sul tuo computer."
    right_content:
      - text: |
          **Suggerimento**: Puoi aggiungere più componenti sullo stesso smartphone premendo il pulsante *SCAN* tante volte quante ne hai bisogno.
      - media: "src/general-scan-button.svg"
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
    media: "[600]https://app.protobject.com/generate?a20-functions&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai creato la tua prima funzione! Ora è tempo di sperimentare."
    content: |
      * Come aggiungeresti un terzo pulsante che chiama la stessa funzione ma con il colore **blu**?
      * Come cambieresti la velocità del lampeggio? (Suggerimento: devi modificare la funzione solo in un punto!)
      * E se volessi creare un secondo schema luminoso completamente diverso? Creeresti una nuova funzione?
    right_content:
      - text: |
          **Sfida**: Modifica il progetto per visualizzare un messaggio sullo schermo. Crea una *nuova* funzione che accetti due parametri: il **testo** da visualizzare e il **colore** del testo.
      - text: |
          **Suggerimento**: Avrai bisogno del componente <comp>ScriviDisegna</comp>. Quindi, definisci una nuova funzione con parametri per il testo e il colore per gestire la scrittura del messaggio sullo schermo.
    media: "src/videos/light_challenge.mp4"
---