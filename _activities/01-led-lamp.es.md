---
layout: activity
title: "Enciende una Lámpara LED"
image: src/01-led-lamp/01.lampara-led.svg
video: src/videos/01_led_lamp.mp4
video_title: "¿Qué haremos?"
description: "Da tus primeros pasos en el mundo de la codificación aprendiendo la magia de la programación por bloques."
lang: es
permalink: /es/actividades/enciende-una-lampara-led/
ref: activity_led_lamp

# ACTIVITY INFO
level: 1
computational_topics:
  - "Fundamentos de Programación"
general_topics:
  - "Ciencia y Tecnología"

tags: [Programación por Bloques, Primera Actividad, Lámpara LED, Comandos Básicos]

introduction: |
  ¿Alguna vez te has preguntado cómo funcionan tus juegos o aplicaciones favoritas? Todo comienza con una sola instrucción. Prepárate para enviar tu primer comando y dar vida a una lámpara LED virtual. En esta misión, descubrirás la magia de la **programación** aprendiendo a decirle a un dispositivo exactamente qué hacer, usando **bloques** visuales y sencillos.
  
teacher: |
  ### **Cursos**
  * Grados 3-12
  
  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet
  
  ### **Descripción**
  En esta actividad, los estudiantes pueden experimentar de manera introductoria con Protobject, aprendiendo sobre programación visual e informática de forma segura y lúdica utilizando un dispositivo.
  
  ### **Objetivos Educativos**
  * Comprender los conceptos de "programación por bloques" y "prototipo".
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar su propio trabajo y el de los demás, tanto individualmente como en equipo.
  * Participar en diálogos y reflexiones para proponer mejoras.
  
  ### **Inicio (10 minutos) - Encendiendo la Idea**
  1.  Da la bienvenida a la clase y presenta la actividad: **"Hoy vamos a aprender a prototipar con Protobject y a encender nuestra primera lámpara LED."**
  2.  Despierta su curiosidad con una pregunta: **"¿Saben qué es la programación?"**
  3.  Después de una breve discusión para recoger sus ideas, es el momento perfecto para introducir los conceptos básicos. Explica que la programación es simplemente una forma de dar instrucciones súper específicas a una computadora, y que usaremos bloques visuales divertidos en lugar de texto complicado. Exploremos estas ideas juntos.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo el Prototipo**
  1.  Ahora que los conceptos clave están claros, ¡es hora de ponerse manos a la obra y dar vida a esa lámpara! Prepara a los estudiantes para la fase práctica.
  2.  Asegúrate de que cada estudiante tenga un dispositivo listo y guíalos a través del **proceso paso a paso para crear su primer prototipo**, como se detalla a continuación.
  3.  **Nota para el profesor:** Experimenta con la actividad antes de la clase para anticipar cualquier pregunta.

  ### **Cierre (5-10 minutos) - Reflexión y Desafío Final**
  1.  ¡Fantástico trabajo! Una vez que los estudiantes hayan encendido sus lámparas con éxito, es hora de despertar aún más su curiosidad y reflexionar sobre lo que acaba de suceder.
  2.  Inicia la discusión con una simple pregunta: **"¡Buen trabajo! La han encendido, pero ¿cómo la apagarían?"** Déjalos experimentar con el bloque **APAGAR**. Este es un gran momento para explicar por qué no parece funcionar (debido a la velocidad de ejecución de la computadora) y para preparar el escenario para la próxima aventura con la temporización. Usa las siguientes indicaciones para guiar la conversación.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Qué es la Programación?"
    type: "learn"
    icon: "book-reader"
    content: |
      La programación consiste en dar a una computadora un conjunto de instrucciones específicas para completar una tarea. De esta manera, la computadora sabe exactamente qué hacer siguiendo los pasos que estableciste.
      Los programadores usan un lenguaje especial que las computadoras pueden entender. A esto lo llamamos **lenguaje de programación**, y puede ser basado en texto o en bloques.
    media: "src/01-led-lamp/a-programming.svg"

  - title: "Texto vs. Bloques: Dos Formas de Programar"
    type: "learn"
    content: 
      - |
        La **programación textual** es como escribir una receta desde cero, usando lenguajes como Python, Java o C++. Puede ser complicado para los principiantes.
      - |
        La **programación por bloques**, por otro lado, es como construir con ladrillos de LEGO®. Cada bloque es una pieza de código pre-hecha que simplemente puedes arrastrar y encajar con otras, sin necesidad de escribir.
        ¡Este es exactamente el tipo de programación que usamos en Protobject!
    media: ["src/01-led-lamp/b-text-programming.svg","src/01-led-lamp/c-block-programming.svg"]

  - title: "¡Bienvenido a Protobject!"
    type: "learn"
    content: |
      Protobject te permite programar tu smartphone y hacer que interactúe con el mundo que te rodea.
      ¿Cómo? ¡Es simple! Conectas un dispositivo, construyes tu código arrastrando bloques al espacio de trabajo y luego activas tu prototipo.
    media: "src/01-led-lamp/d-introb-protobject.es.svg"

  - title: "Activa Tu Prototipo"
    type: "learn"
    content: |
      Cuando tus bloques de código estén listos, puedes dar vida a tu prototipo presionando el **botón rojo**.
      ¡Estamos listos para empezar a experimentar! Sigue las instrucciones a continuación y crea tu primer invento.
    media: "src/01-led-lamp/e-intro2b-protobject.es.svg"

  - id: "create"
    title: "Crear"
    type: "create"
    icon: "cogs"
    heading_text: "Hagamos una lámpara en nuestro smartphone y encendámosla con Protobject."
    ready_message: "Ahora estamos listos para escribir el código."
    steps:
      - "Presiona <addbutton>Añadir dispositivo</addbutton> y selecciona el componente <comp>Lámpara</comp>."
      - "Escanea el código <qr> con tu smartphone."
      - "Recuerda que si no tienes un smartphone para escanear los códigos **QR**, puedes presionar <openwindow>Abrir en esta ventana</openwindow> para abrir los componentes en la misma computadora."

  - title: "Arrastra el bloque ENCENDER"
    type: "create"
    content: |
      ¡Genial! ¡Encendamos nuestra lámpara LED!
      
      Cada bloque representa una **acción**. Empezaremos usando solo un bloque que nos permitirá **encender nuestra lámpara LED**.
      
      Para ello, **arrastra el bloque ENCENDER** al espacio de trabajo.
    content_class: "space-y-2"
    media: "src/01-led-lamp/f-intro3b-protobject.es.svg"

  - title: "¡Ahora activa el prototipo!"
    type: "create"
    content: |
      ¡Tu **lámpara LED** debería **encenderse**!
    content_class: "text-center text-xl"
    media: "src/01-led-lamp/g-intro4c-protobject.es.svg"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    content: 
      - |
        Has dominado el encendido de la lámpara. ¿Cuál es el siguiente paso lógico? ¿Cómo la apagarías?
      - |
        ¿Has intentado añadir el bloque **APAGAR** justo después del primero?
      
    media: ["src/01-led-lamp/h-light-on-to-off.svg", "https://app.protobject.com/generate?encenderApagar&es&static&-1"]
    right_content:
      - text: |
          **Piensa**: ¿Has considerado la **velocidad** a la que una computadora sigue las instrucciones? ¡Es tan increíblemente rápida que la lámpara se enciende y se apaga antes de que tus ojos puedan siquiera notarlo! Para controlar cosas como esta, necesitaremos aprender a manejar el tiempo.

    
---