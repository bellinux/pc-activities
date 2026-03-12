---
layout: activity
title: "El Nivel de Burbuja: ¿Está Recto?"
image: src/15-tilt-sensor/15.sensor-inclinacion.svg
video: src/videos/15_tilt_sensor.mp4
video_title: "¿Qué haremos?"
description: "Usa el sensor de inclinación de tu teléfono y condicionales avanzados ('Sino Si') para construir una herramienta que te diga si algo está perfectamente nivelado."
lang: es
permalink: /es/actividades/el-nivel-de-burbuja-esta-recto/
ref: activity_tilt_sensor

# ACTIVITY INFO
level: 1
computational_topics:
  - "Condicionales y Lógica"
  - "Sensores e Input"
  - "Bucles"
general_topics:
  - "Ciencia y Tecnología"

tags: [Condicionales, Sino Si, Multi-Condición, Sensor de Inclinación, Acelerómetro, Bucle Principal]

introduction: |
  Nuestros programas ya pueden tomar decisiones simples: SI esto, ENTONCES aquello, SINO haz otra cosa. ¡Pero la vida suele ser más complicada que solo dos opciones! En esta misión, aprenderás a manejar múltiples condiciones usando el poderoso comando **'SINO SI'**. Prepárate para usar el **acelerómetro** de tu teléfono para construir un nivel de burbuja digital que cambia de color según cuánto se incline.

teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender los conceptos de “sino si” (elif) y el “plano cartesiano”.
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar el trabajo propio y el de los demás en tareas individuales o en equipo.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - Decisiones con Múltiples Caminos**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy aprenderemos a prototipar un detector de inclinación digital, como el nivel de burbuja de un carpintero."**
  2.  Comienza repasando brevemente el condicional 'SI/SINO' para dos opciones (como ENCENDIDO/APAGADO). Luego, introduce un problema más complejo: **"Un bloque SI/SINO es genial para dos opciones. Pero, ¿y si tienes *cuatro* opciones? Por ejemplo, quieres un programa que sugiera una comida según la hora del día."**
  3.  Usa esta analogía para mostrar por qué necesitamos más que un simple 'SINO'. Esta es la configuración perfecta para introducir la estructura **'SINO SI'** como una forma de encadenar múltiples verificaciones para tomar decisiones más complesas.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo el Nivel de Burbuja**
  1.  Ahora que los estudiantes comprenden cómo construir una decisión de múltiples caminos con 'SINO SI', es hora de aplicar esa lógica a un sensor real.
  2.  Guíalos a través de **las instrucciones para construir el nivel de burbuja y programar la lógica multi-condicional**, como se detalla en la sección práctica a continuación. Asegúrate de que entiendan cómo cada bloque 'SINO SI' verifica un rango diferente de valores de inclinación, creando las diferentes advertencias de color.

  ### **Cierre (5-10 minutos) - Reflexión sobre Sensores y Lógica**
  1.  Una vez que el nivel de burbuja de todos cambie de color correctamente, es hora de reflexionar sobre el sensor y la poderosa lógica que han utilizado.
  2.  Usa la sección final para guiar una discusión sobre las otras capacidades del acelerómetro y para desafiarlos a crear un nuevo prototipo que combine inclinación y sonido.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Más de Dos Opciones?"
    type: "learn"
    icon: "book-reader"
    content: |
      Has visto cómo los condicionales pueden funcionar con dos opciones: **SI** una condición es verdadera, haz algo, **SINO** haz algo diferente. Esto es perfecto para un simple interruptor de encendido/apagado.
      Pero, ¿y si necesitas verificar múltiples condiciones diferentes?
    media: "src/15-tilt-sensor/a-ifsimple.es.svg"

  - title: "Introduciendo 'Sino Si'"
    type: "learn"
    content: |
      La estructura **“sino si”** te permite encadenar múltiples verificaciones en un solo bloque ordenado. Puedes pensar en ello como un árbitro en un partido de fútbol:
      * **SI** la falta es muy grave, **ENTONCES** muestra una tarjeta roja.
      * **SINO SI** la falta es solo una advertencia, **ENTONCES** muestra una tarjeta amarilla.
      * **SINO** (si ninguna de las anteriores es verdadera), **ENTONCES** es solo una falta simple.
      El programa verifica cada condición en orden hasta que encuentra una que es verdadera.
    media: "src/15-tilt-sensor/multiple-if.es.svg"

  - title: "SINO SI: 4 Opciones para nuestro Nivel de Burbuja"
    type: "learn"
    content: |
      Usaremos esta lógica de múltiples caminos para programar un detector de inclinación que nos ayude a colgar cuadros perfectamente rectos.
      La pantalla se iluminará con diferentes colores según el valor de inclinación: verde para nivelado, amarillo para ligeramente desviado, naranja para más inclinado y rojo para muy inclinado.
    media: "src/15-tilt-sensor/y-multiple-inclination.svg"
  
  - title: "¿Cómo detecta el teléfono la inclinación?"
    type: "learn"
    content: |
      Para detectar la inclinación de un teléfono, usamos un pequeño sensor incorporado llamado **acelerómetro**. Este sensor puede medir fuerzas como la gravedad, indicando al teléfono su orientación en el espacio. Mide la inclinación en tres ejes diferentes: X (izquierda-derecha), Y (adelante-atrás) y Z (arriba-abajo). Esto permite que el teléfono sepa si está inclinado hacia un lado, en posición vertical o acostado.
    media: "src/15-tilt-sensor/z-accelerometer.svg"

  - id: "create"
    title: "Crea el Sensor de Inclinación"
    type: "create"
    icon: "cogs"
    heading_text: "Creemos un prototipo que nos ayude a detectar si un cuadro está inclinado."
    content: |
      Primero, agregaremos dos componentes: uno para detectar la inclinación del teléfono y otro para mostrar la luz de color.
    steps:
      - "Haz clic en <addbutton>Añadir dispositivo</addbutton> y selecciona <comp>Inclinación</comp>."
      - "Haz clic de nuevo en <addbutton>Añadir dispositivo</addbutton> y selecciona <comp>Lámpara</comp>."
      - "**Añade ambos dispositivos al mismo smartphone para este proyecto.**"
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
      El bloque "absoluto" (que hace que un número sea positivo) se encuentra en la categoría <category>Matemáticas</category>, dentro del menú desplegable del bloque "raíz cuadrada".
    media: "[700]https://app.protobject.com/generate?a15-inclination&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "¡Has construido un programa que puede tomar decisiones complejas!"
    content: |
      Esta cadena 'SI / SINO SI / SINO' es una herramienta súper poderosa.
      * Nuestro nivel de burbuja usó el eje Y (inclinación hacia adelante y hacia atrás). ¿Qué crees que pasaría si cambiaras el código para leer el eje X (inclinación de izquierda a derecha) en su lugar?
      * ¿Qué otra herramienta o juego del mundo real podrías construir usando el sensor de inclinación de tu teléfono?
    right_content:
      - text: |
          **Desafío**: Crea un reproductor de música donde puedas ajustar el volumen inclinando tu smartphone hacia arriba y hacia abajo.
      - text: |
          **Pista**: Necesitarás el componente <comp>ReproductorSonido</comp>. Dentro de tu bucle principal, puedes establecer el volumen según el valor que obtengas del sensor de inclinación.
---