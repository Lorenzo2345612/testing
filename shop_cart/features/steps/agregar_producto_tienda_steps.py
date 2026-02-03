from behave import given, when, then
from carrito_de_compras import Tienda

@when(u'agrego el producto con nombre "{nombre}" precio {precio:f} descripción "{descripcion}" stock {stock:d}')
def step_impl(context, nombre, precio, descripcion, stock):
    if not hasattr(context, 'tienda'):
        context.tienda = Tienda()
    context.tienda.agregar_producto_tienda(nombre, precio, descripcion, stock)

@then(u'el producto con ID "{id_producto}" existe en la tienda')
def step_impl(context, id_producto):
    assert int(id_producto) in context.tienda.productos, \
        f'El producto con ID {id_producto} no existe en la tienda.'

@then(u'verifico datos del producto con ID "{id_producto}" nombre "{nombre}" precio {precio:f} descripción "{descripcion}" stock {stock:d}')
def step_impl(context, id_producto, nombre, precio, descripcion, stock):
    producto_tienda = context.tienda.productos[int(id_producto)]
    assert producto_tienda.producto.nombre == nombre, \
        f'Se esperaba nombre "{nombre}" pero se obtuvo "{producto_tienda.producto.nombre}".'
    assert producto_tienda.producto.precio == precio, \
        f'Se esperaba precio {precio} pero se obtuvo {producto_tienda.producto.precio}.'
    assert producto_tienda.producto.descripcion == descripcion, \
        f'Se esperaba descripción "{descripcion}" pero se obtuvo "{producto_tienda.producto.descripcion}".'
    assert producto_tienda.stock == stock, \
        f'Se esperaba stock {stock} pero se obtuvo {producto_tienda.stock}.'
