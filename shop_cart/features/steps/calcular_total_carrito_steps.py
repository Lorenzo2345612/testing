from behave import given, when, then
from carrito_de_compras import Tienda

@when(u'calculo el total del carrito del cliente con ID "{id_cliente}"')
def step_impl(context, id_cliente):
    context.total_carrito = context.tienda.calcular_total_del_carrito(int(id_cliente))

@then(u'el total del carrito es {total:f}')
def step_impl(context, total):
    assert context.total_carrito == total, \
        f'Se esperaba un total de {total} pero se obtuvo {context.total_carrito}.'
