input.onSound(DetectedSound.Loud, function () {
    flama = !(flama)
})
let flama = false
flama = true
basic.forever(function () {
    if (flama) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            `)
        // La posición de los leds está dado por 2 números que los llamaremos X e Y.
        // El número X representará la posición de un led en posición horizontal. Es decir la posición en una fila. 
        // 
        // Por otro lado el número Y representa la altura de un led, es decir su posición en una columna.
        // 
        // Por ejemplo, el led de la esquina superior izquierda tiene posición X = 0 e Y = 0, mientra que la esquina inferior derecha tiene posición X= 4 e Y = 4.
        // Siendo X posición para los lados e Y posición arriba o abajo.
        // Este bloque escoge un número al azar entre 1 y 3 inclusive. 
        // Es decir es como si tuvieras un dado de 3 lados en los que te puede salir el número 1, 2 o 3. Cada vez que se llama o ejecuta este bloque es como si se lanzara un nuevo dado. Por esto es posible que cada vez que se ejecuta un ciclo la posición del fuego puede ser diferente al de la vez anterior, pero también existe la posibilidad de que se escoja el mismo número 3 o 4 veces seguidas.
        led.plot(randint(1, 3), 0)
        basic.pause(200)
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            `)
        led.plot(2, 0)
        basic.pause(200)
    } else {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
