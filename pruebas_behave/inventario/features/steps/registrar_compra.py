from behave import when

@when(u'registro una compra del producto con ID "{id}" por cantidad "{cantidad}"')
def step_impl(context, id, cantidad):
    context.mensaje = context.inventario.registrar_compra(int(id), int(cantidad))
