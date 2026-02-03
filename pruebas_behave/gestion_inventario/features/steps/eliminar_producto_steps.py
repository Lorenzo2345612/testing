from behave import given, when, then
from gestion_inventario import GestionInventario


@given(u'que el inventario tiene dos productos')
def step_impl(context):
    context.inventario = GestionInventario()
    context.inventario.agregar_producto(1, "Laptop", 1500.00, 10)
    context.inventario.agregar_producto(2, "Mouse", 25.00, 50)


@when(u'elimino el producto con ID {id:d}')
def step_impl(context, id):
    try:
        context.inventario.eliminar_producto(id)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento eliminar el producto con ID {id:d}')
def step_impl(context, id):
    try:
        context.inventario.eliminar_producto(id)
        context.error = None
    except Exception as e:
        context.error = str(e)


@then(u'el producto se elimina exitosamente')
def step_impl(context):
    assert context.error is None, \
        f'Se esperaba que el producto se eliminara exitosamente, pero se obtuvo el error: {context.error}'


@then(u'el producto con nombre "{nombre}" permanece en el inventario')
def step_impl(context, nombre):
    producto = context.inventario.buscar_producto(nombre)
    assert producto is not None, \
        f'Se esperaba que el producto con nombre "{nombre}" permaneciera en el inventario, pero no se encontró'
    assert producto.nombre == nombre, \
        f'Se esperaba encontrar el producto con nombre "{nombre}", pero se encontró "{producto.nombre}"'