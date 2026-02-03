Característica: El sistema debe permitir registrar un producto con: identificador único, nombre, cantidad en stock y precio unitario.
    Como usuario del sistema de inventario
    Quiero registrar productos
    Para llevar un control adecuado del inventario.

    Escenario: Registrar un producto con datos válidos
        Dado que ingreso el identificador "243", el nombre "Laptop", la cantidad "10" y el precio "999.99"
        Cuando realizo la operación de registrar producto
        Entonces puedo ver el mensaje de éxito "Producto registrado exitosamente."
        Entonces el producto con ID "243" debe estar en el inventario con nombre "Laptop", cantidad "10" y precio "999.99"
    
    Escenario: Registrar un producto con ID duplicado
        Dado que ingreso el identificador "243", el nombre "Laptop", la cantidad "10" y el precio "999.99"
        Cuando realizo la operación de registrar producto
        Entonces puedo ver el mensaje de éxito "Producto registrado exitosamente."
        Dado que ingreso nuevamente el identificador "243", el nombre "Smartphone", la cantidad "5" y el precio "499.99"
        Cuando realizo la operación de registrar producto
        Entonces puedo ver el mensaje de error "ERROR: El ID del producto ya existe."

    Escenario: Registrar un producto con datos inválidos
        Dado que ingreso los datos erroneos "sadd", el nombre "Laptop", la cantidad "33.3" y el precio "0"
        Cuando realizo la operación de registrar producto
        Entonces puedo ver el mensaje de error "ERROR: El ID del producto debe ser un número."