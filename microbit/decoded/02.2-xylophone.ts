// Bucle principal, repite infinitamente la secuencia porgramada dentro de este bloque.
basic.forever(function () {
    // Este bloque recibe un número entre 0 y 1000 y transforma este valor a un sonido, mientras más pequeño el número más grave el sonido, por el contrario si el número es grande el sonido será agudo. 
    // Se suma 1000 a la inclinación para ajustar el rango de sonido en el teclado musical. El teclado musical solo recibe números positivos, mientras la inclinación puede tener valores negativos por lo que sumamos un valor, en este caso 1000, para que detecte todo el rango de movimiento.
    // Recibe el grado de inclinación del teléfono en el eje x.
    music.ringTone(input.acceleration(Dimension.X) + 1000)
    // Retraso de 0.1 segundos para poder hacer diferentes sonidos en un corto periodo de tiempo.
    basic.pause(100)
})
