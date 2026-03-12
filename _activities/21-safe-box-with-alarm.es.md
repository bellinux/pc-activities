---
layout: activity
title: "La Caja Fuerte de Dos Llaves"
image: src/21-safe-box-with-alarm/21.caja-seguridad.svg
video: src/videos/21_safe_box.mp4
video_title: "¿Qué haremos?"
description: "Explora conceptos de ciberseguridad y operadores lógicos ('AND') para construir una alarma de alta seguridad que requiere que se presionen dos botones simultáneamente."
lang: es
permalink: /es/actividades/la-caja-fuerte-de-dos-llaves/
ref: activity_safe_box_with_alarm

# ACTIVITY INFO
level: 2
computational_topics:
  - "Condicionales y Lógica"
  - "Sensores e Input"
general_topics:
  - "Vida Cotidiana"

tags: [Operadores Lógicos (AND), Condicionales Anidados, Ciberseguridad, Autenticación de Dos Factores, Multi-dispositivo, Sensor de Inclinación]

introduction: |
  ¿Cómo protegen los bancos y tus juegos favoritos tu cuenta de los hackers? A menudo, usan más que una simple contraseña. En esta misión, te sumergirás en el mundo de la **ciberseguridad** y los operadores lógicos. Aprenderás cómo funciona el **operador 'AND'** construyendo una caja fuerte de alta seguridad que solo se desactiva si se presionan dos llaves diferentes (botones) exactamente al mismo tiempo, ¡igual que un sistema real de autenticación de dos factores!

teacher: |
  ### **Cursos**
  * Grados 6-12

  ### **Materiales**
  * 3 celulares, tabletas o computadoras
  * Conexión a Internet
  * Una caja (como una caja de zapatos o de pizza) para que actúe como la caja fuerte física
  * Un objeto para que sea el "tesoro" adentro

  ### **Objetivos Educativos**
  * Comprender el concepto del operador lógico AND y los condicionales anidados.
  * Crear un objeto tecnológico (prototipo) utilizando múltiples dispositivos.
  * Identificar relaciones entre la tecnología, la seguridad y el mundo circundante.
  * Evaluar el trabajo propio y el de los compañeros.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - La Cerradura y la Llave Digital**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy vamos a crear una caja fuerte de alta seguridad con una alarma especial de dos llaves."**
  2.  Inicia la lección con una pregunta de gran interés: **"¿Alguna vez han oído hablar de Ciberseguridad? ¿Qué creen que es?"**
  3.  Usa esta discusión para introducir conceptos como la protección de datos y las contraseñas seguras. Luego, introduce la **Autenticación de Dos Factores (2FA)** como una capa extra de seguridad. Explica que nuestra caja fuerte usará este mismo principio, requiriendo que se usen dos 'llaves' a la vez. Este es el momento perfecto para introducir el operador lógico **AND**.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo la Caja Fuerte de Alta Seguridad**
  1.  Ahora que los estudiantes comprenden la lógica del operador 'AND' y su conexión con la ciberseguridad, es hora de construir la caja fuerte.
  2.  Guíalos a través de **las instrucciones para configurar los tres dispositivos y programar la lógica de seguridad**, como se detalla en la sección práctica a continuación. Esta es una gran oportunidad para el trabajo en equipo, con diferentes estudiantes manejando la caja fuerte y cada una de las dos "llaves".

  ### **Cierre (5-10 minutos) - Pensando como un Experto en Seguridad**
  1.  Una vez que las cajas fuertes estén construidas y probadas, es hora de reflexionar sobre la importancia en el mundo real de los conceptos que acaban de usar.
  2.  Usa la sección final para guiar una discusión sobre la ciberseguridad como campo y para animarlos a pensar en otras formas de proteger la información digital.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Qué es la Ciberseguridad?"
    type: "learn"
    icon: "book-reader"
    content: |
      La ciberseguridad es como un escudo digital. Es la práctica de proteger computadoras, teléfonos y datos importantes de personas malintencionadas en línea que quieren robarlos o dañarlos. Así como podrías tener una cerradura en tu diario o en tu habitación, tus cuentas en línea también necesitan protección.
    media: "src/21-safe-box-with-alarm/a-cybersecurity.svg"

  - title: "Sombreros Blancos vs. Sombreros Negros"
    type: "learn"
    content: |
      En Internet, hay "Sombreros Negros" —hackers maliciosos que usan virus informáticos y trucos para robar información. Pero también hay "Sombreros Blancos" —expertos en ciberseguridad que trabajan para construir defensas y proteger datos y sistemas de estos ataques. Son los superhéroes digitales.
    media: 
      - "src/21-safe-box-with-alarm/b-hackers.svg"
      - "src/21-safe-box-with-alarm/b-securityexpert.svg"

  - title: "Tu Primera Línea de Defensa: las Contraseñas"
    type: "learn"
    content: |
      Una de las mejores maneras de protegerte es usando contraseñas seguras y únicas. Una contraseña segura es una que nadie puede adivinar fácilmente. Si tu contraseña es demasiado simple, como "123456" o "contraseña", alguien podría entrar fácilmente en tu "caja fuerte digital" sin tu permiso.
    media: "src/21-safe-box-with-alarm/c-strongpassword.svg"

  - title: "¿Y si te roban la contraseña?"
    type: "learn"
    content: |
      Incluso con una contraseña segura, necesitas un plan de respaldo. Ahí es donde entra en juego la **Autenticación de Dos Factores (2FA)**. Es como necesitar una segunda llave secreta. Por ejemplo, después de ingresar tu contraseña, un sitio podría enviar un código especial a tu teléfono que también tienes que ingresar. Sin ese segundo código, nadie puede entrar, incluso si saben tu contraseña.
    media: "src/21-safe-box-with-alarm/d-two-factor.svg"
  
  - title: "¡Nuestra Caja Fuerte de Dos Factores!"
    type: "learn"
    content: |
      La caja fuerte que estamos construyendo hoy usa el mismo principio de 2FA. Para apagar la alarma, necesitas que dos llaves (nuestros dos botones) se presionen al mismo tiempo. Si un ladrón roba el botón de Martín, todavía no puede desactivar la alarma sin tener también el botón de Juan. ¡Esto hace que el tesoro esté mucho más seguro!
    media: "src/21-safe-box-with-alarm/e-onebutton.svg"

  - title: "Booleanos y el Operador AND"
    type: "learn"
    content: |
      Recuerda que los **Booleanos** son un tipo de dato simple con solo dos valores posibles: **VERDADERO** o **FALSO**. Cuando se presiona un botón, su estado podría ser VERDADERO. Cuando no está presionado, su estado es FALSO.
      El operador lógico **AND** es como un portero estricto que necesita ver dos formas de identificación. Solo devuelve **VERDADERO** si *todas* las condiciones que comprueba son verdaderas. Si incluso una es falsa, todo el resultado es falso.
    media: "src/21-safe-box-with-alarm/f-boolean.es.svg"

  - title: "Cómo AND Asegura Nuestra Caja"
    type: "learn"
    content: |
      Así es como funciona la lógica para nuestra caja fuerte:
      * Si el Botón 1 está presionado (VERDADERO) **Y** el Botón 2 está presionado (VERDADERO) --> El resultado es **VERDADERO**, y la alarma está apagada.
      * Si el Botón 1 está presionado (VERDADERO) **Y** el Botón 2 NO está presionado (FALSO) --> El resultado es **FALSO**, y la alarma está activa.
      * Si ninguno está presionado, el resultado también es **FALSO**. ¡Se requieren ambas llaves al mismo tiempo!
    media: 
      - "src/21-safe-box-with-alarm/l-box-false-false.es.svg"
      - "src/21-safe-box-with-alarm/m-box-true-false.es.svg"
      - "src/21-safe-box-with-alarm/n-box-true-true.es.svg"

  - id: "create"
    title: "Crea la Caja Fuerte"
    type: "create"
    icon: "cogs"
    heading_text: "Para esta actividad, necesitamos 3 dispositivos."
    steps:
      - "En el primer dispositivo (la caja fuerte misma), agrega <comp>DibujarEscribir</comp>, <comp>Inclinación</comp> y <comp>ReproductorSonido</comp>."
      - "En el segundo dispositivo, agrega un <comp>BotónTactil</comp> (esta es la llave de Martín)."
      - "En el tercer dispositivo, agrega otro <comp>BotónTactil</comp> (esta es la llave de Juan)."
    right_content:
      - text: |
          **Consejo**: Puedes agregar múltiples componentes al mismo smartphone presionando el botón *SCAN* de nuevo después de agregar el primero.
      - media: "src/general-scan-button.svg"
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
    media: "[700]https://app.protobject.com/generate?a21-alarmbuttons&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "¡Acabas de usar un principio fundamental de la ciberseguridad!"
    content: |
      * ¿Te pareció interesante este tema? La ciberseguridad es uno de los campos de más rápido crecimiento y más importantes en la tecnología. ¿Es algo que te verías haciendo en el futuro?
      * ¿Qué otros métodos conoces para proteger tus cuentas y datos en línea?
    right_content:
      - text: |
          ¡Recuerda siempre la importancia de la **ciberseguridad** en nuestro mundo digital!
---