---
layout: activity
title: "Código Inteligente: Usando Funciones"
image: src/20-light-button-panel/20.botonera-luces.svg
video: src/videos/20_light_button_panel.mp4
video_title: "¿Qué haremos?"
description: "Aprende a escribir código más limpio y reutilizable creando funciones con parámetros para un juego de luces de dos botones."
lang: es
permalink: /es/actividades/codigo-inteligente-usando-funciones/
ref: activity_light_button_panel

# ACTIVITY INFO
level: 2
computational_topics:
  - "Funciones"
  - "Temporización y Eventos"
general_topics:
  - "Matemáticas y Lógica"

tags: [Funciones, Parámetros, Código Reutilizable, Eventos, Entrada de Usuario]

introduction: |
  ¿Cansado de copiar y pegar los mismos bloques una y otra vez? A medida que tus programas se vuelven más complejos, necesitas una forma de mantenerte organizado y eficiente. ¡El secreto definitivo de los programadores profesionales para esto es la **Función**! En esta misión, aprenderás a agrupar tu código en bloques inteligentes y reutilizables que se pueden llamar en cualquier momento. Prepárate para construir una única función de patrón de luces que puede ser activada por diferentes botones para crear diferentes resultados.

teacher: |
  ### **Cursos**
  * Grados 6-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender el concepto de funciones y parámetros.
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar el trabajo propio y el de los demás.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - El Problema de la Repetición**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy aprenderemos a escribir código más inteligente y eficiente usando funciones."**
  2.  Inicia la lección preguntando: **"Imaginen que están escribiendo un programa y necesitan usar los mismos 10 bloques de código en cinco lugares diferentes. ¿Cuál es el problema de simplemente copiarlos y pegarlos?"** (Guíalos a problemas de tamaño, desorden y la dificultad de hacer cambios: ¡tendrías que corregir un error en 5 lugares!).
  3.  Explica que los programadores tienen una solución poderosa para esto: las **Funciones**. Usa la analogía de una receta: en lugar de escribir los pasos cada vez, simplemente te refieres al nombre de la receta. Este es el punto de entrada perfecto para explicar cómo las funciones nos ayudan a escribir código reutilizable.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo una Función Reutilizable**
  1.  Ahora que los estudiantes comprenden el poder de crear bloques de código reutilizables, es hora de construir su primera función.
  2.  Guíalos a través de **las instrucciones para crear su propia función `secuencia_luces` y luego llamarla desde dos eventos de botones diferentes**, como se detalla en la sección práctica a continuación. Esta es su primera vez definiendo un bloque personalizado y luego usándolo en su programa, lo cual es un paso importante.

  ### **Cierre (5-10 minutos) - El Poder de los Parámetros**
  1.  Una vez que todos tengan su panel de luces de dos botones funcionando desde una sola función, es hora de reflexionar sobre el poder y la elegancia de esta nueva herramienta.
  2.  Usa la sección final para fomentar la experimentación con los parámetros de la función y para desafiarlos a construir una segunda función diferente para otra tarea.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Qué son las funciones?"
    type: "learn"
    icon: "book-reader"
    content: |
      Las funciones son grupos de código reutilizables que puedes nombrar y luego "llamar" cada vez que los necesites.
      Imagina que tienes una receta favorita con cinco pasos para hacer la cena. En lugar de escribir esos cinco pasos cada vez, puedes crear una única "tarjeta de receta" llamada "CENA". Ahora, solo necesitas llamar a esa única función, y el programa ejecuta los cinco pasos. Esta es una función **sin parámetros** porque hace exactamente lo mismo cada vez.
    media: "src/20-light-button-panel/a-dinner.svg"

  - title: "Funciones con Parámetros"
    type: "learn"
    content: |
      Pero, ¿y si quieres hacer la misma receta con diferentes ingredientes principales? Podemos hacer nuestra función más inteligente dándole **parámetros** —entradas que pueden cambiar el resultado.
      Piensa de nuevo en la función CENA. Podemos agregar un parámetro para el ingrediente principal. Ahora, llamar a `CENA(fideos)` dará un resultado diferente que `CENA(arroz)`. Los pasos son los mismos, pero la entrada cambia el resultado.
      En nuestra actividad, crearemos una función `secuencia_luces` con un parámetro de **color**. La función siempre realizará el mismo patrón de parpadeo, pero el color de la luz cambiará según el parámetro que proporcionemos cuando la llamemos.
    media: "src/20-light-button-panel/b-green-red.svg"

  - id: "create"
    title: "Crea el Panel de Luces"
    type: "create"
    icon: "cogs"
    heading_text: "Creemos el prototipo. Necesitaremos 3 dispositivos (o abrirlos en la misma ventana)."
    steps:
      - "En el primer dispositivo, agrega el componente <comp>Lámpara</comp>."
      - "En el segundo dispositivo, agrega el primer <comp>BotónTactil</comp>."
      - "En el tercer dispositivo, agrega el segundo <comp>BotónTactil</comp>. Recuerda, puedes usar <openwindow>Abrir en esta ventana</openwindow> para abrir componentes en tu computadora."
    right_content:
      - text: |
          **Consejo**: Puedes agregar más componentes en el mismo smartphone presionando el botón *SCAN* tantas veces como necesites.
      - media: "src/general-scan-button.svg"
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
    media: "[600]https://app.protobject.com/generate?a20-functions&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "¡Has creado tu primera función! Ahora es el momento de experimentar."
    content: |
      * ¿Cómo agregarías un tercer botón que llame a la misma función pero con el color **azul**?
      * ¿Cómo cambiarías la velocidad del parpadeo? (Pista: ¡solo tienes que editar la función en un lugar!)
      * ¿Y si quisieras crear un segundo patrón de luces completamente diferente? ¿Crearías una nueva función?
    right_content:
      - text: |
          **Desafío**: Modifica el proyecto para mostrar un mensaje en la pantalla. Crea una *nueva* función que tome dos parámetros: el **texto** a mostrar y el **color** del texto.
      - text: |
          **Pista**: Necesitarás el componente <comp>DibujarEscribir</comp>. Luego, define una nueva función con parámetros para el texto y el color para manejar la escritura del mensaje en la pantalla.
    media: "src/videos/light_challenge.mp4"
---