# language: es
Característica: El sistema debe permitir consultar productos del carrito.
    Como cliente
    Quiero consultar los productos de mi carrito
    Para ver qué voy a comprar.

    Escenario: Consultar carrito vacío
        Dado que existe el cliente "Diego Vargas"
        Cuando consulto el carrito del cliente con ID "1"
        Entonces el carrito del cliente con ID "1" está vacío

    Escenario: Consultar carrito con productos
        Dado que existe el cliente "Elena Castro"
        Y que existe el producto con nombre "Laptop" precio 1500.0 descripción "Laptop HP" stock 10
        Y que existe el producto con nombre "Mouse" precio 25.0 descripción "Mouse inalámbrico" stock 50
        Y que el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 1
        Y que el cliente con ID "1" agrega al carrito el producto con ID "2" cantidad 3
        Cuando consulto el carrito del cliente con ID "1"
        Entonces el carrito del cliente con ID "1" contiene 2 tipo de producto
        Y el carrito del cliente con ID "1" tiene el producto con ID "1" con cantidad 1
        Y el carrito del cliente con ID "1" tiene el producto con ID "2" con cantidad 3
