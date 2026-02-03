# language: es
Característica: El sistema debe permitir eliminar productos del carrito.
    Como cliente
    Quiero eliminar productos de mi carrito
    Para gestionar mi compra.

    Escenario: Eliminar producto del carrito exitosamente
        Dado que existe el cliente "Isabel Ortiz"
        Y que existe el producto con nombre "Laptop" precio 1500.0 descripción "Laptop HP" stock 10
        Y que el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 2
        Cuando el cliente con ID "1" elimina del carrito el producto con ID "1"
        Entonces el carrito del cliente con ID "1" está vacío

    Escenario: Eliminar un producto de varios en el carrito
        Dado que existe el cliente "José Suárez"
        Y que existe el producto con nombre "Mouse" precio 25.0 descripción "Mouse inalámbrico" stock 50
        Y que existe el producto con nombre "Teclado" precio 45.0 descripción "Teclado mecánico" stock 30
        Y que el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 1
        Y que el cliente con ID "1" agrega al carrito el producto con ID "2" cantidad 2
        Cuando el cliente con ID "1" elimina del carrito el producto con ID "1"
        Entonces el carrito del cliente con ID "1" contiene 1 tipo de producto
        Y el carrito del cliente con ID "1" tiene el producto con ID "2" con cantidad 2

    Escenario: Intentar eliminar producto que no está en el carrito
        Dado que existe el cliente "Carmen Rojas"
        Y que existe el producto con nombre "Monitor" precio 300.0 descripción "Monitor 24 pulgadas" stock 20
        Y que existe el producto con nombre "Webcam" precio 80.0 descripción "Webcam HD" stock 15
        Y que el cliente con ID "1" agrega al carrito el producto con ID "1" cantidad 1
        Cuando intento que el cliente con ID "1" elimine del carrito el producto con ID "2"
        Entonces obtengo el error "El producto no está en el carrito."

    Escenario: Intentar eliminar producto inexistente del carrito
        Dado que existe el cliente "Andrés Vega"
        Cuando intento que el cliente con ID "1" elimine del carrito el producto con ID "9999"
        Entonces obtengo el error "El producto con el ID proporcionado no existe."
