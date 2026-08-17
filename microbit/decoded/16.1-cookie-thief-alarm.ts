basic.forever(function () {
    // Este es un bloque condicional, ¿Qué quiere decir esto? Es un bloque que se ejecuta o no dependiendo de una condición que nosotros propongamos.
    // En este caso la condición es que la inclinación debe ser superior a cierto valor, al superarse el valor la condición se cumple y por lo tanto se ejecutan todas las instrucciones en el interior de nuestro bloque condicional.
    if (input.acceleration(Dimension.Y) > 400) {
        // Encender la alarma
        basic.showLeds(`
            # . . # #
            . # . # .
            . . . # .
            . # . # .
            # . . # #
            `)
        music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.LoopingInBackground)
        // Dejarla sonando
        basic.pause(6000)
        // Apagar lo que encendimos
        basic.clearScreen()
        music.stopAllSounds()
    }
})
