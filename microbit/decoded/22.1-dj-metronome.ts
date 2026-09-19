let tiempoTranscurrido = 0
let intervaloPulso = 0
let bpm = 0
let ultimoPulso = 0
basic.forever(function () {
    // Convierte la inclinación en bpm (pulsos por minuto): con la micro:bit horizontal da 60, y al inclinarla sube o baja como mucho unos 50.
    bpm = input.acceleration(Dimension.X) / 20 + 60
    // Calcula cuántos milisegundos hay entre un pulso y el siguiente: 60000 (los milisegundos de un minuto) dividido por los bpm.
    intervaloPulso = 60000 / bpm
    tiempoTranscurrido = input.runningTime() - ultimoPulso
    // Si el tiempo que pasó desde el último pulso ya supera el intervalo, es hora de un pulso nuevo.
    if (tiempoTranscurrido > intervaloPulso) {
        // Lo primero es guardar el momento de este pulso: así el cronómetro vuelve a empezar justo desde aquí.
        ultimoPulso = input.runningTime()
        // Suena un tic corto, de 100 milisegundos: es el pulso del metrónomo.
        music.ringTone(262)
        basic.pause(100)
        music.stopAllSounds()
    }
})
