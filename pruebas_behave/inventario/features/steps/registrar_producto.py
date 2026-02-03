from behave import given, when, then
from inventario import Inventario

@given(u'que ingreso el identificador "{id}", el nombre "{nombre}", la cantidad "{cantidad}" y el precio "{precio}"')
def step_impl(context, id, nombre, cantidad, precio):
    context.inventario = Inventario()
    context.id = int(id)
    context.nombre = nombre
    context.cantidad = int(cantidad)
    context.precio = float(precio)

@given(u'que ingreso nuevamente el identificador "{id}", el nombre "{nombre}", la cantidad "{cantidad}" y el precio "{precio}"')
def step_impl(context, id, nombre, cantidad, precio):
    context.id = int(id)
    context.nombre = nombre
    context.cantidad = int(cantidad)
    context.precio = float(precio)

@given(u'que ingreso los datos erroneos "{id}", el nombre "{nombre}", la cantidad "{cantidad}" y el precio "{precio}"')
def step_impl(context, id, nombre, cantidad, precio):
    context.inventario = Inventario()
    context.id = id
    context.nombre = nombre
    context.cantidad = cantidad
    context.precio = precio


@when(u'realizo la operación de registrar producto')
def step_impl(context):
    context.resultado =\
        context.inventario.registrar_producto(context.id,
                                              context.nombre,
                                              context.cantidad,
                                              context.precio)


@then(u'puedo ver el mensaje de éxito "{mensaje_esperado}"')
def step_impl(context, mensaje_esperado):
    assert context.resultado == mensaje_esperado, \
        f'El resultado es {context.resultado} y el esperado es {mensaje_esperado}'

@then(u'el producto con ID "{id}" debe estar en el inventario' \
' con nombre "{nombre}", cantidad "{cantidad}" y precio "{precio}"')
def step_impl(context, id, nombre, cantidad, precio):
    producto = context.inventario.consultar_producto_id(int(id))
    assert producto is not None,\
        'El producto no fue encontrado en el inventario.'
    assert not isinstance(producto, str), \
        f'Se esperaba un objeto Producto, pero se obtuvo un mensaje de error: {producto}'
    assert producto.nombre == nombre, \
        f'El nombre del producto es {producto.nombre} y no "{nombre}".'
    assert producto.cantidad == int(cantidad), \
        f'La cantidad del producto es {producto.cantidad} y no "{cantidad}".'
    assert producto.precio == float(precio), \
        f'El precio del producto es {producto.precio} y no "{precio}".'
    
@then(u'puedo ver el mensaje de error "{mensaje_esperado}"')
def step_impl(context, mensaje_esperado):
    assert context.resultado == mensaje_esperado, \
        f'El resultado es {context.resultado} y el esperado es {mensaje_esperado}'
    
@when(u'ingreso nuevamente el identificador "{id}", el nombre "{nombre}", ' \
'la cantidad "{cantidad}" y el precio "{precio}"')
def step_impl(context, id, nombre, cantidad, precio):
    context.id = int(id)
    context.nombre = nombre
    context.cantidad = int(cantidad)
    context.precio = float(precio)