# language: es
Característica: El sistema debe permitir buscar libros por título o por ID.
    Como bibliotecario
    Quiero buscar libros por diferentes criterios
    Para localizar rápidamente los libros en la biblioteca.

    Escenario: Buscar libros por título cuando hay varios con el mismo título
        Dado que existen los libros con título "Harry Potter y la piedra filosofal" con IDs "1" y "2" registrados
        Cuando busco el libro por título "Harry Potter y la piedra filosofal"
        Entonces obtengo una lista con "2" libros
        Y la lista contiene el libro con ID "1"
        Y la lista contiene el libro con ID "2"

    Escenario: Buscar libro por título que no existe
        Dado que la biblioteca está vacía
        Cuando busco el libro por título "Harry Potter y las reliquias de la muerte"
        Entonces obtengo el mensaje de búsqueda "No existe ese libro"

    Escenario: Buscar libro por ID existente
        Dado que existe el libro con ID "1" con título "El Quijote" y con autor "Cervantes" registrado
        Cuando busco el libro por ID "1"
        Entonces obtengo el libro con ID "1" y título "El Quijote"

    Escenario: Buscar libro por ID que no existe
        Dado que la biblioteca está vacía
        Cuando busco el libro por ID "999"
        Entonces obtengo el mensaje de búsqueda por ID "No existe ese libro"