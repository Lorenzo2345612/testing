# language: es

Característica: Registrar ventas de productos
    Como vendedor del sistema de inventario
    Quiero registrar ventas de productos
    Para disminuir el stock disponible según las ventas realizadas

    Escenario: Registrar venta con stock suficiente
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando registro una venta del producto con ID 1 por cantidad 3
        Entonces la venta se registra exitosamente
        Y el stock del producto con ID 1 disminuye a 7

    Escenario: Registrar venta con cantidad exacta al stock
        Dado que el inventario tiene un producto con ID 1, nombre "Producto", precio 100.00 y cantidad 5
        Cuando registro una venta del producto con ID 1 por cantidad 5
        Entonces la venta se registra exitosamente
        Y el stock del producto con ID 1 disminuye a 0

    Escenario: Intentar registrar venta con stock insuficiente
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 5
        Cuando intento registrar una venta del producto con ID 1 por cantidad 10
        Entonces se produce un error con el mensaje "Stock insuficiente"
        Y el producto con ID 1 tiene cantidad 5

    Escenario: Intentar registrar venta de producto inexistente
        Dado que el inventario está vacío
        Cuando intento registrar una venta del producto con ID 999 por cantidad 1
        Entonces se produce un error con el mensaje "Producto no encontrado"

    Escenario: Intentar registrar venta con cantidad negativa
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando intento registrar una venta del producto con ID 1 por cantidad -1
        Entonces se produce un error con el mensaje "La cantidad a disminuir no puede ser negativa"
        Y el producto con ID 1 tiene cantidad 10

    Escenario: Registrar múltiples ventas sucesivas
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando registro una venta del producto con ID 1 por cantidad 2
        Y registro una venta del producto con ID 1 por cantidad 3
        Entonces el stock del producto con ID 1 disminuye a 5

    Escenario: Intentar venta cuando el stock ya está en cero
        Dado que el inventario tiene un producto con ID 1, nombre "Sin Stock", precio 100.00 y cantidad 0
        Cuando intento registrar una venta del producto con ID 1 por cantidad 1
        Entonces se produce un error con el mensaje "Stock insuficiente"
        Y el producto con ID 1 tiene cantidad 0