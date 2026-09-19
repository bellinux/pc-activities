input.onLogoEvent(TouchButtonEvent.Touched, function () {
    // Suma 1 a la variable "energia" cada vez que se toca el logo, así la variable cuenta cuántas veces lo has tocado.
    energia += 1
})
// Empieza la variable "energia" en 0: todavía no se ha tocado el logo ninguna vez.
let energia = 0
basic.forever(function () {
    if (energia < 6) {
        led.plot(1, 5 - energia)
        led.plot(2, 5 - energia)
        led.plot(3, 5 - energia)
    } else {
        basic.showLeds(`
            . # . # .
            . . . . .
            . . . . .
            # . . . #
            . # # # .
            `)
        music.ringTone(294)
        basic.pause(200)
        music.ringTone(370)
        basic.pause(200)
        music.ringTone(440)
        basic.pause(500)
    }
})
