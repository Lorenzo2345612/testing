from behave import given, when, then
from carrito_de_compras import Tienda

@when(u'intento agregar a tienda producto "{nombre}" con precio {precio:f} descripción "{descripcion}" stock {stock:d}')
def step_impl(context, nombre, precio, descripcion, stock):
    if not hasattr(context, 'tienda'):
        context.tienda = Tienda()
    try:
        context.tienda.agregar_producto_tienda(nombre, precio, descripcion, stock)
        context.error = None
    except ValueError as e:
        context.error = str(e)

@when(u'intento agregar a tienda producto con nombre vacío precio {precio:f} descripción "{descripcion}" stock {stock:d}')
def step_impl(context, precio, descripcion, stock):
    if not hasattr(context, 'tienda'):
        context.tienda = Tienda()
    try:
        context.tienda.agregar_producto_tienda("", precio, descripcion, stock)
        context.error = None
    except ValueError as e:
        context.error = str(e)

@when(u'intento modificar el precio del producto con ID "{id_producto}" a {precio:f}')
def step_impl(context, id_producto, precio):
    try:
        context.tienda.editar_producto_tienda(int(id_producto), precio=precio)
        context.error = None
    except ValueError as e:
        context.error = str(e)

@when(u'intento modificar el stock del producto con ID "{id_producto}" a {stock:d}')
def step_impl(context, id_producto, stock):
    try:
        context.tienda.editar_producto_tienda(int(id_producto), stock=stock)
        context.error = None
    except ValueError as e:
        context.error = str(e)
