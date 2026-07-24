let sonidoFijo = true
basic.forever(function () {
    serial.writeValue("x", Math.round(input.acceleration(Dimension.X) / 250))
    basic.clearScreen()
    if (Math.round(input.acceleration(Dimension.X) / 250) > -2 && Math.round(input.acceleration(Dimension.X) / 250) < 2 && (Math.round(input.acceleration(Dimension.Y) / 250) > -2 && Math.round(input.acceleration(Dimension.Y) / 250) < 2)) {
        led.plot(2 + Math.round(input.acceleration(Dimension.X) / 250), 2 + Math.round(input.acceleration(Dimension.Y) / 250))
        if (sonidoFijo) {
            music.play(music.tonePlayable(175, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
            basic.pause(1000)
            sonidoFijo = false
        }
    } else {
        led.plot(2 + Math.round(input.acceleration(Dimension.X) / 250), 2 + Math.round(input.acceleration(Dimension.Y) / 250))
        sonidoFijo = true
        music.stopMelody(MelodyStopOptions.All)
        basic.pause(100)
        music.play(music.tonePlayable(587, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    }
})
