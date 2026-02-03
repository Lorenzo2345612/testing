from behave import given, when, then
from carrito_de_compras import Tienda

@when(u'el cliente con ID "{id_cliente}" vacía su carrito')
def step_impl(context, id_cliente):
    context.tienda.vaciar_carrito(int(id_cliente))
