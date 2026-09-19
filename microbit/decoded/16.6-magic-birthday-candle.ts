input.onSound(DetectedSound.Loud, function () {
    velaEncendida = !(velaEncendida)
})
let velaEncendida = false
velaEncendida = true
basic.forever(function () {
    if (velaEncendida) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            `)
        // En el bloque 'graficar x y', X es la posición de lado a lado e Y la de arriba abajo: la esquina de arriba a la izquierda es X=0, Y=0.
        // El bloque 'escoger al azar' saca un número entre 1 y 3, como un dado de tres caras: la llama puede cambiar de sitio en cada vuelta o repetirse.
        led.plot(randint(1, 3), 0)
        basic.pause(700)
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            `)
        basic.pause(100)
    } else {
        basic.clearScreen()
    }
})
