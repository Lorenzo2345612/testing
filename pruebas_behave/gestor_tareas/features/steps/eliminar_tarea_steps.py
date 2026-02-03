from behave import given, when, then
from gestor_tareas import GestorTareas


@given(u'que el gestor tiene {cantidad:d} tareas')
def step_impl(context, cantidad):
    context.gestor = GestorTareas()
    for i in range(cantidad):
        context.gestor.agregar_tarea(f"Tarea {i+1}", f"Descripción de la tarea {i+1}")


@when(u'elimino la tarea con ID {id:d}')
def step_impl(context, id):
    try:
        context.resultado = context.gestor.eliminar_tarea(id)
        context.error = None
    except Exception as e:
        context.resultado = False
        context.error = str(e)


@when(u'intento eliminar la tarea con ID {id:d}')
def step_impl(context, id):
    try:
        context.resultado = context.gestor.eliminar_tarea(id)
        context.error = None
    except Exception as e:
        context.resultado = False
        context.error = str(e)


@then(u'la tarea se elimina exitosamente')
def step_impl(context):
    assert context.error is None, \
        f'Se esperaba que la tarea se eliminara exitosamente, pero se obtuvo el error: {context.error}'
    assert context.resultado is True, \
        'Se esperaba que el resultado fuera True'


@then(u'la tarea con ID {id:d} ya no está en el gestor')
def step_impl(context, id):
    for tarea in context.gestor.tareas:
        if tarea.id == id:
            assert False, f'La tarea con ID {id} todavía existe en el gestor'
    # Si llegamos aquí, la tarea no existe (lo cual es lo esperado)
    assert True


@then(u'la tarea con ID {id:d} permanece en el gestor')
def step_impl(context, id):
    tarea_encontrada = False
    for tarea in context.gestor.tareas:
        if tarea.id == id:
            tarea_encontrada = True
            break
    assert tarea_encontrada, \
        f'Se esperaba que la tarea con ID {id} permaneciera en el gestor, pero no se encontró'