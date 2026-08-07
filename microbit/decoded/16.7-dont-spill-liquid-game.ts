let inclinacionY = 0
let inclinacionX = 0
let sonidoFijo = true
basic.forever(function () {
    inclinacionX = Math.round(input.acceleration(Dimension.X) / 250)
    inclinacionY = Math.round(input.acceleration(Dimension.Y) / 250)
})
basic.forever(function () {
    basic.clearScreen()
    if (inclinacionX > -2 && inclinacionX < 2 && (inclinacionY > -2 && inclinacionY < 2)) {
        led.plot(2 + inclinacionX, 2 + inclinacionY)
        if (sonidoFijo) {
            music.play(music.tonePlayable(175, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
            basic.pause(1000)
            sonidoFijo = false
        }
    } else {
        led.plot(Math.constrain(2 + inclinacionX, 0, 4), Math.constrain(2 + inclinacionY, 0, 4))
        sonidoFijo = true
        music.stopMelody(MelodyStopOptions.All)
        basic.pause(100)
        music.play(music.tonePlayable(587, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    }
})
