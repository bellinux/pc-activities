---
layout: activity
title: "L'Interruttore: Acceso o Spento?"
image: src/09-turn-on-the-light/09.enciende-luz.svg
video: src/videos/09_light_switch.mp4
video_title: "Cosa faremo?"
description: "Esplora una logica più avanzata con i condizionali 'Se-Allora-Altrimenti' per creare un interruttore della luce perfettamente funzionante."
lang: it
permalink: /it/attivita/linterruttore-acceso-o-spento/
ref: activity_turn_on_the_light

# ACTIVITY INFO
level: 1
computational_topics:
  - "Condizionali e Logica"
  - "Loop"
general_topics:
  - "Matematica e Logica"

tags: [Condizionali, Se-Allora-Altrimenti, Loop Principale, Interruttore, Interfaccia Utente]

introduction: |
  Finora, abbiamo detto ai nostri programmi 'SE succede questo, ALLORA fai quello'. Ma per quanto riguarda l' 'altrimenti'? Nel mondo reale, le azioni hanno spesso due facce: acceso o spento, bloccato o sbloccato, vero o falso. In questa missione, migliorerai le tue abilità logiche con il condizionale **'SE... ALLORA... ALTRIMENTI'**. Preparati a costruire un interruttore della luce perfettamente funzionante che sa esattamente cosa fare, sia che l'interruttore sia acceso *o* spento.

teacher: |
  ### **Corsi**
  * Classi 3-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere i concetti dei condizionali "se/allora/altrimenti".
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo che li circonda.
  * Valutare il proprio lavoro e quello dei pari.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - Il Potere di 'Altrimenti'**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a costruire un interruttore della luce perfettamente funzionante con Protobject."**
  2.  Inizia riepilogando il semplice condizionale 'SE/ALLORA'. Poi, introduci un problema più complesso con un'analogia: **"Immagina di andare al negozio per il tuo snack preferito. SE ce l'hanno, ALLORA lo compri. Ma se *non* ce l'hanno? Cosa fai ALTRIMENTI?"**
  3.  Questo introduce la necessità di un'azione alternativa. Spiega che questa logica 'SE/ALLORA/ALTRIMENTI' è cruciale per creare programmi interattivi, come l'interruttore della luce che costruiremo oggi.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Programmare una Scelta**
  1.  Ora che gli studenti comprendono la logica di scegliere tra due azioni diverse, è tempo di programmare il loro interruttore digitale.
  2.  Guidali attraverso **le istruzioni per costruire il programma 'SE/ALLORA/ALTRIMENTI'**, come dettagliato nella sezione pratica qui sotto. Presta particolare attenzione a come il blocco 'ACCENDI' va nello slot 'FAI' e il blocco 'SPEGNI' va nello slot 'ALTRIMENTI', rappresentando le due scelte.

  ### **Chiusura (5-10 minuti) - Vedere 'SE/ALTRIMENTI' Ovunque**
  1.  Una volta che tutti hanno un interruttore funzionante, incoraggiali a pensare a come questa logica a due parti si applica al mondo che li circonda.
  2.  Usa la sezione finale per stimolare una sessione di brainstorming su altri scenari 'SE/ALLORA/ALTRIMENTI' e per sfidarli ad aggiornare il loro progetto attuale con il suono.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Miglioriamo la Nostra Logica"
    type: "learn"
    icon: "book-reader"
    content: |
      Abbiamo visto come funziona un semplice condizionale: **SE** una condizione è vera, **ALLORA** accade un'azione. Ma se la condizione è *falsa*? Di solito, il programma non fa nulla.
      Per rendere il nostro codice più intelligente, possiamo aggiungere una seconda parte: un **ALTRIMENTI**.
      La struttura completa, “se, allora, altrimenti”, fornisce al computer un insieme completo di istruzioni: “**se** qualcosa è vero, **allora** fai questo; **altrimenti**, fai qualcosa di completamente diverso.”
    media: "src/09-turn-on-the-light/a-if-else-condition.it.svg"

  - title: "SE premuto, ALLORA acceso, ALTRIMENTI spento."
    type: "learn"
    content: |
      Un interruttore della luce è un esempio perfetto di questo. La logica è semplice: “**se** l'interruttore è attivo, **allora** accendi la luce; **altrimenti**, spegni la luce.”
      Ciò significa che se il programma rileva che l'interruttore è attivo, eseguirà l'azione nella parte "allora" (o "fai"). Ma se l'interruttore *non* è attivo, eseguirà invece l'azione nella parte "altrimenti".
      E come facciamo a far sì che il nostro programma controlli costantemente l'interruttore? Con il **loop principale**, ovviamente!
    media: "src/09-turn-on-the-light/a-if-else-condition-lamp.it.svg"

  - id: "create"
    title: "Crea una Lampada con un Interruttore"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo un prototipo che ci permetta di accendere una luce premendo un pulsante."
    content: |
      Per prima cosa, aggiungeremo due componenti: uno che funga da interruttore e un secondo che sia la nostra luce.
    steps:
      - "Premi <addbutton>Aggiungi Dispositivo</addbutton> e seleziona <comp>Lampada</comp>."
      - "Premi di nuovo <addbutton>Aggiungi Dispositivo</addbutton> e seleziona <comp>Interruttore</comp>."
      - "Ricorda che se non hai smartphone per scansionare i codici <qr>, puoi premere <openwindow>Apri in questa finestra</openwindow> per aprire i componenti sullo stesso computer."
    right_content:
      - text: |
          **Suggerimento**: In Protobject, puoi aggiungere più componenti sullo stesso smartphone premendo il pulsante *SCAN* tante volte quante ne hai bisogno.
      - media: "src/general-scan-button.svg"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
    media: "[700]https://app.protobject.com/generate?a09-lampswitch&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai costruito un programma che può fare una scelta!"
    content: |
      Questa logica 'SE/ALLORA/ALTRIMENTI' è uno dei concetti più importanti di tutta la programmazione.
      *Pensa alla tua vita quotidiana o alle tue app preferite. Dove vedi questo tipo di scelta a due parti? (es. SE una password è corretta, ALLORA accedi, ALTRIMENTI mostra un messaggio di errore).* 
    right_content:
      - text: |
          **Sfida**: Aggiorna questo progetto aggiungendo una musica che suona *solo* quando la luce è accesa.
      - text: |
          **Suggerimento**: Avrai bisogno del componente <comp>RiproduttoreSuoni</comp>. Dove nel tuo blocco SE/ALTRIMENTI metteresti i comandi 'riproduci suono' e 'ferma suono'?
---