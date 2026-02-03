from behave import given, when, then
from gestion_inventario import GestionInventario


@when(u'registro una compra del producto con ID {id:d} por cantidad {cantidad:d}')
def step_impl(context, id, cantidad):
    try:
        context.inventario.registrar_compra(id, cantidad)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento registrar una compra del producto con ID {id:d} por cantidad {cantidad:d}')
def step_impl(context, id, cantidad):
    try:
        context.inventario.registrar_compra(id, cantidad)
        context.error = None
    except Exception as e:
        context.error = str(e)


@then(u'la compra se registra exitosamente')
def step_impl(context):
    assert context.error is None, \
        f'Se esperaba que la compra se registrara exitosamente, pero se obtuvo el error: {context.error}'


@then(u'el stock del producto con ID {id:d} aumenta a {cantidad:d}')
def step_impl(context, id, cantidad):
    producto = context.inventario.gestion_productos.obtener_producto(id)
    assert producto is not None, \
        f'No se encontró el producto con ID {id} en el inventario'
    assert producto.cantidad == cantidad, \
        f'Se esperaba que el producto con ID {id} tuviera cantidad {cantidad}, pero tiene {producto.cantidad}'


@then(u'el valor total del inventario es {valor:f}')
def step_impl(context, valor):
    valor_total = sum(
        p.precio * p.cantidad for p in context.inventario.obtener_productos()
    )
    assert valor_total == valor, \
        f'Se esperaba que el valor total del inventario fuera {valor}, pero es {valor_total}'