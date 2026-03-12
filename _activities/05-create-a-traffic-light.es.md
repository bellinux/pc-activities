---
layout: activity
title: "El Semáforo"
image: src/05-creating-a-traffic-light/05.semaforo.svg
video: src/videos/05_traffic_light.mp4
video_title: "¿Qué haremos?"
description: "¡Dile adiós al código repetitivo! Aprende a usar bucles infinitos para automatizar la clásica secuencia de un semáforo."
lang: es
permalink: /es/actividades/el-semaforo/
ref: activity_create_a_traffic_light

# ACTIVITY INFO
level: 1
computational_topics:
  - "Bucles"
  - "Temporización y Eventos"
general_topics:
  - "Vida Cotidiana"

tags: [Bucles, Bucle Principal, Repetir por siempre, Automatización, Tiempos, Semáforo]

introduction: |
  ¿Cómo haces que un programa se ejecute por sí solo, para siempre? Si tuvieras que programar un semáforo para todo un día copiando y pegando comandos, ¡tu programa tendría millones de líneas! En esta misión, aprenderás el secreto de los programadores para la automatización: el **bucle** infinito. Prepárate para construir un semáforo inteligente y totalmente automatizado que nunca se detiene.
  

teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Teléfono móvil, tableta o computadora
  * Conexión a internet

  ### **Objetivos Educativos**
  * Comprender el concepto de "repetir por siempre" (Bucle Principal).
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el entorno circundante.
  * Evaluar su propio trabajo y el de los demás, tanto individualmente como en equipo.
  * Participar en diálogos y reflexiones para proponer mejoras.

  ### **Inicio (10 minutos) - El Problema de la Repetición**
  1.  Da la bienvenida a los estudiantes e introduce la actividad del día: **"Hoy vamos a aprender a prototipar un semáforo automatizado."**
  2.  Comienza repasando el concepto de secuencia. Pregunta a la clase: **"Sabemos cómo encender una luz durante unos segundos. Pero, ¿cómo crearíamos una secuencia, como una luz verde, luego una amarilla y después una roja?"**
  3.  Después de que hagan una lluvia de ideas, introduce el desafío mayor: **"Bien, pero ¿qué pasa si necesitamos que ese semáforo funcione durante una hora entera o todo el día? ¡Copiar y pegar esa secuencia cientos de veces sería imposible!"** Esto plantea el problema perfecto para el cual los bucles son la solución.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo el Sistema Automatizado**
  1.  Ahora que los estudiantes comprenden el poder de los bucles para la automatización, es hora de construir el semáforo.
  2.  Guíalos a través de **las instrucciones para crear la secuencia de luces y colocarla dentro del bucle infinito**, como se detalla en la sección práctica a continuación. Esta es su primera experiencia creando un programa que se ejecuta por sí solo.

  ### **Cierre (5-10 minutos) - Del Código al Mundo Real**
  1.  Una vez que el semáforo de todos esté funcionando continuamente, es hora de conectar su creación digital con el mundo que los rodea.
  2.  Usa la sección final para iniciar una discusión sobre cómo funcionan los semáforos en nuestras ciudades y por qué son tan importantes para la seguridad y el orden. Esto les ayuda a ver la aplicación en el mundo real de los conceptos de programación que acaban de aprender.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Qué podemos hacer con una lámpara LED?"
    type: "learn"
    icon: "book-reader"
    content: |
      Si programamos una lámpara LED para que cambie de verde a amarillo y luego a rojo en una secuencia temporizada... ¡hemos creado un semáforo!
      Para hacer esto, solo necesitamos programar los **tiempos** correctos y los **colores** correctos.
    media: "src/05-creating-a-traffic-light/a.trafficlight.svg"

  - title: "El Problema: ¡El Código se Detiene!"
    type: "learn"
    content: |
      Si solo programas un ciclo (verde, amarillo, rojo), el programa lo ejecutará una vez y luego se detendrá. Para que se repita, podrías copiar y pegar los bloques una y otra vez.
      Pero, ¿y si quisieras que el semáforo funcionara durante una hora? **¡Terminarías con una enorme cantidad de código repetido!** Eso es ineficiente e imposible de manejar.
    media: "src/05-creating-a-traffic-light/a.trafficlight-seq.svg"

  - title: "La Solución: El Bucle 'Repetir por Siempre'"
    type: "learn"
    content: |
      ### ¿Cómo hacemos que se repita por sí solo? ¡Usamos un bucle!

      El bloque **"repetir por siempre"** es una herramienta fundamental en la programación. Este concepto, también conocido como el **Bucle Principal**, le dice a la computadora que repita todo el código que está dentro una y otra vez, hasta que el usuario detenga manualmente el programa.
      ¡Al colocar nuestra secuencia de semáforo dentro de este bucle, podemos mantenerlo funcionando indefinidamente!
    media: "src/05-creating-a-traffic-light/a.trafficlight-seq2.es.svg"
  
  - title: "¡Manos a la obra!"
    type: "learn"
    content: |
      Vamos a crear nuestro prototipo de semáforo colocando el código de colores y tiempos dentro del bucle **“repetir por siempre”**. Programaremos la luz para que esté en verde durante 6 segundos, en amarillo durante 1 segundo y en rojo durante 6 segundos, creando un ciclo realista.
    media: "src/a.working.svg"

  - id: "create"
    title: "¡Haz nuestro Semáforo!"
    type: "create"
    icon: "cogs"
    heading_text: "¡Construyamos nuestro semáforo!"
    steps:
      - "Presiona <addbutton>Añadir Dispositivo</addbutton> y selecciona <comp>Lámpara</comp>."
      - "Escanea el código <qr>."
      - "Recuerda que si no tienes un smartphone, puedes presionar <openwindow>Abrir en esta ventana</openwindow> para abrir los componentes en la misma computadora."
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono de signo de interrogación para abrir los comentarios que explican el código.

      El bloque "repetir por siempre" se encuentra en la categoría <category>Básico</category>.
    media: "[700]https://app.protobject.com/generate?a05-trafficlight&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "¡Has construido un semáforo que funciona! Ahora, pensemos en el mundo real."
    content: |
      * ¿Cómo funcionan los semáforos reales? ¿Están solos o trabajan en equipo?
      * ¿Cuántos semáforos se necesitan generalmente para controlar una sola intersección?
      * ¿Cuál es el propósito más importante de un semáforo en nuestras comunidades?
---