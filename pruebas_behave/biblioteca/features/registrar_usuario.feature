# language: es
Característica: El sistema debe permitir registrar usuarios en la biblioteca.
    Como bibliotecario
    Quiero registrar usuarios en el sistema
    Para gestionar los préstamos de libros.

    Escenario: Registrar usuario exitosamente
        Dado que la biblioteca está vacía
        Cuando registro el usuario con ID "2" y nombre "Juan Pérez"
        Entonces obtengo el mensaje de usuario "Usuario registrado correctamente"
        Y el usuario con ID "2" está registrado

    Escenario: Registrar usuario sin nombre
        Dado que la biblioteca está vacía
        Cuando registro el usuario con ID "3" sin nombre
        Entonces obtengo el mensaje de usuario "Completa el nombre del usuario"
        Y el usuario con ID "3" no está registrado

    Escenario: Registrar usuario con nombre que contiene números
        Dado que la biblioteca está vacía
        Cuando registro el usuario con ID "5" y nombre con números "12345"
        Entonces obtengo el mensaje de usuario "El nombre no puede contener números"
        Y el usuario con ID "5" no está registrado

    Escenario: Registrar usuario con ID existente
        Dado que hay un usuario registrado con ID "1" y con nombre "Ana"
        Cuando registro el usuario con ID "1" y nombre "Pedro"
        Entonces obtengo el mensaje de usuario "Ya existe un usuario con ese identificador"
        Y la biblioteca tiene "1" usuarios registrados

    Escenario: Registrar usuario con ID negativo
        Dado que la biblioteca está vacía
        Cuando registro el usuario con ID negativo "-5" y nombre "María García"
        Entonces obtengo el mensaje de usuario "El id debe ser un número positivo entero"
        Y el usuario con ID "-5" no está registrado

    Escenario: Registrar usuario con ID no numérico
        Dado que la biblioteca está vacía
        Cuando registro el usuario con ID no numérico "abc" y nombre "Carlos López"
        Entonces obtengo el mensaje de usuario "El id debe ser un número positivo entero"
        Y la biblioteca tiene "0" usuarios registrados

    Escenario: Registrar usuarios con mismo nombre pero diferente ID
        Dado que hay un usuario registrado con ID "1" y con nombre "Ana"
        Cuando registro el usuario con ID "5" y nombre "Ana"
        Entonces obtengo el mensaje de usuario "Usuario registrado correctamente"
        Y la biblioteca tiene "2" usuarios registrados

    Escenario: Registrar usuario con nombre de solo espacios en blanco
        Dado que la biblioteca está vacía
        Cuando registro el usuario con ID "6" y nombre con solo espacios
        Entonces obtengo el mensaje de usuario "El nombre no puede estar vacío o contener solo espacios"
        Y el usuario con ID "6" no está registrado

    Escenario: Consultar usuarios registrados
        Dado que hay un usuario registrado con ID "1" y con nombre "Ana"
        Y que hay un usuario registrado con ID "2" y con nombre "María García"
        Cuando consulto los usuarios registrados
        Entonces obtengo una lista con el usuario de ID "1"
        Y obtengo una lista con el usuario de ID "2"

    Escenario: Consultar usuarios cuando no hay registrados
        Dado que la biblioteca está vacía
        Cuando consulto los usuarios registrados
        Entonces obtengo el mensaje de consulta de usuarios "No hay usuarios registrados"