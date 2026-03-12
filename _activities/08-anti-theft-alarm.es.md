---
layout: activity
title: "La Alarma Antirrobo"
image: src/08-anti-theft-alarm/08.alarma-antirobo.svg
video: src/videos/08_alarm.mp4
video_title: "¿Qué haremos?"
description: "¡Haz que tu código sea inteligente! Usa condicionales ('Si-Entonces') para tomar decisiones y construir una alarma que reaccione al movimiento."
lang: es
permalink: /es/actividades/la-alarma-antirrobo/
ref: activity_anti_theft_alarm

# ACTIVITY INFO
level: 1
computational_topics:
  - "Condicionales y Lógica"
  - "Bucles"
  - "Sensores e Input"
general_topics:
  - "Vida Cotidiana"

tags: [Condicionales, Si-Entonces, Bucle Principal, Sensores, Sensor de Movimiento, Cámara]

introduction: |
  ¡Enseñemos a nuestros programas a ver y reaccionar al mundo! Esta misión te introduce al poder de los **sensores** y la **lógica condicional**. Aprenderás a usar un comando simple pero poderoso 'SI sucede esto, ENTONCES haz aquello' para construir una alarma antirrobo inteligente que se activa cuando detecta movimiento. ¡Prepárate para crear tu primer sistema inteligente!

teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender el concepto de condicionales "SI-ENTONCES".
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar el trabajo personal y el de los demás.
  * Participar en discusiones y reflexionar sobre ideas de mejora.

  ### **Inicio (10 minutos) - La Lógica de una Alarma**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy aprenderemos a prototipar una alarma que detecta movimiento."**
  2.  Pregunta a la clase: **"¿Alguna vez han visto una puerta automática o una luz de seguridad? ¿Cómo creen que saben que están ahí?"**
  3.  Después de discutir sus ideas sobre los sensores, explica que usaremos la cámara de su teléfono como un sensor de movimiento. Pero, ¿cómo *decide* un programa cuándo hacer sonar la alarma? Este es el momento perfecto para introducir la **lógica condicional**—la declaración 'SI/ENTONCES'.
  4.  Finalmente, explica que el programa necesita verificar el movimiento constantemente, no solo una vez, lo que requiere un **Bucle Principal** para ejecutar la verificación una y otra vez.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo el Sistema de Seguridad**
  1.  Ahora que entienden la lógica de "SI se detecta movimiento, ENTONCES hacer sonar la alarma", es hora de construir el sistema de seguridad.
  2.  Guía a los estudiantes a través de **las instrucciones para agregar los componentes y construir el código condicional**, como se detalla en la sección práctica a continuación. Asegúrate de que entiendan por qué el bloque SI debe colocarse dentro del bucle principal para ser efectivo.

  ### **Cierre (5-10 minutos) - Informe de Seguridad**
  1.  Una vez que las alarmas funcionen, es hora de un informe de experto en seguridad. Un verdadero experto en seguridad siempre piensa en las debilidades de su sistema.
  2.  Usa la sección final para guiar una discusión sobre las limitaciones de su alarma basada en cámara. Esto los alienta a pensar críticamente sobre cómo funciona la tecnología en el mundo real y cómo podría mejorarse.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Has oído hablar de los sensores de movimiento?"
    type: "learn"
    icon: "book-reader"
    content: |
      Los sensores de movimiento son dispositivos inteligentes que pueden detectar cuándo alguien o algo se mueve cerca de ellos.
      
      Algunos, como los de las puertas automáticas, funcionan con **infrarrojos** (un tipo de luz que no podemos ver) o **ultrasonidos** (un sonido que no podemos oír). Detectan cambios cuando sus señales rebotan en un objeto en movimiento.
    media: "src/08-anti-theft-alarm/a-movement-sensor.svg"

  - title: "Usando una Cámara como Sensor de Movimiento"
    type: "learn"
    content: |
      También existen sensores de movimiento **basados en cámaras**, que es lo que usaremos en esta actividad.
      Un programa puede observar el video de una cámara y detectar **cambios entre fotogramas**. Si una gran parte de la imagen cambia de repente, el programa sabe que **algo se está moviendo**.
    media: "src/08-anti-theft-alarm/a-smartphone-camera.svg"

  - title: "SI hay movimiento, ENTONCES sonar la alarma"
    type: "learn"
    content: |
      Para que nuestro programa sea inteligente, necesitamos enseñarle a tomar decisiones. La forma más sencilla de hacerlo es сon una declaración condicional: **SI una condición es verdadera, ENTONCES ocurre una acción.**
      Esta estructura "SI... ENTONCES..." es un bloque de construcción fundamental de toda la programación, desde juegos simples hasta inteligencia artificial compleja.
    media: "src/08-anti-theft-alarm/a-simple-condition.es.svg"
  
  - title: "Un Ejemplo Práctico"
    type: "learn"
    content: |
      Veamos cómo usar un condicional para activar nuestra alarma.
      Le diremos al programa: **SI** la cantidad de movimiento detectada por la cámara es mayor que un cierto número (como 40), **ENTONCES** reproduce el sonido de la alarma.
      Pero, ¿cómo hacemos que el programa verifique el movimiento *continuamente*? ¡No podemos verificar solo una vez! Aquí es donde un **bucle principal** es esencial. Al colocar nuestra verificación 'SI movimiento' dentro de un bucle 'repetir para siempre', creamos un sistema que siempre está vigilando.
    media: "src/08-anti-theft-alarm/a-mov-condition.es.svg"

  - id: "create"
    title: "¡Creemos nuestra alarma antirrobo!"
    type: "create"
    icon: "cogs"
    heading_text: "Construyamos el prototipo para nuestra alarma."
    content: |
      Primero, necesitamos agregar dos componentes: uno para (1) detectar movimiento y otro para (2) reproducir el sonido de la alarma.
    steps:
      - "Agrega el componente <comp>MovimientosCámara</comp> que detecta movimiento a través de la cámara del teléfono."
      - "Agrega el componente <comp>ReproductorSonido</comp> para reproducir el sonido de una alarma."
      - "Recuerda que si no tienes un smartphone para escanear los códigos <qr>, puedes hacer clic en <openwindow>Abrir en esta ventana</openwindow>."
    right_content:
      - text: |
          **Sugerencia**: En Protobject, puedes agregar más componentes en el mismo smartphone presionando el botón SCAN tantas veces como necesites.
      - media: "src/general-scan-button.svg"
    ready_message: "¡Estamos listos para empezar a prototipar!"


  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
      Los bloques condicionales se encuentran en la categoría <category>Lógica</category>.
    media: "[700]https://app.protobject.com/generate?a08-alarm&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Has construido un sistema de seguridad. Ahora, piensa como un experto en seguridad."
    content: |
      * ¿Qué pasaría si un ladrón entrara de noche con todas las luces apagadas? ¿Funcionaría todavía un sensor basado en cámara?
      * ¿Qué tan confiable es esta alarma? ¿Qué podría activar accidentalmente una falsa alarma (como una mascota corriendo)?
    right_content:
      - text: |
          **Pista:** Pensar en las debilidades de un sistema es el primer paso para hacerlo más fuerte. ¡Nuestro sensor depende de la luz y las imágenes para funcionar!
---