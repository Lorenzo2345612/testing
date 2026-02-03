from behave import given, when, then
from carrito_de_compras import Tienda

@given(u'que existe el cliente "{nombre}"')
def step_impl(context, nombre):
    if not hasattr(context, 'tienda'):
        context.tienda = Tienda()
    context.tienda.agregar_cliente(nombre)

@when(u'el cliente con ID "{id_cliente}" agrega al carrito el producto con ID "{id_producto}" cantidad {cantidad:d}')
def step_impl(context, id_cliente, id_producto, cantidad):
    context.tienda.agregar_producto_al_carrito(int(id_cliente), int(id_producto), cantidad)

@when(u'intento que el cliente con ID "{id_cliente}" agregue al carrito el producto con ID "{id_producto}" cantidad {cantidad:d}')
def step_impl(context, id_cliente, id_producto, cantidad):
    if not hasattr(context, 'tienda'):
        context.tienda = Tienda()
    try:
        context.tienda.agregar_producto_al_carrito(int(id_cliente), int(id_producto), cantidad)
        context.error = None
    except ValueError as e:
        context.error = str(e)

@then(u'el carrito del cliente con ID "{id_cliente}" contiene {cantidad:d} tipo de producto')
def step_impl(context, id_cliente, cantidad):
    productos = context.tienda.obtener_productos_del_carrito(int(id_cliente))
    assert len(productos) == cantidad, \
        f'Se esperaba {cantidad} tipo(s) de producto pero se obtuvo {len(productos)}.'

@then(u'el carrito del cliente con ID "{id_cliente}" tiene el producto con ID "{id_producto}" con cantidad {cantidad:d}')
def step_impl(context, id_cliente, id_producto, cantidad):
    productos = context.tienda.obtener_productos_del_carrito(int(id_cliente))
    producto_encontrado = next((p for p in productos if p.id == int(id_producto)), None)
    assert producto_encontrado is not None, \
        f'No se encontró el producto con ID {id_producto} en el carrito.'
    cantidad_actual = productos[producto_encontrado]
    assert cantidad_actual == cantidad, \
        f'Se esperaba cantidad {cantidad} pero se encontró {cantidad_actual}.'
