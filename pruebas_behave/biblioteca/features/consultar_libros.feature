# language: es
Característica: El sistema debe permitir consultar libros disponibles y verificar disponibilidad.
    Como bibliotecario
    Quiero consultar los libros disponibles
    Para conocer el inventario actual de la biblioteca.

    Escenario: Consultar libros disponibles cuando hay libros
        Dado que existe el libro con ID "1" con título "El Quijote" y con autor "Cervantes" registrado
        Cuando consulto los libros disponibles
        Entonces obtengo una lista con el libro de ID "1"

    Escenario: Consultar libros disponibles cuando no hay libros
        Dado que la biblioteca está vacía
        Cuando consulto los libros disponibles
        Entonces obtengo el mensaje de consulta "No hay libros disponibles"

    Escenario: Seleccionar libro disponible
        Dado que existe el libro con ID "1" con título "El Quijote" y con autor "Cervantes" registrado
        Cuando selecciono el libro con ID "1"
        Entonces obtengo la disponibilidad "Está disponible"

    Escenario: Seleccionar libro no disponible
        Dado que existe el libro con ID "2" con título "1984", con autor "George Orwell" y no disponible
        Cuando selecciono el libro con ID "2"
        Entonces obtengo la disponibilidad "Está prestado"

    Escenario: Seleccionar libro inexistente
        Dado que la biblioteca está vacía
        Cuando selecciono el libro con ID "999"
        Entonces obtengo la disponibilidad "No existe ese libro"