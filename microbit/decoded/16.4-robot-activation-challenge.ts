input.onLogoEvent(TouchButtonEvent.Touched, function () {
    // Aumenta en 1 el valor de la variable "Toques". Cada vez que se presione el botón la cantidad aumenta en 1, es decir la variable cuenta la cantidad de veces que se aprieta el botón.
    Toques += 1
})
// Inicia la variable "Toques" con valor inicial = 0.
let Toques = 0
basic.forever(function () {
    // Muestra en pantalla el valor actual de la varibale "Toques", es decir el número que tiene "guardado".
    basic.showNumber(Toques)
})
