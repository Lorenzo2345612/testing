from behave import given, when, then
from carrito_de_compras import Tienda

@when(u'consulto los productos de la tienda')
def step_impl(context):
    if not hasattr(context, 'tienda'):
        context.tienda = Tienda()
    context.productos_consultados = context.tienda.consultar_productos()

@then(u'obtengo una lista con {cantidad:d} productos')
def step_impl(context, cantidad):
    assert len(context.productos_consultados) == cantidad, \
        f'Se esperaba {cantidad} producto(s) pero se obtuvo {len(context.productos_consultados)}.'
