input.onSound(DetectedSound.Loud, function () {
    // Este bloque "niega" o "contradice" lo de dentro.
    // 
    // En este caso nuestra variable "estado" puede tomar valores verdadero o falso. 
    // 
    // Si es que al detectar un sonido alto la variable estado es verdadero, al negar se transoforma en algo falso, ya que algo falso es lo mismo decir que algo es no verdadero.
    // 
    // Y por otro lado si la varibale estado es falso, algo no faslo es algo verdadero, por lo que la variable "estado" va a ir cambiando entre vardadero y falso al detectar cada sonido fuerte.
    estado = !(estado)
    if (estado) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
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
let estado = false
estado = false
