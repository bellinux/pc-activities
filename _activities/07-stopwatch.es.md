---
layout: activity
title: "Construye Tu Propio Cronómetro"
image: src/07-stopwatch/stopwatch-cover.svg
video: src/videos/07_stopwatch.mp4
video_title: "¿Qué haremos?"
description: "Domina el uso de variables y bucles para construir un cronómetro funcional que cuenta los segundos en la pantalla."
lang: es
permalink: /es/actividades/construye-tu-propio-cronometro/
ref: activity_stopwatch

# ACTIVITY INFO
level: 1
computational_topics:
  - "Bucles"
  - "Variables y Datos"
  - "Temporización y Eventos"
general_topics:
  - "Matemáticas y Lógica"

tags: [Variables, Contador, Bucles, Bucle Principal, Temporización, Cronómetro]

introduction: |
  ¿Alguna vez te has preguntado cómo un juego lleva la puntuación o un reloj cuenta los segundos? Todo se trata de recordar y actualizar un número. En esta misión, descubrirás ese secreto combinando **bucles** y **variables** para construir un cronómetro totalmente funcional. Prepárate para aprender a hacer que tu programa cuente, recuerde y muestre información que cambia con el tiempo.

teacher: |
  ### **Cursos**
  * Grados 3 a 12
  
  ### **Materiales**
  * Teléfono móvil, tableta o computadora
  * Conexión a Internet
  
  ### **Descripción**
  En esta actividad, los estudiantes combinarán bucles y variables para crear una aplicación práctica: un cronómetro. Aprenderán a inicializar, incrementar y mostrar el valor de una variable a lo largo del tiempo, reforzando estos conceptos básicos de la informática.
  
  ### **Objetivos Educativos**
  * Comprender el concepto de una variable como contador.
  * Crear un objeto tecnológico (prototipo) utilizando un dispositivo.
  * Identificar relaciones entre la tecnología y el medio ambiente.
  * Evaluar el trabajo propio y el de los demás.
  * Participar en discusiones y reflexiones para proponer mejoras.
  
  ### **Inicio (10 minutos) - El Desafío de Contar**
  1.  Da la bienvenida a la clase y presenta la actividad: **"Hoy aprenderemos a construir un cronómetro que cuenta los segundos desde cero."**
  2.  Despierta la curiosidad con una pregunta: **"¿Cómo creen que una computadora 'recuerda' a qué número ha llegado mientras cuenta?"**
  3.  Después de una breve discusión, explica que las computadoras, al igual que nosotros, pueden 'olvidar' si no tienen un lugar donde almacenar información. Esta es la oportunidad perfecta para introducir el concepto de variable como una 'caja de memoria' para nuestro programa. Exploremos cómo funciona.

  {{learn}}
  
  ### **Desarrollo (20-30 minutos) - Construyendo el Contador**
  1.  Ahora que la teoría es sólida, es hora de construir el cronómetro y ver estos conceptos en acción. Este proyecto es un fantástico ejemplo de cómo los bucles y las variables trabajan juntos.
  2.  Guía a los estudiantes a través de **las instrucciones para configurar la variable y crear el bucle de conteo**, como se detalla en la sección práctica a continuación.
  3.  **Nota para el profesor:** Experimenta con la actividad antes de la clase para anticipar preguntas.

  ### **Cierre (5-10 minutos) - Reflexión y Mejoras**
  1.  Una vez que todos tengan un cronómetro funcionando, es hora de reflexionar sobre la poderosa herramienta que acaban de usar y pensar en cómo hacer su proyecto aún mejor.
  2.  Usa la sección final para guiar una discusión sobre otros usos de las variables y para introducir una nueva y desafiante característica para su cronómetro: ¡agregar minutos!
  
  {{reflect}}
  
  #### **Información adicional para el profesor**
  La solución al desafío propuesto en la sección de reflexión está disponible en [este enlace](https://app.protobject.com/generate?cronometro-desafio). Úsala como referencia para guiar a los estudiantes que puedan tener dificultades.

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "¿Cómo funciona un cronómetro?"
    type: "learn"
    icon: "book-reader"
    content: |
      Un cronómetro tiene un trabajo simple: contar los segundos que pasan. Cada segundo, esencialmente dice: "**Oye, pasó otro segundo. Sumaré 1 al número total de segundos que ya he contado.**"
      Entonces, si el cronómetro está en 9 segundos, después de que pase un segundo más, calcula 9 + 1 = 10 segundos. Este proceso se repite una y otra vez... **¡Es un trabajo perfecto para un bucle!**
    media: "src/07-stopwatch/a-count.svg"
  
  - title: "¿Y si perdemos la cuenta?"
    type: "learn"
    content: |
      ¿Alguna vez has estado contando algo y has olvidado el último número en el que estabas? ¡Tienes que empezar de nuevo! **Una computadora puede tener el mismo problema.**
      Para evitar esto, probablemente escribirías el número. Luego, para continuar contando, solo mirarías el número, sumarías 1 y escribirías el nuevo total. ¡Estás almacenando un valor que cambia con el tiempo!
    media: "src/07-stopwatch/a-count-lost.svg"

  - title: "¿Cómo lo 'anota' la computadora?"
    type: "learn"
    content: |
      Para resolver este problema de memoria, usamos una herramienta de programación fundamental: una **Variable**.
      Piensa en una variable como una pequeña caja dentro de la memoria de la computadora donde puedes almacenar algo. Para mantener las cosas organizadas y recordar lo que hay dentro, le das un nombre a la caja.
      Al usar una variable, podemos hacer que nuestra computadora lleve la cuenta sin olvidar nunca en qué número está.
    media: "src/07-stopwatch/a-num-var.es.svg"

  - title: "¿Cómo la usamos?"
    type: "learn"
    content: |
      Primero, necesitamos crear nuestra variable y darle un nombre para saber para qué sirve. En este caso, llamémosla "**tiempo**".
      A continuación, debemos darle un valor inicial. Como un cronómetro comienza a contar desde 0, al principio de nuestro programa, estableceremos la variable "**tiempo**" en 0.
    media: "src/07-stopwatch/a-num-var-time.es.svg"

  - title: "Las variables... ¡Varían!"
    type: "learn"
    content: |
      Como su nombre indica, el valor dentro de una variable puede cambiar, o "variar". Podemos sacar el valor, cambiarlo y luego guardar el nuevo valor en la misma variable.
      Para nuestro cronómetro, cada vez que se ejecute nuestro bucle principal, le diremos al programa que sume 1 al valor de la variable "**tiempo**". **¡Y así, estamos contando!**
    media: "src/07-stopwatch/a-var-change.es.svg"

  - title: "¡Manos a la obra!"
    type: "learn"
    content: |
      Para construir nuestro cronómetro, comenzaremos creando una variable llamada "tiempo" y estableciendo su valor inicial en 0. Luego, crearemos un bucle que se repite una y otra vez. Dentro del bucle, aumentaremos el valor de nuestra variable "tiempo" en 1 y luego esperaremos un segundo.
    media: "src/a.working.svg"

  - id: "create"
    title: "Crear"
    type: "create"
    icon: "cogs"
    heading_text: "Ahora construiremos nuestro propio cronómetro."
    ready_message: "Ahora estamos listos para escribir el código."
    steps:
      - "Presiona <addbutton>Añadir dispositivo</addbutton> y selecciona el componente <comp>DibujarEscribir</comp>. Llamémoslo **Cronómetro** para poder escribir los números en la pantalla."
      - "Escanea el código <qr>."
      - "Recuerda que si no tienes un smartphone para escanear los códigos **QR**, puedes presionar <openwindow>Abrir en esta ventana</openwindow> para abrir los componentes en la misma computadora."

  - title: "Composición del Código"
    type: "code-composition"
    icon: "code"
    content: |
      Haz clic en el símbolo del signo de interrogación para abrir los comentarios que explican el código.
      Las variables se gestionan en la categoría <category>Variables</category>.
    media: "https://app.protobject.com/generate?a07-stopwatch&es&dynamic&-1"


  - id: "reflect"
    title: "¿Qué más podemos inventar?"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Respondamos las siguientes preguntas:"
    content: |
      * Además de números, ¿qué otros tipos de información podríamos almacenar en una variable?
      * ¿Qué otros prototipos podrías construir ahora que sabes cómo hacer un contador?
      * ¿Cómo podríamos hacer que nuestro cronómetro cuente también los minutos además de los segundos?
    right_content:
      - text: |
          **Desafío**: ¡Mejoremos nuestro cronómetro para incluir los minutos!
      - text: |
          **Pista**: ¿Cuántos segundos hay en un minuto? Es posible que necesites una segunda variable para rastrear los minutos. ¿Podría un bucle *dentro* de tu bucle principal ayudarte a contar los segundos hasta 60 antes de sumar uno a tu contador de minutos?
---