Característica: El sistema debe permitir registrar compras de productos.
    Como usuario del sistema de inventario
    Quiero registrar compras de productos
    Para llevar control de las entradas de inventario.

    Escenario: Registrar compra exitosa
        Dado que registro un producto con ID "243", nombre "Laptop", cantidad "10" y precio "999.99"
        Cuando registro una compra del producto con ID "243" por cantidad "5"
        Entonces obtengo el mensaje "Compra registrada exitosamente."
        Y el producto con ID "243" tiene cantidad "15"

    Escenario: Registrar compra de producto inexistente
        Dado que el inventario está vacío
        Cuando registro una compra del producto con ID "999" por cantidad "5"
        Entonces obtengo el mensaje "ERROR: Producto no encontrado."