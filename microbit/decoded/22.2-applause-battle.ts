input.onSound(DetectedSound.Loud, function () {
    if (activo) {
        inicio = input.runningTime()
    }
})
let activo = false
let inicio = 0
inicio = 0
activo = true
basic.forever(function () {
    if (inicio > 0) {
        // Muestra la cantidad de segundos en los que persiste un sonido, en este caso mediremos cuanto es la duración de una cantidad de aplausos.
        basic.showNumber((input.runningTime() - inicio) / 1000)
        // Si los aplausos se detienen termina el temporizador y finaliza la medición.
        if (input.soundLevel() < 5) {
            inicio = 0
            activo = false
            basic.pause(5000)
            activo = true
        }
    }
})
