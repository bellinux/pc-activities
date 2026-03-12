---
layout: activity
title: "L'Allarme Antifurto"
image: src/08-anti-theft-alarm/08.alarma-antirobo.svg
video: src/videos/08_alarm.mp4
video_title: "Cosa faremo?"
description: "Rendi il tuo codice intelligente! Usa i condizionali ('Se-Allora') per prendere decisioni e costruire un allarme che reagisce al movimento."
lang: it
permalink: /it/attivita/lallarme-antifurto/
ref: activity_anti_theft_alarm

# ACTIVITY INFO
level: 1
computational_topics:
  - "Condizionali e Logica"
  - "Loop"
  - "Sensori e Input"
general_topics:
  - "Vita Quotidiana"

tags: [Condizionali, Se-Allora, Loop Principale, Sensori, Sensore di Movimento, Fotocamera]

introduction: |
  Insegniamo ai nostri programmi a vedere e reagire al mondo! Questa missione ti introduce al potere dei **sensori** e della **logica condizionale**. Imparerai a usare un semplice ma potente comando 'SE succede questo, ALLORA fai quello' per costruire un allarme antifurto intelligente che si attiva quando rileva un movimento. Preparati a creare il tuo primo sistema intelligente!

teacher: |
  ### **Corsi**
  * Classi 3-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere il concetto di condizionali "SE-ALLORA".
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello degli altri.
  * Partecipare a discussioni e riflettere su idee di miglioramento.

  ### **Inizio (10 minuti) - La Logica di un Allarme**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a prototipare un allarme che rileva il movimento."**
  2.  Chiedi alla classe: **"Avete mai visto una porta automatica o una luce di sicurezza? Come pensate che sappiano che siete lì?"**
  3.  Dopo aver discusso le loro idee sui sensori, spiega che useremo la fotocamera del loro telefono come sensore di movimento. Ma come fa un programma a *decidere* quando far suonare l'allarme? Questo è il momento perfetto per introdurre la **logica condizionale**—l'istruzione 'SE/ALLORA'.
  4.  Infine, spiega che il programma deve controllare costantemente la presenza di movimento, non solo una volta, il che richiede un **Loop Principale** per eseguire il controllo più e più volte.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione del Sistema di Sicurezza**
  1.  Ora che hanno capito la logica di "SE viene rilevato un movimento, ALLORA suona l'allarme", è tempo di costruire il sistema di sicurezza.
  2.  Guida gli studenti attraverso **le istruzioni per aggiungere i componenti e costruire il codice condizionale**, come dettagliato nella sezione pratica qui sotto. Assicurati che capiscano perché il blocco SE deve essere posizionato all'interno del loop principale per essere efficace.

  ### **Chiusura (5-10 minuti) - Debriefing sulla Sicurezza**
  1.  Una volta che gli allarmi funzionano, è tempo di un debriefing da esperti di sicurezza. Un vero esperto di sicurezza pensa sempre ai punti deboli del proprio sistema.
  2.  Usa la sezione finale per guidare una discussione sui limiti del loro allarme basato sulla fotocamera. Questo li incoraggia a pensare in modo critico a come funziona la tecnologia nel mondo reale e a come potrebbe essere migliorata.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Hai mai sentito parlare di sensori di movimento?"
    type: "learn"
    icon: "book-reader"
    content: |
      I sensori di movimento sono dispositivi intelligenti in grado di rilevare quando qualcuno o qualcosa si muove vicino a loro.
      
      Alcuni, come quelli delle porte automatiche, funzionano con **infrarossi** (un tipo di luce che non possiamo vedere) o **ultrasuoni** (un suono che non possiamo sentire). Rilevano i cambiamenti quando i loro segnali rimbalzano su un oggetto in movimento.
    media: "src/08-anti-theft-alarm/a-movement-sensor.svg"

  - title: "Usare una Fotocamera come Sensore di Movimento"
    type: "learn"
    content: |
      Esistono anche sensori di movimento **basati su fotocamere**, che è quello che useremo in questa attività.
      Un programma può guardare il feed video di una fotocamera e rilevare **cambiamenti tra i fotogrammi**. Se una grande parte dell'immagine cambia improvvisamente, il programma sa che **qualcosa si sta muovendo**.
    media: "src/08-anti-theft-alarm/a-smartphone-camera.svg"

  - title: "SE c'è movimento, ALLORA suona l'allarme"
    type: "learn"
    content: |
      Per rendere il nostro programma intelligente, dobbiamo insegnargli a prendere decisioni. Il modo più semplice per farlo è con un'istruzione condizionale: **SE una condizione è vera, ALLORA accade un'azione.**
      Questa struttura "SE... ALLORA..." è un elemento fondamentale di tutta la programmazione, dai semplici giochi all'intelligenza artificiale complessa.
    media: "src/08-anti-theft-alarm/a-simple-condition.it.svg"
  
  - title: "Un Esempio Pratico"
    type: "learn"
    content: |
      Vediamo come usare un condizionale per attivare il nostro allarme.
      Diremo al programma: **SE** la quantità di movimento rilevata dalla fotocamera è maggiore di un certo numero (come 40), **ALLORA** riproduci il suono dell'allarme.
      Ma come facciamo a far sì che il programma controlli il movimento *continuamente*? Non possiamo controllare solo una volta! È qui che un **loop principale** è essenziale. Inserendo il nostro controllo 'SE movimento' all'interno di un loop 'ripeti per sempre', creiamo un sistema che è sempre in guardia.
    media: "src/08-anti-theft-alarm/a-mov-condition.it.svg"

  - id: "create"
    title: "Creiamo il nostro allarme antifurto!"
    type: "create"
    icon: "cogs"
    heading_text: "Costruiamo il prototipo per il nostro allarme."
    content: |
      Per prima cosa, dobbiamo aggiungere due componenti: uno per (1) rilevare il movimento e un altro per (2) riprodurre il suono dell'allarme.
    steps:
      - "Aggiungi il componente <comp>MovimentiFotocamera</comp> che rileva il movimento attraverso la fotocamera del telefono."
      - "Aggiungi il componente <comp>RiproduttoreSuoni</comp> per riprodurre il suono di un allarme."
      - "Ricorda che se non hai uno smartphone per scansionare i codici <qr>, puoi cliccare su <openwindow>Apri in questa finestra</openwindow>."
    right_content:
      - text: |
          **Suggerimento**: In Protobject, puoi aggiungere più componenti sullo stesso smartphone premendo il pulsante SCAN tante volte quante ne hai bisogno.
      - media: "src/general-scan-button.svg"
    ready_message: "Siamo pronti per iniziare a prototipare!"


  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
      I blocchi condizionali si trovano nella categoria <category>Logica</category>.
    media: "[700]https://app.protobject.com/generate?a08-alarm&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai costruito un sistema di sicurezza. Ora, pensa come un esperto di sicurezza."
    content: |
      * Cosa succederebbe se un ladro entrasse di notte con tutte le luci spente? Un sensore basato su fotocamera funzionerebbe ancora?
      * Quanto è affidabile questo allarme? Cosa potrebbe accidentalmente innescare un falso allarme (come un animale domestico che passa di corsa)?
    right_content:
      - text: |
          **Suggerimento:** Pensare ai punti deboli di un sistema è il primo passo per renderlo più forte. Il nostro sensore si basa sulla luce e sulle immagini per funzionare!
---