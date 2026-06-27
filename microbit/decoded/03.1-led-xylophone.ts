basic.forever(function () {
    basic.clearScreen()
    // Dibuja un punto dependiendo de la cantidad de inclinación. Mientras más inclinado, más a los extremos aparecerá el punto.
    // Transforma los datos de inclinación a una aceptable e una posición del dibujo utilizando ejes x e y.
    led.plot(2 + Math.round(input.acceleration(Dimension.X) / 350), 2)
    music.ringTone(input.acceleration(Dimension.X) + 1000)
    basic.pause(100)
})
