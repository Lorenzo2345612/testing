# language: es
Característica: El sistema debe permitir eliminar productos de la tienda.
    Como administrador
    Quiero eliminar productos de la tienda
    Para mantener el catálogo actualizado.

    Escenario: Eliminar producto de la tienda exitosamente
        Dado que existe el producto con nombre "Laptop" precio 1500.0 descripción "Laptop HP" stock 10
        Cuando elimino el producto con ID "1" de la tienda
        Entonces el producto con ID "1" no existe en la tienda

    Escenario: Eliminar producto que está en un carrito
        Dado que existe el cliente "Juan Pérez"
        Y que existe el producto con nombre "Mouse" precio 25.0 descripción "Mouse inalámbrico" stock 50
        Y que el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 2
        Cuando elimino el producto con ID "1" de la tienda
        Entonces el producto con ID "1" no existe en la tienda
        Y el carrito del cliente con ID "1" está vacío

    Escenario: Intentar eliminar producto inexistente
        Cuando intento eliminar el producto con ID "9999" de la tienda
        Entonces obtengo el error "El producto con el ID proporcionado no existe."
