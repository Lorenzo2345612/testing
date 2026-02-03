# language: es

Característica: Buscar productos en el inventario
    Como usuario del sistema de inventario
    Quiero buscar productos por nombre
    Para obtener información detallada de un producto específico

    Escenario: Buscar producto existente por nombre exacto
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando busco el producto con nombre "Laptop"
        Entonces encuentro el producto con ID 1
        Y encuentro el producto con nombre "Laptop"
        Y encuentro el producto con precio 1500.00
        Y encuentro el producto con cantidad 10

    Escenario: Buscar producto inexistente
        Dado que el inventario está vacío
        Cuando busco el producto con nombre "Tablet"
        Entonces no encuentro ningún producto

    Escenario: Buscar producto por nombre con diferente capitalización (minúsculas)
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando busco el producto con nombre "Laptop" en minúsculas
        Entonces encuentro el producto con ID 1
        Y encuentro el producto con nombre "Laptop"

    Escenario: Buscar producto por nombre con diferente capitalización (mayúsculas)
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando busco el producto con nombre "Laptop" en mayúsculas
        Entonces encuentro el producto con ID 1
        Y encuentro el producto con nombre "Laptop"

    Escenario: Buscar producto por nombre con espacios extras
        Dado que el inventario tiene un producto con ID 1, nombre "Teclado Mecánico", precio 150.00 y cantidad 5
        Cuando busco el producto con nombre "Teclado Mecánico" con espacios extras
        Entonces encuentro el producto con ID 1
        Y encuentro el producto con nombre "Teclado Mecánico"

    Escenario: Buscar productos con nombres similares - primer producto
        Dado que el inventario tiene productos con nombres similares
        Cuando busco el producto con nombre "Mouse Inalámbrico"
        Entonces encuentro el producto con ID 1
        Y encuentro el producto con nombre "Mouse Inalámbrico"
        Y encuentro el producto con precio 30.00

    Escenario: Buscar productos con nombres similares - segundo producto
        Dado que el inventario tiene productos con nombres similares
        Cuando busco el producto con nombre "Mouse USB"
        Entonces encuentro el producto con ID 2
        Y encuentro el producto con nombre "Mouse USB"
        Y encuentro el producto con precio 20.00

    Escenario: Buscar producto inexistente cuando hay otros productos
        Dado que el inventario tiene un producto con ID 1, nombre "Laptop", precio 1500.00 y cantidad 10
        Cuando busco el producto con nombre "Tablet"
        Entonces no encuentro ningún producto

    Escenario: Buscar producto con nombre largo
        Dado que el inventario tiene un producto con ID 1, nombre "Este es un nombre de producto extremadamente largo que podría causar problemas en algunos sistemas pero debería funcionar correctamente", precio 100.00 y cantidad 5
        Cuando busco el producto con nombre "Este es un nombre de producto extremadamente largo que podría causar problemas en algunos sistemas pero debería funcionar correctamente"
        Entonces encuentro el producto con ID 1

    Escenario: Buscar producto con caracteres especiales
        Dado que el inventario tiene un producto con ID 1, nombre "Niño's Toy® (Ñandú) - 50% OFF! #Especial", precio 75.50 y cantidad 12
        Cuando busco el producto con nombre "Niño's Toy® (Ñandú) - 50% OFF! #Especial"
        Entonces encuentro el producto con ID 1
        Y encuentro el producto con nombre "Niño's Toy® (Ñandú) - 50% OFF! #Especial"