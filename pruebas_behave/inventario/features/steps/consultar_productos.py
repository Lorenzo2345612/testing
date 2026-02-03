from behave import given, when, then
from inventario import Inventario

@given(u'que el inventario actual está vacío')
def step_impl(context):
    context.inventario = Inventario()

@when(u'solicito consultar todos los productos')
def step_impl(context):
    context.productos_consultados = context.inventario.listar_productos()


@then(u'obtengo una lista vacía')
def step_impl(context):
    assert context.productos_consultados == [], 'Se esperaba una lista vacía.'


@then(u'obtengo una lista con 1 producto')
def step_impl(context):
    assert len(context.productos_consultados) == 1, 'Se esperaba una lista con 1 producto.'


@then(u'el producto en la lista tiene ID "{id}", nombre "Laptop", cantidad "{cantidad}" y precio "{precio}"')
def step_impl(context, id, cantidad, precio):
    producto = context.productos_consultados[0]
    assert producto.id == int(id), \
        f'El ID del producto es {producto.id} y no "{id}".'
    assert producto.nombre == "Laptop", \
        f'El nombre del producto es {producto.nombre} y no "Laptop".'
    assert producto.cantidad == int(cantidad), \
        f'La cantidad del producto es {producto.cantidad} y no "{cantidad}".'
    assert producto.precio == float(precio), \
        f'El precio del producto es {producto.precio} y no "{precio}".'