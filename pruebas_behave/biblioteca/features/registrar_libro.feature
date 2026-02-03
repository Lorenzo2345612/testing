# language: es
Característica: El sistema debe permitir registrar libros en la biblioteca.
    Como bibliotecario
    Quiero registrar libros en el sistema
    Para gestionar el inventario de la biblioteca.

    Escenario: Registrar libro exitosamente
        Dado que la biblioteca está vacía
        Cuando registro el libro con ID "1", título "El Quijote" y autor "Cervantes"
        Entonces obtengo el mensaje "Se ha registrado correctamente"
        Y el libro con ID "1" está en la biblioteca

    Escenario: Registrar libro sin autor
        Dado que la biblioteca está vacía
        Cuando registro el libro con ID "2", título "Libro Sin Autor" y sin autor
        Entonces obtengo el mensaje "Se ha registrado correctamente"
        Y el libro con ID "2" está en la biblioteca
        Y el libro con ID "2" tiene el autor "Completa el nombre del autor"

    Escenario: Registrar libro con campos vacíos
        Dado que la biblioteca está vacía
        Cuando registro el libro con ID "3", sin título y sin autor
        Entonces obtengo el mensaje "Se ha registrado correctamente"
        Y el libro con ID "3" está en la biblioteca
        Y el libro con ID "3" tiene el título "Completa los campos: título y autor"
        Y el libro con ID "3" tiene el autor "Completa los campos: título y autor"

    Escenario: Registrar libro ya existente
        Dado que existe el libro con ID "1" con título "El Quijote" y con autor "Cervantes" registrado
        Cuando registro el libro con ID "1", título "El Quijote" y autor "Cervantes"
        Entonces obtengo el mensaje "Ya se encuentra registrado ese libro"
        Y la biblioteca tiene "1" libros registrados

    Escenario: Registrar libro con ID negativo
        Dado que la biblioteca está vacía
        Cuando registro el libro con ID negativo "-5", título "Harry Potter y la cámara secreta" y autor "J.K. Rowling"
        Entonces obtengo el mensaje "El id debe ser un número positivo entero"
        Y el libro con ID "-5" no está en la biblioteca

    Escenario: Registrar libro con ID no numérico
        Dado que la biblioteca está vacía
        Cuando registro el libro con ID no numérico "abc", título "1984" y autor "George Orwell"
        Entonces obtengo el mensaje "El id debe ser un número positivo entero"
        Y la biblioteca tiene "0" libros registrados

    Escenario: Registrar libro con mismo título y autor pero diferente ID
        Dado que existe el libro con ID "1" con título "El Quijote" y con autor "Cervantes" registrado
        Cuando registro el libro con ID "2", título "El Quijote" y autor "Cervantes"
        Entonces obtengo el mensaje "Se ha registrado correctamente"
        Y la biblioteca tiene "2" libros registrados