---
layout: activity
title: "Costruisci un Rilevatore di Cadute"
image: src/16-fall-detector/16.detector-caida.svg
video: src/videos/16_fall_detector.mp4
video_title: "Cosa faremo?"
description: "Impara a misurare l'accelerazione totale con il sensore di movimento del tuo telefono per creare un sistema in grado di rilevare una caduta improvvisa."
lang: it
permalink: /it/attivita/costruisci-un-rilevatore-di-cadute/
ref: activity_fall_detector

# ACTIVITY INFO
level: 1
computational_topics:
  - "Sensori e Input"
  - "Condizionali e Logica"
  - "Loop"
general_topics:
  - "Vita Quotidiana"

tags: [Accelerometro, Sensori, Valore Assoluto, Loop Principale, Condizionali, Salute, Sicurezza]

introduction: |
  Sapevi che il tuo telefono può percepire quando sta cadendo? Il suo **accelerometro** integrato è così sensibile che può rilevare improvvisi cambiamenti di movimento. Sommando i dati di tutti e tre gli assi di movimento (X, Y e Z), possiamo misurare la forza totale di un impatto. In questa missione, sfrutterai questa potenza per costruire un vero rilevatore di cadute che suona un allarme quando rileva un colpo secco e improvviso.
  
teacher: |
  ### **Corsi**
  * Classi 3-12

  ### **Materiali**
  * Cellulare, tablet o computer
  * Connessione a Internet

  ### **Obiettivi Educativi**
  * Comprendere i concetti di “se-altrimenti” e il “piano cartesiano”.
  * Creare un oggetto tecnologico (prototipo) utilizzando un dispositivo.
  * Identificare le relazioni tra la tecnologia e il mondo circostante.
  * Valutare il proprio lavoro e quello degli altri.
  * Partecipare a dialoghi e riflessioni su idee di miglioramento.

  ### **Inizio (10 minuti) - La Fisica di una Caduta**
  1.  Dai il benvenuto agli studenti e presenta l'attività del giorno: **"Oggi impareremo a prototipare un ‘rilevatore di cadute’ con i nostri telefoni."**
  2.  Inizia chiedendo alla classe: **"Come fanno gli smartwatch o i telefoni a sapere a volte se una persona è caduta?"** Guida la discussione verso l'idea di rilevare un movimento improvviso.
  3.  Spiega che l'**accelerometro** del telefono è la chiave. Introduci la sfida principale: una caduta può avvenire in qualsiasi direzione, quindi come può il nostro programma rilevare la *magnitudo* complessiva del movimento? Questo porta perfettamente al concetto di combinare gli assi X, Y e Z per ottenere un valore di movimento totale.

  {{learn}}

  ### **Sviluppo (20-30 minuti) - Costruzione del Rilevatore**
  1.  Ora che gli studenti comprendono la logica della misurazione del movimento totale, è tempo di costruire il rilevatore di cadute.
  2.  Guidali attraverso **le istruzioni per creare il prototipo e programmare la logica di rilevamento**, come dettagliato nella sezione pratica qui sotto. Sottolinea come l'istruzione 'SE' viene utilizzata per verificare se il movimento totale supera una certa soglia.
  3.  Fai testare ai studenti i loro prototipi scuotendo attentamente ma rapidamente il dispositivo, o lasciandolo cadere da una distanza molto breve su una superficie morbida come un libro o un cuscino.

  ### **Chiusura (5-10 minuti) - Affidabilità nel Mondo Reale**
  1.  Una volta che i rilevatori di cadute funzionano, è tempo di pensare alle implicazioni e alle sfide del mondo reale di un tale dispositivo.
  2.  Usa la sezione finale per guidare una discussione critica sull'affidabilità del loro rilevatore di cadute. Questo li incoraggia a pensare come ingegneri ai falsi positivi e a migliorare i loro progetti.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Come fa il telefono a rilevare una caduta?"
    type: "learn"
    icon: "book-reader"
    content: |
      L'**accelerometro** del tuo telefono è un potente sensore di movimento. Misura costantemente l'accelerazione in tre direzioni o "assi": sinistra-destra (asse X), avanti-indietro (asse Y) e su-giù (asse Z).
      Quando un telefono viene lasciato cadere, subisce un cambiamento brusco e improvviso di accelerazione. Per rilevare una caduta, non ci interessa la *direzione* della caduta, ma solo che sia stato un colpo potente. Per misurare questo colpo totale, possiamo prendere il **valore assoluto** (la versione positiva del numero) del movimento su ciascun asse e sommarli. Questo ci dà un singolo numero che rappresenta la magnitudo totale del movimento.
    media: "src/16-fall-detector/z-accelerometer.svg"

  - title: "Mettiamoci al lavoro!"
    type: "learn"
    content: |
      Protobject semplifica questo processo per noi con la variabile `movimentoGenerale`. Questa variabile speciale fa automaticamente i calcoli per noi: somma i valori assoluti degli assi X, Y e Z in tempo reale.
      Tutto ciò che dobbiamo fare è impostare una soglia. Diremo al nostro programma: **SE** il valore di `movimentoGenerale` supera un certo numero (come 150), significa che si è verificato un colpo secco e dovremmo attivare un suono di allarme.
    media: "src/a.working.svg"

  - id: "create"
    title: "Crea il Rilevatore di Cadute"
    type: "create"
    icon: "cogs"
    heading_text: "Creiamo un prototipo per rilevare le cadute."
    content: |
      Per prima cosa, dobbiamo aggiungere due componenti: uno per (1) rilevare i movimenti dello smartphone e un altro per (2) riprodurre i suoni.
    steps:
      - "Premi <addbutton>Aggiungi dispositivo</addbutton> e seleziona <comp>Movimento</comp>."
      - "Clicca di nuovo su <addbutton>Aggiungi dispositivo</addbutton> e seleziona <comp>RiproduttoreSuoni</comp>."
    right_content:
      - text: |
          **Suggerimento**: In Protobject, puoi aggiungere più componenti sullo stesso smartphone premendo di nuovo il pulsante *SCAN* dopo aver aggiunto il primo.
      - media: "src/general-scan-button.svg"
    ready_message: "Siamo pronti per iniziare a prototipare!"

  - title: "Composizione del Codice"
    type: "code-composition"
    icon: "code"
    content: |
      Clicca sull'icona del punto interrogativo per aprire i commenti che spiegano il codice.
      
      **Nota:** Questo codice utilizza la variabile `movimentoGenerale`. Come sfida extra, prova a modificare il codice per fare i calcoli manualmente sommando tu stesso i valori assoluti degli assi X, Y e Z!
    media: "[700]https://app.protobject.com/generate?a16-falldetector&it&dynamic&-1"

  - id: "reflect"
    title: "Rifletti"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Hai costruito un dispositivo con applicazioni nel mondo reale. Ora, pensiamo come ingegneri."
    content: |
      * Quanto pensi sia affidabile questo rilevatore di cadute? Un falso allarme potrebbe essere attivato semplicemente correndo, saltando o appoggiando il telefono troppo forte?
      * Ti fideresti di usarlo in una situazione reale per una persona anziana? Quali miglioramenti dovresti apportare prima?
    right_content:
      - text: |
          **Sfida**: Crea una luce che cambia colore in base alle accelerazioni del telefono.
      - text: |
          **Suggerimento**: Puoi alimentare i valori dei tre diversi assi dell'accelerometro (X, Y e Z) nei tre canali di colore primari (Rosso, Verde e Blu) di una lampada. Usa un evento per rilevare i cambiamenti nell'accelerometro.
---