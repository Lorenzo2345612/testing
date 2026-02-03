from behave import given, when, then
from gestion_inventario import GestionInventario


@when(u'actualizo el stock del producto con ID {id:d} a cantidad {cantidad:d}')
def step_impl(context, id, cantidad):
    try:
        context.inventario.actualizar_stock(id, cantidad)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento actualizar el stock del producto con ID {id:d} a cantidad {cantidad:d}')
def step_impl(context, id, cantidad):
    try:
        context.inventario.actualizar_stock(id, cantidad)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento actualizar el stock del producto con ID {id:d} a cantidad "{cantidad_str}"')
def step_impl(context, id, cantidad_str):
    try:
        context.inventario.actualizar_stock(id, cantidad_str)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento actualizar el stock del producto con ID {id:d} a cantidad None')
def step_impl(context, id):
    try:
        context.inventario.actualizar_stock(id, None)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento actualizar el stock del producto con ID {id:d} a cantidad decimal {cantidad:f}')
def step_impl(context, id, cantidad):
    try:
        context.inventario.actualizar_stock(id, cantidad)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento actualizar el stock del producto con ID {id:d} a una lista')
def step_impl(context, id):
    try:
        context.inventario.actualizar_stock(id, [20])
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento actualizar el stock del producto con ID {id:d} a un diccionario')
def step_impl(context, id):
    try:
        context.inventario.actualizar_stock(id, {"cantidad": 25})
        context.error = None
    except Exception as e:
        context.error = str(e)


@then(u'el stock se actualiza exitosamente')
def step_impl(context):
    assert context.error is None, \
        f'Se esperaba que el stock se actualizara exitosamente, pero se obtuvo el error: {context.error}'


@then(u'el producto con ID {id:d} ya no está en el inventario')
def step_impl(context, id):
    producto = context.inventario.gestion_productos.obtener_producto(id)
    assert producto is None, \
        f'Se esperaba que el producto con ID {id} no existiera, pero existe en el inventario'
