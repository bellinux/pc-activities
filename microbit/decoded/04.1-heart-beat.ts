// Este bloque se encarga de ejecutar infinitamente la secuencia que tiene dentro.
basic.forever(function () {
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    music.play(music.tonePlayable(587, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    // Este tipo de bloque permite esperar una cantidad de tiempo personalizada antes de ejecutar la siguiente orden.
    basic.pause(300)
    music.play(music.tonePlayable(587, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    // Este bloque es como el bloque "repetir para siempre" solo que permite personalizar la cantidad de veces que se tiene que repetir.
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            . # . # .
            # . # . #
            # . . . #
            . # . # .
            . . # . .
            `)
        basic.pause(10)
        basic.showLeds(`
            . . . . .
            . # . # .
            . # # # .
            . . # . .
            . . . . .
            `)
        basic.pause(10)
    }
})
