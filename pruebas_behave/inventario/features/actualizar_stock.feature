Característica: El sistema debe permitir actualizar el stock de un producto existente.
    Como usuario del sistema de inventario
    Quiero actualizar el stock de productos
    Para mantener actualizada la cantidad disponible.

    Escenario: Actualizar stock exitosamente
        Dado que registro un producto con ID "243", nombre "Laptop", cantidad "10" y precio "999.99"
        Entonces obtengo el mensaje "Producto registrado exitosamente."
        Cuando actualizo el stock del producto con ID "243" a cantidad "20"
        Entonces obtengo el mensaje "Stock actualizado exitosamente."
        Y el producto con ID "243" tiene cantidad "20"

    Escenario: Actualizar stock de producto inexistente
        Dado que el inventario está vacío
        Cuando actualizo el stock del producto con ID "999" a cantidad "20"
        Entonces obtengo el mensaje "ERROR: Producto no encontrado."