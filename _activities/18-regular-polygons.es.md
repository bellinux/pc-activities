---
layout: activity
title: "Arte Geométrico: Dibujando Polígonos"
image: src/18-regular-polygons/18.poligonos-regulares.svg
video: src/videos/18_regular_polygons.mp4
video_title: "¿Qué haremos?"
description: "Explora el poder de los bucles 'Mientras' para dibujar programáticamente formas geométricas perfectas, desde triángulos hasta hectágonos."
lang: es
permalink: /es/actividades/arte-geometrico-dibujando-poligonos/
ref: activity_regular_polygons

# ACTIVITY INFO
level: 2
computational_topics:
  - "Bucles"
  - "Gráficos y Dibujo"
  - "Variables y Datos"
general_topics:
  - "Matemáticas y Lógica"
  - "Arte y Música"

tags: [Bucles, Bucle While, Dibujo, Plano Cartesiano, Geometría, Variables]

introduction: |
  ¿Por qué dibujar un triángulo a mano cuando puedes programar un programa para dibujar un hectágono de 100 lados en segundos? En esta misión, combinarás geometría y programación para crear un potente generador de polígonos. Aprenderás a usar el **bucle 'Repetir Mientras'** —un bucle que se ejecuta mientras una condición es verdadera— para dibujar cualquier forma geométrica perfecta que puedas imaginar.

teacher: |
  ### **Cursos**
  * Grados 6-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender el concepto de un bucle "while" en programación.
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar el trabajo propio y el de los compañeros.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - El Bucle Condicional**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy aprenderemos a dibujar formas geométricas complejas usando código."**
  2.  Introduce un nuevo tipo de bucle. Pregunta a la clase: **"Hemos visto un bucle que se ejecuta para siempre. Pero, ¿y si queremos un bucle que se ejecute solo *mientras* una cierta condición es verdadera, y luego se detenga?"**
  3.  Explica que esto es lo que hace un bucle "while". Luego, conéctalo a una tarea real: dibujar un polígono. Pregunta: **"¿Cómo dibujaríamos un cuadrado? Dibujamos un lado, giramos 90 grados, dibujamos otro lado... repetimos la acción 'dibuja y gira' *mientras* todavía nos queden lados por dibujar."** Esta es la introducción perfecta a la lógica que construirán.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - El Generador de Polígonos**
  1.  Ahora que los estudiantes comprenden la lógica de usar un bucle 'while' y las matemáticas simples detrás de los polígonos, es hora de construir su generador de formas.
  2.  Guíalos a través de **las instrucciones para crear el programa que dibuja polígonos según la entrada de la perilla**, como se detalla en la sección práctica a continuación. Presta mucha atención a la condición del bucle `while` (p. ej., `while contador < lados`) y cómo se calcula el ángulo de giro.

  ### **Cierre (5-10 minutos) - Codificación Creativa**
  1.  Una vez que todos tengan un generador de polígonos interactivo, es hora de experimentar y jugar el papel de un codificador creativo.
  2.  Usa la sección final para desafiarlos a modificar las variables del programa. Esto los alienta a ver cómo pequeños cambios en el código pueden llevar a grandes cambios en el resultado visual, que es un concepto central en el arte generativo.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "El Bucle 'Repetir Mientras'"
    type: "learn"
    icon: "book-reader"
    content: |
      Un bucle **‘repetir mientras’** es como un guardia persistente. Primero comprueba una condición. **Mientras** esa condición sea verdadera, ejecuta un bloque de código una y otra vez. En el momento en que la condición se vuelve falsa, el bucle se detiene.
      Esto es perfecto para situaciones en las que no se conoce el número exacto de repeticiones de antemano, pero se conoce el objetivo que se está tratando de alcanzar.
    media: "[600]https://app.protobject.com/generate?mientras&es&static&-1"

  - title: "¿Qué es un polígono regular?"
    type: "learn"
    content: |
      Un polígono regular es una forma en la que todos los lados tienen la misma longitud y todos los ángulos interiores son iguales. Conoces los simples: un triángulo equilátero (3 lados), un cuadrado (4 lados), un pentágono (5 lados).
      Pero, ¿qué pasa con un decágono (10 lados) o un icoságono (20 lados)? ¡Dibujarlos a mano sería muy tedioso!
    media: "src/18-regular-polygons/a.polyexample.svg"

  - title: "El Secreto de la Geometría: 360 Grados"
    type: "learn"
    content: |
      Aquí hay un truco de geometría genial: la suma de los ángulos exteriores de *cualquier* polígono regular es siempre **360°**.
      Entonces, para averiguar cuánto necesita girar nuestro "lápiz" en cada esquina, ¡simplemente dividimos 360 por el número de lados!
      - **Triángulo**: 360 / 3 = 120° de giro
      - **Cuadrado**: 360 / 4 = 90° de giro
      - **Pentágono**: 360 / 5 = 72° de giro
    media: "src/18-regular-polygons/b.angleexample.svg"

  - title: "¡Combinemos bucles y geometría!"
    type: "learn"
    content: |
      Observa el patrón repetitivo para dibujar cualquier polígono: **dibuja una línea**, luego **gira**. Repetimos este proceso hasta que hayamos dibujado todos los lados.
      ¡Este es un trabajo perfecto para un bucle `repetir mientras`! Podemos decirle al programa: **MIENTRAS** el número de lados que hemos dibujado sea menor que el número total de lados que queremos, **HAZ** la acción "dibuja y gira".
    media: "src/18-regular-polygons/z-square-anim2.svg"

  - id: "create"
    title: "Crea el Dibujador de Polígonos"
    type: "create"
    icon: "cogs"
    heading_text: "Creemos el prototipo. Necesitaremos un smartphone y una computadora/tableta."
    steps:
      - "Añade el dispositivo <comp>Perilla</comp> para controlar el número de lados."
      - "Añade el dispositivo <comp>DibujarEscribir</comp> abriéndolo en la misma computadora/tableta haciendo clic en <openwindow>Abrir en esta ventana</openwindow>."
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
    media: "[600]https://app.protobject.com/generate?a18-polygons&es&dynamic&-1"

  - id: "reflect"
    title: "Desafío: Modificaciones Creativas de Código"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Ahora que has implementado el generador de polígonos, ¡juguemos con el código!"
    content: |
      * **Mod #1: Control del Perímetro.** ¿Cómo cambiarías el código para hacer el polígono más grande o más pequeño?
      * **Mod #2: Dirección de Giro.** ¿Qué sucede si giras a la derecha en lugar de a la izquierda?
      * **Mod #3: Color Dinámico.** ¿Cómo podemos cambiar el color de las líneas según el número de lados del polígono?
---