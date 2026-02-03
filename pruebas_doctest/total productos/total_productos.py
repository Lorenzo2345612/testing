'''
Primera ejecución

Resultado:

1 items had failures:
  12 of  12 in total_productos.calculate_total_price
***Test Failed*** 12 failures.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Codigo minimo para la primera ejecucion

def calculate_total_price(products):
    total = 0.0
    for product in products:
        total += product['precio_unitario'] * product['cantidad']
    return total

Resultado:
1 items had failures:
   9 of  12 in total_productos.calculate_total_price
***Test Failed*** 9 failures.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Codigo minimo para la segunda ejecucion

def calculate_total_price(products):
    total = 0.0
    for product in products:
        subtotal = product['precio_unitario'] * product['cantidad']

        if subtotal > 1000.0:
            subtotal -= subtotal * 0.1

        total += subtotal
    return total

Resultado:
1 items had failures:
   8 of  12 in total_productos.calculate_total_price
***Test Failed*** 8 failures.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Codigo minimo para la tercera ejecucion

def calculate_total_price(products):
        total = 0.0
    for product in products:
        subtotal = product['precio_unitario'] * product['cantidad']

        if subtotal > 1000.0:
            subtotal -= subtotal * 0.1

        total += subtotal

    if total > 5000.0:
        total -= total * 0.05
    return total

Resultado:
1 items had failures:
   6 of  12 in total_productos.calculate_total_price
***Test Failed*** 6 failures.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Codigo minimo para la cuarta ejecucion

def calculate_total_price(products):
    total = 0.0
    for product in products:
        cantidad = product.get('cantidad')
        if cantidad < 0:
            return 'No se aceptan cantidades negativas'
        subtotal = product.get('precio_unitario') * cantidad

        if subtotal > 1000.0:
            subtotal -= subtotal * 0.1

        total += subtotal

    if total > 5000.0:
        total -= total * 0.05
    return total

Resultado:
1 items had failures:
   5 of  12 in total_productos.calculate_total_price
***Test Failed*** 5 failures.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Codigo minimo para la quinta ejecucion

def calculate_total_price(products):
        total = 0.0
    for product in products:
        cantidad = product.get('cantidad')
        if cantidad < 0:
            return 'No se aceptan cantidades negativas'
        
        precio_unitario = product.get('precio_unitario')
        if precio_unitario < 0:
            return 'No se aceptan precios unitarios negativos'
        
        subtotal = precio_unitario * cantidad

        if subtotal > 1000.0:
            subtotal -= subtotal * 0.1

        total += subtotal

    if total > 5000.0:
        total -= total * 0.05
    return total

Resultado:
1 items had failures:
   4 of  12 in total_productos.calculate_total_price
***Test Failed*** 4 failures.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Codigo minimo para la sexta ejecucion

def calculate_total_price(products):
    total = 0.0
    for product in products:
        if 'cantidad' not in product:
            return 'El producto debe tener la clave cantidad'


        cantidad = product.get('cantidad')
        if cantidad < 0:
            return 'No se aceptan cantidades negativas'
        
        precio_unitario = product.get('precio_unitario')
        if precio_unitario < 0:
            return 'No se aceptan precios unitarios negativos'
        
        subtotal = precio_unitario * cantidad

        if subtotal > 1000.0:
            subtotal -= subtotal * 0.1

        total += subtotal

    if total > 5000.0:
        total -= total * 0.05
    return total

Resultado:
1 items had failures:
   3 of  12 in total_productos.calculate_total_price
***Test Failed*** 3 failures.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Codigo minimo para la septima ejecucion

def calculate_total_price(products):
        total = 0.0
    for product in products:
        if 'cantidad' not in product:
            return 'El producto debe tener la clave cantidad'
        
        if 'precio_unitario' not in product:
            return 'El producto debe tener la clave precio_unitario'


        cantidad = product.get('cantidad')
        if cantidad < 0:
            return 'No se aceptan cantidades negativas'
        
        precio_unitario = product.get('precio_unitario')
        if precio_unitario < 0:
            return 'No se aceptan precios unitarios negativos'
        
        subtotal = precio_unitario * cantidad

        if subtotal > 1000.0:
            subtotal -= subtotal * 0.1

        total += subtotal

    if total > 5000.0:
        total -= total * 0.05
    return total

Resultado:
1 items had failures:
   2 of  12 in total_productos.calculate_total_price
***Test Failed*** 2 failures.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Codigo minimo para la octava ejecucion

def calculate_total_price(products):
        total = 0.0
    for product in products:
        if 'cantidad' not in product:
            return 'El producto debe tener la clave cantidad'
        
        if 'precio_unitario' not in product:
            return 'El producto debe tener la clave precio_unitario'
        
        if 'nombre' not in product:
            return 'El producto debe tener la clave nombre'


        cantidad = product.get('cantidad')
        if cantidad < 0:
            return 'No se aceptan cantidades negativas'
        
        precio_unitario = product.get('precio_unitario')
        if precio_unitario < 0:
            return 'No se aceptan precios unitarios negativos'
        
        subtotal = precio_unitario * cantidad

        if subtotal > 1000.0:
            subtotal -= subtotal * 0.1

        total += subtotal

    if total > 5000.0:
        total -= total * 0.05
    return total

Resultado:
1 items had failures:
   1 of  12 in total_productos.calculate_total_price
***Test Failed*** 1 failures.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Codigo minimo para la novena ejecucion

def calculate_total_price(products):
       total = 0.0
    for product in products:
        if 'cantidad' not in product:
            return 'El producto debe tener la clave cantidad'
        
        if 'precio_unitario' not in product:
            return 'El producto debe tener la clave precio_unitario'
        
        if 'nombre' not in product:
            return 'El producto debe tener la clave nombre'


        cantidad = product.get('cantidad')
        precio_unitario = product.get('precio_unitario')

        if any(not isinstance(value, (int, float)) for value in [cantidad, precio_unitario]):
            return 'El precio unitario y la cantidad deben ser numeros'
        
        if cantidad < 0:
            return 'No se aceptan cantidades negativas'
        if precio_unitario < 0:
            return 'No se aceptan precios unitarios negativos'
        
        subtotal = precio_unitario * cantidad

        if subtotal > 1000.0:
            subtotal -= subtotal * 0.1

        total += subtotal

    if total > 5000.0:
        total -= total * 0.05
    return total
    
Resultado:
1 items had no tests:
    total_productos
1 items passed all tests:
  12 tests in total_productos.calculate_total_price
12 tests in 2 items.
12 passed and 0 failed.
Test passed.
'''



def calculate_total_price(products: list[set]) -> float:
    """
    Tests

    Calculate the price of bought 2 units of Product 1 with a unit price of 300.0,
    1 unit of Product 2 with a unit price of 150.0, and 3 units of Product 3 with a unit price of 200.0.

    >>> calculate_total_price([
    ...     {
    ...         "nombre": "Producto 1",
    ...         "precio_unitario": 300.0,
    ...         "cantidad": 2
    ...     },
    ...     {
    ...         "nombre": "Producto 2",
    ...         "precio_unitario": 150.0,
    ...         "cantidad": 1
    ...     },
    ...     {
    ...         "nombre": "Producto 3",
    ...         "precio_unitario": 200.0,
    ...         "cantidad": 3
    ...     }
    ... ])
    1350.0

    Calculate the price of bought 1001 units of Product 5 with a unit price of 1.0,
    9 units of Product 6 with a unit price of 100.0 and 1 unit of Product 7 with a unit price of 1000.0.
    Appliying a 10% discount to each product if your subtotal is greater than 1000.0.

    >>> calculate_total_price([
    ...     {
    ...         "nombre": "Producto 5",
    ...         "precio_unitario": 1.0,
    ...         "cantidad": 1001
    ...     },
    ...     {
    ...         "nombre": "Producto 6",
    ...         "precio_unitario": 100.0,
    ...         "cantidad": 9
    ...     },
    ...     {
    ...         "nombre": "Producto 7",
    ...         "precio_unitario": 1000.0,
    ...         "cantidad": 1
    ...     }
    ... ])
    2800.9
    

    Calculate the price of bought 12 units of Product 8 with a unit price of 500.0,
    1 unit of Product 15 with a unit price of 1.0.
    Applying a 10% discount to each product if subtotal is greater than 1000.0.
    Applying a 5% discount to the total if total is greater than 5000.0.
    >>> calculate_total_price([
    ...     {
    ...         "nombre": "Producto 8",
    ...         "precio_unitario": 500.0,
    ...         "cantidad": 12
    ...     },
    ...     {
    ...         "nombre": "Producto 15",
    ...         "precio_unitario": 1.0,
    ...         "cantidad": 1
    ...     }
    ... ])
    5130.95

    Calculate the price of bought 10 units of Product 8 with a unit price of 500.0,
    5 units of Product 9 with a unit price of 200.0 and 2 units of Product 10 with a unit price of 300.0,
    Appliying a 10% discount to each product if subtotal is greater than 1000.0.
    Applying a 5% discount to the total if total is greater than 5000.0.

    >>> calculate_total_price([
    ...     {
    ...         "nombre": "Producto 8",
    ...         "precio_unitario": 500.0,
    ...         "cantidad": 10
    ...     },
    ...     {
    ...         "nombre": "Producto 9",
    ...         "precio_unitario": 200.0,
    ...         "cantidad": 5
    ...     },
    ...     {
    ...         "nombre": "Producto 10",
    ...         "precio_unitario": 300.0,
    ...         "cantidad": 2
    ...     }
    ... ])
    5795.0

    Calculate the price of not bought products.
    >>> calculate_total_price([])
    0.0

    Calculate the price with a product with zero quantity.
    >>> calculate_total_price([
    ...     {
    ...         "nombre": "Producto 11",
    ...         "precio_unitario": 100.0,
    ...         "cantidad": 0
    ...     }
    ... ])
    0.0

    Calculate the price with a product with negative quantity.
    >>> calculate_total_price([
    ...     {
    ...         "nombre": "Producto 12",
    ...         "precio_unitario": 100.0,
    ...         "cantidad": -5
    ...     }
    ... ])
    'No se aceptan cantidades negativas'

    Calculate the price with a product with negative unit price.
    >>> calculate_total_price([
    ...     {
    ...         "nombre": "Producto 13",
    ...         "precio_unitario": -100.0,
    ...         "cantidad": 5
    ...     }
    ... ])
    'No se aceptan precios unitarios negativos'

    Calculate the price with a product without 'cantidad' key.
    >>> calculate_total_price([
    ...     {
    ...         "nombre": "Producto 14",
    ...         "precio_unitario": 100.0
    ...     }
    ... ])
    'El producto debe tener la clave cantidad'

    Calculate the price with a product without 'precio_unitario' key.
    >>> calculate_total_price([
    ...     {
    ...         "nombre": "Producto 14",
    ...         "cantidad": 5
    ...     }
    ... ])
    'El producto debe tener la clave precio_unitario'

    Calculate the price with a product without 'nombre' key.
    >>> calculate_total_price([
    ...     {
    ...         "precio_unitario": 100.0,
    ...         "cantidad": 5
    ...     }
    ... ])
    'El producto debe tener la clave nombre'

    Calculate the price using letters instead of numbers.
    >>> calculate_total_price([
    ...     {
    ...         "nombre": "Producto 15",
    ...         "precio_unitario": "cien",
    ...         "cantidad": "cinco"
    ...     }
    ... ])
    'El precio unitario y la cantidad deben ser numeros'
    
    """
    total = 0.0
    for product in products:
        if 'cantidad' not in product:
            return 'El producto debe tener la clave cantidad'
        
        if 'precio_unitario' not in product:
            return 'El producto debe tener la clave precio_unitario'
        
        if 'nombre' not in product:
            return 'El producto debe tener la clave nombre'


        cantidad = product.get('cantidad')
        precio_unitario = product.get('precio_unitario')

        if any(not isinstance(value, (int, float)) for value in [cantidad, precio_unitario]):
            return 'El precio unitario y la cantidad deben ser numeros'
        
        if cantidad < 0:
            return 'No se aceptan cantidades negativas'
        if precio_unitario < 0:
            return 'No se aceptan precios unitarios negativos'
        
        subtotal = precio_unitario * cantidad

        if subtotal > 1000.0:
            subtotal -= subtotal * 0.1

        total += subtotal

    if total > 5000.0:
        total -= total * 0.05
    return total