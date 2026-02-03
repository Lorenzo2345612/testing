Característica: El sistema debe permitir registrar ventas de productos.
    Como usuario del sistema de inventario
    Quiero registrar ventas de productos
    Para llevar control de las salidas de inventario.

    Escenario: Registrar venta exitosa
        Dado que registro un producto con ID "243", nombre "Laptop", cantidad "10" y precio "999.99"
        Cuando registro una venta del producto con ID "243" por cantidad "2"
        Entonces obtengo el mensaje "Venta registrada exitosamente."
        Y el producto con ID "243" tiene cantidad "8"

    Escenario: Registrar venta de producto inexistente
        Dado que el inventario está vacío
        Cuando registro una venta del producto con ID "999" por cantidad "2"
        Entonces obtengo el mensaje "ERROR: Producto no encontrado."

    Escenario: Registrar venta con stock insuficiente
        Dado que registro un producto con ID "243", nombre "Laptop", cantidad "10" y precio "999.99"
        Cuando registro una venta del producto con ID "243" por cantidad "15"
        Entonces obtengo el mensaje "ERROR: Stock insuficiente."
        Y el producto con ID "243" mantiene cantidad "10"