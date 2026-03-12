---
layout: activity
title: "Il Faro"
image: src/19-lighthouse-with-a-switch/19.faro_.svg
video: src/videos/19_lighthouse.mp4
video_title: "Cosa faremo?"
description: "Padroneggia il loop 'For' per creare un bellissimo effetto di lampeggio graduale per un faro che puoi accendere e spegnere."
lang: it
permalink: /it/attivita/il-faro/
ref: activity_lighthouse_with_a_switch

# ACTIVITY INFO
level: 2
computational_topics:
  - "Loop"
  - "Temporizzazione ed Eventi"
  - "Variabili e Dati"
  - "Condizionali e Logica"
general_topics:
  - "Scienza e Tecnologia"

tags: [Loop, Loop For, Loop Annidati, Variabili, Temporizzazione, Effetto Graduale, Eventi]

introduction: |
  Una semplice luce lampeggiante è bella, ma un vero faro ha un bagliore dolce e graduale. Come possiamo programmare quell'effetto di dissolvenza in entrata e in uscita? In questa missione, imparerai a usare il **loop 'For'** — un potente loop progettato per essere eseguito per un numero preciso di passaggi. Preparati a programmare un bellissimo faro pulsante che si illumina e si attenua gradualmente.

teacher: |
  ### **Corsi**
  * Classi 6-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere il concetto di un loop FOR.
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello dei pari.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - Il Loop Controllato**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a prototipare un faro con una luce graduale e luminosa."**
  2.  Introduci il nuovo strumento di programmazione di oggi. Chiedi alla classe: **"E se avessimo bisogno di un loop che venga eseguito un numero esatto di volte, come 100 passaggi per passare da debole a luminoso?"**
  3.  Spiega che mentre un loop 'per sempre' è ottimo per l'automazione infinita, a volte abbiamo bisogno di più controllo. È qui che entra in gioco il **loop 'For'**. Scomponi i suoi componenti per loro: una variabile contatore, un valore iniziale, un valore finale e un passo. Questo è lo strumento perfetto per creare animazioni fluide e graduali.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione del Bagliore**
  1.  Ora che gli studenti comprendono i meccanismi di un loop 'For', è tempo di costruire l'effetto di bagliore graduale.
  2.  Guidali attraverso **le istruzioni per creare il prototipo del faro**, come dettagliato nella sezione pratica qui sotto. Presta molta attenzione a come useranno due loop 'For': uno per contare in avanti (dissolvenza in entrata) e un secondo per contare all'indietro (dissolvenza in uscita).

  ### **Chiusura (5-10 minuti) - Il Grande Dibattito sui Loop**
  1.  Una volta che tutti hanno un faro funzionante con un impulso fluido, è tempo di un'immersione più profonda nella teoria dei loop. Questo è un momento concettuale chiave.
  2.  Usa la sezione finale per guidare una discussione critica che confronta il loop 'For' con il loop 'While' che hanno visto prima. Sfidali a ricostruire questo progetto con lo strumento "sbagliato" per vedere perché i programmatori scelgono loop diversi per lavori diversi.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Il Loop FOR"
    type: "learn"
    icon: "book-reader"
    content: |
      Un loop **‘conta con variabile’**, noto nella maggior parte dei linguaggi di programmazione come loop **‘for’**, è progettato per ripetere un blocco di codice un numero specifico e noto di volte. Utilizza una variabile contatore per tenere traccia del suo progresso da un punto di partenza a un punto di arrivo.
    media: "src/19-lighthouse-with-a-switch/a-what-is.svg"

  - title: "Componenti del loop FOR"
    type: "learn"
    content: |
      Pensa a un **loop 'For'** come a un piano di missione:
      1.  **Variabile**: Il tuo contatore o "agente" che eseguirà il conteggio (ad es. `i` o `intensita`).
      2.  **Valore iniziale**: Il numero di partenza per il tuo contatore.
      3.  **Valore finale**: Il numero di destinazione in cui il loop si fermerà.
      4.  **Passi**: Quanto cambia il contatore in ogni ripetizione (ad es. contando in avanti di 1, o all'indietro di 1).
    media: "[600]https://app.protobject.com/generate?contador&it&static&-1"

  - title: "Come lo usiamo per un bagliore graduale?"
    type: "learn"
    content: |
      Un loop **'for'** è perfetto per l'animazione perché viene eseguito per un numero noto di passaggi.
      Per far illuminare gradualmente il nostro faro, useremo un loop 'for' che conta una variabile `intensita` da 0 a 100. In ogni passaggio, impostiamo la luminosità della luce sul valore corrente di `intensita`. Questo crea una dissolvenza in entrata fluida.
      Per attenuarlo, useremo un secondo loop 'for' che conta `intensita` da 100 a 0!
    media: 
      - "src/19-lighthouse-with-a-switch/b-cycle.svg"
      - "src/19-lighthouse-with-a-switch/z.lighthoyuse-anim.svg"

  - id: "create"
    title: "Crea il Faro"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo il prototipo che ci permette di controllare il faro."
    content: |
      Avremo bisogno di 2 componenti: una lampada che sia la nostra fonte di luce e un interruttore per accendere e spegnere l'intero sistema.
    steps:
      - "Premi <addbutton>Aggiungi Dispositivo</addbutton>, seleziona <comp>Lampada</comp> e usa <openwindow>Apri in questa finestra</openwindow> o uno smartphone."
      - "Premi <addbutton>Aggiungi Dispositivo</addbutton> e seleziona <comp>Interruttore</comp>."
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
    media: "[700]https://app.protobject.com/generate?a19-lighthouse&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti: FOR vs. WHILE"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Ora hai usato diversi tipi di loop. Confrontiamoli."
    content: |
      * Qual è la differenza principale tra un **loop 'for'** (conta con variabile) e un **loop 'while'** (ripeti mentre)?
      * Un loop 'for' è ottimo quando conosci i punti di inizio e fine esatti (come da 0 a 100). Un loop 'while' è ottimo quando devi solo aspettare che una condizione cambi.
      * Ci sono casi in cui potresti usare entrambi? Assolutamente!
    right_content:
      - text: |
          **Sfida**: Puoi modificare questo progetto per farlo funzionare allo stesso modo ma usando blocchi **"ripeti mentre"** invece di blocchi "conta con variabile"?
      - text: |
          **Suggerimento**: Dovresti creare la tua variabile `intensita`, aggiungere o sottrarre manualmente 1 da essa all'interno del loop e far funzionare il loop *mentre* `intensita` è inferiore a 100 (o maggiore di 0).
---