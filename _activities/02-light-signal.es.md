---
layout: activity
title: "Crea una Baliza Intermitente"
image: src/02-light-signals/cover.svg
video: src/videos/02_beacon.mp4
video_title: "¿Qué haremos?"
description: "Descubre cómo controlar la velocidad de tu código programando una secuencia de luces intermitentes."
lang: es
permalink: /es/actividades/crea-una-baliza-intermitente/
ref: activity_light_signals

# ACTIVITY INFO
level: 1
computational_topics:
  - "Fundamentos de Programación"
  - "Temporización y Eventos"
general_topics:
  - "Ciencia y Tecnología"

tags: [Temporización, Bloque de Retardo, Secuenciación, Señal Luminosa, Efecto Intermitente]

introduction: |
  ¿Alguna vez has visto las luces intermitentes de una torre o un vehículo de emergencia y te has preguntado cómo se controlan? Ese parpadeo no es aleatorio, está programado con un sentido del **tiempo**. En esta misión, te convertirás en el maestro del tiempo, aprendiendo a usar **retardos** para crear tu propia baliza intermitente desde cero.
  
teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Descripción**
  En esta actividad, los estudiantes aprenderán el concepto fundamental de programación de la "temporización". Usarán bloques de retardo para controlar la secuencia de una lámpara virtual, creando un efecto clásico de baliza intermitente y comprendiendo por qué las pausas son cruciales en la codificación.

  ### **Objetivos Educativos**
  * Comprender los conceptos de "LED" y "temporización".
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar el trabajo personal y el de los demás en trabajos individuales o en equipo.
  * Discutir y reflexionar sobre ideas de mejora.

  ### **Inicio (10 minutos) - Introduciendo el Concepto de Tiempo**
  1.  Da la bienvenida a los estudiantes y presenta la actividad: **"Hoy aprenderemos a prototipar una baliza que se enciende y se apaga."**
  2.  Para iniciar la discusión, comienza con una pregunta: **"¿Saben qué hace que la pantalla de su celular se ilumine?"**
  3.  Después de que compartan sus ideas, explica que la pantalla está hecha de pequeñas luces llamadas LED. Luego, plantea un experimento mental: **"Imagina que escribes un programa que le dice a una lámpara que se encienda, y en la siguiente línea, le dices que se apague. ¿Qué crees que verías realmente?"** Déjalos debatir. La respuesta es... ¡nada! Este es el momento perfecto para explicar que las computadoras son increíblemente rápidas y por qué necesitamos programar pausas, introduciendo el concepto de "Temporización".

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo la Baliza**
  1.  Con la teoría de la temporización cubierta, es hora de ponerla en práctica y construir la baliza intermitente.
  2.  Guía a tus estudiantes a través de **las instrucciones para conectar el dispositivo y codificar la secuencia de luces** detalladas en la sección práctica a continuación. Anímalos a experimentar con diferentes tiempos de retardo para ver cómo afecta la velocidad del parpadeo.

  ### **Cierre (5-10 minutos) - Reflexión y Aplicaciones Futuras**
  1.  ¡Excelente! Una vez que todos tengan una baliza funcionando, pasa a una discusión final para consolidar su comprensión y desafiarlos a pensar en grande.
  2.  Inicia la reflexión haciendo la pregunta clave de la actividad: **"¿En qué otras situaciones podríamos usar la temporización?"** Usa las siguientes indicaciones para guiar una conversación sobre cómo se usa la temporización en la tecnología que nos rodea.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Qué es un LED?"
    type: "learn"
    icon: "book-reader"
    content: |
      ¿Alguna vez has mirado muy de cerca la pantalla de tu televisor o smartphone? Está compuesta por millones de pequeñas y potentes luces llamadas **LED**.
      Los LED están en todas partes a nuestro alrededor, desde los grandes que iluminan una habitación hasta los pequeños que trabajan juntos para crear las imágenes que ves en una pantalla.
    media: "src/02-light-signals/a-examples1.svg"

  - title: "¿Y la pantalla del celular?"
    type: "learn"
    content_class: "space-y-2 text-xl"
    content: |
      La pantalla de tu celular está llena de miles de estos pequeños LED. Cuando ves un video o miras una foto, estas son las luces que se encienden и se apagan para formar la imagen.
      ¡Cuando prototipamos con Protobject, estos son los mismos LED que estamos controlando con nuestro código!
    media: "src/02-light-signals/b-led-smartphone.svg"

  - title: "El Problema de la Velocidad"
    type: "learn"
    content: |
      Aquí tienes un acertijo: imagina que le dices a tu prototipo que encienda una lámpara **ON**, y luego en la siguiente instrucción, le dices que la apague **OFF**. Esperarías ver un destello rápido, ¿verdad? ¡Pero en realidad no verías nada!
      ¿Por qué? **¡Las máquinas son increíblemente rápidas!** La lámpara se enciende, pero se apaga tan rápidamente que nuestros ojos humanos ni siquiera pueden percibirlo.
    media: "src/02-light-signals/c-no-time.svg"
  
  - title: "¡Las Instrucciones Deben Ser Precisas!"
    type: "learn"
    content: |
      Las computadoras no pueden adivinar lo que queremos. Si nuestras instrucciones son ambiguas, el programa no funcionará como se espera.
      En nuestro acertijo de la luz intermitente, la pieza que faltaba era decirle a la computadora **cuánto tiempo esperar** entre encender y apagar la luz. Esta acción de pausar durante una duración específica se llama **Temporización**.
    media: "src/02-light-signals/d-time.svg"

  - title: "¿Qué significa 'temporización'?"
    type: "learn"
    content: |
      Para hacer que una luz parpadee como una baliza, necesitamos crear una secuencia que incluya **tiempos de espera**, o retardos, entre los comandos ON y OFF.
      En programación, podemos medir el tiempo en diferentes unidades. En Protobject, podemos usar **segundos** o **milisegundos** (1000 milisegundos = 1 segundo) para controlar nuestra temporización perfectamente.
    media: "src/02-light-signals/e-sequence.svg"

  - id: "create"
    title: "Crea una Baliza"
    type: "create"
    icon: "cogs"
    heading_text: "Vamos a crear un prototipo de una baliza."

    steps:
      - "Presiona <addbutton>Añadir dispositivo</addbutton> y selecciona el componente <comp>Lámpara</comp>."
      - "Escanea el código <qr> con tu smartphone."
      - "Si no tienes un smartphone, puedes presionar <openwindow>Abrir en esta ventana</openwindow> para abrir la lámpara en la misma computadora."

  - title: "¿Dónde están los bloques de retardo?"
    type: "create"
    content_class: "text-center text-xl"
    content: |
      Primero, busquemos los bloques que controlan el tiempo. Abre la categoría <category>Temporización</category>.
    media: "src/02-light-signals/f-delay-a.es.svg"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el signo de interrogación para abrir los comentarios que explican el código.
      
      *Recuerda*: los bloques de retardo se encuentran en la categoría <category>Temporización</category>.
    media: "[600]https://app.protobject.com/generate?a02-timing&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Has aprendido a controlar una baliza. ¡Ahora, piensa en grande!"
    content: |
      * ¿En qué otras situaciones del mundo real podrías usar la temporización y los retardos? Piensa en juegos, animaciones o incluso herramientas que usas todos los días.
    right_content:
      - text: |
          **Recuerda:** la programación consiste en crear una secuencia clara de pasos para lograr un objetivo.
          ¡Al agregar retardos, convertiste una simple luz en una baliza funcional!
---