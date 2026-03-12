---
layout: activity
title: "Construye un Detector de Caídas"
image: src/16-fall-detector/16.detector-caida.svg
video: src/videos/16_fall_detector.mp4
video_title: "¿Qué haremos?"
description: "Aprende a medir la aceleración total con el sensor de movimiento de tu teléfono para crear un sistema que pueda detectar una caída repentina."
lang: es
permalink: /es/actividades/construye-un-detector-de-caidas/
ref: activity_fall_detector

# ACTIVITY INFO
level: 1
computational_topics:
  - "Sensores e Input"
  - "Condicionales y Lógica"
  - "Bucles"
general_topics:
  - "Vida Cotidiana"

tags: [Acelerómetro, Sensores, Valor Absoluto, Bucle Principal, Condicionales, Salud, Seguridad]

introduction: |
  ¿Sabías que tu teléfono puede sentir cuándo se está cayendo? Su **acelerómetro** incorporado es tan sensible que puede detectar cambios bruscos de movimiento. Al sumar los datos de los tres ejes de movimiento (X, Y y Z), podemos medir la fuerza total de un impacto. En esta misión, aprovecharás ese poder para construir un detector de caídas real que suena una alarma cuando detecta una sacudida brusca y repentina.
  
teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender los conceptos de “si-sino” y el “plano cartesiano”.
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar el trabajo propio y el de los demás.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - La Física de una Caída**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy aprenderemos a prototipar un ‘detector de caídas’ con nuestros teléfonos."**
  2.  Comienza preguntando a la clase: **"¿Cómo saben a veces los smartwatches o los teléfonos si una persona se ha caído?"** Guía la discusión hacia la idea de detectar un movimiento brusco.
  3.  Explica que el **acelerómetro** del teléfono es la clave. Introduce el desafío principal: una caída puede ocurrir en cualquier dirección, entonces, ¿cómo puede nuestro programa detectar la *magnitud* general del movimiento? Esto conduce perfectamente al concepto de combinar los ejes X, Y y Z para obtener un valor de movimiento total.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo el Detector**
  1.  Ahora que los estudiantes comprenden la lógica de medir el movimiento total, es hora de construir el detector de caídas.
  2.  Guíalos a través de **las instrucciones para crear el prototipo y programar la lógica de detección**, como se detalla en la sección práctica a continuación. Enfatiza cómo se utiliza la declaración 'SI' para verificar si el movimiento total excede un cierto umbral.
  3.  Haz que los estudiantes prueben sus prototipos agitando cuidadosa pero rápidamente el dispositivo, o dejándolo caer una distancia muy corta sobre una superficie blanda como un libro o una almohada.

  ### **Cierre (5-10 minutos) - Fiabilidad en el Mundo Real**
  1.  Una vez que los detectores de caídas funcionen, es hora de pensar en las implicaciones y desafíos del mundo real de dicho dispositivo.
  2.  Usa la sección final para guiar una discusión crítica sobre la fiabilidad de su detector de caídas. Esto los alienta a pensar como ingenieros sobre los falsos positivos y a mejorar sus diseños.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Cómo detecta el teléfono una caída?"
    type: "learn"
    icon: "book-reader"
    content: |
      El **acelerómetro** de tu teléfono es un potente sensor de movimiento. Mide constantemente la aceleración en tres direciones o "ejes": izquierda-derecha (eje X), adelante-atrás (eje Y) y arriba-abajo (eje Z).
      Cuando un teléfono se cae, experimenta un cambio brusco y repentino en la aceleración. Para detectar una caída, no nos importa la *dirección* de la caída, solo que fue una sacudida potente. Para medir esta sacudida total, podemos tomar el **valor absoluto** (la versión positiva del número) del movimiento en cada eje y sumarlos. Esto nos da un solo número que representa la magnitud total del movimiento.
    media: "src/16-fall-detector/z-accelerometer.svg"

  - title: "¡Manos a la obra!"
    type: "learn"
    content: |
      Protobject nos simplifica este proceso con la variable `movimientoGeneral`. Esta variable especial hace los cálculos por nosotros automáticamente: suma los valores absolutos de los ejes X, Y y Z en tiempo real.
      Todo lo que necesitamos hacer es establecer un umbral. Le diremos a nuestro programa: **SI** el valor de `movimientoGeneral` excede un cierto número (como 150), significa que ha ocurrido una sacudida brusca y debemos activar un sonido de alarma.
    media: "src/a.working.svg"

  - id: "create"
    title: "Crea el Detector de Caídas"
    type: "create"
    icon: "cogs"
    heading_text: "Creemos un prototipo para detectar caídas."
    content: |
      Primero, necesitamos agregar dos componentes: uno para (1) detectar los movimientos del smartphone y otro para (2) reproducir sonidos.
    steps:
      - "Presiona <addbutton>Añadir dispositivo</addbutton> y selecciona <comp>Movimiento</comp>."
      - "Haz clic de nuevo en <addbutton>Añadir dispositivo</addbutton> y selecciona <comp>ReproductorSonido</comp>."
    right_content:
      - text: |
          **Consejo**: En Protobject, puedes agregar más componentes en el mismo smartphone presionando el botón *SCAN* de nuevo después de agregar el primero.
      - media: "src/general-scan-button.svg"
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
      
      **Nota:** Este código utiliza la variable `movimientoGeneral`. Como un desafío adicional, ¡intenta modificar el código para hacer los cálculos manualmente sumando tú mismo los valores absolutos de los ejes X, Y y Z!
    media: "[700]https://app.protobject.com/generate?a16-falldetector&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Has construido un dispositivo con aplicaciones en el mundo real. Ahora, pensemos como ingenieros."
    content: |
      * ¿Cuán confiable crees que es este detector de caídas? ¿Podría activarse una falsa alarma simplemente corriendo, saltando o dejando el teléfono con demasiada fuerza?
      * ¿Confiarías en que se use en una situación de la vida real para una persona mayor? ¿Qué mejoras necesitarías hacer primero?
    right_content:
      - text: |
          **Desafío**: Crea una luz que cambie de color según las aceleraciones del teléfono.
      - text: |
          **Pista**: Puedes alimentar los valores de los tres ejes diferentes del acelerómetro (X, Y y Z) en los tres canales de color primarios (Rojo, Verde y Azul) de una lámpara. Usa un evento para detectar cambios en el acelerómetro.
---