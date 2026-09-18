// El bloque 'para siempre' ejecuta una y otra vez, sin parar, la secuencia que tiene dentro.
basic.forever(function () {
    music.ringTone(587)
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    // El bloque 'pausa (ms)' hace una pausa del tiempo que tú elijas antes de pasar a la orden siguiente. 'mostrar LEDs' ya espera 400 ms por su cuenta: por eso aquí bastan 500 ms para que el corazón grande dure unos 900.
    basic.pause(500)
    music.stopAllSounds()
    // Este bloque repite lo que tiene dentro la cantidad de veces que tú elijas.
    for (let index = 0; index < 2; index++) {
        basic.showLeds(`
            . # . # .
            # . # . #
            # . . . #
            . # . # .
            . . # . .
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . # . # .
            . # # # .
            . . # . .
            . . . . .
            `)
        basic.pause(100)
    }
})
