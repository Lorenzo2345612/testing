# language: es
Característica: El sistema debe permitir prestar libros a usuarios registrados.
    Como bibliotecario
    Quiero prestar libros a usuarios
    Para gestionar el inventario de la biblioteca.

    Escenario: Prestar libro existente a usuario existente
        Dado que hay un libro registrado con ID "24" y un usuario registrado con ID "32"
        Cuando presto el libro con ID "24" al usuario con ID "32"
        Entonces obtengo el mensaje de préstamo "El libro se ha prestado con éxito"
        Y el libro con ID "24" no está disponible
        Y existe un préstamo del libro con ID "24" al usuario con ID "32"

    Escenario: Prestar libro a usuario no existente
        Dado que hay un libro registrado con ID "37" y título "El señor de los anillos"
        Cuando presto el libro con ID "37" al usuario con ID "999"
        Entonces obtengo el mensaje de préstamo "No existe ese usuario"
        Y el libro con ID "37" está disponible
        Y no existe un préstamo del libro con ID "37" al usuario con ID "999"

    Escenario: Prestar libro no existente
        Dado que existe el usuario con ID "38" registrado
        Cuando presto el libro con ID "9999" al usuario con ID "38"
        Entonces obtengo el mensaje de préstamo "No existe ese libro"
        Y no existe un préstamo del libro con ID "9999" al usuario con ID "38"

    Escenario: Prestar libro ya prestado a otro usuario
        Dado que hay un libro registrado con ID "80"
        Y que existen dos usuarios con IDs "80" y "81" registrados
        Y que el libro con ID "80" está prestado al usuario con ID "80"
        Cuando presto el libro con ID "80" al usuario con ID "81"
        Entonces obtengo el mensaje de préstamo "El libro ya está prestado"
        Y el libro con ID "80" no está disponible
        Y existe un préstamo del libro con ID "80" al usuario con ID "80"
        Y no existe un préstamo del libro con ID "80" al usuario con ID "81"