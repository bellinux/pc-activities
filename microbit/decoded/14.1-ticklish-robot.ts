// Cuando el micrófono del dispositivo detecta un sonido fuerte, se ejecutarán las instrucciones dentro del bloque.
input.onSound(DetectedSound.Loud, function () {
    for (let index = 0; index < 8; index++) {
        basic.showLeds(`
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            . . . . .
            `)
        basic.pause(100)
        music.ringTone(349)
        basic.showLeds(`
            . # . # .
            . . . . .
            . . . . .
            # . . . #
            . # # # .
            `)
        basic.pause(100)
        music.ringTone(330)
    }
    // Corta la risa; sin este bloque, la melodía se repetiría sin parar.
    music.stopAllSounds()
    basic.showLeds(`
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        . . . . .
        `)
})
basic.showLeds(`
    . # . # .
    . . . . .
    . . . . .
    # . . . #
    . # # # .
    `)
