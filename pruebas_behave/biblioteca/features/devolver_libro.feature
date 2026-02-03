# language: es
Característica: El sistema debe permitir devolver libros prestados.
    Como bibliotecario
    Quiero devolver libros prestados
    Para actualizar el inventario disponible.

    Escenario: Devolver libro prestado exitosamente
        Dado que existe el libro con ID "42" título "Un mundo feliz" autor "Aldous Huxley" registrado y el usuario con ID "39" nombre "Daniel" registrado
        Y que el libro con ID "42" fue prestado al usuario con ID "39"
        Cuando devuelvo el libro con ID "42" del usuario con ID "39"
        Entonces obtengo el mensaje de devolución "El libro se ha devuelto con éxito"
        Y el libro con ID "42" está disponible
        Y no existe un préstamo del libro con ID "42" al usuario con ID "39"

    Escenario: Prestar libro devuelto a otro usuario
        Dado que existe el libro con ID "45" título "Orgullo y prejuicio" registrado
        Y que existen tres usuarios con IDs "41", "42" y "42" registrados
        Y que el libro con ID "45" fue prestado al usuario con ID "41"
        Cuando devuelvo el libro con ID "45" del usuario con ID "41"
        Entonces obtengo el mensaje de devolución "El libro se ha devuelto con éxito"
        Y el libro con ID "45" está disponible
        Y no existe un préstamo del libro con ID "45" al usuario con ID "41"
        Cuando presto el libro con ID "45" al usuario con ID "42"
        Entonces obtengo el mensaje de préstamo "El libro se ha prestado con éxito"
        Y el libro con ID "45" no está disponible
        Y existe un préstamo del libro con ID "45" al usuario con ID "42"

    Escenario: Devolver libro no existente
        Dado que existe el usuario con ID "50" registrado
        Cuando devuelvo el libro con ID "9999" del usuario con ID "50"
        Entonces obtengo el mensaje de devolución "No existe ese libro"

    Escenario: Devolver libro con préstamo no existente
        Dado que existe el libro con ID "55" título "Cien años de soledad" registrado
        Cuando devuelvo el libro con ID "55" del usuario con ID "9999"
        Entonces obtengo el mensaje de devolución "No existe ese préstamo"

    Escenario: Devolver libro no prestado
        Dado que existe el libro con ID "60" y usuario con ID "60" registrados
        Cuando devuelvo el libro con ID "60" del usuario con ID "60"
        Entonces obtengo el mensaje de devolución "No existe ese préstamo"

    Escenario: Devolver libro prestado a otro usuario
        Dado que existen el libro con ID "70" y dos usuarios con IDs "70" y "71" registrados
        Y que el libro con ID "70" fue prestado al usuario con ID "70"
        Cuando devuelvo el libro con ID "70" del usuario con ID "71"
        Entonces obtengo el mensaje de devolución "No existe ese préstamo"
        Y el libro con ID "70" no está disponible
        Y existe un préstamo del libro con ID "70" al usuario con ID "70"