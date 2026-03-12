---
layout: activity
title: "Toca una Canción"
image: src/03-playing-happy-birthday/03.tocando-melodia.svg
video: src/videos/03_happy_birthday.mp4
video_title: "¿Qué haremos?"
description: "¡Convierte tu dispositivo en un instrumento musical! Aprende a secuenciar notas y a controlar su tiempo para tocar una melodía familiar."
lang: es
permalink: /es/actividades/toca-una-cancion/
ref: activity_playing_happy_birthday

# ACTIVITY INFO
level: 1
computational_topics:
  - "Fundamentos de Programación"
  - "Temporización y Eventos"
general_topics:
  - "Arte y Música"

tags: [Notas Musicales, Secuenciación, Temporización, Sonido, Altavoz]

introduction: |
  ¡Es hora de convertirte en un músico digital! Esta actividad convertirá tu dispositivo en un instrumento. Aprenderás a programar una secuencia de **notas musicales** y a usar la **temporización** para controlar su ritmo, armando la clásica canción de 'Feliz Cumpleaños' bloque por bloque.
  
teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Smartphone, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender los conceptos de secuenciación de pasos.
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar el trabajo personal y el de los demás.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - La Ciencia del Sonido**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy vamos a aprender a crear un prototipo de un juguete musical."**
  2.  Despierta su curiosidad con una pregunta: **"¿Cómo creen que su teléfono o sus auriculares producen sonido?"**
  3.  Después de una breve discusión, es hora de desmitificar la tecnología. Exploremos cómo un simple altavoz puede convertir señales eléctricas silenciosas en la música y los sonidos que escuchamos todos los días.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Componiendo la Melodía**
  1.  Ahora que todos entienden los conceptos básicos del sonido digital, ¡comencemos a componer! La misión es recrear la canción "Feliz Cumpleaños" programando la secuencia correcta de notas y retardos.
  2.  Guía a tus estudiantes a través de **las instrucciones paso a paso para construir la melodía**, que se detallan en la sección práctica a continuación.
  3.  La secuencia de notas requerida es: **Do4, Do4, Sol4, Sol4, La4, La4, Sol4, Fa4, Fa4, Mi4, Mi4, Re4, Re4, Do4**. Asegúrate de que organicen los bloques en este orden preciso.

  ### **Cierre (5-10 minutos) - Reflexión y Remezcla**
  1.  Una vez que los estudiantes tengan una canción que funcione, desafíalos a pensar como productores de música. ¿Cómo podrían cambiar el tempo?
  2.  Plantea el desafío: **"¿Y si quisiéramos tocar la canción más rápido o más lento?"** Usa esta pregunta para iniciar una discusión sobre cómo cambiar cada valor de retardo puede ser tedioso, preparando el terreno para conceptos más avanzados como las variables. Usa la sección final para guiar la conversación.

  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Cómo producen sonido los dispositivos?"
    type: "learn"
    icon: "book-reader"
    content: |
      ¿Alguna vez te has preguntado cómo tu teléfono puede reproducir tus canciones favoritas? La magia ocurre en un pequeño componente llamado **altavoz**. Piénsalo como un dispositivo que convierte señales eléctricas en ondas de sonido. Un imán y una bobina en su interior se mueven cuando la electricidad pasa a través de ellos, haciendo vibrar un cono. Estas vibraciones crean las ondas de sonido que viajan por el aire hasta nuestros oídos.
      Nuestro cerebro interpreta estas ondas como música, voces o efectos de sonido, lo que nos permite disfrutar de una película o cantar una canción.
    media: "src/03-playing-happy-birthday/a-speaker.svg"

  - title: "¡Los altavoces están en todas partes!"
    type: "learn"
    content: |
      ¡Puedes encontrar altavoces en todo tipo de dispositivos! Están en tu televisor, dentro de tus auriculares y, por supuesto, en tu smartphone. Si alguna vez has visto un video o escuchado música en tu teléfono, has oído sus altavoces en acción.
    media:
      - "src/03-playing-happy-birthday/a-tv.svg"
      - "src/03-playing-happy-birthday/a-headphones.svg"
      - "src/03-playing-happy-birthday/a-smartphone.svg"

  - id: "create"
    title: "Toquemos una Canción"
    type: "create"
    icon: "cogs"
    heading_text: "Vamos a crear un prototipo que toque 'Feliz Cumpleaños' en el teléfono. Primero, conectemos nuestro dispositivo."
    steps:
      - "Haz clic en <addbutton>Añadir dispositivo</addbutton> en la barra lateral izquierda."
      - "Selecciona el componente <comp>TecladoMusical</comp> para tocar notas en el smartphone."
      - "Escanea el código <qr> con tu smartphone o presiona <openwindow>Abrir en esta ventana</openwindow>."

  - title: "¡Arrastra las notas!"
    type: "create"
    content: |
      Para construir una melodía, necesitas arrastrar los bloques de notas al espacio de trabajo en la secuencia correcta.
    media: "src/03-playing-happy-birthday/a-dragnote.es.svg"
    
  - title: "¿Cómo controlar la duración de una nota?"
    type: "create"
    content: |
      ### ¡Usamos retardos!

      Una melodía no se trata solo de notas; también se trata de ritmo. Para controlar cuánto tiempo suena una nota, necesitas agregar una pausa antes de que comience la siguiente.
      
      Por ejemplo:
      * toca una nota
      * **espera 400 milisegundos**
      * toca la siguiente nota
      * **espera 200 milisegundos**
      * … y así sucesivamente.
    right_content:
      - text: |
          **Consejo Profesional:** Los bloques de **retardo** que controlan estas pausas se encuentran en la categoría <category>Temporización</category>. ¡Son esenciales para crear el ritmo de tu canción!

  - title: "¿Cuál es la secuencia de notas y retardos?"
    type: "create"
    content: |
      La parte principal de “Feliz Cumpleaños” tiene esta secuencia de notas con sus respectivos retardos, medidos en milisegundos (ms).
    media: "src/03-playing-happy-birthday/a-noteduration.es.it.svg"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
    media: "[700]https://app.protobject.com/generate?a03-melody&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Has codificado una canción, pero ¿y si quisieras un remix?"
    content: |
      Para cambiar el tempo, necesitas ajustar los retardos. En este momento, tu canción usa pausas de 200, 400 y 600 milisegundos.

      ¿Y si quisieras tocarla el doble de rápido? Tendrías que volver y cambiar *cada bloque de retardo* a mano. ¡Eso suena a mucho trabajo! ¿Hay una forma más inteligente y eficiente de controlar la velocidad?
---