// Cuando el micrófono del dispositivo detecta un sonido fuerte, se ejecutarán las instrucciones dentro del bloque.
input.onSound(DetectedSound.Loud, function () {
    // Reproduce un sonido predeterminado.
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Nyan), music.PlaybackMode.InBackground)
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
    // En caso de que el sonido reproducido al inicio dure más que el bloque anterior, este bloque fuerza a detenerlo para evitar que continue sonado cuando no debería.
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
