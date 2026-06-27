input.onSound(DetectedSound.Loud, function () {
    estado = !(estado)
    if (estado) {
        // Este bloque crea una variable llamada "columnas". Luego asigna valores desde 0 hasta 4 en aumentos de 1 y cada vez que toma un nuevo valor se ejecutará lo de dentro.
        // 
        // Es decir inicia con columnas = 0, luego ejecuta lo de dentro y al terminar ahora columnas = 1 y se vuelve a ejecutar todo. Una vez columnas = 4 se ejecuta lo de dentro y pasa al siguiente bloque de instrucciones que no esté dentro, en este caso pasa al bloque "graficar x..."
        for (let columnas = 0; columnas <= 4; columnas++) {
            // Este bloque crea una variable llamada "filas". Luego asigna valores desde 0 hasta 4 en aumentos de 1 y cada vez que toma un nuevo valor se ejecutará lo de dentro.
            // 
            // Es decir inicia con filas = 0, luego ejecuta lo de dentro y al terminar ahora filas = 1 y se vuelve a ejecutar todo. Una vez filas = 4 se ejecuta lo de dentro y pasa al siguiente bloque de instrucciones que no esté dentro, en este caso pasa al bloque "graficar x..."
            // 
            // Se puede analizar que por cada vez que el valor de columna cambia se ejecuta 5 veces el bloque donde cambia fila (0, 1, 2, 3, 4) y como columnas cambia 5 veces, el bloque de "graficar x..." se ejecuta 5x5 = 25 veces, que corresponde a la cantidad total de leds.
            for (let filas = 0; filas <= 4; filas++) {
                led.plot(filas, columnas)
                basic.pause(20)
            }
        }
        led.plot(0, 0)
    } else {
        // Este bloque crea una variable llamada "columnas". Luego asigna valores desde 0 hasta 4 en aumentos de 1 y cada vez que toma un nuevo valor se ejecutará lo de dentro.
        // 
        // Es decir inicia con columnas = 0, luego ejecuta lo de dentro y al terminar ahora columnas = 1 y se vuelve a ejecutar todo. Una vez columnas = 4 se ejecuta lo de dentro y pasa al siguiente bloque de instrucciones que no esté dentro, en este caso pasa al bloque "graficar x..."
        for (let columnas = 0; columnas <= 4; columnas++) {
            // Este bloque crea una variable llamada "filas". Luego asigna valores desde 0 hasta 4 en aumentos de 1 y cada vez que toma un nuevo valor se ejecutará lo de dentro.
            // 
            // Es decir inicia con filas = 0, luego ejecuta lo de dentro y al terminar ahora filas = 1 y se vuelve a ejecutar todo. Una vez filas = 4 se ejecuta lo de dentro y pasa al siguiente bloque de instrucciones que no esté dentro, en este caso pasa al bloque "graficar x..."
            // 
            // Se puede analizar que por cada vez que el valor de columna cambia se ejecuta 5 veces el bloque donde cambia fila (0, 1, 2, 3, 4) y como columnas cambia 5 veces, el bloque de "graficar x..." se ejecuta 5x5 = 25 veces, que corresponde a la cantidad total de leds.
            for (let filas = 0; filas <= 4; filas++) {
                led.unplot(filas, columnas)
                basic.pause(20)
            }
        }
    }
})
let estado = false
estado = false
