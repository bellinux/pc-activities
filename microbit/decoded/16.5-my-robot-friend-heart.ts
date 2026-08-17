// Este bloque detecta el momento en cambia la posición del dispositivo, cuando lo hace se editan las variables "pausaLarga" y "pausaCorta". Al inclinar el dispositivo hacia esta dirección, la velocidad de latido aumentará ya que los tiempos son más cortos.
input.onGesture(Gesture.LogoUp, function () {
    pausaLarga = 100
    pausaCorta = 10
})
// Este bloque detecta el momento en cambia la posición del dispositivo, cuando lo hace se editan las variables "pausaLarga" y "pausaCorta". Al inclinar el dispositivo hacia esta dirección, la velocidad de latido disminuirá ya que los tiempos son más largos.
input.onGesture(Gesture.LogoDown, function () {
    pausaLarga = 500
    pausaCorta = 250
})
let pausaCorta = 0
let pausaLarga = 0
pausaLarga = 500
pausaCorta = 250
basic.forever(function () {
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    music.play(music.tonePlayable(587, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    // Se utiliza la variable "pausaLarga" para cambiar la velocidad de latido del corazón grande dependiendo de la posición del dispositivo.
    basic.pause(pausaLarga)
    music.play(music.tonePlayable(587, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            . # . # .
            # . # . #
            # . . . #
            . # . # .
            . . # . .
            `)
        // Se utiliza la variable "pausaCorta" para cambiar la velocidad de latido del corazón chico dependiendo de la posición del dispositivo.
        basic.pause(pausaCorta)
        basic.showLeds(`
            . . . . .
            . # . # .
            . # # # .
            . . # . .
            . . . . .
            `)
        basic.pause(pausaCorta)
    }
})
