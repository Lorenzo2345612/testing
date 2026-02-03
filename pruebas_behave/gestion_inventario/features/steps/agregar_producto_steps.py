from behave import given, when, then
from gestion_inventario import GestionInventario


@given(u'que el inventario está vacío')
def step_impl(context):
    context.inventario = GestionInventario()


@given(u'que el inventario tiene un producto con ID {id:d}, nombre "{nombre}", precio {precio:f} y cantidad {cantidad:d}')
def step_impl(context, id, nombre, precio, cantidad):
    context.inventario = GestionInventario()
    context.inventario.agregar_producto(id, nombre, precio, cantidad)


@given(u'el inventario tiene un producto con ID {id:d}, nombre "{nombre}", precio {precio:f} y cantidad {cantidad:d}')
def step_impl(context, id, nombre, precio, cantidad):
    if not hasattr(context, 'inventario'):
        context.inventario = GestionInventario()
    context.inventario.agregar_producto(id, nombre, precio, cantidad)


@when(u'agrego un producto con ID {id:d}, nombre "{nombre}", precio {precio:f} y cantidad {cantidad:d}')
def step_impl(context, id, nombre, precio, cantidad):
    try:
        context.inventario.agregar_producto(id, nombre, precio, cantidad)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento agregar un producto con ID {id:d}, nombre "{nombre}", precio {precio:f} y cantidad {cantidad:d}')
def step_impl(context, id, nombre, precio, cantidad):
    try:
        context.inventario.agregar_producto(id, nombre, precio, cantidad)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento agregar un producto con ID None, nombre "{nombre}", precio {precio:f} y cantidad {cantidad:d}')
def step_impl(context, nombre, precio, cantidad):
    try:
        context.inventario.agregar_producto(None, nombre, precio, cantidad)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento agregar un producto con ID {id:d}, nombre None, precio {precio:f} y cantidad {cantidad:d}')
def step_impl(context, id, precio, cantidad):
    try:
        context.inventario.agregar_producto(id, None, precio, cantidad)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento agregar un producto con ID {id:d}, nombre vacío, precio {precio:f} y cantidad {cantidad:d}')
def step_impl(context, id, precio, cantidad):
    try:
        context.inventario.agregar_producto(id, "", precio, cantidad)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento agregar un producto con ID {id:d}, nombre con solo espacios, precio {precio:f} y cantidad {cantidad:d}')
def step_impl(context, id, precio, cantidad):
    try:
        context.inventario.agregar_producto(id, "   ", precio, cantidad)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento agregar un producto con ID "{id_str}", nombre "{nombre}", precio {precio:f} y cantidad {cantidad:d}')
def step_impl(context, id_str, nombre, precio, cantidad):
    try:
        context.inventario.agregar_producto(id_str, nombre, precio, cantidad)
        context.error = None
    except Exception as e:
        context.error = str(e)


@then(u'el producto se agrega exitosamente al inventario')
def step_impl(context):
    assert context.error is None, \
        f'Se esperaba que el producto se agregara exitosamente, pero se obtuvo el error: {context.error}'


@then(u'el inventario tiene {cantidad:d} producto')
def step_impl(context, cantidad):
    productos = context.inventario.obtener_productos()
    assert len(productos) == cantidad, \
        f'Se esperaba que el inventario tuviera {cantidad} producto(s), pero tiene {len(productos)}'


@then(u'el inventario tiene {cantidad:d} productos')
def step_impl(context, cantidad):
    productos = context.inventario.obtener_productos()
    assert len(productos) == cantidad, \
        f'Se esperaba que el inventario tuviera {cantidad} producto(s), pero tiene {len(productos)}'


@then(u'el producto con ID {id:d} existe en el inventario')
def step_impl(context, id):
    producto = context.inventario.gestion_productos.obtener_producto(id)
    assert producto is not None, \
        f'Se esperaba encontrar el producto con ID {id} en el inventario, pero no existe'


@then(u'el producto con ID {id:d} no se encuentra en el inventario')
def step_impl(context, id):
    producto = context.inventario.gestion_productos.obtener_producto(id)
    assert producto is None, \
        f'Se esperaba que el producto con ID {id} no existiera, pero existe en el inventario'


@then(u'el producto con ID {id:d} tiene nombre "{nombre}"')
def step_impl(context, id, nombre):
    producto = context.inventario.gestion_productos.obtener_producto(id)
    assert producto is not None, \
        f'No se encontró el producto con ID {id} en el inventario'
    assert producto.nombre == nombre, \
        f'Se esperaba que el producto tuviera nombre "{nombre}", pero tiene "{producto.nombre}"'


@then(u'el producto con ID {id:d} tiene precio {precio:f}')
def step_impl(context, id, precio):
    producto = context.inventario.gestion_productos.obtener_producto(id)
    assert producto is not None, \
        f'No se encontró el producto con ID {id} en el inventario'
    assert producto.precio == precio, \
        f'Se esperaba que el producto tuviera precio {precio}, pero tiene {producto.precio}'


@then(u'el producto con ID {id:d} tiene cantidad {cantidad:d}')
def step_impl(context, id, cantidad):
    producto = context.inventario.gestion_productos.obtener_producto(id)
    assert producto is not None, \
        f'No se encontró el producto con ID {id} en el inventario'
    assert producto.cantidad == cantidad, \
        f'Se esperaba que el producto tuviera cantidad {cantidad}, pero tiene {producto.cantidad}'


@then(u'se produce un error con el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    assert context.error is not None, \
        f'Se esperaba un error con mensaje "{mensaje}", pero no se produjo ningún error'
    assert mensaje in context.error, \
        f'Se esperaba el mensaje de error "{mensaje}", pero se obtuvo "{context.error}"'


@then(u'se produce un error de validación')
def step_impl(context):
    assert context.error is not None, \
        f'Se esperaba un error de validación, pero no se produjo ningún error'