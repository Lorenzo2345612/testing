# language: es
Característica: El sistema debe permitir vaciar el carrito.
    Como cliente
    Quiero vaciar mi carrito
    Para empezar una nueva compra.

    Escenario: Vaciar carrito con productos
        Dado que existe el cliente "Patricia Méndez"
        Y que existe el producto con nombre "Laptop" precio 1500.0 descripción "Laptop HP" stock 10
        Y que existe el producto con nombre "Mouse" precio 25.0 descripción "Mouse inalámbrico" stock 50
        Y que el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 1
        Y que el cliente con ID "1" agrega al carrito el producto con ID "2" cantidad 3
        Cuando el cliente con ID "1" vacía su carrito
        Entonces el carrito del cliente con ID "1" está vacío

    Escenario: Vaciar carrito vacío
        Dado que existe el cliente "Ricardo Navarro"
        Cuando el cliente con ID "1" vacía su carrito
        Entonces el carrito del cliente con ID "1" está vacío

    Escenario: Verificar total después de vaciar carrito
        Dado que existe el cliente "Verónica Silva"
        Y que existe el producto con nombre "Teclado" precio 45.0 descripción "Teclado mecánico" stock 30
        Y que el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 5
        Cuando el cliente con ID "1" vacía su carrito
        Y calculo el total del carrito del cliente con ID "1"
        Entonces el total del carrito es 0.0
