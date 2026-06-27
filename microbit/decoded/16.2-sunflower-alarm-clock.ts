basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.forever(function () {
    // Este bloque es un condicional extendido, en la actividad anterior teníamos un bloque que ejecutaba su contenido si se cumple la condición, en este caso se extiende el bloque condicional y se le da la instrucción de que si se cumple la condición se ejecuta la primera parte del bloque, pero si no se cumple se ejecuta otra parte diferente. 
    // 
    // En la actividad anterior si no se cumplía la condición no pasaba nada más que no ejecutar lo de dentro, en este caso si no se cumple se ejecuta una serie de instrucciones específicas.
    if (input.lightLevel() > 100) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Prelude), music.PlaybackMode.LoopingInBackground)
        basic.showLeds(`
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            `)
    } else {
        music.stopAllSounds()
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
