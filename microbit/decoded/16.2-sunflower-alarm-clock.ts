basic.forever(function () {
    // Condicional extendido: un condicional simple ejecuta su contenido solo si la condición se cumple, y si no, no hace nada. Aquí hay dos caminos: si la condición se cumple se ejecuta la primera parte; si no, se ejecuta una parte distinta.
    if (input.lightLevel() > 100) {
        basic.showLeds(`
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            `)
        music.ringTone(587)
        basic.pause(200)
        music.ringTone(740)
        basic.pause(500)
    } else {
        music.stopAllSounds()
        basic.clearScreen()
    }
})
