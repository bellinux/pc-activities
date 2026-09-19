// El bloque 'para siempre' repite sin parar toda la secuencia que está dentro.
basic.forever(function () {
    // Este bloque toca un sonido de la frecuencia que le des, en hercios (Hz): cuanto más pequeño el número, más grave; cuanto más grande, más agudo.
    // Suma 440 a la inclinación dividida por 20: 440 Hz es la nota La, el sonido que escuchas con la micro:bit horizontal. Al inclinar la micro:bit, la inclinación va más o menos de −1000 a 1000; dividida por 20, el sonido sube o baja como mucho 50 Hz, entre unos 390 y 490 Hz.
    // Entrega cuánto está inclinada la micro:bit en el eje y.
    music.ringTone(440 + input.acceleration(Dimension.Y) / 20)
    // El bloque 'pausa (ms)' hace una pausa de 100 milisegundos (0,1 segundos), así puedes tocar muchos sonidos distintos en poco tiempo.
    basic.pause(100)
    music.stopAllSounds()
    basic.pause(50)
})
