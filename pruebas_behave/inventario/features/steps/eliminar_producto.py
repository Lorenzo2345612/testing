from behave import when, then

@when(u'elimino el producto con ID "{id}"')
def step_impl(context, id):
    context.mensaje = context.inventario.eliminar_producto(int(id))


@then(u'el producto con ID "{id}" ya no está en el inventario')
def step_impl(context, id):
    producto = context.inventario.consultar_producto_id(int(id))
    assert producto is None, \
        f'Se esperaba que el producto con ID "{id}" no estuviera en el inventario.'