Característica: El sistema debe permitir consultar todos los productos en el inventario.
    Como usuario del sistema de inventario
    Quiero consultar todos los productos del inventario
    Para tener una visión general del inventario.

    Escenario: Consultar productos cuando el inventario está vacío
        Dado que el inventario actual está vacío
        Cuando solicito consultar todos los productos
        Entonces obtengo una lista vacía

    Escenario: Consultar productos cuando hay un solo producto
        Dado que registro un producto con ID "243", nombre "Laptop", cantidad "10" y precio "999.99"
        Cuando solicito consultar todos los productos
        Entonces obtengo una lista con 1 producto
        Y el producto en la lista tiene ID "243", nombre "Laptop", cantidad "10" y precio "999.99"