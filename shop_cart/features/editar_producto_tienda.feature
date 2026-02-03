# language: es
Característica: El sistema debe permitir editar productos de la tienda.
    Como administrador
    Quiero editar productos de la tienda
    Para mantener la información actualizada.

    Escenario: Editar nombre de producto
        Dado que existe el producto con nombre "Laptop" precio 1500.0 descripción "Laptop HP" stock 10
        Cuando edito solo el nombre del producto con ID "1" a "Laptop Dell"
        Entonces el nombre del producto con ID "1" es "Laptop Dell"

    Escenario: Editar precio de producto
        Dado que existe el producto con nombre "Mouse" precio 25.0 descripción "Mouse inalámbrico" stock 50
        Cuando edito solo el precio del producto con ID "1" a 30.0
        Entonces el precio del producto con ID "1" es 30.0

    Escenario: Editar stock de producto
        Dado que existe el producto con nombre "Teclado" precio 45.0 descripción "Teclado mecánico" stock 30
        Cuando edito solo el stock del producto con ID "1" a 50
        Entonces el stock del producto con ID "1" es 50

    Escenario: Editar múltiples campos de producto
        Dado que existe el producto con nombre "Monitor" precio 300.0 descripción "Monitor viejo" stock 10
        Cuando edito campos múltiples del producto con ID "1" nombre "Monitor Samsung" precio 350.0 descripción "Monitor 27 pulgadas"
        Entonces verifico producto con ID "1" tiene nombre "Monitor Samsung" precio 350.0 descripción "Monitor 27 pulgadas"

    Escenario: Intentar editar producto inexistente
        Cuando intento editar producto inexistente con ID "9999" nombre "Producto"
        Entonces obtengo el error "El producto con el ID proporcionado no existe."
