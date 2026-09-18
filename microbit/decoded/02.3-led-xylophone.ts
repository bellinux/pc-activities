basic.forever(function () {
    basic.clearScreen()
    // Dibuja un punto según la inclinación: con la micro:bit horizontal queda en el centro, y mientras más la inclinas, más se acerca al borde de la pantalla.
    // Convierte la inclinación en la posición del punto: la divide por 450 y la redondea, así queda entre −2 y 2, y le suma 2, el centro de la pantalla. Resultado: una posición del 0 al 4.
    led.plot(2 + Math.round(input.acceleration(Dimension.X) / 450), 2)
    music.ringTone(440 + input.acceleration(Dimension.X) / 20)
    basic.pause(100)
    music.stopAllSounds()
    basic.pause(50)
})
