---
layout: activity
title: "Controla la Intensidad de la Luz"
image: src/13-lamp-with-variable-intensity/13.lampara-intensidad-variable.svg
video: src/videos/13_light_intensity.mp4
video_title: "¿Qué haremos?"
description: "Explora el mundo del color y la luz usando una perilla para cambiar gradualmente el brillo de una lámpara de negro a blanco."
lang: es
permalink: /es/actividades/controla-la-intensidad-de-la-luz/
ref: activity_lamp_with_variable_intensity

# ACTIVITY INFO
level: 1
computational_topics:
  - "Sensores e Input"
  - "Temporización y Eventos"
general_topics:
  - "Ciencia y Tecnología"

tags: [Potenciómetro, Eventos, Entrada Analógica, Color, Escala de Grises, Intensidad de Luz]

introduction: |
  Hemos usado una perilla para controlar el volumen; ¡ahora usemos ese mismo poder analógico para controlar la luz! En esta misión, te sumergirás en la ciencia del color digital (RGB) y aprenderás cómo tu pantalla crea cada tono, desde el negro puro hasta el blanco brillante. Luego construirás tu propio interruptor atenuador, usando un **potenciómetro** para controlar suavemente la intensidad de una lámpara virtual.

teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender los conceptos de eventos y potenciómetros.
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar el trabajo propio y el de los demás.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - La Ciencia del Color de la Pantalla**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy aprenderemos a prototipar una lámpara con intensidad variable, un interruptor atenuador."**
  2.  Haz una pregunta guía: **"¿Alguna vez han notado que los colores en una revista impresa se ven diferentes a la misma imagen en una pantalla? ¿Por qué creen que es así?"**
  3.  Esta pregunta es la puerta de entrada perfecta para explicar la diferencia entre el **color sustractivo** (tinta/pintura) y el **color aditivo** (luz/pantallas). Explica que las pantallas usan el modelo aditivo RGB (Rojo, Verde, Azul). Luego, introduce la herramienta para el control gradual: el **potenciómetro**, que actuará como nuestro atenuador.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo el Atenuador**
  1.  Ahora que los estudiantes comprenden la teoría del color aditivo y cómo un potenciómetro puede controlarlo, es hora de construir el interruptor atenuador.
  2.  Guíalos a través de **las instrucciones para crear la lámpara y programar el control de intensidad**, como se detalla en la sección práctica a continuación. Asegúrate de que vean cómo el único valor de la perilla se introduce en los tres canales de color (R, G y B) para crear un efecto de escala de grises.

  ### **Cierre (5-10 minutos) - Reflexión sobre Color y Control**
  1.  Una vez que todos tengan un interruptor atenuador que funcione, es hora de reflexionar sobre la teoría del color que acaban de poner en práctica.
  2.  Usa la sección final para guiar una discusión sobre el control de colores individuales (un gran adelanto para la próxima actividad) y para desafiarlos a combinar luz y sonido en su proyecto.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Colores de Impresión vs. Pantalla"
    type: "learn"
    icon: "book-reader"
    content: |
      El **color sustractivo** (como la tinta sobre el papel) comienza con una superficie blanca y *resta* luz. Mezclar todos los colores primarios de tinta (Cian, Magenta, Amarillo) da como resultado el negro.
      El **color aditivo** (como la pantalla de un teléfono) comienza con una superficie negra y *agrega* luz. Los colores primarios son Rojo, Verde y Azul (RGB). Mezclar los tres a máxima intensidad crea una luz blanca pura. ¡Este es el modelo que usamos en Protobject!
    media: "src/13-lamp-with-variable-intensity/a-additive-substactive.es.svg"

  - title: "Color Aditivo y Tonos de Gris"
    type: "learn"
    content: |
      En el modelo aditivo RGB, podemos crear diferentes tonos de gris mezclando **cantidades iguales** de luz roja, verde y azul.
      * Una **baja intensidad** de los tres colores da como resultado un **gris oscuro**.
      * Una **alta intensidad** de los tres da como resultado un **gris claro**.
      * El **negro** es la ausencia total de luz (todos los colores apagados), mientras que el **blanco** es los tres colores a su máxima intensidad.
    media: "src/13-lamp-with-variable-intensity/b-opacity.svg"

  - title: "Usando un Potenciómetro para Controlar la Intensidad"
    type: "learn"
    content: |
      Para controlar el brillo de nuestra luz, necesitamos una entrada analógica. ¡El **potenciómetro** es la herramienta perfecta para esto! Es un componente, generalmente controlado con una perilla, que proporciona un rango suave de valores.
      Podemos usar el valor del potenciómetro para establecer el brillo de los píxeles rojos, verdes y azules en la pantalla, todo al mismo tiempo. Al girar la perilla, podemos hacer que la pantalla muestre cualquier tono, desde el negro hasta el blanco.
    media: "src/13-lamp-with-variable-intensity/b-opacity-knob.svg"
  
  - title: "¡Manos a la obra!"
    type: "learn"
    content: |
      Usaremos el potenciómetro para modificar la intensidad de nuestra lámpara. A medida que giremos la perilla, nuestro programa leerá su valor y lo convertirá en un nivel de brillo para la lámpara, ajustándolo en tiempo real.
    media: "src/a.working.svg"

  - id: "create"
    title: "Crea la Lámpara Variable"
    type: "create"
    icon: "cogs"
    heading_text: "Creemos el prototipo para controlar la intensidad de la luz."
    content: |
      Primero, agregaremos dos componentes: uno que actúe como nuestra lámpara y otro que sea nuestra perilla atenuadora.
    steps:
      - "Presiona <addbutton>Añadir Dispositivo</addbutton>, selecciona <comp>Lámpara</comp> y presiona <openwindow>Abrir en esta ventana</openwindow>."
      - "Presiona de nuevo <addbutton>Añadir Dispositivo</addbutton>, selecciona <comp>Perilla</comp> y escanea el código <qr> con tu smartphone."
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
      Los bloques de color se encuentran en la categoría <category>Color</category>.
      **Recuerda**: Puedes construir esto usando un **evento** (más eficiente) o un **bucle principal**.
    media: "[700]https://app.protobject.com/generate?a13.knobluz&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "¡Has controlado la intensidad de la luz blanca!"
    content: |
      Lo hiciste enviando el *mismo* valor desde la perilla a los canales Rojo, Verde y Azul.
      *Pero, ¿y si enviaras valores *diferentes*? ¿Cómo programarías la perilla para ajustar solo la intensidad de la luz roja, mientras que el verde y el azul permanecen apagados?*
    right_content:
      - text: |
          **Desafío**: Modifica el proyecto para que cuando la intensidad de la luz (el valor de la perilla) supere los 80, comience a sonar una canción.
      - text: |
          **Pista**: Necesitarás el componente <comp>ReproductorSonido</comp>. Dentro de tu evento o bucle, puedes usar un condicional: **SI** el valor de la perilla es mayor que 80, **ENTONCES** reproduce la canción, **SINO** detén la canción.
---