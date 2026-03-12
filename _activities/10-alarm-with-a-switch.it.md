---
layout: activity
title: "Un Allarme Più Intelligente con gli Eventi"
image: src/10-alarm-with-a-switch/10.alarma-toque.svg
video: src/videos/10_alarm_switch.mp4
video_title: "Cosa faremo?"
description: "Scopri un modo più efficiente per programmare! Impara come gli eventi permettono al tuo programma di reagire istantaneamente ad azioni come la pressione di un pulsante."
lang: it
permalink: /it/attivita/un-allarme-piu-intelligente-con-gli-eventi/
ref: activity_alarm_with_a_switch

# ACTIVITY INFO
level: 1
computational_topics:
  - "Temporizzazione ed Eventi"
  - "Condizionali e Logica"
general_topics:
  - "Vita Quotidiana"

tags: [Eventi, Stati, Condizionali, Interruttore, Programmazione Efficiente]

introduction: |
  Abbiamo usato i loop per controllare costantemente se qualcosa sta accadendo, ma non è un po' inefficiente, come chiedere continuamente "Siamo arrivati?" durante un viaggio in auto? C'è un modo molto più intelligente! E se i nostri componenti potessero semplicemente *dirci* quando succede qualcosa? Benvenuto nel potente mondo della **programmazione basata sugli eventi**. In questa missione, costruirai un allarme che non controlla, ma *ascolta*, rendendo il tuo codice più veloce e professionale.

teacher: |
  ### **Corsi**
  * Classi 3-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere il concetto di evento.
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello degli altri.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - Un Modo Più Intelligente per Ascoltare**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a creare un semplice allarme che emette un suono quando si preme un pulsante, ma usando un metodo nuovo e più intelligente."**
  2.  Inizia chiedendo alla classe: **"Come funziona effettivamente un semplice pulsante o interruttore?"** Guidali verso l'idea di due stati: ACCESO e SPENTO.
  3.  Poi, introduci il concetto fondamentale di oggi: l'efficienza. Chiedi loro: **"Usando un loop, il nostro programma deve chiedere costantemente al pulsante: 'Sei premuto? Sei premuto?'. E se il pulsante potesse semplicemente inviare un messaggio al programma *solo* quando viene effettivamente premuto?"** Questo introduce il concetto di **evento** come notifica, un modo più efficiente di programmare.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione di un Allarme Guidato dagli Eventi**
  1.  Ora che gli studenti comprendono la differenza tra controllare costantemente con un loop e ascoltare efficientemente un evento, è tempo di costruire l'allarme più intelligente.
  2.  Guidali attraverso **le istruzioni per costruire il programma guidato dagli eventi**, come dettagliato nella sezione pratica qui sotto. Sottolinea che la logica principale di questo programma **non** utilizza un loop "ripeti per sempre", perché l'evento fa il lavoro per noi.

  ### **Chiusura (5-10 minuti) - Gli Eventi sono Ovunque**
  1.  Once everyone has a working, event-driven alarm, it's time to reflect on this powerful new programming paradigm.
  2.  Usa la sezione finale per stimolare una discussione su dove altro vengono utilizzati gli eventi nella tecnologia moderna (ogni clic, tocco e notifica è un evento!) e per sfidarli a combinare eventi con variabili per aggiungere una nuova funzionalità.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Come funziona un interruttore?"
    type: "learn"
    icon: "book-reader"
    content: |
      Creeremo un allarme che viene attivato da un interruttore. Ma per farlo, dobbiamo capire come 'pensa' un interruttore.
      Nella programmazione, un semplice interruttore ha due possibili **stati**:
      * **Acceso:** L'interruttore è attivato. Possiamo rappresentare questo stato con il numero **1**.
      * **Spento:** L'interruttore è disattivato. Possiamo rappresentarlo con il numero **0**.
      Un interruttore può trovarsi solo in uno stato alla volta. Leggendo se lo stato è 1 o 0, il computer può decidere cosa fare dopo.
    media: "src/10-alarm-with-a-switch/interruptor-animd.svg"

  - title: "Come fa il computer a conoscere lo stato?"
    type: "learn"
    content: |
      Il computer può essere programmato per "ascoltare" un segnale dall'interruttore.
      **Ogni volta che lo stato del pulsante cambia (da Spento a Acceso, o da Acceso a Spento), notifica il computer!**
      Questa notifica è chiamata **evento**. Una volta che il computer riceve l'evento, può eseguire un pezzo di codice specifico per reagire ad esso.
    media: "src/10-alarm-with-a-switch/evento-icon.es.it.svg"

  - title: "Perché non usare semplicemente un loop principale?"
    type: "learn"
    content: |
      Usare un **Loop Principale** per controllare un pulsante è come un passeggero sul sedile posteriore che chiede costantemente: *“Sei già stato premuto?! E adesso?! Sei stato premuto ora?!”* anche quando non sta succedendo nulla. È ripetitivo e spreca l'energia del computer.
      Con gli **eventi**, il programma è silenzioso. Aspetta semplicemente. L'interruttore stesso invia un singolo segnale al computer *solo quando il suo stato è cambiato*. Questo è molto più efficiente e professionale!
    media: "src/10-alarm-with-a-switch/evento-scheme.it.svg"
  
  - title: "Abbiamo ricevuto l'evento… E adesso?"
    type: "learn"
    content: |
      Una volta che l'interruttore invia il suo segnale, il computer può usare un condizionale per decidere cosa fare in base allo stato attuale dell'interruttore.
      Per il nostro allarme, la logica è semplice: **SE** il nuovo stato dell'interruttore è **ACCESO**, riproduciamo un suono. **ALTRIMENTI** (significa che il suo nuovo stato è **SPENTO**), fermiamo il suono.
    media: "src/10-alarm-with-a-switch/if-else-alarm.it.svg"

  - id: "create"
    title: "Crea l'Allarme"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo un prototipo che suona un allarme quando un interruttore viene attivato."
    content: |
      Per prima cosa, aggiungeremo due componenti che ci permettono di (1) attivare l'allarme e (2) riprodurre il suono.
    steps:
      - "Premi <addbutton>Aggiungi dispositivo</addbutton> e seleziona <comp>RiproduttoreSuoni</comp>."
      - "Premi di nuovo <addbutton>Aggiungi Dispositivo</addbutton> e seleziona <comp>Interruttore</comp>."
      - "Ricorda che se non hai uno smartphone per scansionare i codici <qr>, puoi cliccare su <openwindow>Apri in questa finestra</openwindow>."
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
    media: "[700]https://app.protobject.com/generate?a10-alarmswitch&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai appena imparato un modo più professionale di programmare!"
    content: |
      Gli eventi sono la spina dorsale di tutte le interfacce utente moderne: ogni clic, tocco e scorrimento è un evento.
      *Oltre ai pulsanti, quali altre cose sul tuo telefono o in un gioco potrebbero innescare un evento? (Pensa alle notifiche, al termine di un download, a un personaggio che tocca una moneta, ecc.)*
    right_content:
      - text: |
          **Sfida**: Aggiorniamo il nostro allarme per contare e visualizzare quante volte è stato attivato!
      - text: |
          **Suggerimento**: Avrai bisogno di una variabile per memorizzare il conteggio e del dispositivo <comp>ScriviDisegna</comp> per mostrarlo sullo schermo. Dove aggiungeresti `1` alla variabile?
---