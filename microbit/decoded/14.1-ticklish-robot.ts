// Cuando el micrófono del dispositivo detecta un sonido fuerte, se ejecutarán las instrucciones dentro del bloque.
input.onSound(DetectedSound.Loud, function () {
    // Reproduce un sonido predeterminado.
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.BaDing), music.PlaybackMode.LoopingInBackground)
    for (let index = 0; index < 8; index++) {
        basic.showLeds(`
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            . . . . .
            `)
        basic.pause(100)
        basic.showLeds(`
            . # . # .
            . . . . .
            . . . . .
            # . . . #
            . # # # .
            `)
        basic.pause(100)
    }
    // Corta la risa; sin este bloque, la melodía se repetiría sin parar.
    music.stopMelody(MelodyStopOptions.All)
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
