"""
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
"""
