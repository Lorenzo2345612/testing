# language: es

Característica: Eliminar productos del inventario
    Como administrador del sistema de inventario
    Quiero poder eliminar productos
    Para mantener el inventario actualizado cuando un producto ya no está disponible

    Escenario: Eliminar un producto existente
        Dado que el inventario tiene dos productos
        Cuando elimino el producto con ID 1
        Entonces el producto se elimina exitosamente
        Y el inventario tiene 1 producto
        Y el producto con ID 1 no se encuentra en el inventario
        Y el producto con nombre "Mouse" permanece en el inventario

    Escenario: Intentar eliminar un producto inexistente
        Dado que el inventario está vacío
        Cuando intento eliminar el producto con ID 999
        Entonces se produce un error con el mensaje "Producto no encontrado"

    Escenario: Intentar eliminar de inventario vacío
        Dado que el inventario está vacío
        Cuando intento eliminar el producto con ID 1
        Entonces se produce un error con el mensaje "Producto no encontrado"

    Escenario: Eliminar todos los productos del inventario
        Dado que el inventario tiene dos productos
        Cuando elimino el producto con ID 1
        Y elimino el producto con ID 2
        Entonces el inventario tiene 0 productos

    Escenario: Intentar operaciones en producto eliminado - venta
        Dado que el inventario tiene un producto con ID 1, nombre "Producto Temporal", precio 50.00 y cantidad 10
        Cuando elimino el producto con ID 1
        Y intento registrar una venta del producto con ID 1 por cantidad 5
        Entonces se produce un error con el mensaje "Producto no encontrado"

    Escenario: Intentar operaciones en producto eliminado - compra
        Dado que el inventario tiene un producto con ID 1, nombre "Producto Temporal", precio 50.00 y cantidad 10
        Cuando elimino el producto con ID 1
        Y intento registrar una compra del producto con ID 1 por cantidad 5
        Entonces se produce un error con el mensaje "Producto no encontrado"

    Escenario: Intentar operaciones en producto eliminado - actualizar stock
        Dado que el inventario tiene un producto con ID 1, nombre "Producto Temporal", precio 50.00 y cantidad 10
        Cuando elimino el producto con ID 1
        Y intento actualizar el stock del producto con ID 1 a cantidad 20
        Entonces se produce un error con el mensaje "Producto no encontrado"