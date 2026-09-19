// 'al detectar el sonido alto' avisa que alguien ha empezado a gritar, y entonces ponemos 'partidaEnCurso' en verdadero.
input.onSound(DetectedSound.Loud, function () {
    partidaEnCurso = true
})
let fila = 0
let columna = 0
let partidaEnCurso = false
// Creamos la variable 'partidaEnCurso' y la ponemos en falso: al empezar, no hay ninguna partida en curso.
partidaEnCurso = false
basic.forever(function () {
    if (partidaEnCurso) {
        columna = 0
        fila = 0
        // 'mientras' da vueltas mientras el nivel de sonido sea 20 o más, o sea mientras dura el grito, y sale cuando te callas.
        while (input.soundLevel() >= 20) {
            // Encendemos un LED en la columna y la fila de ahora: cuanto más largo es el grito, más LEDs se encienden, hasta llenar la pantalla.
            led.plot(columna, fila)
            // 'pausa (ms) 200' espera un momento antes del siguiente LED: cada LED encendido vale 200 milisegundos de grito, así que la pantalla se llena en 5 segundos.
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
        // Cuando termina el grito suenan tres notas que suben (do, mi, sol): la última se queda 5 segundos mientras miras el resultado.
        music.ringTone(262)
        basic.pause(200)
        music.ringTone(330)
        basic.pause(200)
        music.ringTone(392)
        basic.pause(5000)
        music.stopAllSounds()
        // Apagamos toda la pantalla para dejarla lista para el próximo grito.
        basic.clearScreen()
        partidaEnCurso = false
    }
})
