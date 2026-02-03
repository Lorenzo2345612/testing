from behave import given, when, then
from carrito_de_compras import Tienda

@when(u'elimino el producto con ID "{id_producto}" de la tienda')
def step_impl(context, id_producto):
    context.tienda.eliminar_producto_tienda(int(id_producto))

@when(u'intento eliminar el producto con ID "{id_producto}" de la tienda')
def step_impl(context, id_producto):
    if not hasattr(context, 'tienda'):
        context.tienda = Tienda()
    try:
        context.tienda.eliminar_producto_tienda(int(id_producto))
        context.error = None
    except ValueError as e:
        context.error = str(e)

@then(u'el producto con ID "{id_producto}" no existe en la tienda')
def step_impl(context, id_producto):
    assert int(id_producto) not in context.tienda.productos, \
        f'El producto con ID {id_producto} no debería existir en la tienda.'
