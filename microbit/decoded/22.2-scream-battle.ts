input.onSound(DetectedSound.Loud, function () {
    partidaEnCurso = true
})
let fila = 0
let columna = 0
let partidaEnCurso = false
partidaEnCurso = false
basic.forever(function () {
    if (partidaEnCurso) {
        columna = 0
        fila = 0
        while (input.soundLevel() >= 5) {
            led.plot(columna, fila)
            music.play(music.builtinPlayableSoundEffect(soundExpression.happy), music.PlaybackMode.UntilDone)
            basic.pause(200)
            columna = columna + 1
            if (columna > 4) {
                columna = 0
                fila = fila + 1
            }
            if (fila > 4) {
                fila = 0
            }
        }
        music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.LoopingInBackground)
        basic.pause(5000)
        music.stopAllSounds()
        basic.clearScreen()
        partidaEnCurso = false
    }
})
