---
layout: activity
title: "El Puntero Digital"
image: src/22-presentation-pointer/22.puntero-presentaciones.svg
video: src/videos/22_laser_pointer.mp4
video_title: "¿Qué haremos?"
description: "Combina el acelerómetro, el giroscopio y el magnetómetro de tu teléfono para crear un puntero que puedas controlar con el movimiento."
lang: es
permalink: /es/actividades/el-puntero-digital/
ref: activity_presentation_pointer

# ACTIVITY INFO
level: 3
computational_topics:
  - "Sensores e Input"
  - "Gráficos y Dibujo"
  - "Bucles"
general_topics:
  - "Ciencia y Tecnología"

tags: [Fusión de Sensores, Acelerómetro, Giroscopio, Magnetómetro, Eventos, Bucle Principal, Dibujo, Coordenadas]

introduction: |
  ¿Cómo sabe tu teléfono que debe girar la pantalla cuando lo pones de lado? ¿O cómo un casco de realidad virtual rastrea cada uno de tus movimientos? El secreto es una técnica poderosa llamada **Fusión de Sensores**. En esta misión avanzada de Nivel 3, aprenderás cómo tu teléfono combina su acelerómetro, giroscopio y magnetómetro para determinar su orientación exacta en el espacio 3D. ¡Prepárate para aprovechar estos datos para construir un puntero digital controlado por movimiento, como un puntero láser de alta tecnología!
teacher: |
  ### **Cursos**
  * Grados 9-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender qué son los sensores de movimiento del teléfono y cómo funcionan juntos (Fusión de Sensores).
  * Ser capaz de posicionar elementos en un plano cartesiano.
  * Comprender el concepto de una función computable.
  * Evaluar el trabajo propio y el de los demás.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - El Sexto Sentido del Teléfono**
  1.  Introduce la actividad: **"Hoy aprenderemos a prototipar un puntero de presentación controlado por movimiento, utilizando algunos de los sensores más avanzados de su teléfono."**
  2.  Inicia esta lección avanzada con una pregunta intrigante: **"Su teléfono es solo un bloque de vidrio y metal. ¿Cómo sabe cuál es la dirección hacia arriba, abajo, izquierda y derecha en el mundo real?"**
  3.  Explica que no es uno, sino un equipo de sensores que trabajan juntos. Presenta brevemente a los tres jugadores clave: el acelerómetro (para el movimiento), el giroscopio (para la rotación) y el magnetómetro (como una brújula). Luego, introduce el concepto principal: la **Fusión de Sensores**, el proceso de combinar todos estos datos para obtener un resultado súper preciso.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Programando con Datos Fusionados**
  1.  Ahora que los estudiantes tienen una comprensión conceptual de la Fusión de Sensores, es hora de usar esos datos fusionados para controlar un objeto en la pantalla.
  2.  Guíalos a través de **las instrucciones para crear el puntero y programar la lógica de control de movimiento**, como se detalla en la sección práctica a continuación. Esta es una construcción compleja, así que presta mucha atención a cómo se utilizan las salidas X e Y del sensor para actualizar las coordenadas del puntero.

  ### **Cierre (5-10 minutos) - El Equipo de Sensores**
  1.  Una vez que todos tengan su puntero controlado por movimiento funcionando, es hora de reflexionar sobre la tecnología avanzada que acaban de implementar.
  2.  Usa la sección final para guiar una discusión que refuerce su comprensión de los diferentes sensores y sus roles, y para desafiarlos con una versión multijugador del proyecto.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Cómo sabe el teléfono su orientación?"
    type: "learn"
    icon: "book-reader"
    content: |
      Imagina que estás en una habitación oscura y vacía con los ojos vendados. Probablemente aún podrías señalar 'arriba' y 'abajo' porque puedes sentir la gravedad. Tu teléfono hace algo similar, pero es mucho más avanzado. Para conocer su orientación exacta en el espacio 3D, utiliza un equipo de sensores especializados.
    media: "src/22-presentation-pointer/a-orientation.svg"

  - title: "Conoce al Equipo de Sensores"
    type: "learn"
    content: |
      El sentido de la orientación de tu teléfono proviene de tres especialistas principales:
      * **Acelerómetro**: El 'Detector de Movimiento'. Siente la aceleración lineal: moverse hacia adelante/atrás, izquierda/derecha y arriba/abajo.
      * **Giroscopio**: El 'Especialista en Rotación'. Detecta giros y vueltas, midiendo los cambios en el ángulo del teléfono.
      * **Magnetómetro**: El 'Navegador'. Es una brújula digital que detecta campos magnéticos, sabiendo siempre en qué dirección está el Norte.
    media: 
      - "src/22-presentation-pointer/z-accelerometer.svg"
      - "src/22-presentation-pointer/b-gyroscope-orientation.svg"
      - "src/22-presentation-pointer/c-magnetometer.svg"

  - title: "Trabajando Juntos: Fusión de Sensores"
    type: "learn"
    content: |
      Ninguno de estos sensores es perfecto por sí solo. El acelerómetro puede ser tembloroso y el giroscopio puede 'desviarse' con el tiempo. Pero cuando trabajan juntos, sus fortalezas cubren las debilidades de los demás. Esta colaboración se llama **Fusión de Sensores**. El software del teléfono 'fusiona' inteligentemente los datos de los tres sensores para obtener una única lectura muy precisa de su orientación. ¡Es el trabajo en equipo definitivo!
    media: "src/22-presentation-pointer/d-fusion.es.svg"
  
  - title: "De la Fusión a las Coordenadas"
    type: "learn"
    content: |
      El resultado de la Fusión de Sensores es un flujo de datos numéricos. Nuestro trabajo como programadores es dar sentido a esos datos. Cuando movemos el teléfono, los valores de los ejes de rotación X e Y cambian. Al leer estos valores, podemos mapear el movimiento físico del teléfono a las coordenadas X e Y de un puntero en nuestro lienzo digital.
    media: "src/22-presentation-pointer/e-coordenates.svg"

  - id: "create"
    title: "Crea el Puntero de Presentación"
    type: "create"
    icon: "cogs"
    heading_text: "Creemos el prototipo: necesitaremos un smartphone y una computadora/tableta."
    steps:
      - "En el mismo smartphone, agrega los componentes <comp>Dirección</comp> y <comp>BotónTactil</comp>."
      - "Agrega el dispositivo <comp>DibujarEscribir</comp> abriéndolo en tu computadora/tableta haciendo clic en <openwindow>Abrir en esta ventana</openwindow>."
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
    media: "[600]https://app.protobject.com/generate?a22-pointermap&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "¡Acabas de aprovechar una característica avanzada del smartphone! Repasemos el equipo de sensores:"
    content: |
      * ¿Qué sensor actúa como una brújula, detectando el norte magnético?
      * ¿Qué sensor es el mejor para detectar inclinaciones y giros?
      * ¿Cuál es el propósito del botón 'reset' en este proyecto? ¿Qué sucede si no lo usas?
    right_content:
      - text: |
          **Desafío**: ¡Programemos dos punteros simultáneamente para que dos personas puedan señalar de forma independiente diferentes áreas de la pantalla con sus propios teléfonos!
---