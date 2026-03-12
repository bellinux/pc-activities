---
layout: activity
title: "El Control de Volumen"
image: src/12-volume-control-with-a-potentiometer/12.control-volumen.svg
video: src/videos/12_music_volume.mp4
video_title: "¿Qué haremos?"
description: "Aprende a leer la entrada continua de una perilla virtual (potenciómetro) para controlar el volumen de una canción en tiempo real."
lang: es
permalink: /es/actividades/el-control-de-volumen/
ref: activity_volume_control_with_a_potentiometer

# ACTIVITY INFO
level: 1
computational_topics:
  - "Sensores e Input"
  - "Bucles"
general_topics:
  - "Arte y Música"
  - "Ciencia y Tecnología"

tags: [Entrada Analógica, Potenciómetro, Perilla, Bucle Principal, Control de Volumen]

introduction: |
  Hasta ahora, nuestros botones han estado ENCENDIDOS o APAGADOS. Pero, ¿qué pasa con todos los controles intermedios? Piensa en una perilla de volumen, un atenuador de luz o un joystick. Estos requieren un control suave y gradual. En esta misión, explorarás el mundo de la **entrada analógica** programando una perilla virtual, también conocida como **potenciómetro**. Prepárate para aprender a leer un valor que cambia continuamente para controlar el volumen de tu proyecto en tiempo real.

teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender el concepto de potenciómetro.
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar el trabajo propio y el de los demás.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - Más Allá de Encendido y Apagado**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy vamos a aprender a crear una perilla de volumen que nos dé un control suave y gradual."**
  2.  Haz una pregunta guía: **"Piensen en una perilla de volumen en un estéreo o un interruptor atenuador para una luz. ¿En qué se diferencia de un simple botón de encendido/apagado?"**
  3.  Guía la discusión hacia la idea de valores 'graduales' o 'intermedios'. Explica que esto se llama **control analógico**, y el componente que nos permite hacer esto es un potenciómetro. Profundicemos en cómo funciona y cómo podemos programarlo.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo el Controlador de Volumen**
  1.  Ahora que los estudiantes comprenden el concepto de un potenciómetro и cómo leer su valor, es hora de construir un controlador de volumen en tiempo real.
  2.  Guíalos a través de **las instrucciones para conectar los componentes y programar la lógica de control de volumen**, como se detalla en la sección práctica a continuación. Anímalos a ver cómo el valor de la perilla afecta directamente el volumen del reproductor de audio a medida que la giran.

  ### **Cierre (5-10 minutos) - El Mundo de lo Analógico**
  1.  Una vez que todos tengan una perilla de volumen que funcione, es hora de hacer una lluvia de ideas sobre otros usos para esta potente entrada analógica.
  2.  Usa la sección final para iniciar una discusión creativa sobre otras cosas que se pueden controlar gradualmente y para desafiarlos a visualizar los datos de su nuevo sensor.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Qué es un potenciómetro?"
    type: "learn"
    icon: "book-reader"
    content: |
      ¿Alguna vez has ajustado el volumen de una radio? ¿O has cambiado el brillo de una lámpara usando un atenuador? Si es así, probablemente hayas usado un potenciómetro.
      Es la tecnología detrás de cualquier control que no es solo encendido o apagado, sino que permite un rango suave de valores intermedios. ¡Generalmente, lo controlas con una **perilla**!
    media: "src/12-volume-control-with-a-potentiometer/a.main-knob.svg"

  - title: "¿Cómo funciona?"
    type: "learn"
    content: |
      Un potenciómetro funciona cambiando su resistencia eléctrica a medida que lo giras. Piénsalo como un grifo para la electricidad. Al girar la perilla, puedes cambiar **gradualmente** cuánta corriente eléctrica fluye a través de él.
      En el caso de un altavoz, ajustar la corriente te permite **aumentar o disminuir el volumen** suavemente.
    media: "src/12-volume-control-with-a-potentiometer/b.knob-music-anim.svg"

  - title: "¿Cómo lo programamos?"
    type: "learn"
    content: |
      Para que nuestra perilla de volumen funcione, nuestro programa necesita saber su posición actual. Tenemos dos excelentes maneras de hacer esto:
      * **El Bucle Principal:** Podemos poner nuestro código dentro de un bucle "repetir para siempre". El programa verificará constantemente el valor de la perilla y actualizará el volumen, una y otra vez.
      * **Eventos:** ¡Una forma más eficiente! Podemos usar un evento que se active *solo cuando se gira la perilla*. El programa espera en silencio hasta que recibe una señal, luego actualiza el volumen.
      ¡En programación, a menudo hay diferentes soluciones para el mismo problema!
    media: "src/12-volume-control-with-a-potentiometer/c.loop-or-event.es.svg"

  - id: "create"
    title: "¡Manos a la obra!"
    type: "create"
    icon: "cogs"
    heading_text: "Vamos a crear un prototipo que nos permita controlar el volumen de una canción con un potenciómetro."
    content: |
      Primero, agregaremos dos componentes: uno para (1) reproducir la música y un segundo para (2) actuar como nuestra perilla de control.
    steps:
      - "Presiona <addbutton>Añadir Dispositivo</addbutton> y selecciona <comp>Perilla</comp>."
      - "Presiona de nuevo <addbutton>Añadir Dispositivo</addbutton> y selecciona <comp>ReproductorSonido</comp>."
      - "Recuerda que si no tienes un smartphone para escanear los códigos <qr>, puedes presionar <openwindow>Abrir en esta ventana</openwindow>."
    right_content:
      - text: |
          **Sugerencia**: En Protobject, puedes agregar más componentes en el mismo smartphone presionando el botón *SCAN* tantas veces como necesites.
      - media: "src/general-scan-button.svg"
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
      **Recuerda**: Puedes construir esto usando un **bucle principal** o, para un enfoque más eficiente, usar el **evento** que se activa **cuando se gira la perilla**.
    media: "[700]https://app.protobject.com/generate?a12-knobvolume&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "¡Acabas de desbloquear el poder del control analógico!"
    content: |
      El simple ENCENDIDO/APAGADO está bien, pero el control gradual abre un mundo completamente nuevo de posibilidades.
      *¿Qué otras cosas en un juego o una aplicación te gustaría controlar suavemente con una perilla o un deslizador? (Piensa en la velocidad del personaje, el brillo de la pantalla o el tamaño del pincel en una aplicación de dibujo).* 
    right_content:
      - text: |
          **Desafío**: Creemos un visualizador que muestre el volumen actual como un número en la pantalla.
      - text: |
          **Pista**: Necesitarás el componente <comp>DibujarEscribir</comp>. Dentro de tu bucle o evento, ¿cómo puedes tomar el valor de la perilla y decirle al componente WriteDraw que lo muestre como texto?
---