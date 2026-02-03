from behave import given, when, then
from inventario import Inventario

@given(u'que registro un producto con ID "{id}", nombre "{nombre}", ' \
'cantidad "{cantidad}" y precio "{precio}"')
def step_impl(context, id, nombre, cantidad, precio):
    context.inventario = Inventario()
    context.mensaje = context.inventario.registrar_producto(int(id),
                                          nombre,
                                          int(cantidad),
                                          float(precio))



@then(u'obtengo el producto con ID "{id}", nombre "{nombre}", ' \
'cantidad "{cantidad}" y precio "{precio}"')
def step_impl(context, id, nombre, cantidad, precio):
    producto = context.producto_consultado
    assert producto is not None,\
        'El producto no fue encontrado en el inventario.'
    assert not isinstance(producto, str), \
        f'Se esperaba un objeto Producto, pero se obtuvo '\
            'un mensaje de error: {producto}'
    assert producto.id == int(id), \
        f'El ID del producto es {producto.id} y no "{id}".'
    assert producto.nombre == nombre, \
        f'El nombre del producto es {producto.nombre} y no "{nombre}".'
    assert producto.cantidad == int(cantidad), \
        f'La cantidad del producto es {producto.cantidad} y no "{cantidad}".'
    assert producto.precio == float(precio), \
        f'El precio del producto es {producto.precio} y no "{precio}".'


@given(u'que el inventario está vacío')
def step_impl(context):
    context.inventario = Inventario()


@then(u'no obtengo ningún producto')
def step_impl(context):
    assert context.producto_consultado is None or \
           isinstance(context.producto_consultado, str), \
        'Se esperaba no encontrar ningún producto, pero se obtuvo uno.'


@when(u'busco el producto por ID "{id}"')
def step_impl(context, id):
    context.producto_consultado =\
        context.inventario.consultar_producto_id(int(id))

@when(u'busco el producto por nombre "{nombre}"')
def step_impl(context, nombre):
    context.producto_consultado = \
        context.inventario.consultar_producto_nombre(nombre)