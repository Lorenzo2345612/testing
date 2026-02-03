from behave import given, when, then
from gestion_inventario import GestionInventario


@when(u'busco el producto con nombre "{nombre}"')
def step_impl(context, nombre):
    context.producto_encontrado = context.inventario.buscar_producto(nombre)


@when(u'busco el producto con nombre "{nombre}" con espacios extras')
def step_impl(context, nombre):
    context.producto_encontrado = context.inventario.buscar_producto(f"  {nombre}  ")


@when(u'busco el producto con nombre "{nombre}" en minúsculas')
def step_impl(context, nombre):
    context.producto_encontrado = context.inventario.buscar_producto(nombre.lower())


@when(u'busco el producto con nombre "{nombre}" en mayúsculas')
def step_impl(context, nombre):
    context.producto_encontrado = context.inventario.buscar_producto(nombre.upper())


@then(u'encuentro el producto con ID {id:d}')
def step_impl(context, id):
    assert context.producto_encontrado is not None, \
        f'Se esperaba encontrar un producto con ID {id}, pero no se encontró ninguno'
    assert context.producto_encontrado.id == id, \
        f'Se esperaba encontrar el producto con ID {id}, pero se encontró el ID {context.producto_encontrado.id}'


@then(u'encuentro el producto con nombre "{nombre}"')
def step_impl(context, nombre):
    assert context.producto_encontrado is not None, \
        f'Se esperaba encontrar un producto con nombre "{nombre}", pero no se encontró ninguno'
    assert context.producto_encontrado.nombre == nombre, \
        f'Se esperaba encontrar el producto con nombre "{nombre}", pero se encontró "{context.producto_encontrado.nombre}"'


@then(u'encuentro el producto con precio {precio:f}')
def step_impl(context, precio):
    assert context.producto_encontrado is not None, \
        f'Se esperaba encontrar un producto, pero no se encontró ninguno'
    assert context.producto_encontrado.precio == precio, \
        f'Se esperaba encontrar el producto con precio {precio}, pero se encontró {context.producto_encontrado.precio}'


@then(u'encuentro el producto con cantidad {cantidad:d}')
def step_impl(context, cantidad):
    assert context.producto_encontrado is not None, \
        f'Se esperaba encontrar un producto, pero no se encontró ninguno'
    assert context.producto_encontrado.cantidad == cantidad, \
        f'Se esperaba encontrar el producto con cantidad {cantidad}, pero se encontró {context.producto_encontrado.cantidad}'


@then(u'no encuentro ningún producto')
def step_impl(context):
    assert context.producto_encontrado is None, \
        f'Se esperaba no encontrar ningún producto, pero se encontró uno con nombre "{context.producto_encontrado.nombre}"'


@given(u'que el inventario tiene productos con nombres similares')
def step_impl(context):
    context.inventario = GestionInventario()
    context.inventario.agregar_producto(1, "Mouse Inalámbrico", 30.00, 10)
    context.inventario.agregar_producto(2, "Mouse USB", 20.00, 15)