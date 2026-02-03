Característica: El sistema debe manejar casos especiales del inventario.
    Como usuario del sistema de inventario
    Quiero que el sistema maneje casos especiales
    Para tener un control preciso del inventario.

    Escenario: Consultar total de inventario vacío
        Dado que el inventario está vacío
        Cuando consulto el total del inventario
        Entonces obtengo el valor "0.00"

    Escenario: Consultar total de inventario con varios productos
        Dado que registro un producto con ID "243", nombre "Laptop", cantidad "10" y precio "999.99"
        Y registro un producto con ID "124", nombre "Mouse", cantidad "50" y precio "19.99"
        Cuando consulto el total del inventario
        Entonces obtengo el valor "10999.40"

    Escenario: Registrar venta que deja stock en cero
        Dado que registro un producto con ID "243", nombre "Laptop", cantidad "10" y precio "999.99"
        Cuando registro una venta del producto con ID "243" por cantidad "10"
        Entonces obtengo el mensaje "Venta registrada exitosamente."
        Y el producto con ID "243" tiene cantidad "0"
        Y cuando intento registrar otra venta del producto con ID "243" por cantidad "1"
        Entonces obtengo el mensaje "ERROR: Stock insuficiente."