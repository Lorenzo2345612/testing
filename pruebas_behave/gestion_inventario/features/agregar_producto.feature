# language: es

Característica: Agregar productos al inventario
    Como administrador del sistema de inventario
    Quiero poder agregar nuevos productos
    Para mantener un registro actualizado de los productos disponibles

    Escenario: Agregar un producto exitosamente
        Dado que el inventario está vacío
        Cuando agrego un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Entonces el producto se agrega exitosamente al inventario
        Y el inventario tiene 1 producto
        Y el producto con ID 1 existe en el inventario
        Y el producto con ID 1 tiene nombre "Laptop"
        Y el producto con ID 1 tiene precio 1500.00
        Y el producto con ID 1 tiene cantidad 10

    Escenario: Agregar múltiples productos con diferentes IDs
        Dado que el inventario está vacío
        Cuando agrego un producto con ID 1, nombre "Producto 1", precio 50.00 y cantidad 10
        Y agrego un producto con ID 100, nombre "Producto 100", precio 75.00 y cantidad 20
        Y agrego un producto con ID 999, nombre "Producto 999", precio 25.50 y cantidad 5
        Entonces el inventario tiene 3 productos
        Y el producto con ID 1 existe en el inventario
        Y el producto con ID 100 existe en el inventario
        Y el producto con ID 999 existe en el inventario

    Escenario: Intentar agregar un producto con ID duplicado
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando intento agregar un producto con ID 1, nombre "Mouse", precio 25.00 y cantidad 50
        Entonces se produce un error con el mensaje "El ID del producto ya existe"
        Y el inventario tiene 1 producto

    Escenario: Intentar agregar un producto con ID negativo
        Dado que el inventario está vacío
        Cuando intento agregar un producto con ID -1, nombre "Producto", precio 100.00 y cantidad 10
        Entonces se produce un error con el mensaje "El ID debe ser un entero no negativo"
        Y el inventario tiene 0 productos

    Escenario: Intentar agregar un producto con precio negativo
        Dado que el inventario está vacío
        Cuando intento agregar un producto con ID 1, nombre "Producto", precio -50.00 y cantidad 10
        Entonces se produce un error con el mensaje "El precio debe ser un número positivo"
        Y el inventario tiene 0 productos

    Escenario: Intentar agregar un producto con cantidad negativa
        Dado que el inventario está vacío
        Cuando intento agregar un producto con ID 1, nombre "Producto", precio 100.00 y cantidad -5
        Entonces se produce un error con el mensaje "La cantidad debe ser un entero no negativo"
        Y el inventario tiene 0 productos

    Escenario: Intentar agregar un producto con ID None
        Dado que el inventario está vacío
        Cuando intento agregar un producto con ID None, nombre "Producto", precio 100.00 y cantidad 10
        Entonces se produce un error con el mensaje "Todos los campos son obligatorios"
        Y el inventario tiene 0 productos

    Escenario: Intentar agregar un producto con nombre None
        Dado que el inventario está vacío
        Cuando intento agregar un producto con ID 1, nombre None, precio 100.00 y cantidad 10
        Entonces se produce un error con el mensaje "Todos los campos son obligatorios"
        Y el inventario tiene 0 productos


    Escenario: Intentar agregar un producto con ID string
        Dado que el inventario está vacío
        Cuando intento agregar un producto con ID "PROD001", nombre "Producto String", precio 99.99 y cantidad 15
        Entonces se produce un error de validación
        Y el inventario tiene 0 productos

    Escenario: Agregar un producto con precio cero
        Dado que el inventario está vacío
        Cuando agrego un producto con ID 1, nombre "Muestra Gratis", precio 0.00 y cantidad 100
        Entonces el producto se agrega exitosamente al inventario
        Y el producto con ID 1 tiene precio 0.00

    Escenario: Agregar un producto con cantidad cero
        Dado que el inventario está vacío
        Cuando agrego un producto con ID 1, nombre "Sin Stock", precio 100.00 y cantidad 0
        Entonces el producto se agrega exitosamente al inventario
        Y el producto con ID 1 tiene cantidad 0

    Escenario: Agregar un producto con nombre muy largo
        Dado que el inventario está vacío
        Cuando agrego un producto con ID 1, nombre "Este es un nombre de producto extremadamente largo que podría causar problemas en algunos sistemas pero debería funcionar correctamente", precio 100.00 y cantidad 5
        Entonces el producto se agrega exitosamente al inventario
        Y el producto con ID 1 tiene nombre "Este es un nombre de producto extremadamente largo que podría causar problemas en algunos sistemas pero debería funcionar correctamente"

    Escenario: Agregar un producto con nombre con caracteres especiales
        Dado que el inventario está vacío
        Cuando agrego un producto con ID 1, nombre "Niño's Toy® (Ñandú) - 50% OFF! #Especial", precio 75.50 y cantidad 12
        Entonces el producto se agrega exitosamente al inventario
        Y el producto con ID 1 tiene nombre "Niño's Toy® (Ñandú) - 50% OFF! #Especial"