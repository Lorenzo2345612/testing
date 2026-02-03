from behave import given, when, then
from carrito_de_compras import Tienda

@given(u'que el cliente con ID "{id_cliente}" agrega al carrito el producto con ID "{id_producto}" cantidad {cantidad:d}')
def step_impl(context, id_cliente, id_producto, cantidad):
    context.tienda.agregar_producto_al_carrito(int(id_cliente), int(id_producto), cantidad)

@when(u'consulto el carrito del cliente con ID "{id_cliente}"')
def step_impl(context, id_cliente):
    context.productos_carrito = context.tienda.obtener_productos_del_carrito(int(id_cliente))

@then(u'el carrito del cliente con ID "{id_cliente}" está vacío')
def step_impl(context, id_cliente):
    productos = context.tienda.obtener_productos_del_carrito(int(id_cliente))
    assert len(productos) == 0, \
        f'Se esperaba que el carrito estuviera vacío pero tiene {len(productos)} producto(s).'
