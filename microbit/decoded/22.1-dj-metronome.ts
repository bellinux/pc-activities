let tiempoTranscurrido = 0
let intervaloPulso = 0
let bpm = 0
let ultimoPulso = 0
basic.forever(function () {
    bpm = input.acceleration(Dimension.X) + 600
    intervaloPulso = 60000 / bpm
    tiempoTranscurrido = input.runningTime() - ultimoPulso
    if (tiempoTranscurrido > intervaloPulso) {
        // Reproduce un tono específico, en este caso simulará la frecuencia de un metrónomo.
        music.play(music.tonePlayable(233, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        ultimoPulso = input.runningTime()
    }
})
