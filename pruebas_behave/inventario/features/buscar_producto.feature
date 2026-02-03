Característica: El sistema debe permitir buscar productos por ID.
    Como usuario del sistema de inventario
    Quiero buscar productos específicos
    Para obtener información detallada de un producto.

    Escenario: Buscar producto existente por ID
        Dado que registro un producto con ID "243", nombre "Laptop", cantidad "10" y precio "999.99"
        Cuando busco el producto por ID "243"
        Entonces obtengo el producto con ID "243", nombre "Laptop", cantidad "10" y precio "999.99"

    Escenario: Buscar producto existente por nombre
        Dado que registro un producto con ID "124", nombre "Mouse", cantidad "50" y precio "19.99"
        Cuando busco el producto por nombre "Mouse"
        Entonces obtengo el producto con ID "124", nombre "Mouse", cantidad "50" y precio "19.99"

    Escenario: Buscar producto inexistente por ID
        Dado que el inventario está vacío
        Cuando busco el producto por ID "999"
        Entonces no obtengo ningún producto