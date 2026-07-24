# Equivalencia entre Protobject y Microbit

Documento para registrar observaciones sobre la equivalencia entre las
implementaciones de Protobject y Microbit para cada actividad.

---

## 02.1 - Heart Beat

### Equivalencia general
    Los .ptj y .hex utilizan directamente los mismos elementos para su funcionamiento, la estructura es exactamente igual y el funcionamiento también. Por lo tanto, son equivalentes.


### Componentes

**Protobject**
    - DibujoLED (Para mostrar el corazón)
    - BateríaMusical (Para los latidos)

**Microbit**
    - Pantalla LED (Para mostrar el corazón)
    - Music (Para los latidos)

---

## 02.2 - Xylophone

### Equivalencia general
    La estructura y funcionamiento son los mismos, la única diferencia es que en protobject se debe escalar con un valor distinto la inclinación para obtener el sonido de la nota musical, lo cual no es un problema.

### Componentes

**Protobject**
    - TecladoMusical (Para hacer sonar las notas musicales)
    - Inclinación (Para detectar la inclinación del dispositivo)

**Microbit**
    - Music (Utilizando ring tone para el sonido)
    - Acceleration (El movimiento de la placa)
---

## 02.3 - LED Xylophone

### Equivalencia general
    Ocurre lo mismo que con Xylophone, donde nuevamente la estructura y funcionamiento es exactamente igual (la única diferencia es que en celular, la actividad está hecha para que este sea utilizado en horizontal, pero las coordenadas utilizadas es en base a la posición vertical del teléfono, al final esto no da problemas ya que funciona de igual forma que en microbit al utilizarlo en horizontal), también se escalan de manera distinta ciertos valores, pero como mencioné, es necesario ya que cada sistema es distinto.

### Componentes

**Protobject**
    - TecladoMusical (Para hacer sonar las notas musicales)
    - Inclinación (Para detectar la inclinación del dispositivo)
    - DibujoLED (Para mostrar la posición del led respecto a la inclinación)

**Microbit**
    - Music (Utilizando ring tone para el sonido)
    - Acceleration (El movimiento de la placa)
    - Pantalla LED (También para mostrar la posición del led respecto a la inclinación de la placa)
---

## 03.1 - Music Visualizer

### Equivalencia general
    En este caso la actividad es equivalente en estructura algorítimica, pero no lo era en funcionamiento al 100%, dado que había un problema, donde al no haber ruido, el led no aparecía en pantalla (Esto en protobject), mientras que en Microbit, al no haber ruido, el LED se mostraba en la posición de más a la izquierda. Arreglé la versión de protobject para que funcione de la misma manera, añadiendo un "+ 1" a la posición X, lo cual no cambia la equivalencia, ya que lo importante es que su lógica y funcionamiento sean iguales.

### Componentes

**Protobject**
    - DibujoLED (Para mostrar la posición del led respecto al ruido)
    - NivelRuido (Para recibir el ruido como entrada)

**Microbit**
    - Pantalla LED (Se utilizan para exactamente lo mismo) 
    - SoundLevel 
---

## 14.1 - Ticklish Robot

### Equivalencia general
    No hubo necesidad de cambios, ya son equivalentes lógica y funcionalmente, la única diferencia es que se utilizan distintos sonidos, lo cual no afecta.

### Componentes

**Protobject**
    - NivelRuido (Para detectar aumento de ruido repentino)
    - DibujoLED (Para animar la cara al aumentar el ruido)
    - ReproductorSonido (Para reproducir un sonido al aumentar el ruido)

**Microbit**
    - Input de sonido (Para el nivel de ruido)
    - Pantalla LED (Como el dibujo led)
    - Music (Como reproductor de sonido) 

---

## 16.1 - Cookie Thief Alarm

### Equivalencia general
    Sin cambios, ambos funcionan lógicamente igual, la diferencia es que en Protobject se utiliza el bloque "Al iniciar el programa" para limpiar el dibujo led, pero como en microbit no es necesario, no afecta.

### Componentes

**Protobject**
    - Inclinación (Para detectar si se abrió la caja)
    - DibujoLED (Para mostrar la cara de alerta al abrir la caja)
    - ReproductorSonido (Para hacer sonar la alarma)

**Microbit**
    - Acceleration (Equivalente a inclinación en este contexto)
    - Pantalla Led (equivalente a DibujoLed)
    - Music (Como reproductor de sonido)

---

## 16.2 - Sunflower Alarm Clock

### Equivalencia general
    Sin cambios, solo se diferencian en que en protobject se detecta la luz desde la cámara trasera (al usar un teléfono celular), a diferencia de microbit, que con la placa se detecta desde arriba, a pesar de ello, no causa problemas ya que funciona de la misma manera.

### Componentes

**Protobject**
    - IntensidadLuz (Para detectar nivel de luz)
    - ReproductorSonido (Para colocar música al superar nivel de luz)
    - DibujoLED (Para mostrar girasol al haber luz)

**Microbit**
    - LightLevel (Se utiliza igual que IntensidadLuz)
    - Music (Como reproductor sonido)
    - Pantalla LED (Mismo uso que DibujoLED)
---

## 16.3 - Bat in the Dark

### Equivalencia general
    Exactamente igual que con el caso anterior, no hay diferencias.

### Componentes
    Se utilizan los mismos componentes que en el anterior, pero sin Music y ReproductorSonido.

---

## 16.4 - Robot Activation Challenge

### Equivalencia general
    La actividad en protobject era distinta a la de microbit, por lo que me aseguré de hacer que ambas tengan la misma estructura, lógica y funcionamiento, de modo que ahora sí son equivalentes. Se utilizan distintos valores máximos de energía para la activación dados los tamaños de las pantallas leds de cada dispositivo, pero no afecta.

### Componentes

**Protobject**
    - BotónTáctil (Para aumentar energía)
    - ReproductorSonido (Para colocar música al activar el robot)
    - DibujoLED (Para mostrar cara del robot al activar)

**Microbit**
    - Botón del logo (Como botón táctil)
    - Music (como reproductor de sonido)
    - Pantalla led (como el dibujo led)

---

## 16.5 - My Robot Friend Heart

### Equivalencia general
-

### Componentes

**Protobject**
- 

**Microbit**
- 

### Comentarios
-

---

## 16.6 - Magic Birthday Candle

### Equivalencia general
-

### Componentes

**Protobject**
- 

**Microbit**
- 

### Comentarios
-

---

## 16.7 - Don't Spill Liquid Game

### Equivalencia general
-

### Componentes

**Protobject**
- 

**Microbit**
- 

### Comentarios
-

---

## 17.1 - Magic Clap Switch

### Equivalencia general
-

### Componentes

**Protobject**
- 

**Microbit**
- 

### Comentarios
-

---

## 17.2 - Cinematic Power On

### Equivalencia general
-

### Componentes

**Protobject**
- 

**Microbit**
- 

### Comentarios
-

---

## 19.1 - Digital Hot Potato

### Equivalencia general
-

### Componentes

**Protobject**
- 

**Microbit**
- 

### Comentarios
-

---

## 22.1 - DJ Metronome

### Equivalencia general
-

### Componentes

**Protobject**
- 

**Microbit**
- 

### Comentarios
-

---

## 22.2 - Applause Battle

### Equivalencia general
-

### Componentes

**Protobject**
- 

**Microbit**
- 

### Comentarios
-