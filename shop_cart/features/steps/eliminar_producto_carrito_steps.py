from behave import given, when, then
from carrito_de_compras import Tienda

@when(u'el cliente con ID "{id_cliente}" elimina del carrito el producto con ID "{id_producto}"')
def step_impl(context, id_cliente, id_producto):
    context.tienda.eliminar_producto_del_carrito(int(id_cliente), int(id_producto))

@when(u'intento que el cliente con ID "{id_cliente}" elimine del carrito el producto con ID "{id_producto}"')
def step_impl(context, id_cliente, id_producto):
    if not hasattr(context, 'tienda'):
        context.tienda = Tienda()
    try:
        context.tienda.eliminar_producto_del_carrito(int(id_cliente), int(id_producto))
        context.error = None
    except ValueError as e:
        context.error = str(e)
