---
layout: activity
title: "Espectáculo de Luces y Sonido"
image: src/04-melody-of-happy-birthday-with-lights/04.melodia-con-luces.svg
video: src/videos/04_birthday_light.mp4
video_title: "¿Qué haremos?"
description: "Combina luces y música en perfecta sincronía y aprende a usar variables para controlar fácilmente la velocidad de tu código."
lang: es
permalink: /es/actividades/espectaculo-de-luces-y-sonido/
ref: activity_melody_of_happy_birthday_with_lights

# ACTIVITY INFO
level: 1
computational_topics:
  - "Variables y Datos"
  - "Temporización y Eventos"
general_topics:
  - "Arte y Música"

tags: [Variables, Sincronización, Temporización, Control Multi-dispositivo, Luces, Sonido]

introduction: |
  ¿Listo para ser el director de tu propio espectáculo de luces y sonido? Vamos a combinar música y luces para crear una actuación perfectamente sincronizada. Pero, ¿qué sucede cuando quieres cambiar el tempo? Editar docenas de bloques de retardo uno por uno es una pesadilla. En esta misión, aprenderás un secreto de nivel profesional para resolver esto: las **variables**. Actúan como un control remoto maestro para tu código, permitiéndote cambiar la velocidad de todo tu espectáculo con una sola edición.
  
teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender el concepto de variable y su uso.
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar el trabajo propio y el de los demás.
  * Discutir y reflexionar sobre ideas de mejora.

  ### **Inicio (10 minutos) - El Desafío del Director**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy aprenderemos a prototipar un espectáculo de luces y música sincronizado y fácil de controlar."**
  2.  Inicia la discusión preguntando: **"Piensen en un concierto en vivo. ¿Qué lo hace tan emocionante?"** Guíalos hacia la idea de luces y visuales que se mueven en perfecto tiempo con la música (sincronización).
  3.  Luego, plantea el desafío principal de hoy: **"Ahora, imaginen que son el director de ese espectáculo. Han programado 50 notas y 50 destellos de luz. ¿Qué pasa si de repente quieren que toda la canción vaya más rápido para el final? ¡Tendrían que encontrar y cambiar 100 bloques de retardo diferentes!"** Esto resalta un gran problema: la ineficiencia. Ahora puedes presentar la solución elegante que usan los programadores.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo un Espectáculo Ajustable**
  1.  Ahora que los estudiantes entienden que las variables son la solución para construir un programa inteligente y ajustable, es hora de ponerlas en práctica.
  2.  Guíalos a través del **proceso para crear su prototipo sincronizado**, como se detalla en la sección práctica a continuación. Recuérdales constantemente que noten cómo la única variable `tiempo` se usa una y otra vez, actuando como el control maestro para la velocidad del espectáculo.

  ### **Cierre (5-10 minutos) - El Poder de un Solo Cambio**
  1.  Una vez que los prototipos funcionen, el momento "wow" llega al ver la variable en acción.
  2.  Indícales que **cambien solo el número en el bloque inicial `establecer tiempo a...`**. Haz que prueben un número grande y luego un número pequeño para ver cuán drásticamente cambia el tempo de todo el espectáculo. Esto demuestra el poder y la eficiencia de su nueva herramienta. Usa la sección final para desafiarlos a expandir su creación.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "El Desafío: Sincronización y Velocidad"
    type: "learn"
    icon: "book-reader"
    content: |
      El primer objetivo de un buen espectáculo de luces es la **sincronización**, asegurarse de que cada destello de luz ocurra en el mismo momento exacto que una nota musical. Esto crea un efecto profesional y emocionante.
      Pero hay un segundo desafío más grande: el **control**. Imagina que construyes toda tu secuencia, pero luego decides que quieres que se ejecute más rápido. Tendrías que volver y cambiar manualmente el valor de retardo para *cada nota* y *cada luz*. Para una canción larga, ¡eso podría significar cientos de cambios! Esto es lento y una receta para cometer errores.
    media: "src/04-melody-of-happy-birthday-with-lights/a-light.notes_.svg"

  - title: "La Solución: una Variable como Control Maestro"
    type: "learn"
    content: |
      Para resolver el problema de tener que cambiar muchos valores a la vez, los programadores usan **variables**.
      Una **variable** es como una caja con una etiqueta. Puedes almacenar una sola pieza de información, como un número, dentro de esta caja. La parte poderosa es que luego puedes usar esta caja en muchos lugares de tu código.
      Si quieres cambiar el número, solo tienes que cambiarlo **dentro de la caja una vez**. En todos los lugares donde usaste la caja, el valor se actualizará automáticamente. ¡Es como un control maestro para tu código!
    media: "src/04-melody-of-happy-birthday-with-lights/b-variable.notes.es.svg"

  - id: "create"
    title: "Crea un Espectáculo de Luces Musical"
    type: "create"
    icon: "cogs"
    heading_text: "Creemos un prototipo que toque ♪ Feliz Cumpleaños ♪ con luces perfectamente sincronizadas y ajustables."
    content: |
      Primero, agregaremos los dos componentes que necesitamos: uno para el sonido y otro para la luz.
    steps:
      - "Presiona <addbutton>Añadir Dispositivo</addbutton> y selecciona <comp>TecladoMusical</comp>."
      - "Presiona de nuevo <addbutton>Añadir Dispositivo</addbutton> y selecciona <comp>Lámpara</comp>."
      - "Recuerda que si no tienes smartphones para escanear los códigos <qr>, puedes presionar <openwindow>Abrir en esta ventana</openwindow>."
    right_content:
      - text: |
          **Sugerencia**: En Protobject, puedes agregar más componentes en el mismo smartphone presionando el botón SCAN tantas veces como necesites.
      - media: "src/general-scan-button.svg"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código. Observa cómo la variable `tiempo` se define una vez al principio y luego se usa para todos los retardos. Los bloques de multiplicación se encuentran en la categoría <category>Matemáticas</category>.
    media: "[700]https://app.protobject.com/generate?a04-melody-light&es&dynamic&-1"
    right_content:
      - text: |
          **Experimenta**: ¡La magia ocurre aquí! Intenta cambiar el único valor de la variable "tiempo" en la parte superior del código. Establécelo en `100` para verlo ir súper rápido, o en `500` para verlo ir lento.

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Has construido un espectáculo inteligente y ajustable. ¿Qué sigue?"
    content: |
      Has visto lo poderosa que puede ser una sola variable. ¿Y si quisieras hacer tu espectáculo aún más grande? ¿Cómo agregarías una segunda lámpara que parpadee junto con la música, tal vez en un teléfono diferente o con un color diferente?
    right_content:
      - text: |
          Piensa en cómo agregarías un nuevo componente <comp>Lámpara</comp> y lo conectarías a la misma variable maestra `tiempo`.
---