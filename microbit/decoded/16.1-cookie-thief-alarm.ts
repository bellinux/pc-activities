basic.forever(function () {
    // Este es un bloque condicional, ¿Qué quiere decir esto? Es un bloque que se ejecuta o no dependiendo de una condición que nosotros propongamos.
    // En este caso la condición es que la inclinación debe ser superior a cierto valor, al superarse el valor la condición se cumple y por lo tanto se ejecutan todas las instrucciones en el interior de nuestro bloque condicional.
    if (input.acceleration(Dimension.Y) > 400) {
        // Simula un sonido de alerta de robo.
        music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.LoopingInBackground)
        basic.showLeds(`
            # . . # #
            . # . # .
            . . . # .
            . # . # .
            # . . # #
            `)
        basic.pause(6000)
        basic.clearScreen()
        music.stopAllSounds()
    }
})
