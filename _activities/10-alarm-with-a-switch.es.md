---
layout: activity
title: "Una Alarma Más Inteligente con Eventos"
image: src/10-alarm-with-a-switch/10.alarma-toque.svg
video: src/videos/10_alarm_switch.mp4
video_title: "¿Qué haremos?"
description: "¡Descubre una forma más eficiente de programar! Aprende cómo los eventos permiten que tu programa reaccione instantáneamente a acciones como presionar un botón."
lang: es
permalink: /es/actividades/una-alarma-mas-inteligente-con-eventos/
ref: activity_alarm_with_a_switch

# ACTIVITY INFO
level: 1
computational_topics:
  - "Temporización y Eventos"
  - "Condicionales y Lógica"
general_topics:
  - "Vida Cotidiana"

tags: [Eventos, Estados, Condicionales, Interruptor, Programación Eficiente]

introduction: |
  Hemos usado bucles para verificar constantemente si algo está sucediendo, pero ¿no es eso un poco ineficiente, como preguntar constantemente "¿Ya llegamos?" en un viaje por carretera? ¡Hay una forma mucho más inteligente! ¿Y si nuestros componentes pudieran simplemente *decirnos* cuándo sucede algo? Bienvenido al poderoso mundo de la **programación basada en eventos**. En esta misión, construirás una alarma que no verifica, sino que *escucha*, haciendo tu código más rápido y profesional.

teacher: |
  ### **Cursos**
  * Grados 3-12

  ### **Materiales**
  * Celular, tableta o computadora
  * Conexión a Internet

  ### **Objetivos Educativos**
  * Comprender el concepto de evento.
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el mundo circundante.
  * Evaluar el trabajo propio y el de los demás.
  * Participar en diálogos y reflexiones sobre ideas de mejora.

  ### **Inicio (10 minutos) - Una Forma Más Inteligente de Escuchar**
  1.  Da la bienvenida a los estudiantes y presenta la actividad del día: **"Hoy aprenderemos a crear una alarma simple que suena cuando presionas un botón, pero usando un método nuevo y más inteligente."**
  2.  Comienza preguntando a la clase: **"¿Cómo funciona realmente un simple botón o interruptor?"** Guíalos hacia la idea de dos estados: ENCENDIDO y APAGADO.
  3.  Luego, introduce el concepto central de hoy: la eficiencia. Pregúntales: **"Usando un bucle, nuestro programa tiene que preguntar constantemente al botón: '¿Estás presionado? ¿Estás presionado?'. ¿Y si el botón pudiera simplemente enviar un mensaje al programa *solo* cuando realmente se presiona?"** Esto introduce el concepto de un **evento** como una notificación, una forma más eficiente de programar.

  {{learn}}

  ### **Desarrollo (20-30 minutos) - Construyendo una Alarma Dirigida por Eventos**
  1.  Ahora que los estudiantes comprenden la diferencia entre verificar constantemente con un bucle y escuchar eficientemente un evento, es hora de construir la alarma más inteligente.
  2.  Guíalos a través de **las instrucciones para construir el programa dirigido por eventos**, como se detalla en la sección práctica a continuación. Enfatiza que la lógica principal de este programa **no** utiliza un bucle "repetir para siempre", porque el evento hace el trabajo por nosotros.

  ### **Cierre (5-10 minutos) - Los Eventos Están en Todas Partes**
  1.  Una vez que todos tengan una alarma funcional y dirigida por eventos, es hora de reflexionar sobre este nuevo y poderoso paradigma de programación.
  2.  Usa la sección final para iniciar una discusión sobre dónde más se usan los eventos en la tecnología moderna (¡cada clic, toque y notificación es un evento!) y para desafiarlos a combinar eventos con variables para agregar una nueva característica.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Cómo funciona un interruptor?"
    type: "learn"
    icon: "book-reader"
    content: |
      Vamos a crear una alarma que se activa con un interruptor. Pero para hacerlo, necesitamos entender cómo 'piensa' un interruptor.
      En programación, un interruptor simple tiene dos posibles **estados**:
      * **Encendido:** El interruptor está activado. Podemos representar este estado con el número **1**.
      * **Apagado:** El interruptor está desactivado. Podemos representarlo con el número **0**.
      Un interruptor solo puede estar en un estado a la vez. Al leer si el estado es 1 o 0, la computadora puede decidir qué hacer a continuación.
    media: "src/10-alarm-with-a-switch/interruptor-animd.svg"

  - title: "¿Cómo sabe la computadora el estado?"
    type: "learn"
    content: |
      La computadora puede ser programada para "escuchar" una señal del interruptor.
      **¡Cada vez que el estado del botón cambia (de Apagado a Encendido, o de Encendido a Apagado), notifica a la computadora!**
      Esta notificación se llama **evento**. Una vez que la computadora recibe el evento, puede ejecutar un fragmento de código específico para reaccionar a él.
    media: "src/10-alarm-with-a-switch/evento-icon.es.it.svg"

  - title: "¿Por qué no usar simplemente un bucle principal?"
    type: "learn"
    content: |
      Usar un **Bucle Principal** para verificar un botón es como un conductor en el asiento trasero que pregunta constantemente: *“¡¿Ya lo presionaste?! ¡¿Y ahora?! ¡¿Ya lo presionaste?!”* incluso cuando no pasa nada. Es repetitivo y desperdicia la energía de la computadora.
      Con los **eventos**, el programa está en silencio. Simplemente espera. El interruptor mismo envía una sola señal a la computadora *solo cuando su estado ha cambiado*. ¡Esto es mucho más eficiente y profesional!
    media: "src/10-alarm-with-a-switch/evento-scheme.es.svg"
  
  - title: "Recibimos el evento… ¿Y ahora qué?"
    type: "learn"
    content: |
      Una vez que el interruptor envía su señal, la computadora puede usar un condicional para decidir qué hacer según el estado actual del interruptor.
      Para nuestra alarma, la lógica es simple: **SI** el nuevo estado del interruptor es **ENCENDIDO**, reproducimos un sonido. **SINO** (lo que significa que su nuevo estado es **APAGADO**), detenemos el sonido.
    media: "src/10-alarm-with-a-switch/if-else-alarm.es.svg"

  - id: "create"
    title: "Crea la Alarma"
    type: "create"
    icon: "cogs"
    heading_text: "Creemos un prototipo que haga sonar una alarma cuando se active un interruptor."
    content: |
      Primero, agregaremos dos componentes que nos permitan (1) activar la alarma y (2) reproducir el sonido.
    steps:
      - "Presiona <addbutton>Añadir dispositivo</addbutton> y selecciona <comp>ReproductorSonido</comp>."
      - "Presiona de nuevo <addbutton>Añadir Dispositivo</addbutton> y selecciona <comp>Interruptor</comp>."
      - "Recuerda que si no tienes un smartphone para escanear los códigos <qr>, puedes hacer clic en <openwindow>Abrir en esta ventana</openwindow>."
    right_content:
      - text: |
          **Consejo**: En Protobject, puedes agregar más componentes en el mismo smartphone presionando el botón *SCAN* tantas veces como necesites.
      - media: "src/general-scan-button.svg"
    ready_message: "¡Estamos listos para empezar a prototipar!"

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el ícono del signo de interrogación para abrir los comentarios que explican el código.
    media: "[700]https://app.protobject.com/generate?a10-alarmswitch&es&dynamic&-1"

  - id: "reflect"
    title: "Reflexiona"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "¡Acabas de aprender una forma más profesional de programar!"
    content: |
      Los eventos son la columna vertebral de todas las interfaces de usuario modernas: cada clic, toque y deslizamiento es un evento.
      *Además de los botones, ¿qué otras cosas en tu teléfono o en un juego podrían desencadenar un evento? (Piensa en notificaciones, la finalización de una descarga, un personaje que toca una moneda, etc.)*
    right_content:
      - text: |
          **Desafío**: ¡Mejoremos nuestra alarma para que cuente y muestre cuántas veces se ha activado!
      - text: |
          **Pista**: Necesitarás una variable para almacenar el conteo y el dispositivo <comp>DibujarEscribir</comp> para mostrarlo en la pantalla. ¿Dónde agregarías `1` a la variable?
---