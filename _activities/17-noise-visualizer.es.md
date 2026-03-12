---
layout: activity
title: "El Medidor de Ruido"
image: src/17-noise-visualizer/17.visualizador-ruido.svg
video: src/videos/17_noise_visualizer.mp4
video_title: "¿Qué haremos?"
description: "Aprende los conceptos básicos de dibujar en un lienzo digital creando una línea que crece y se encoge con el volumen del ruido circundante."
lang: es
permalink: /es/actividades/el-medidor-de-ruido/
ref: activity_noise_visualizer

# ACTIVITY INFO
level: 2
computational_topics:
  - "Gráficos y Dibujo"
  - "Sensores e Input"
  - "Bucles"
general_topics:
  - "Matemáticas y Lógica"
  - "Arte y Música"

tags: [Plano Cartesiano, Dibujo, Coordenadas, Sensor de Ruido, Bucle Principal, Visualización de Datos]

introduction: |
  ¿Cómo puedes convertir el sonido en una imagen? En esta misión de Nivel 2, ¡nos sumergiremos en el mundo de los gráficos digitales! Aprenderás cómo los programadores usan el **Plano Cartesiano** (coordenadas X e Y) para dibujar formas y líneas en una pantalla. Prepárate para construir un visualizador de ruido en tiempo real que utiliza la entrada de tu micrófono para controlar una pantalla gráfica dinámica.
  
teacher: |
  ### **Cursos**
  * Grados 6-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender los conceptos del plano cartesiano y el dibujo en pantalla.
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar las relaciones entre la tecnología y el mundo circundante.
  * Evaluar su propio trabajo y el de los demás.
  * Participar en diálogos y reflexionar sobre ideas de mejora.

  ### **Inicio (10 minutos) - El Lienzo es un Mapa**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy aprenderemos a prototipar un visualizador de ruido, convirtiendo el sonido en gráficos."**
  2.  Inicia la lección con una pregunta que se conecte con sus clases de matemáticas: **"¿Alguna vez han oído hablar del plano cartesiano en matemáticas? ¿Para qué se usa?"**
  3.  Conecta sus respuestas con el mundo de la programación. Explica que cada pantalla, desde su teléfono hasta un videojuego, es una cuadrícula. Los programadores usan coordenadas X e Y para colocar cada elemento visual. Hoy, se convertirán en artistas digitales, usando este sistema para dibujar una línea cuya longitud es controlada por el sonido.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Dibujando con Datos**
  1.  Ahora que los estudiantes comprenden los fundamentos de dibujar en un plano de coordenadas, es hora de construir su visualizador de sonidos.
  2.  Guíalos a través de **las instrucciones para crear el lienzo de dibujo y programar la lógica de visualización**, como se detalla en la sección práctica a continuación. Presta mucha atención al bloque `dibuja línea` y cómo el nivel de ruido del sensor se utiliza para determinar la longitud de la línea en tiempo real.

  ### **Cierre (5-10 minutos) - El Artista Digitale**
  1.  Una vez que todos tengan un visualizador que funcione y reaccione a su voz, es hora de riflettere sui nuovi poteri grafici che hanno sbloccato.
  2.  Usa la sección final para desafiar su comprensión del sistema de coordenadas y para introducir un desafío de visualización más complejo que involucre formas y texto.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Qué es el Plano Cartesiano?"
    type: "learn"
    icon: "book-reader"
    content: |
      Piensa en una pantalla no como una superficie plana, sino como una hoja de papel cuadriculado. Para decirle a la computadora dónde dibujar algo, necesitas darle una "dirección", como una ubicación en un mapa. Este mapa se llama **Plano Cartesiano**. Es un sistema de coordenadas compuesto por dos ejes perpendiculares: la línea horizontal se llama **eje X**, y la línea vertical se llama **eje Y**. El punto donde se encuentran es el "origen" (0,0).
    media: "src/17-noise-visualizer/a-cartesian.svg"

  - title: "¿Cómo funcionan los ejes X e Y?"
    type: "learn"
    content: |
      El **eje X** (horizontal) funciona como una recta numérica: los números más pequeños están a la izquierda y los números más grandes a la derecha. El **eje Y** (vertical) coloca los números más pequeños en la parte inferior y los más grandes en la parte superior. Al combinar un valor X y un valor Y, podemos definir la ubicación precisa de cualquier punto en la pantalla.
    media: 
      - "src/17-noise-visualizer/b-cartesianx.svg"
      - "src/17-noise-visualizer/c-cartesiany.svg"

  - title: "El Primer Cuadrante"
    type: "learn"
    content: |
      El plano cartesiano se divide en cuatro cuadrantes. En Protobject, para simplificar las cosas, usamos principalmente el **primer cuadrante**, donde tanto los valores X como los Y son números positivos. El punto de origen (0,0) corresponde a la esquina inferior izquierda de nuestro lienzo de dibujo.
    media: "src/17-noise-visualizer/d-quadrants.svg"

  - title: "Cómo Dibujar una Línea"
    type: "learn"
    content: |
      Para dibujar una línea, solo necesitas darle a la computadora tres instrucciones: un punto de partida (una coordenada X, Y), la dirección en la que viajar (un ángulo) y qué tan lejos ir (una longitud).
      Para una barra vertical, comenzaremos en la parte inferior de la pantalla, apuntaremos hacia arriba (un ángulo de 90 grados) y haremos que la longitud cambie según el nivel de ruido.
    media: "src/17-noise-visualizer/f-drawlin.svg"

  - title: "¿Por qué visualizar el ruido?"
    type: "learn"
    content: |
      Visualizar la intensidad del sonido no es solo por diversión; ¡es útil! En entornos ruidosos como fábricas, un medidor de ruido puede ayudar a proteger la audición de los trabajadores. En un aula o una biblioteca, puede ser una excelente señal visual para ayudar a todos a ser más conscientes de los niveles de ruido, creando un mejor ambiente para aprender y concentrarse.
    media: 
      - "src/17-noise-visualizer/g-mechanical.svg"
      - "src/17-noise-visualizer/h-classrooml.svg"

  - id: "create"
    title: "Crea el Visualizador de Ruido"
    type: "create"
    icon: "cogs"
    heading_text: "Creemos el prototipo que visualiza el nivel de ruido en tiempo real."
    content: |
      Primero, necesitamos agregar dos componentes: uno para (1) detectar el ruido con el micrófono y otro para (2) actuar como nuestro lienzo de dibujo.
    steps:
      - "Presiona <addbutton>Añadir Dispositivo</addbutton>, selecciona <comp>NivelRuido</comp> y escanea el código <qr> con tu smartphone."
      - "Haz clic en <addbutton>Añadir Dispositivo</addbutton>, selecciona <comp>DibujarEscribir</comp> y presiona <openwindow>Abrir en esta ventana</openwindow> para generar una superficie de dibujo en la computadora."
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código. ¡Nota que tenemos que limpiar la pantalla en cada ciclo del bucle para borrar la línea vieja antes de dibujar la nueva!
    media: "[600]https://app.protobject.com/generate?a17-noisevisualizer&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "¡Acabas de dibujar con datos! Ahora, seamos creativos."
    content: |
      * Nuestro código dibuja una línea vertical. ¿Cómo cambiarías los parámetros del bloque "dibuja línea" para que en su lugar sea una línea **horizontal**?
      * Además de una línea, ¿de qué otras formas podrías visualizar el ruido? ¿Un círculo que crece? ¿Un color que cambia de verde a rojo?
    right_content:
      - text: |
          **Desafío**: Creemos un visualizador de ruido para un aula. Queremos que muestre un círculo que crece a medida que aumenta el nivel de ruido. Además, si el nivel de ruido es demasiado alto (supera un valor específico), debería mostrar la palabra **¡SILENCIO!** en la pantalla.
      - text: |
          **Pista**: Puedes usar el bloque "dibuja un punto en" para dibujar el círculo y establecer su tamaño según el nivel de ruido. Necesitarás un condicional (bloque SI) para verificar el nivel de ruido y decidir cuándo escribir el texto.
    media: "src/videos/silent_challenge.mp4"
---