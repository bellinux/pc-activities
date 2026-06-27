let bpm = 0
let ultimoBeat = 0
basic.forever(function () {
    let intervaloBeat = 0
    bpm = input.acceleration(Dimension.X) + 600
    ultimoBeat = 600000 + bpm
    if (input.runningTime() - ultimoBeat > intervaloBeat) {
        // Reproduce un tono específico, en este caso simulará la frecuencia de un metrónomo.
        music.play(music.tonePlayable(233, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        ultimoBeat = input.runningTime()
    }
})
