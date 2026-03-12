---
layout: activity
title: "Spettacolo di Luci e Suoni"
image: src/04-melody-of-happy-birthday-with-lights/04.melodia-con-luces.svg
video: src/videos/04_birthday_light.mp4
video_title: "Cosa faremo?"
description: "Combina luci e musica in perfetta sincronia e impara a usare le variabili per controllare facilmente la velocità del tuo codice."
lang: it
permalink: /it/attivita/spettacolo-di-luci-e-suoni/
ref: activity_melody_of_happy_birthday_with_lights

# ACTIVITY INFO
level: 1
computational_topics:
  - "Variabili e Dati"
  - "Temporizzazione ed Eventi"
general_topics:
  - "Arte e Musica"

tags: [Variabili, Sincronizzazione, Temporizzazione, Controllo Multi-dispositivo, Luci, Suono]

introduction: |
  Pronto a dirigere il tuo spettacolo di luci e suoni? Combineremo musica e luci per creare una performance perfettamente sincronizzata. Ma cosa succede quando vuoi cambiare il tempo? Modificare decine di blocchi di ritardo uno per uno è un incubo. In questa missione, imparerai un segreto da professionisti per risolvere questo problema: le **variabili**. Agiscono come un telecomando principale per il tuo codice, permettendoti di cambiare la velocità dell'intero spettacolo con una singola modifica.
  
teacher: |
  ### **Corsi**
  * Classi 3-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere il concetto di variabile e il suo utilizzo.
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello degli altri.
  * Discutere e riflettere su idee di miglioramento.

  ### **Inizio (10 minuti) - La Sfida del Regista**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a prototipare uno spettacolo di luci e musica sincronizzato e facile da controllare."**
  2.  Stimola la discussione chiedendo: **"Pensate a un concerto dal vivo. Cosa lo rende così emozionante?"** Guidali verso l'idea di luci ed elementi visivi che si muovono tutti in perfetto tempismo con la musica (sincronizzazione).
  3.  Poi, poni la sfida principale di oggi: **"Ora, immaginate di essere il regista di quello spettacolo. Avete programmato 50 note e 50 lampi di luce. Cosa succede se improvvisamente volete che l'intera canzone vada più veloce per il finale? Dovreste trovare e cambiare 100 diversi blocchi di ritardo!"** Questo evidenzia un grosso problema: l'inefficienza. Ora puoi introdurre la soluzione elegante che usano i programmatori.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione di uno Spettacolo Regolabile**
  1.  Ora che gli studenti hanno capito che le variabili sono la soluzione per costruire un programma intelligente e regolabile, è tempo di metterle in pratica.
  2.  Guidali attraverso **il processo per creare il loro prototipo sincronizzato**, come dettagliato nella sezione pratica qui sotto. Ricorda costantemente loro di notare come la singola variabile `tempo` venga utilizzata più e più volte, agendo come controllo principale per la velocità dello spettacolo.

  ### **Chiusura (5-10 minuti) - Il Potere di una Singola Modifica**
  1.  Una volta che i prototipi funzionano, il momento "wow" arriva vedendo la variabile in azione.
  2.  Istruiscili a **cambiare solo il numero nel blocco iniziale `imposta tempo a...`**. Fagli provare un numero grande e poi un numero piccolo per vedere quanto drasticamente cambia il tempo dell'intero spettacolo. Questo dimostra la potenza e l'efficienza del loro nuovo strumento. Usa la sezione finale per sfidarli a espandere la loro creazione.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "La Sfida: Sincronizzazione e Velocità"
    type: "learn"
    icon: "book-reader"
    content: |
      Il primo obiettivo di un buon spettacolo di luci è la **sincronizzazione**, assicurarsi che ogni lampo di luce avvenga esattamente nello stesso momento di una nota musicale. Questo crea un effetto professionale ed emozionante.
      Ma c'è una seconda sfida, più grande: il **controllo**. Immagina di costruire la tua intera sequenza, ma poi decidi di volerla far andare più veloce. Dovresti tornare indietro e cambiare manualmente il valore del ritardo per *ogni singola nota* e *ogni singola luce*. Per una canzone lunga, potrebbero essere centinaia di modifiche! Questo è lento e una ricetta per gli errori.
    media: "src/04-melody-of-happy-birthday-with-lights/a-light.notes_.svg"

  - title: "La Soluzione: una Variabile come Controllo Principale"
    type: "learn"
    content: |
      Per risolvere il problema di dover cambiare molti valori contemporaneamente, i programmatori usano le **variabili**!
      Una **variabile** è come una scatola con un'etichetta. Puoi conservare un singolo pezzo di informazione, come un numero, all'interno di questa scatola. La parte potente è che puoi quindi usare questa scatola in molti punti del tuo codice.
      Se vuoi cambiare il numero, devi cambiarlo solo **una volta all'interno della scatola**. Ovunque tu abbia usato la scatola, il valore si aggiornerà automaticamente. È come un controllo principale per il tuo codice!
    media: "src/04-melody-of-happy-birthday-with-lights/b-variable.notes.it.svg"

  - id: "create"
    title: "Crea uno Spettacolo di Luci Musicale"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo un prototipo che suona ♪ Tanti Auguri ♪ con luci perfettamente sincronizzate e regolabili."
    content: |
      Per prima cosa, aggiungeremo i due componenti di cui abbiamo bisogno: uno per il suono e uno per la luce.
    steps:
      - "Premi <addbutton>Aggiungi Dispositivo</addbutton> e seleziona <comp>TastieraMusicale</comp>."
      - "Premi di nuovo <addbutton>Aggiungi Dispositivo</addbutton> e seleziona <comp>Lampada</comp>."
      - "Ricorda che se non hai smartphone per scansionare i codici <qr>, puoi premere <openwindow>Apri in questa finestra</openwindow>."
    right_content:
      - text: |
          **Suggerimento**: In Protobject, puoi aggiungere più componenti sullo stesso smartphone premendo il pulsante SCAN tante volte quante ne hai bisogno.
      - media: "src/general-scan-button.svg"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice. Nota come la variabile `tempo` viene definita una volta all'inizio e poi utilizzata per tutti i ritardi. I blocchi di moltiplicazione si trovano nella categoria <category>Matematica</category>.
    media: "[700]https://app.protobject.com/generate?a04-melody-light&it&dynamic&-1"
    right_content:
      - text: |
          **Sperimenta**: La magia accade qui! Prova a cambiare il singolo valore della variabile "tempo" all'inizio del codice. Impostalo su `100` per vederlo andare super veloce, o su `500` per vederlo andare lento.

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai costruito uno spettacolo intelligente e regolabile. E adesso?"
    content: |
      Hai visto quanto può essere potente una singola variabile. E se volessi rendere il tuo spettacolo ancora più grande? Come aggiungeresti una seconda lampada che lampeggia insieme alla musica, magari su un telefono diverso o con un colore diverso?
    right_content:
      - text: |
          Pensa a come aggiungeresti un nuovo componente <comp>Lampada</comp> e lo collegheresti alla stessa variabile principale `tempo`.
---