let inclinacionY = 0
let inclinacionX = 0
let sonidoFijo = true
basic.forever(function () {
    inclinacionX = Math.ceil((input.acceleration(Dimension.X) + 1023) * 4 / 2046)
    inclinacionY = Math.ceil((input.acceleration(Dimension.Y) + 1023) * 4 / 2046)
})
basic.forever(function () {
    basic.clearScreen()
    if (inclinacionX >= 1 && inclinacionX <= 3 && (inclinacionY >= 1 && inclinacionY <= 3)) {
        led.plot(inclinacionX, inclinacionY)
        if (sonidoFijo) {
            music.play(music.tonePlayable(175, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
            basic.pause(100)
            sonidoFijo = false
        }
    } else {
        led.plot(inclinacionX, inclinacionY)
        sonidoFijo = true
        music.stopMelody(MelodyStopOptions.All)
        basic.pause(100)
        music.play(music.tonePlayable(587, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    }
})
