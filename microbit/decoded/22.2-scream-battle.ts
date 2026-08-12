input.onSound(DetectedSound.Loud, function () {
    detectado = true
})
let detectado = false
detectado = false
basic.forever(function () {
    if (detectado) {
        while (input.soundLevel() >= 5) {
            for (let fila = 0; fila <= 4; fila++) {
                for (let columna = 0; columna <= 4; columna++) {
                    if (input.soundLevel() >= 5) {
                        led.plot(columna, fila)
                        music.play(music.builtinPlayableSoundEffect(soundExpression.happy), music.PlaybackMode.UntilDone)
                        basic.pause(500)
                    }
                }
            }
        }
        music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.LoopingInBackground)
        basic.pause(5000)
        music.stopAllSounds()
        basic.clearScreen()
        detectado = false
    }
})
