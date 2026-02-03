from behave import given, when, then

@when(u'consulto el total del inventario')
def step_impl(context):
    context.total = context.inventario.consultar_total_inventario()

@then(u'obtengo el valor "{valor}"')
def step_impl(context, valor):
    assert f"{context.total:.2f}" == valor, \
        f'Se esperaba que el total del inventario fuera "{valor}" "\
            "y se obtuvo "{context.total:.2f}".'

@then(u'cuando intento registrar otra venta del producto con ID "{id}" por ' \
'cantidad "{cantidad}"')
def step_impl(context, id, cantidad):
    context.mensaje = context.inventario.registrar_venta(int(id), int(cantidad))

@given(u'registro un producto con ID "{id}", nombre "{nombre}", ' \
'cantidad "{cantidad}" y precio "{precio}"')
def step_impl(context, id, nombre, cantidad, precio):
    context.mensaje = context.inventario.registrar_producto(int(id),
                                          nombre,
                                          int(cantidad),
                                          float(precio))