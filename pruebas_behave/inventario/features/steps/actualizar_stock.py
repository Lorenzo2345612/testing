from behave import when, then
@when(u'actualizo el stock del producto con ID "{id}" a cantidad "{cantidad}"')
def step_impl(context, id, cantidad):
    context.mensaje = context.inventario.actualizar_stock(int(id), int(cantidad))


@then(u'obtengo el mensaje "{mensaje_esperado}"')
def step_impl(context, mensaje_esperado):
    assert context.mensaje == mensaje_esperado, \
        f'Se esperaba el mensaje "{mensaje_esperado}" y se obtuvo"\
            "{context.mensaje}".'


@then(u'el producto con ID "{id}" tiene cantidad "{cantidad}"')
def step_impl(context, id, cantidad):
    producto = context.inventario.consultar_producto_id(int(id))
    assert producto is not None, \
        f'No se encontró el producto con ID "{id}" en el inventario.'
    assert not isinstance(producto, str), \
        f'Se esperaba un objeto Producto, pero se obtuvo un mensaje de error: {producto}'
    assert producto.cantidad == int(cantidad), \
        f'Se esperaba que el producto con ID "{id}" tuviera cantidad "{cantidad}" y se obtuvo'\
        f' "{producto.cantidad}".'