Característica: El sistema debe permitir eliminar un producto del inventario.
    Como usuario del sistema de inventario
    Quiero eliminar productos
    Para mantener el inventario actualizado.

    Escenario: Eliminar producto exitosamente
        Dado que registro un producto con ID "243", nombre "Laptop", cantidad "10" y precio "999.99"
        Entonces obtengo el mensaje "Producto registrado exitosamente."
        Cuando elimino el producto con ID "243"
        Entonces obtengo el mensaje "Producto eliminado exitosamente."
        Y el producto con ID "243" ya no está en el inventario

    Escenario: Eliminar producto inexistente
        Dado que el inventario está vacío
        Cuando elimino el producto con ID "999"
        Entonces obtengo el mensaje "ERROR: Producto no encontrado."