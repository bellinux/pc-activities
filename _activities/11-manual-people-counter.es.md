---
layout: activity
title: "Crea un Contador de Personas"
image: src/11-manual-people-counter/11.contador-personas.svg
video: src/videos/11_people_counter.mp4
video_title: "¿Qué haremos?"
description: "Usa eventos y variables para construir una herramienta práctica para contar personas, como en un concierto o una tienda real."
lang: es
permalink: /es/actividades/crea-un-contador-de-personas/
ref: activity_manual_people_counter

# ACTIVITY INFO
level: 1
computational_topics:
  - "Temporización y Eventos"
  - "Variables y Datos"
  - "Condicionales y Lógica"
general_topics:
  - "Matemáticas y Lógica"

tags: [Eventos, Variables, Contador, Entrada de Usuario, Datos]

introduction: |
  ¿Alguna vez has estado en un gran evento o en una tienda concurrida y has visto a alguien en la puerta con un contador, contando a todos los que entran? ¡Construyamos una versión digital de eso! En esta misión, combinarás dos de los conceptos más poderosos de la programación — **eventos** y **variables** — para crear un práctico contador de personas. Prepárate para construir una herramienta real que escuche las entradas y rastree los datos.

teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender los conceptos de "evento" y "datos numéricos".
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar las relaciones entre la tecnología y el mundo que los rodea.
  * Evaluar el trabajo propio y el de los demás.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - La Lógica de un Contador**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy vamos a aprender a prototipar un contador de personas digital."**
  2.  Pregunta a la clase: **"¿Qué es un dispositivo de conteo y dónde han visto uno en uso?"** (ej. tiendas, conciertos, transporte).
  3.  Después de discutir sus usos en el mundo real, explica la lógica detrás de él. Necesitamos un lugar para 'almacenar' el conteo actual y una forma de 'saber' cuándo agregar una persona más. Este es el escenario perfecto para mostrar cómo las **variables** (para almacenar datos) y los **eventos** (para activar acciones) trabajan juntos para crear una herramienta útil.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construcción del Dispositivo**
  1.  Ahora que los estudiantes comprenden la lógica de usar una variable como contador y un evento como disparador, es hora de construir el dispositivo.
  2.  Guíalos a través de **las instrucciones para crear la interfaz de usuario y programar la lógica de conteo**, como se detalla en la sección práctica a continuación. Este proyecto es una fantástica aplicación del mundo real de los conceptos que han aprendido.

  ### **Cierre (5-10 minutos) - Reflexión y Mejoras**
  1.  Una vez que todos tengan un contador que funcione, es hora de un ejercicio de pensamiento crítico. ¿Es un evento la *única* forma de construir esto? ¿Y cómo podemos hacerlo aún más útil?
  2.  Usa las secciones finales para guiar una discusión que compare la eficiencia de los eventos frente a los bucles, y luego desafíalos a mejorar su contador con una nueva característica importante: la resta.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Qué es un dispositivo de conteo?"
    type: "learn"
    icon: "book-reader"
    content: |
      Un dispositivo de conteo, o "clicker", es una herramienta simple que se usa para **llevar la cuenta de una cantidad**. Podría usarse para contar productos en un almacén, vueltas en una carrera o, en nuestro caso, personas que ingresan a un lugar.
      Cada vez que alguien entra, **presionas un botón** y el **contador en la pantalla aumenta en uno**. Es una forma simple y efectiva de llevar una cuenta precisa.
    media: "src/11-manual-people-counter/a.lcd-counter.svg"

  - title: "¿Cuál es el propósito de un contador de personas?"
    type: "learn"
    content: |
      Los contadores de personas son sorprendentemente útiles en muchas situaciones. Las tiendas los usan para rastrear el flujo de clientes, los organizadores de eventos los usan para controlar la capacidad del lugar por seguridad, y el transporte público puede usar los datos para mejorar el servicio. Es una herramienta simple que ayuda a que los sistemas sean más seguros y eficientes.
    media:
      - "src/11-manual-people-counter/b.shop_.example.svg"
      - "src/11-manual-people-counter/b.event_.example.svg"
      - "src/11-manual-people-counter/b.bus_.example.svg"

  - title: "Usamos una variable para llevar la cuenta"
    type: "learn"
    content: |
      ¿Recuerdas las **variables**? Son como cajas etiquetadas para almacenar información. Para nuestro contador de personas, una variable es la herramienta perfecta para actuar como nuestro marcador digital. Crearemos una variable para almacenar el conteo actual y podremos actualizar el valor dentro de ella cada vez que entre una nueva persona.
    media: "src/11-manual-people-counter/c.variable-use.es.svg"

  - title: "¿Y cómo sabemos cuándo contar?"
    type: "learn"
    content: |
      ¿Cómo sabemos *cuándo* actualizar nuestra variable? ¡Usamos un **evento**!
      En lugar de preguntar constantemente "¿Está presionado el botón?", el programa simplemente escucha. Cuando presionas el botón, envía una señal — un evento — a nuestro código. Ese evento es el disparador que le dice a nuestro programa: '¡Ok, es hora de sumar 1 a la variable del contador!' Es una forma eficiente e inteligente de programar.
    media: "src/11-manual-people-counter/evento-icon.es.it.svg"

  - id: "create"
    title: "Construyamos el contador"
    type: "create"
    icon: "cogs"
    heading_text: "Vamos a crear un prototipo que nos permita contar las personas que entran a un lugar."
    content: |
      Primero, necesitamos agregar dos componentes: uno para (1) mostrar el número de personas y un segundo para (2) actuar como nuestro botón de "agregar".
    steps:
      - "Presiona <addbutton>Añadir dispositivo</addbutton> y selecciona <comp>DibujarEscribir</comp>, el dispositivo donde mostraremos el número."
      - "Presiona de nuevo <addbutton>Añadir dispositivo</addbutton> y selecciona <comp>BotónTactil</comp> para crear el botón."
      - "Recuerda que si no tienes un smartphone, puedes presionar <openwindow>Abrir en esta ventana</openwindow>."
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
    media: "[700]https://app.protobject.com/generate?a11-peoplecounter&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "¿Y si usáramos un bucle principal en lugar de un evento?"
    content: |
      Construiste este contador usando un evento, que es súper eficiente. Pero, ¿podrías construirlo con un bucle principal? Echa un vistazo al código a continuación. ¿Cuál es la principal diferencia? ¿Qué crees que pasaría si mantuvieras presionado el botón en la versión del bucle en comparación con la versión del evento?
    media: "[450]https://app.protobject.com/generate?contarpersonaswhile&es&dynamic&-1"

  - title: "Desafío"
    icon: "trophy"
    type: "reflect"
    heading_text: "Tu contador solo puede subir. Pero, ¿qué pasa si la gente se va?"
    content: |
      ¡Un contador real necesita una forma de restar! Tu desafío es agregar un segundo botón a tu prototipo que **disminuya** el conteo en uno cada vez que se presione.
    media: "src/videos/counter_challenge.mp4"
    right_content:
      - text: |
          **Pista:** Necesitarás agregar un segundo componente <comp>BotónTactil</comp>. ¿Cómo programarías un *segundo* evento para manejar la resta?
---