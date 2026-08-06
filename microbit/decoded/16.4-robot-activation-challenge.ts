input.onLogoEvent(TouchButtonEvent.Touched, function () {
    // Aumenta en 1 el valor de la variable "Toques". Cada vez que se presione el botón la cantidad aumenta en 1, es decir la variable cuenta la cantidad de veces que se aprieta el botón.
    energia += 1
})
// Inicia la variable "Toques" con valor inicial = 0.
let energia = 0
basic.forever(function () {
    if (energia < 5) {
        led.plot(1, 5 - energia)
        led.plot(2, 5 - energia)
        led.plot(3, 5 - energia)
    } else {
        basic.clearScreen()
        images.iconImage(IconNames.Happy).showImage(0)
        music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
    }
})
