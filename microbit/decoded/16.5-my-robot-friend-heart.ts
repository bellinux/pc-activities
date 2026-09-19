// Cuando pones la micro:bit con el logo hacia arriba, este bloque pone 'pausaLarga' en 200 y 'pausaCorta' en 100: tiempos más cortos y el corazón late más rápido.
input.onGesture(Gesture.LogoUp, function () {
    pausaLarga = 200
    pausaCorta = 100
})
// Cuando pones la micro:bit con el logo hacia abajo, este bloque deja 'pausaLarga' en 600 y 'pausaCorta' en 300: tiempos más largos y el corazón late más lento.
input.onGesture(Gesture.LogoDown, function () {
    pausaLarga = 600
    pausaCorta = 300
})
let pausaCorta = 0
let pausaLarga = 0
pausaLarga = 600
pausaCorta = 300
basic.forever(function () {
    music.ringTone(554)
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
    // El bloque 'pausa (ms)' espera los milisegundos que guarda la variable 'pausaLarga': cambia esa variable y el corazón grande late más rápido o más lento.
    basic.pause(pausaLarga)
    music.stopAllSounds()
    for (let index = 0; index < 2; index++) {
        music.ringTone(494)
        basic.showLeds(`
            . # . # .
            # . # . #
            # . . . #
            . # . # .
            . . # . .
            `)
        // El bloque 'pausa (ms)' espera los milisegundos que guarda la variable 'pausaCorta': así de rápido late el corazón chico.
        basic.pause(pausaCorta)
        music.stopAllSounds()
        music.ringTone(523)
        basic.showLeds(`
            . . . . .
            . # . # .
            . # # # .
            . . # . .
            . . . . .
            `)
        basic.pause(pausaCorta)
        music.stopAllSounds()
    }
})
