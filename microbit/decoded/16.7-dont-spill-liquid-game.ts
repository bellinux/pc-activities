let centradoY = false
let centradoX = false
let ledY = 0
let yDesplazado = 0
let ledX = 0
let xDesplazado = 0
let debeSonarAlarma = true
basic.forever(function () {
    xDesplazado = input.acceleration(Dimension.X) + 1023
    ledX = Math.ceil(xDesplazado * 4 / 2046)
    yDesplazado = input.acceleration(Dimension.Y) + 1023
    ledY = Math.ceil(yDesplazado * 4 / 2046)
    centradoX = ledX >= 1 && ledX <= 3
    centradoY = ledY >= 1 && ledY <= 3
    basic.clearScreen()
    if (centradoX && centradoY) {
        led.plot(ledX, ledY)
        if (debeSonarAlarma) {
            music.play(music.tonePlayable(175, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
            basic.pause(100)
            debeSonarAlarma = false
        }
    } else {
        led.plot(ledX, ledY)
        music.stopMelody(MelodyStopOptions.All)
        basic.pause(100)
        music.play(music.tonePlayable(587, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
        debeSonarAlarma = true
    }
})
