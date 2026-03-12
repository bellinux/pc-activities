---
layout: activity
title: "El Interruptor: ¿Encendido o Apagado?"
image: src/09-turn-on-the-light/09.enciende-luz.svg
video: src/videos/09_light_switch.mp4
video_title: "¿Qué haremos?"
description: "Explora una lógica más avanzada con condicionales 'Si-Entonces-Sino' para crear un interruptor de luz totalmente funcional."
lang: es
permalink: /es/actividades/el-interruptor-encendido-o-apagado/
ref: activity_turn_on_the_light

# ACTIVITY INFO
level: 1
computational_topics:
  - "Condicionales y Lógica"
  - "Bucles"
general_topics:
  - "Matemáticas y Lógica"

tags: [Condicionales, Si-Entonces-Sino, Bucle Principal, Interruptor, Interfaz de Usuario]

introduction: |
  Hasta ahora, hemos dicho a nuestros programas 'SI sucede esto, ENTONCES haz aquello'. Pero, ¿qué pasa con el 'si no'? En el mundo real, las acciones a menudo tienen dos caras: encendido o apagado, bloqueado o desbloqueado, verdadero o falso. En esta misión, mejorarás tus habilidades lógicas con el condicional **'SI... ENTONCES... SINO'**. Prepárate para construir un interruptor de luz totalmente funcional que sepa exactamente qué hacer, ya sea que el interruptor esté encendido *o* apagado.

teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender los conceptos de los condicionales "si/entonces/sino".
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo que los rodea.
  * Evaluar el trabajo personal y el de los compañeros.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - El Poder de 'Sino'**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy aprenderemos a construir un interruptor de luz totalmente funcional con Protobject."**
  2.  Comienza repasando el condicional simple 'SI/ENTONCES'. Luego, introduce un problema más complejo con una analogía: **"Imagina que vas a la tienda por tu snack favorito. SI lo tienen, ENTONCES lo compras. Pero, ¿y si *no* lo tienen? ¿Qué haces SINO (de lo contrario)?"**
  3.  Esto introduce la necesidad de una acción alternativa. Explica que esta lógica 'SI/ENTONCES/SINO' es crucial para crear programas interactivos, como el interruptor de luz que construiremos hoy.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Programando una Elección**
  1.  Ahora que los estudiantes comprenden la lógica de elegir entre dos acciones diferentes, es hora de programar su interruptor digital.
  2.  Guíalos a través de **las instrucciones para construir el programa 'SI/ENTONCES/SINO'**, como se detalla en la sección práctica a continuación. Presta especial atención a cómo el bloque 'ENCENDER' va en la ranura 'HACER' y el bloque 'APAGAR' va en la ranura 'SINO', representando las dos opciones.

  ### **Cierre (5-10 minutos) - Viendo 'SI/SINO' en Todas Partes**
  1.  Una vez que todos tengan un interruptor que funcione, anímalos a pensar en cómo esta lógica de dos partes se aplica al mundo que los rodea.
  2.  Usa la sección final para iniciar una sesión de lluvia de ideas sobre otros escenarios 'SI/ENTONCES/SINO' y para desafiarlos a mejorar su proyecto actual con sonido.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Mejorando Nuestra Lógica"
    type: "learn"
    icon: "book-reader"
    content: |
      Hemos visto cómo funciona un condicional simple: **SI** una condición es verdadera, **ENTONCES** ocurre una acción. Pero, ¿y si la condición es *falsa*? Generalmente, el programa simplemente no hace nada.
      Para hacer nuestro código más inteligente, podemos agregar una segunda parte: un **SINO**.
      La estructura completa, “si, entonces, sino”, le da a la computadora un conjunto completo de instrucciones: “**si** algo es verdadero, **entonces** haz esto; **sino** (de lo contrario), haz algo completamente diferente.”
    media: "src/09-turn-on-the-light/a-if-else-condition.es.svg"

  - title: "SI está presionado, ENTONCES encendido, SINO apagado."
    type: "learn"
    content: |
      Un interruptor de luz es un ejemplo perfecto de esto. La lógica es simple: “**si** el interruptor está activo, **entonces** enciende la luz; **sino**, apaga la luz.”
      Esto significa que si el programa detecta que el interruptor está activo, ejecutará la acción en la parte "entonces" (o "hacer"). Pero si el interruptor *no* está activo, ejecutará la acción en la parte "sino" en su lugar.
      ¿Y cómo hacemos que nuestro programa verifique el interruptor constantemente? ¡Con el **bucle principal**, por supuesto!
    media: "src/09-turn-on-the-light/a-if-else-condition-lamp.es.svg"

  - id: "create"
    title: "Crea una Lámpara con un Interruptor"
    type: "create"
    icon: "cogs"
    heading_text: "Creemos un prototipo que nos permita encender una luz presionando un botón."
    content: |
      Primero, agregaremos dos componentes: uno que actúe como nuestro interruptor y un segundo que sea nuestra luz.
    steps:
      - "Presiona <addbutton>Añadir Dispositivo</addbutton> y selecciona <comp>Lámpara</comp>."
      - "Presiona de nuevo <addbutton>Añadir Dispositivo</addbutton> y selecciona <comp>Interruptor</comp>."
      - "Recuerda que si no tienes smartphones para escanear los códigos <qr>, puedes presionar <openwindow>Abrir en esta ventana</openwindow> para abrir los componentes en la misma computadora."
    right_content:
      - text: |
          **Consejo**: En Protobject, puedes agregar más componentes en el mismo smartphone presionando el botón *SCAN* tantas veces como necesites.
      - media: "src/general-scan-button.svg"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
    media: "[700]https://app.protobject.com/generate?a09-lampswitch&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "¡Has construido un programa que puede tomar una decisión!"
    content: |
      Esta lógica 'SI/ENTONCES/SINO' es uno de los conceptos más importantes de toda la programación.
      *Piensa en tu vida diaria o en tus aplicaciones favoritas. ¿Dónde ves este tipo de elección de dos partes? (ej. SI una contraseña es correcta, ENTONCES inicia sesión, SINO muestra un mensaje de error).* 
    right_content:
      - text: |
          **Desafío**: Mejora este proyecto agregando música que se reproduzca *solo* cuando la luz esté encendida.
      - text: |
          **Pista**: Necesitarás el componente <comp>ReproductorSonido</comp>. ¿Dónde en tu bloque SI/SINO pondrías los comandos 'reproducir sonido' y 'detener sonido'?
---