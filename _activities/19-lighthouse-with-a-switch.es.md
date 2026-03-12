---
layout: activity
title: "El Faro"
image: src/19-lighthouse-with-a-switch/19.faro_.svg
video: src/videos/19_lighthouse.mp4
video_title: "¿Qué haremos?"
description: "Domina el bucle 'For' para crear un hermoso efecto de parpadeo gradual para un faro que puedes encender y apagar."
lang: es
permalink: /es/actividades/el-faro/
ref: activity_lighthouse_with_a_switch

# ACTIVITY INFO
level: 2
computational_topics:
  - "Bucles"
  - "Temporización y Eventos"
  - "Variables y Datos"
  - "Condicionales y Lógica"
general_topics:
  - "Ciencia y Tecnología"

tags: [Bucles, Bucle For, Bucles Anidados, Variables, Temporización, Efecto Gradual, Eventos]

introduction: |
  Una simple luz intermitente es genial, pero un faro real tiene un brillo suave y gradual. ¿Cómo podemos codificar ese efecto de aparición y desaparición suave? En esta misión, aprenderás a usar el **bucle 'For'** —un potente bucle diseñado para ejecutarse un número preciso de pasos. Prepárate para programar un hermoso faro pulsante que se ilumina y se atenúa gradualmente.

teacher: |
  ### **Cursos**
  * Grados 6-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender el concepto de un bucle FOR.
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar el trabajo propio y el de los compañeros.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - El Bucle Controlado**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy aprenderemos a prototipar un faro con una luz gradual y brillante."**
  2.  Introduce la nueva herramienta de programación de hoy. Pregunta a la clase: **"¿Qué pasa si necesitamos un bucle que se ejecute un número exacto de veces, como 100 pasos para pasar de tenue a brillante?"**
  3.  Explica que si bien un bucle 'para siempre' es ideal para la automatización sin fin, a veces necesitamos más control. Aquí es donde entra en juego el **bucle 'For'**. Desglosa sus componentes para ellos: una variable de contador, un valor de inicio, un valor final y un tamaño de paso. Esta es la herramienta perfecta para crear animaciones suaves y graduales.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo el Brillo**
  1.  Ahora que los estudiantes comprenden la mecánica de un bucle 'For', es hora de construir el efecto de brillo gradual.
  2.  Guíalos a través de **las instrucciones para crear el prototipo del faro**, como se detalla en la sección práctica a continuación. Presta mucha atención a cómo usarán dos bucles 'For': uno para contar hacia arriba (aparecer) y un segundo para contar hacia abajo (desaparecer).

  ### **Cierre (5-10 minutos) - El Gran Debate de los Bucles**
  1.  Una vez que todos tengan un faro que funcione con un pulso suave, es hora de una inmersión más profunda en la teoría de los bucles. Este es un momento conceptual clave.
  2.  Usa la sección final para guiar una discusión crítica que compare el bucle 'For' con el bucle 'While' que han visto antes. Desafíalos a reconstruir este proyecto con la herramienta "incorrecta" para ver por qué los programadores eligen diferentes bucles para diferentes trabajos.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "El Bucle FOR"
    type: "learn"
    icon: "book-reader"
    content: |
      Un bucle **‘contar con variable’**, conocido en la mayoría de los lenguajes de programación como un bucle **‘for’**, está diseñado para repetir un bloque de código un número específico y conocido de veces. Utiliza una variable de contador para realizar un seguimiento de su progreso desde un punto de inicio hasta un punto final.
    media: "src/19-lighthouse-with-a-switch/a-what-is.svg"

  - title: "Componentes del bucle FOR"
    type: "learn"
    content: |
      Piensa en un **bucle 'For'** como un plan de misión:
      1.  **Variable**: Tu contador o "agente" que realizará el conteo (p. ej., `i` o `intensidad`).
      2.  **Valor inicial**: El número de inicio para tu contador.
      3.  **Valor final**: El número objetivo donde se detendrá el bucle.
      4.  **Pasos**: Cuánto cambia el contador en cada repetición (p. ej., contando hacia arriba de 1 en 1, o hacia abajo de 1 en 1).
    media: "[600]https://app.protobject.com/generate?contador&es&static&-1"

  - title: "¿Cómo lo usamos para un brillo gradual?"
    type: "learn"
    content: |
      Un bucle **'for'** es perfecto para la animación porque se ejecuta un número conocido de pasos.
      Para hacer que nuestro faro se ilumine gradualmente, usaremos un bucle 'for' que cuenta una variable `intensidad` de 0 a 100. En cada paso, establecemos el brillo de la luz al valor actual de `intensidad`. Esto crea una aparición suave.
      Para atenuarlo, ¡usaremos un segundo bucle 'for' que cuenta `intensidad` de 100 a 0!
    media: 
      - "src/19-lighthouse-with-a-switch/b-cycle.svg"
      - "src/19-lighthouse-with-a-switch/z.lighthoyuse-anim.svg"

  - id: "create"
    title: "Crea el Faro"
    type: "create"
    icon: "cogs"
    heading_text: "Creemos el prototipo que nos permita controlar el faro."
    content: |
      Necesitaremos 2 componentes: una lámpara que sea nuestra fuente de luz y un interruptor para encender y apagar todo el sistema.
    steps:
      - "Presiona <addbutton>Añadir Dispositivo</addbutton>, selecciona <comp>Lámpara</comp> y usa <openwindow>Abrir en esta ventana</openwindow> o un smartphone."
      - "Presiona <addbutton>Añadir Dispositivo</addbutton> y selecciona <comp>Interruptor</comp>."
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
    media: "[700]https://app.protobject.com/generate?a19-lighthouse&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona: FOR vs. WHILE"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Ahora has usado diferentes tipos de bucles. Comparémoslos."
    content: |
      * ¿Cuál es la principal diferencia entre un **bucle 'for'** (contar con variable) y un **bucle 'while'** (repetir mientras)?
      * Un bucle 'for' es ideal cuando conoces los puntos de inicio y final exactos (como de 0 a 100). Un bucle 'while' es ideal cuando solo necesitas esperar a que cambie una condición.
      * ¿Hay casos en los que podrías usar cualquiera de los dos? ¡Absolutamente!
    right_content:
      - text: |
          **Desafío**: ¿Puedes modificar este proyecto para que funcione de la misma manera pero usando bloques **"repetir mientras"** en lugar de bloques "contar con variable"?
      - text: |
          **Pista**: Necesitarías crear tu propia variable `intensidad`, sumar o restar manualmente 1 de ella dentro del bucle, y hacer que el bucle se ejecute *mientras* `intensidad` sea menor que 100 (o mayor que 0).
---