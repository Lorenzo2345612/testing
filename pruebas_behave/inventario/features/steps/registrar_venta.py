from behave import when, then

@when(u'registro una venta del producto con ID "{id}" por cantidad "{cantidad}"')
def step_impl(context, id, cantidad):
    context.mensaje = context.inventario.registrar_venta(int(id), int(cantidad))


@then(u'el producto con ID "{id}" mantiene cantidad "{cantidad}"')
def step_impl(context, id, cantidad):
    producto = context.inventario.consultar_producto_id(int(id))
    assert producto is not None, \
        f'No se encontró el producto con ID "{id}" en el inventario.'
    assert not isinstance(producto, str), \
        f'Se esperaba un objeto Producto, pero se obtuvo un mensaje de error: {producto}'
    assert producto.cantidad == int(cantidad), \
        f'Se esperaba que el producto con ID "{id}" tuviera cantidad "{cantidad}" y se obtuvo'\
        f' "{producto.cantidad}".'

