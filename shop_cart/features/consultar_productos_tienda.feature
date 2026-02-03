# language: es
Característica: El sistema debe permitir consultar productos de la tienda.
    Como administrador o cliente
    Quiero consultar los productos de la tienda
    Para ver el inventario disponible.

    Escenario: Consultar productos cuando la tienda está vacía
        Cuando consulto los productos de la tienda
        Entonces obtengo una lista con 0 productos

    Escenario: Consultar productos con un producto registrado
        Dado que existe el producto con nombre "Laptop" precio 1500.0 descripción "Laptop HP" stock 10
        Cuando consulto los productos de la tienda
        Entonces obtengo una lista con 1 productos

    Escenario: Consultar productos con múltiples productos registrados
        Dado que existe el producto con nombre "Laptop" precio 1500.0 descripción "Laptop HP" stock 10
        Y que existe el producto con nombre "Mouse" precio 25.0 descripción "Mouse inalámbrico" stock 50
        Y que existe el producto con nombre "Teclado" precio 45.0 descripción "Teclado mecánico" stock 30
        Cuando consulto los productos de la tienda
        Entonces obtengo una lista con 3 productos
