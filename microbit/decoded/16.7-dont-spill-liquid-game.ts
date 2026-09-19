let centradoY = false
let centradoX = false
let ledY = 0
let yDesplazado = 0
let ledX = 0
let xDesplazado = 0
// Creamos la variable 'debeSonarAlarma' y la ponemos en verdadero, para recordar que la nota de acierto todavía no ha empezado a sonar.
let debeSonarAlarma = true
basic.forever(function () {
    xDesplazado = input.acceleration(Dimension.X) + 615
    // Convertimos la inclinación de la micro:bit, ya desplazada en 'xDesplazado', en un número del 0 al 4 y lo guardamos en la variable 'ledX': es la posición del LED que se encenderá.
    ledX = Math.ceil(xDesplazado * 4 / 1640)
    yDesplazado = input.acceleration(Dimension.Y) + 615
    ledY = Math.ceil(yDesplazado * 4 / 1640)
    centradoX = ledX >= 1 && ledX <= 3
    centradoY = ledY >= 1 && ledY <= 3
    basic.clearScreen()
    // Este bloque 'si' pregunta si 'centradoX' y 'centradoY' son verdaderas a la vez: si es así, la micro:bit está nivelada.
    if (centradoX && centradoY) {
        led.plot(ledX, ledY)
        if (debeSonarAlarma) {
            // Suena una nota grave y se queda sonando, y la variable 'debeSonarAlarma' pasa a falso para no volver a empezarla en cada vuelta.
            music.ringTone(262)
            debeSonarAlarma = false
        }
    } else {
        led.plot(ledX, ledY)
        basic.pause(100)
        // Si está torcida suena una nota aguda que se para y vuelve a empezar en cada vuelta, así que hace 'pip pip' para avisarte.
        music.ringTone(784)
        basic.pause(100)
        music.stopAllSounds()
        debeSonarAlarma = true
    }
})
