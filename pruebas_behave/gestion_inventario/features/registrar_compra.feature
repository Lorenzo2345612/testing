# language: es

Característica: Registrar compras de productos
    Como administrador del sistema de inventario
    Quiero registrar compras de productos
    Para aumentar el stock disponible según las compras realizadas

    Escenario: Registrar compra de producto existente
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando registro una compra del producto con ID 1 por cantidad 15
        Entonces la compra se registra exitosamente
        Y el stock del producto con ID 1 aumenta a 25

    Escenario: Registrar compra cuando el stock está en cero
        Dado que el inventario tiene un producto con ID 1, nombre "Sin Stock", precio 100.00 y cantidad 0
        Cuando registro una compra del producto con ID 1 por cantidad 50
        Entonces la compra se registra exitosamente
        Y el stock del producto con ID 1 aumenta a 50

    Escenario: Intentar registrar compra de producto inexistente
        Dado que el inventario está vacío
        Cuando intento registrar una compra del producto con ID 999 por cantidad 5
        Entonces se produce un error con el mensaje "Producto no encontrado"

    Escenario: Intentar registrar compra con cantidad negativa
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando intento registrar una compra del producto con ID 1 por cantidad -5
        Entonces se produce un error con el mensaje "La cantidad a aumentar no puede ser negativa"
        Y el producto con ID 1 tiene cantidad 10

    Escenario: Registrar múltiples compras sucesivas
        Dado que el inventario tiene un producto con ID 1, nombre "Mouse", precio 25.00 y cantidad 10
        Cuando registro una compra del producto con ID 1 por cantidad 20
        Y registro una compra del producto con ID 1 por cantidad 15
        Entonces el stock del producto con ID 1 aumenta a 45

    Escenario: Registrar compra con cantidad muy grande
        Dado que el inventario tiene un producto con ID 1, nombre "Stock Masivo", precio 1.00 y cantidad 1000
        Cuando registro una compra del producto con ID 1 por cantidad 999000
        Entonces la compra se registra exitosamente
        Y el stock del producto con ID 1 aumenta a 1000000

    Escenario: Operaciones combinadas de compra y venta
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Y el inventario tiene un producto con ID 2, nombre "Mouse", precio 25.00 y cantidad 50
        Cuando registro una venta del producto con ID 1 por cantidad 2
        Y registro una compra del producto con ID 2 por cantidad 25
        Entonces el stock del producto con ID 1 disminuye a 8
        Y el stock del producto con ID 2 aumenta a 75

    Escenario: Calcular valor total del inventario después de compras
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Y el inventario tiene un producto con ID 2, nombre "Mouse", precio 25.00 y cantidad 50
        Y el inventario tiene un producto con ID 3, nombre "Teclado", precio 75.00 y cantidad 30
        Entonces el valor total del inventario es 18500.00