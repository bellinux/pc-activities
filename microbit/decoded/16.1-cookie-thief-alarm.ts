basic.forever(function () {
    // El bloque 'si … entonces' hace una pregunta: ¿la inclinación en x es mayor que 400? Si la respuesta es verdadera, ejecuta todo lo que tiene dentro; si es falsa, se lo salta y sigue vigilando.
    if (input.acceleration(Dimension.X) > 400) {
        // Enciende la alarma: aparece una cara enojada en la pantalla.
        basic.showLeds(`
            # . . # #
            . # . # .
            . . . # .
            . # . # .
            # . . # #
            `)
        // La alarma pita 8 veces: 200 milisegundos de sonido y 500 de silencio.
        for (let index = 0; index < 8; index++) {
            music.ringTone(622)
            basic.pause(200)
            music.stopAllSounds()
            basic.pause(500)
            music.ringTone(622)
        }
        // Al terminar, apaga la pantalla y el sonido: el programa vuelve a vigilar la tapa.
        basic.clearScreen()
        music.stopAllSounds()
    }
})
