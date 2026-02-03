# language: es
Característica: El sistema debe permitir agregar productos a la tienda.
    Como administrador
    Quiero agregar productos a la tienda
    Para mantener el inventario actualizado.

    Escenario: Agregar producto a la tienda exitosamente
        Cuando agrego el producto con nombre "Laptop" precio 1500.0 descripción "Laptop HP" stock 10
        Entonces el producto con ID "1" existe en la tienda
        Y verifico datos del producto con ID "1" nombre "Laptop" precio 1500.0 descripción "Laptop HP" stock 10

    Escenario: Agregar múltiples productos a la tienda
        Cuando agrego el producto con nombre "Mouse" precio 25.0 descripción "Mouse inalámbrico" stock 50
        Y agrego el producto con nombre "Teclado" precio 45.0 descripción "Teclado mecánico" stock 30
        Entonces el producto con ID "1" existe en la tienda
        Y el producto con ID "2" existe en la tienda

    Escenario: Agregar producto con stock cero
        Cuando agrego el producto con nombre "Monitor" precio 300.0 descripción "Monitor 24 pulgadas" stock 0
        Entonces el stock del producto con ID "1" es 0
