from behave import given, when, then
from carrito_de_compras import Tienda

@given(u'que existe el producto con nombre "{nombre}" precio {precio:f} descripción "{descripcion}" stock {stock:d}')
def step_impl(context, nombre, precio, descripcion, stock):
    if not hasattr(context, 'tienda'):
        context.tienda = Tienda()
    context.tienda.agregar_producto_tienda(nombre, precio, descripcion, stock)

@when(u'edito solo el nombre del producto con ID "{id_producto}" a "{nombre}"')
def step_impl(context, id_producto, nombre):
    context.tienda.editar_producto_tienda(int(id_producto), nombre=nombre)

@when(u'edito solo el precio del producto con ID "{id_producto}" a {precio:f}')
def step_impl(context, id_producto, precio):
    context.tienda.editar_producto_tienda(int(id_producto), precio=precio)

@when(u'edito solo el stock del producto con ID "{id_producto}" a {stock:d}')
def step_impl(context, id_producto, stock):
    context.tienda.editar_producto_tienda(int(id_producto), stock=stock)

@when(u'edito campos múltiples del producto con ID "{id_producto}" nombre "{nombre}" precio {precio:f} descripción "{descripcion}"')
def step_impl(context, id_producto, nombre, precio, descripcion):
    context.tienda.editar_producto_tienda(int(id_producto), nombre=nombre, precio=precio, descripcion=descripcion)

@when(u'intento editar producto inexistente con ID "{id_producto}" nombre "{nombre}"')
def step_impl(context, id_producto, nombre):
    if not hasattr(context, 'tienda'):
        context.tienda = Tienda()
    try:
        context.tienda.editar_producto_tienda(int(id_producto), nombre=nombre)
        context.error = None
    except ValueError as e:
        context.error = str(e)

@then(u'el nombre del producto con ID "{id_producto}" es "{nombre}"')
def step_impl(context, id_producto, nombre):
    producto_tienda = context.tienda.productos[int(id_producto)]
    assert producto_tienda.producto.nombre == nombre, \
        f'Se esperaba nombre "{nombre}" pero se obtuvo "{producto_tienda.producto.nombre}".'

@then(u'el precio del producto con ID "{id_producto}" es {precio:f}')
def step_impl(context, id_producto, precio):
    producto_tienda = context.tienda.productos[int(id_producto)]
    assert producto_tienda.producto.precio == precio, \
        f'Se esperaba precio {precio} pero se obtuvo {producto_tienda.producto.precio}.'

@then(u'el stock del producto con ID "{id_producto}" es {stock:d}')
def step_impl(context, id_producto, stock):
    producto_tienda = context.tienda.productos[int(id_producto)]
    assert producto_tienda.stock == stock, \
        f'Se esperaba stock {stock} pero se obtuvo {producto_tienda.stock}.'

@then(u'verifico producto con ID "{id_producto}" tiene nombre "{nombre}" precio {precio:f} descripción "{descripcion}"')
def step_impl(context, id_producto, nombre, precio, descripcion):
    producto_tienda = context.tienda.productos[int(id_producto)]
    assert producto_tienda.producto.nombre == nombre, \
        f'Se esperaba nombre "{nombre}" pero se obtuvo "{producto_tienda.producto.nombre}".'
    assert producto_tienda.producto.precio == precio, \
        f'Se esperaba precio {precio} pero se obtuvo {producto_tienda.producto.precio}.'
    assert producto_tienda.producto.descripcion == descripcion, \
        f'Se esperaba descripción "{descripcion}" pero se obtuvo "{producto_tienda.producto.descripcion}".'

@then(u'obtengo el error "{mensaje_error}"')
def step_impl(context, mensaje_error):
    assert context.error == mensaje_error, \
        f'Se esperaba el error "{mensaje_error}" y se obtuvo "{context.error}".'
