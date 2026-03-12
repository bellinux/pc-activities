---
layout: activity
title: "Un Avvertimento Lampeggiante"
image: src/06-traffic-light-with-flashing-yellow-light/06.semaforo-luz-intermitente.svg
video: src/videos/06_intermittent_traffic_light.mp4
video_title: "Cosa faremo?"
description: "Approfondisci l'automazione annidando i loop per creare un semaforo con luce gialla lampeggiante realistico."
lang: it
permalink: /it/attivita/un-avvertimento-lampeggiante/
ref: activity_traffic_light_with_flashing_yellow_light

# ACTIVITY INFO
level: 1
computational_topics:
  - "Loop"
  - "Temporizzazione ed Eventi"
general_topics:
  - "Vita Quotidiana"

tags: [Loop Annidati, Loop Principale, Automazione, Sequenza Lampeggiante, Temporizzazione]

introduction: |
  Pronto a rendere le tue automazioni ancora più intelligenti? I semafori del mondo reale non cambiano solo colore, spesso danno un avvertimento con una luce gialla lampeggiante. Per programmare questo effetto senza creare confusione, imparerai una tecnica avanzata: i **loop annidati**. Preparati a inserire un loop *dentro* un altro loop per costruire programmi più complessi e potenti.

teacher: |
  ### **Corsi**
  * Classi 3-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere il concetto di "loop", sia generale che annidato.
  * Sviluppare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e l'ambiente circostante.
  * Valutare il proprio lavoro e quello degli altri, sia individualmente che in team.
  * Partecipare a dialoghi e riflessioni per proporre miglioramenti.

  ### **Inizio (10 minuti) - La Sfida del Lampeggio**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a creare un semaforo più avanzato e realistico."**
  2.  Chiedi alla classe di pensare ai semafori del mondo reale: **"Cosa fa spesso la luce gialla prima di diventare rossa per attirare la vostra attenzione?"** Guidali verso l'idea di un avvertimento lampeggiante.
  3.  Poni la sfida di programmazione: **"Come potremmo programmarlo? Potremmo copiare e incollare i blocchi ACCESO/SPENTO per la luce gialla, ma il nostro codice diventerebbe lungo e disordinato molto velocemente!"** Questo introduce il problema della ripetizione.
  4.  Spiega che per risolvere questo problema in modo efficiente, abbiamo bisogno di un nuovo tipo di loop, uno che possa essere eseguito un numero specifico di volte *all'interno* del nostro loop principale "per sempre". Questa è l'introduzione perfetta al concetto di loop annidati.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione con Loop Annidati**
  1.  Ora che hanno compreso il concetto di annidare un loop dentro un altro, è tempo di costruire il semaforo avanzato.
  2.  Guidali attraverso **le istruzioni per modificare la sequenza del semaforo**, mostrando loro esattamente dove aggiungere il nuovo loop numerato per creare l'effetto lampeggiante giallo. Questa sarà la loro prima volta a creare un loop all'interno di un loop.

  ### **Chiusura (5-10 minuti) - Vedere Loop Ovunque**
  1.  Una volta che tutti hanno un semaforo funzionante e lampeggiante, allarga la discussione per pensare a dove altro si applica questo potente concetto.
  2.  Usa la sezione finale per stimolare una discussione creativa sui loop nella vita di tutti i giorni e per sfidarli con una simulazione di traffico ancora più complessa.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Come possiamo programmare una luce lampeggiante?"
    type: "learn"
    icon: "book-reader"
    content: |
      Immagina di aver costruito un semaforo automatizzato che cicla attraverso i suoi colori all'interno di un loop "ripeti per sempre". È un ottimo inizio, ma possiamo renderlo più realistico.
      E se volessimo che la **luce gialla lampeggiasse** alcune volte prima di diventare rossa? Questo sarebbe un avvertimento molto migliore e più sicuro per i conducenti.
    media: "src/06-traffic-light-with-flashing-yellow-light/a.traffic-interm.svg"

  - title: "Quindi, aggiungiamo solo più blocchi?"
    type: "learn"
    content: |
      Per far lampeggiare la luce, dovremmo aggiungere una sequenza come questa al nostro loop principale:
      **Verde → Giallo ACCESO → SPENTO → Giallo ACCESO → SPENTO → Giallo ACCESO → SPENTO → Rosso**
      Questo funziona, ma sta solo ripetendo la sequenza **“Giallo ACCESO → SPENTO”**. Ancora una volta, **il nostro codice diventerebbe molto lungo e ripetitivo!** Ci deve essere un modo più intelligente.
    media: "src/06-traffic-light-with-flashing-yellow-light/a.loop.large.it.svg"

  - title: "Perché non un altro loop 'per sempre'?"
    type: "learn"
    content: |
      Non puoi avere due capitani su una nave e non puoi avere più di un loop "ripeti per sempre" (Loop Principale) in un programma! Se lo facessi, il computer non saprebbe quale è il programma principale o cosa eseguire. Si confonderebbe!
    media: "src/06-traffic-light-with-flashing-yellow-light/a.pc_.confused.svg"

  - title: "La soluzione: un loop dentro un loop!"
    type: "learn"
    content: |
      È qui che un diverso tipo di **loop** torna utile! Possiamo usare un loop che si ripete un numero specifico di volte (nell'immagine, 3 volte). Questo è perfetto per la parte lampeggiante.
      Ancora meglio, possiamo **annidare i loop**. Ciò significa mettere un loop *dentro* un altro. Ripetizioni dentro le ripetizioni!
    media: "src/06-traffic-light-with-flashing-yellow-light/a.general.loop-2.it.svg"

  - title: "Giallo lampeggiante: un loop annidato"
    type: "learn"
    content: |
      Usando un loop numerato, possiamo ripetere i blocchi **“Giallo ACCESO → SPENTO”** quante volte vogliamo. Mettendo questo loop più piccolo *dentro* il nostro loop principale "per sempre", creiamo un programma potente ed efficiente:
      Loop Principale ( **Verde →** *Loop Interno* ( **Giallo ACCESO → SPENTO** [x4] ) **→ Rosso** )
    media: "src/06-traffic-light-with-flashing-yellow-light/a.general.loop-inside-2.it.svg"

  - id: "create"
    title: "Costruiamo il nostro semaforo lampeggiante!"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo il nostro semaforo avanzato."
    steps:
      - "Premi <addbutton>Aggiungi Dispositivo</addbutton> e seleziona <comp>Lampada</comp>."
      - "Scansiona il codice <qr>."
      - "Ricorda che se non hai uno smartphone, puoi premere <openwindow>Apri in questa finestra</openwindow>."
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
      I blocchi “ripeti per sempre” e il loop numerato si trovano entrambi nella categoria <category>Base</category>.
    media: "[700]https://app.protobject.com/generate?a06-trafficlighflashing&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Ora hai imparato a usare i loop annidati! Chiediti:"
    content: |
      * I loop non sono solo per il codice; sono ovunque. Dove puoi vedere schemi o cicli che si ripetono nella vita di tutti i giorni (pensa alla musica, alle routine quotidiane, alla natura)?
      * Quale altro prototipo interessante potresti costruire usando un loop dentro un loop?
    right_content:
      - text: |
          **Sfida**: Facciamo funzionare 2 semafori a un incrocio in sincronia!
          
          *Quando uno è rosso, l'altro dovrebbe essere verde e viceversa.*
      - media: "src/06-traffic-light-with-flashing-yellow-light/traffic-challenge.svg"
---