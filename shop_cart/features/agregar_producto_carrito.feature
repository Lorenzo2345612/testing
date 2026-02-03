# language: es
Característica: El sistema debe permitir agregar productos al carrito.
    Como cliente
    Quiero agregar productos al carrito
    Para realizar una compra.

    Escenario: Agregar producto al carrito exitosamente
        Dado que existe el cliente "María García"
        Y que existe el producto con nombre "Laptop" precio 1500.0 descripción "Laptop HP" stock 10
        Cuando el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 2
        Entonces el carrito del cliente con ID "1" contiene 1 tipo de producto
        Y el carrito del cliente con ID "1" tiene el producto con ID "1" con cantidad 2

    Escenario: Agregar múltiples productos al carrito
        Dado que existe el cliente "Carlos López"
        Y que existe el producto con nombre "Mouse" precio 25.0 descripción "Mouse inalámbrico" stock 50
        Y que existe el producto con nombre "Teclado" precio 45.0 descripción "Teclado mecánico" stock 30
        Cuando el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 1
        Y el cliente con ID "1" agrega al carrito el producto con ID "2" cantidad 2
        Entonces el carrito del cliente con ID "1" contiene 2 tipo de producto

    Escenario: Agregar mismo producto dos veces incrementa cantidad
        Dado que existe el cliente "Ana Martínez"
        Y que existe el producto con nombre "Monitor" precio 300.0 descripción "Monitor 24 pulgadas" stock 20
        Cuando el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 1
        Y el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 2
        Entonces el carrito del cliente con ID "1" tiene el producto con ID "1" con cantidad 3

    Escenario: Intentar agregar producto sin stock suficiente
        Dado que existe el cliente "Pedro Sánchez"
        Y que existe el producto con nombre "Tablet" precio 500.0 descripción "Tablet 10 pulgadas" stock 5
        Cuando intento que el cliente con ID "1" agregue al carrito el producto con ID "1" cantidad 10
        Entonces obtengo el error "No hay suficiente stock disponible para el producto solicitado."

    Escenario: Intentar agregar producto inexistente al carrito
        Dado que existe el cliente "Laura Fernández"
        Cuando intento que el cliente con ID "1" agregue al carrito el producto con ID "9999" cantidad 1
        Entonces obtengo el error "El producto con el ID proporcionado no existe."

    Escenario: Intentar agregar producto con cantidad cero
        Dado que existe el cliente "Roberto Torres"
        Y que existe el producto con nombre "Webcam" precio 80.0 descripción "Webcam HD" stock 15
        Cuando intento que el cliente con ID "1" agregue al carrito el producto con ID "1" cantidad 0
        Entonces obtengo el error "La cantidad debe ser un entero positivo."

    Escenario: Intentar agregar producto con cantidad negativa
        Dado que existe el cliente "Sofía Ramírez"
        Y que existe el producto con nombre "Audífonos" precio 60.0 descripción "Audífonos Bluetooth" stock 25
        Cuando intento que el cliente con ID "1" agregue al carrito el producto con ID "1" cantidad -1
        Entonces obtengo el error "La cantidad debe ser un entero positivo."
