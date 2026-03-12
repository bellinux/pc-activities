---
layout: activity
title: "Una Advertencia Intermitente"
image: src/06-traffic-light-with-flashing-yellow-light/06.semaforo-luz-intermitente.svg
video: src/videos/06_intermittent_traffic_light.mp4
video_title: "¿Qué haremos?"
description: "Profundiza en la automatización anidando bucles para crear un semáforo con luz amarilla intermitente realista."
lang: es
permalink: /es/actividades/una-advertencia-intermitente/
ref: activity_traffic_light_with_flashing_yellow_light

# ACTIVITY INFO
level: 1
computational_topics:
  - "Bucles"
  - "Temporización y Eventos"
general_topics:
  - "Vida Cotidiana"

tags: [Bucles Anidados, Bucle Principal, Automatización, Secuencia Intermitente, Temporización]

introduction: |
  ¿Listo para hacer tus automatizaciones aún más inteligentes? Los semáforos del mundo real no solo cambian de color, a menudo dan una advertencia con una luz amarilla intermitente. Para codificar este efecto sin crear un desorden, aprenderás una técnica avanzada: los **bucles anidados**. Prepárate para colocar un bucle *dentro* de otro bucle para construir programas más complejos y potentes.

teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender el concepto de "bucle", tanto general como anidado.
  * Desarrollar un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el entorno circundante.
  * Evaluar el trabajo propio y el de los demás, tanto individualmente como en equipo.
  * Participar en diálogos y reflexiones para proponer mejoras.

  ### **Inicio (10 minutos) - El Desafío del Parpadeo**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy vamos a aprender a crear un semáforo más avanzado y realista."**
  2.  Pide a la clase que piense en los semáforos del mundo real: **"¿Qué hace a menudo la luz amarilla justo antes de ponerse roja para llamar su atención?"** Guíalos hacia la idea de una advertencia intermitente.
  3.  Plantea el desafío de programación: **"¿Cómo codificaríamos eso? Podríamos copiar y pegar los bloques de ENCENDIDO/APAGADO para la luz amarilla, ¡pero nuestro código se volvería largo y desordenado muy rápido!"** Esto introduce el problema de la repetición.
  4.  Explica que para resolver este problema de manera eficiente, necesitamos un nuevo tipo de bucle, uno que pueda ejecutarse un número específico de veces *dentro* de nuestro bucle principal "para siempre". Esta es la introducción perfecta al concepto de bucles anidados.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo con Bucles Anidados**
  1.  Ahora que han comprendido el concepto de anidar un bucle dentro de otro, es hora de construir el semáforo avanzado.
  2.  Guíalos a través de **las instrucciones para modificar la secuencia del semáforo**, mostrándoles exactamente dónde agregar el nuevo bucle numerado para crear el efecto de parpadeo amarillo. Esta será su primera vez creando un bucle dentro de un bucle.

  ### **Cierre (5-10 minutos) - Viendo Bucles por Todas Partes**
  1.  Una vez que todos tengan un semáforo que funcione y parpadee, amplía la discusión para pensar en dónde más se aplica este poderoso concepto.
  2.  Usa la sección final para iniciar una discusión creativa sobre los bucles en la vida cotidiana y para desafiarlos con una simulación de tráfico aún más compleja.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Cómo podemos programar una luz intermitente?"
    type: "learn"
    icon: "book-reader"
    content: |
      Imagina que hemos construido un semáforo automatizado que cicla a través de sus colores dentro de un bucle "repetir para siempre". Es un gran comienzo, pero podemos hacerlo más realista.
      ¿Y si quisiéramos que la **luz amarilla parpadeara** varias veces antes de ponerse roja? Esta sería una advertencia mucho mejor y más segura para los conductores.
    media: "src/06-traffic-light-with-flashing-yellow-light/a.traffic-interm.svg"

  - title: "Entonces, ¿simplemente agregamos más bloques?"
    type: "learn"
    content: |
      Para hacer que la luz parpadee, tendríamos que agregar una secuencia como esta a nuestro bucle principal:
      **Verde → Amarillo ENCENDIDO → APAGADO → Amarillo ENCENDIDO → APAGADO → Amarillo ENCENDIDO → APAGADO → Rojo**
      Esto funciona, pero solo está repitiendo la secuencia **“Amarillo ENCENDIDO → APAGADO”**. Una vez más, ¡**nuestro código se volvería muy largo y repetitivo**! Debe haber una forma más inteligente.
    media: "src/06-traffic-light-with-flashing-yellow-light/a.loop.large.es.svg"

  - title: "¿Por qué no otro bucle 'para siempre'?"
    type: "learn"
    content: |
      No puedes tener dos capitanes en un barco, ¡y no puedes tener más de un bucle "repetir para siempre" (Bucle Principal) en un programa! Si lo hicieras, la computadora no sabría cuál es el programa principal o qué ejecutar. ¡Se confundiría!
    media: "src/06-traffic-light-with-flashing-yellow-light/a.pc_.confused.svg"

  - title: "La solución: ¡un bucle dentro de un bucle!"
    type: "learn"
    content: |
      ¡Aquí es donde un tipo diferente de **bucle** es útil! Podemos usar un bucle que se repite un número específico de veces (en la imagen, 3 veces). Esto es perfecto para la parte intermitente.
      Aún mejor, podemos **anidar bucles**. Esto significa poner un bucle *dentro* de otro. ¡Repeticiones dentro de repeticiones!
    media: "src/06-traffic-light-with-flashing-yellow-light/a.general.loop-2.es.svg"

  - title: "Amarillo intermitente: un bucle anidado"
    type: "learn"
    content: |
      Al usar un bucle numerado, podemos repetir los bloques **“Amarillo ENCENDIDO → APAGADO”** tantas veces como necesitemos. Al poner este bucle más pequeño *dentro* de nuestro bucle principal "para siempre", creamos un programa potente y eficiente:
      Bucle Principal ( **Verde →** *Bucle Interno* ( **Amarillo ENCENDIDO → APAGADO** [x4] ) **→ Rojo** )
    media: "src/06-traffic-light-with-flashing-yellow-light/a.general.loop-inside-2.es.svg"

  - id: "create"
    title: "¡Construyamos nuestro semáforo intermitente!"
    type: "create"
    icon: "cogs"
    heading_text: "Creemos nuestro semáforo avanzado."
    steps:
      - "Presiona <addbutton>Añadir Dispositivo</addbutton> y selecciona <comp>Lámpara</comp>."
      - "Escanea el código <qr>."
      - "Recuerda que si no tienes un smartphone, puedes presionar <openwindow>Abrir en esta ventana</openwindow>."
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
      Los bloques “repetir para siempre” y el bucle numerado se encuentran ambos en la categoría <category>Básico</category>.
    media: "[700]https://app.protobject.com/generate?a06-trafficlighflashing&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "¡Ahora has dominado los bucles anidados! Pregúntate:"
    content: |
      * Los bucles no son solo para el código; están en todas partes. ¿Dónde puedes ver patrones o ciclos que se repiten en la vida cotidiana (piensa en la música, las rutinas diarias, la naturaleza)?
      * ¿Qué otro prototipo genial podrías construir usando un bucle dentro de un bucle?
    right_content:
      - text: |
          **Desafío**: ¡Hagamos que 2 semáforos en una intersección funcionen en sincronía!
          
          *Cuando uno esté en rojo, el otro debería estar en verde y viceversa.*
      - media: "src/06-traffic-light-with-flashing-yellow-light/traffic-challenge.svg"
---