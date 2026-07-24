basic.showLeds(`
    # . # . #
    . # . # .
    # . # . #
    . # . # .
    # . # . #
    `)
basic.forever(function () {
    // Este bloque ajusta el nivel de brillo de los leds. Toma valores entre 0 y 255, donde 0 es el silencio absoluto y 255 es ruido máximo.
    // Este bloque utiliza el micrófono del dispositivo, un sonido muy fuerte será representado con un valor de 255 mientras que el silencio absoluto será representado con un valor de 0.
    led.setBrightness(input.soundLevel())
})
