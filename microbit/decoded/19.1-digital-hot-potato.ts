let listo = false
let tiempoRestante = 0
// Al tocar el logo, 'listo' pasa a verdadero: así el bucle principal sabe que tiene que empezar una ronda.
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    listo = true
})
basic.forever(function () {
    if (listo) {
        // Elige al azar cuántos segundos dura la ronda, entre 5 y 15: nadie sabe cuándo va a explotar la papa.
        tiempoRestante = randint(5, 15)
        // Mientras quede tiempo, en cada vuelta suena un 'tic', se resta 1 a 'tiempoRestante' y se espera un segundo.
        while (tiempoRestante > 0) {
            music.ringTone(208)
            tiempoRestante += -1
            basic.pause(200)
            music.stopAllSounds()
            basic.pause(800)
        }
        music.ringTone(311)
        basic.pause(500)
        music.ringTone(294)
        basic.pause(500)
        music.ringTone(277)
        basic.pause(500)
        music.ringTone(262)
        basic.pause(1000)
        music.stopAllSounds()
        // La ronda terminó: 'listo' vuelve a falso. Si alguien tocó el logo durante la ronda, ese toque no cuenta y el juego espera un toque nuevo.
        listo = false
    }
})
