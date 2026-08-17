input.onLogoEvent(TouchButtonEvent.Touched, function () {
    if (listo) {
        listo = false
        // Temporizador con tiempo inicial aleatorio, valor entre 5 y 15.
        tiempoRestante = randint(5, 15)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Baddy), music.PlaybackMode.LoopingInBackground)
        while (tiempoRestante > 0) {
            tiempoRestante += -1
            basic.pause(1000)
        }
        music.stopAllSounds()
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Wawawawaa), music.PlaybackMode.InBackground)
        basic.pause(4000)
        music.stopAllSounds()
        listo = true
    }
})
let tiempoRestante = 0
let listo = false
listo = true
