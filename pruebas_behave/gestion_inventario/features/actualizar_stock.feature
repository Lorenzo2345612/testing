# language: es

Característica: Actualizar stock de productos
    Como administrador del sistema de inventario
    Quiero actualizar el stock de productos existentes
    Para mantener actualizadas las cantidades disponibles

    Escenario: Actualizar stock de producto existente
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando actualizo el stock del producto con ID 1 a cantidad 20
        Entonces el stock se actualiza exitosamente
        Y el producto con ID 1 tiene cantidad 20

    Escenario: Actualizar stock a cero
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando actualizo el stock del producto con ID 1 a cantidad 0
        Entonces el stock se actualiza exitosamente
        Y el producto con ID 1 tiene cantidad 0

    Escenario: Actualizar stock de producto inexistente
        Dado que el inventario está vacío
        Cuando intento actualizar el stock del producto con ID 999 a cantidad 20
        Entonces se produce un error con el mensaje "Producto no encontrado"

    Escenario: Actualizar stock con cantidad negativa
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando intento actualizar el stock del producto con ID 1 a cantidad -5
        Entonces se produce un error con el mensaje "La cantidad no puede ser negativa"
        Y el producto con ID 1 tiene cantidad 10

    Escenario: Actualizar stock con cantidad no numérica (string)
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando intento actualizar el stock del producto con ID 1 a cantidad "veinte"
        Entonces se produce un error con el mensaje "La cantidad debe ser un entero"
        Y el producto con ID 1 tiene cantidad 10

    Escenario: Actualizar stock con cantidad None
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando intento actualizar el stock del producto con ID 1 a cantidad None
        Entonces se produce un error con el mensaje "La cantidad debe ser un entero"
        Y el producto con ID 1 tiene cantidad 10

    Escenario: Actualizar stock con cantidad decimal
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando intento actualizar el stock del producto con ID 1 a cantidad decimal 20.5
        Entonces se produce un error con el mensaje "La cantidad debe ser un entero"
        Y el producto con ID 1 tiene cantidad 10

    Escenario: Actualizar stock con lista como cantidad
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando intento actualizar el stock del producto con ID 1 a una lista
        Entonces se produce un error con el mensaje "La cantidad debe ser un entero"
        Y el producto con ID 1 tiene cantidad 10

    Escenario: Actualizar stock con diccionario como cantidad
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando intento actualizar el stock del producto con ID 1 a un diccionario
        Entonces se produce un error con el mensaje "La cantidad debe ser un entero"
        Y el producto con ID 1 tiene cantidad 10

    Escenario: Actualizar stock a cantidad muy grande
        Dado que el inventario tiene un producto con ID 1, nombre "Stock Masivo", precio 1.00 y cantidad 100
        Cuando actualizo el stock del producto con ID 1 a cantidad 1000000
        Entonces el stock se actualiza exitosamente
        Y el producto con ID 1 tiene cantidad 1000000