# language: es
Característica: El sistema debe manejar casos especiales y validaciones.
    Como sistema de carrito de compras
    Quiero validar las operaciones y manejar errores
    Para garantizar la integridad de los datos.

    Escenario: Intentar agregar producto con precio negativo
        Cuando intento agregar a tienda producto "Producto" con precio -100.0 descripción "Descripción" stock 10
        Entonces obtengo el error "El precio debe ser un número positivo."

    Escenario: Intentar agregar producto con nombre vacío
        Cuando intento agregar a tienda producto con nombre vacío precio 100.0 descripción "Descripción" stock 10
        Entonces obtengo el error "El nombre del producto debe ser una cadena no vacía."

    Escenario: Intentar agregar producto con stock negativo
        Cuando intento agregar a tienda producto "Producto" con precio 100.0 descripción "Descripción" stock -5
        Entonces obtengo el error "El stock debe ser un entero no negativo."

    Escenario: Intentar editar producto con precio negativo
        Dado que existe el producto con nombre "Monitor" precio 300.0 descripción "Monitor 24 pulgadas" stock 10
        Cuando intento modificar el precio del producto con ID "1" a -50.0
        Entonces obtengo el error "El precio debe ser un número positivo."

    Escenario: Intentar editar producto con stock negativo
        Dado que existe el producto con nombre "Teclado" precio 45.0 descripción "Teclado mecánico" stock 30
        Cuando intento modificar el stock del producto con ID "1" a -10
        Entonces obtengo el error "El stock debe ser un entero no negativo."

    Escenario: Intentar agregar al carrito con cliente inexistente
        Dado que existe el producto con nombre "Mouse" precio 25.0 descripción "Mouse inalámbrico" stock 50
        Cuando intento que el cliente con ID "9999" agregue al carrito el producto con ID "1" cantidad 1
        Entonces obtengo el error "El cliente con el ID proporcionado no existe."

    Escenario: Operaciones combinadas - agregar, calcular total y vaciar
        Dado que existe el cliente "Tomás Rivera"
        Y que existe el producto con nombre "Laptop" precio 1000.0 descripción "Laptop Dell" stock 10
        Y que existe el producto con nombre "Mouse" precio 20.0 descripción "Mouse USB" stock 50
        Cuando el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 1
        Y el cliente con ID "1" agrega al carrito el producto con ID "2" cantidad 2
        Y calculo el total del carrito del cliente con ID "1"
        Entonces el total del carrito es 1040.0
        Cuando el cliente con ID "1" vacía su carrito
        Entonces el carrito del cliente con ID "1" está vacío

    Escenario: Verificar stock no se modifica al agregar al carrito
        Dado que existe el producto con nombre "Tablet" precio 500.0 descripción "Tablet 10 pulgadas" stock 20
        Y que existe el cliente "Sara Flores"
        Cuando el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 5
        Entonces el stock del producto con ID "1" es 20
