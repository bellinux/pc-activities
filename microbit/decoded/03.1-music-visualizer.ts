basic.forever(function () {
    // Limpia la pantalla antes de realizar el siguiente dibujo.
    basic.clearScreen()
    // Dibuja en la columna X el nivel de ruido. El valor se divide para ajustarlo al rango de la matriz LED y utilizar toda la barra.
    led.plot(2, Math.constrain(4 - input.soundLevel() / 60, 0, 4))
    // Dibuja en la columna X el nivel de ruido. El valor se divide para ajustarlo al rango de la matriz LED y utilizar toda la barra.
    led.plot(1, Math.constrain(4 - input.soundLevel() / 60, 0, 4))
    // Dibuja en la columna X el nivel de ruido. El valor se divide para ajustarlo al rango de la matriz LED y utilizar toda la barra.
    led.plot(3, Math.constrain(4 - input.soundLevel() / 60, 0, 4))
})
