# language: es
Característica: El sistema debe calcular el total del carrito.
    Como cliente
    Quiero calcular el total de mi carrito
    Para saber cuánto voy a pagar.

    Escenario: Calcular total de carrito vacío
        Dado que existe el cliente "Fernando Delgado"
        Cuando calculo el total del carrito del cliente con ID "1"
        Entonces el total del carrito es 0.0

    Escenario: Calcular total con un producto
        Dado que existe el cliente "Gabriela Morales"
        Y que existe el producto con nombre "Laptop" precio 1500.0 descripción "Laptop HP" stock 10
        Y que el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 2
        Cuando calculo el total del carrito del cliente con ID "1"
        Entonces el total del carrito es 3000.0

    Escenario: Calcular total con múltiples productos
        Dado que existe el cliente "Hugo Herrera"
        Y que existe el producto con nombre "Mouse" precio 25.0 descripción "Mouse inalámbrico" stock 50
        Y que existe el producto con nombre "Teclado" precio 45.0 descripción "Teclado mecánico" stock 30
        Y que existe el producto con nombre "Monitor" precio 300.0 descripción "Monitor 24 pulgadas" stock 20
        Y que el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 2
        Y que el cliente con ID "1" agrega al carrito el producto con ID "2" cantidad 1
        Y que el cliente con ID "1" agrega al carrito el producto con ID "3" cantidad 1
        Cuando calculo el total del carrito del cliente con ID "1"
        Entonces el total del carrito es 395.0
