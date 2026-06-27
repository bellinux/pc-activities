input.onLogoEvent(TouchButtonEvent.Touched, function () {
    if (pausado) {
        pausado = false
        tiempo = randint(5, 15)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Baddy), music.PlaybackMode.LoopingInBackground)
        // Temporizador con tiempo inicial aleatorio, valor entre 5 y 15.
        while (tiempo > 0) {
            tiempo += -1
            basic.pause(1000)
        }
        music.stopAllSounds()
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Wawawawaa), music.PlaybackMode.InBackground)
        pausado = true
    }
})
let tiempo = 0
let pausado = false
pausado = true
