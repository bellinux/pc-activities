// Este bloque detecta el momento en cambia la posición del dispositivo, cuando lo hace se editan las variables "latidoGrande" y "latidoPequeño". Dependiendo de la posición la velocidad de latido aumentará (Los tiempos son más largos, es decir las variables toman valores grandes).
// 
// En este bloque específico la velocidad de latidos aumentará.
input.onGesture(Gesture.LogoUp, function () {
    latidoPequeño = 10
    latidoGrande = 100
})
// Este bloque detecta el momento en cambia la posición del dispositivo, cuando lo hace se editan las variables "latidoGrande" y "latidoPequeño". Dependiendo de la posición la velocidad de latido aumentará (Los tiempos son más largos, es decir las variables toman valores grandes).
// 
// En este bloque específico la velocidad de latidos se reducirá.
input.onGesture(Gesture.ScreenUp, function () {
    latidoPequeño = 250
    latidoGrande = 500
})
let latidoGrande = 0
let latidoPequeño = 0
latidoPequeño = 250
latidoGrande = 500
basic.forever(function () {
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    music.play(music.tonePlayable(587, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    // Se utiliza la variable "latidoGrande" para cambiar la velocidad de latido del corazón grande dependiendo de la posición del dispositivo.
    basic.pause(latidoGrande)
    music.play(music.tonePlayable(587, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            . # . # .
            # . # . #
            # . . . #
            . # . # .
            . . # . .
            `)
        // Se utiliza la variable "latidoPequeño" para cambiar la velocidad de latido del corazón chico dependiendo de la posición del dispositivo.
        basic.pause(latidoPequeño)
        basic.showLeds(`
            . . . . .
            . # . # .
            . # # # .
            . . # . .
            . . . . .
            `)
        basic.pause(latidoPequeño)
    }
})
