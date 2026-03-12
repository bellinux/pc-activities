---
layout: activity
title: "Mezclando Colores RGB"
image: src/14-colors-on-the-screen/14.colores-pantalla2.svg
video: src/videos/14_color_mix.mp4
video_title: "¿Qué haremos?"
description: "¡Conviértete en un artista digital! Usa tres perillas para controlar los canales Rojo, Verde y Azul y mezcla cualquier color que puedas imaginar."
lang: es
permalink: /es/actividades/mezclando-colores-rgb/
ref: activity_colors_on_the_screen

# ACTIVITY INFO
level: 1
computational_topics:
  - "Sensores e Input"
  - "Bucles"
general_topics:
  - "Arte y Música"
  - "Ciencia y Tecnología"

tags: [Teoría del Color, RGB, Potenciómetro, Bucle Principal, Entrada Analógica, Mezcla de Colores]

introduction: |
  ¿Cómo es que la pantalla de tu teléfono o televisor crea millones de colores diferentes si solo usa tres tipos de luces diminutas? ¡Mezclándolos! En esta misión, te convertirás en un artista digital y un científico del color. Tomarás el control de los tres colores primarios de la luz —**Rojo**, **Verde** y **Azul (RGB)**— usando tres perillas separadas para mezclar cualquier color que puedas imaginar y dominar el arcoíris digital.

teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender el concepto de color y cómo se representa digitalmente (RGB).
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar el trabajo propio y el de los demás individualmente o en equipo.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - La Ciencia del Color**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy aprenderemos cómo las pantallas crean cada color que han visto."**
  2.  Haz una pregunta guía: **"¿Cómo creen que sus ojos ven el color de una manzana? ¿Y en qué se diferencia de cómo una pantalla *crea* el color?"**
  3.  Esta discusión llevará naturalmente a la idea de luz reflejada versus luz emitida. Explica que las pantallas funcionan *sumando* luz, lo cual es el momento perfecto para introducir los dos principales modelos de color: Aditivo (para pantallas) y Sustractivo (para impresión).

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Mezclando el Arcoíris**
  1.  Ahora que los estudiantes tienen una sólida comprensión de la teoría del color RGB, es hora de ponerla en práctica y convertirse en mezcladores de colores digitales.
  2.  Guíalos a través de **las instrucciones para configurar su controlador de tres perillas y programar la lógica de mezcla de colores**, como se detalla en la sección práctica a continuación. Este es un gran ejercicio para manejar múltiples entradas en tiempo real a la vez.

  ### **Cierre (5-10 minutos) - Convirtiéndose en un Experto en Color**
  1.  Una vez que todos estén experimentando con la creación de diferentes colores, reúne al grupo para una reflexión final sobre lo que han aprendido.
  2.  Usa la sección final para reforzar los conceptos básicos de la teoría del color y para desafiarlos a crear una lámpara que cambie de color automáticamente, sin ninguna perilla.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Cómo vemos los colores?"
    type: "learn"
    icon: "book-reader"
    content: |
      Cuando la luz incide en un objeto, como una manzana, la superficie del objeto absorbe la mayor parte de la luz pero refleja una parte. Nuestros ojos ven esta luz reflejada.
      Si vemos una manzana **roja**, significa que su piel está absorbiendo todos los colores *excepto* el rojo. La luz roja rebota, llega a nuestros ojos y nuestro cerebro dice: "¡Eso es rojo!"
    media: "src/14-colors-on-the-screen/a.reflection2.svg"

  - title: "¿Cómo mezclamos los colores?"
    type: "learn"
    content: |
      Para crear colores con luz, tenemos que mezclar diferentes **rayos de luz**. Si mezclamos **todos** los colores de la luz, obtenemos **luz blanca** pura. La ausencia total de luz es el **negro**.
      ¡Puedes ver esto en la naturaleza! Después de llover, pequeñas gotas de agua en el aire pueden actuar como prismas y **separar** la luz solar blanca en todos sus colores componentes, ¡creando un **arcoíris**!
    media: "src/14-colors-on-the-screen/b.color_.freedom2.svg"

  - title: "Síntesis Sustractiva (Pintura y Tinta)"
    type: "learn"
    content: |
      En este modelo, el color de un objeto depende de la luz que **refleja**. Los colores primarios son Cian, Magenta y Amarillo. Debido a que este modelo funciona *restando* (absorbiendo) luz, la mezcla de los tres colores da como resultado el **Negro**. Este modelo se utiliza para cosas que no emiten su propia luz, como la impresión de fotografías, tintes y pinturas.
    media: "src/14-colors-on-the-screen/c-sustractive.es.svg"
  
  - title: "Síntesis Aditiva (Pantallas y Luz)"
    type: "learn"
    content: |
      En este modelo, el color se crea **sumando** diferentes luces. Los colores primarios son **Rojo, Verde y Azul (RGB)**.
      - **Rojo + Verde** = **Amarillo**
      - **Verde + Azul** = **Cian**
      - **Rojo + Azul** = **Magenta**
      Como estamos mezclando luz pura, la combinación de los tres a máxima intensidad da como resultado la **Luz Blanca**. Este modelo se utiliza para todas las pantallas, como televisores, teléfonos y monitores de computadora.
    media: "src/14-colors-on-the-screen/d-additive.es.svg"

  - title: "¿Cómo usa un monitor el RGB?"
    type: "learn"
    content: |
      Tu pantalla está hecha de millones de pequeños puntos llamados píxeles. Cada píxel es en realidad un equipo de tres LED aún más pequeños: uno **R**ojo, uno **V**erde y uno **A**zul.
      Para crear un color específico para ese píxel, digamos, morado, la pantalla le dice a los LED rojo y azul que se enciendan brillantemente, y al verde que permanezca tenue. ¡Multiplica ese proceso por millones de píxeles y obtendrás una imagen completa y rica!
    media: "src/14-colors-on-the-screen/e-pixels.svg"

  - id: "create"
    title: "¡Juguemos con los Colores!"
    type: "create"
    icon: "cogs"
    heading_text: "Creemos un prototipo que nos permita mezclar y crear cualquier color de luz."
    content: |
      Necesitaremos 4 componentes: 1 lámpara para mostrar el color y 3 perillas para controlar cada color primario (Rojo, Verde y Azul).
    steps:
      - "Presiona <addbutton>Añadir dispositivo</addbutton>, selecciona <comp>Lámpara</comp> y presiona <openwindow>Abrir en esta ventana</openwindow>."
      - "Presiona <addbutton>Añadir dispositivo</addbutton>, selecciona <comp>Perilla</comp> y escanea el código <qr> con un smartphone para controlar el color **rojo**."
      - "Añade dos componentes más de <comp>Perilla</comp> en otros dos smartphones para controlar los colores **verde** y **azul**."
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
    media: "[700]https://app.protobject.com/generate?a14-colors&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "¡Ahora eres un maestro del arcoíris digital!"
    content: |
      * ¿Cuáles son las 'recetas' RGB para algunos de tus colores favoritos, como el naranja, el rosa o el turquesa? ¡Experimenta y descúbrelo!
      * Cuando editas una foto en una aplicación, ¿estás usando el modelo de color Aditivo o Sustractivo? ¿Y cuando mezclas pintura para un proyecto de arte?
    right_content:
      - text: |
          **Desafío**: ¡Creemos una lámpara que cambie gradualmente a través de todos los colores del arcoíris por sí sola, sin ser controlada por perillas!
      - text: |
          **Pista**: Podrías usar bucles y variables para aumentar y disminuir lentamente los valores de Rojo, Verde y Azul con el tiempo.
---