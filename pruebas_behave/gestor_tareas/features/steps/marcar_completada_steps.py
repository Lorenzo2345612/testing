from behave import given, when, then
from gestor_tareas import GestorTareas


@given(u'que el gestor tiene una tarea con ID {id:d} y estado "{estado}"')
def step_impl(context, id, estado):
    context.gestor = GestorTareas()
    # Agregar tareas hasta llegar al ID deseado
    for i in range(id):
        context.gestor.agregar_tarea(f"Tarea {i+1}", f"Descripción {i+1}")

    # Si el estado debe ser diferente a pendiente, modificarlo
    if estado == "completada":
        context.gestor.marcar_completada(id)


@when(u'marco la tarea con ID {id:d} como completada')
def step_impl(context, id):
    try:
        context.resultado = context.gestor.marcar_completada(id)
        context.error = None
    except Exception as e:
        context.resultado = False
        context.error = str(e)


@when(u'intento marcar la tarea con ID {id:d} como completada')
def step_impl(context, id):
    try:
        context.resultado = context.gestor.marcar_completada(id)
        context.error = None
    except Exception as e:
        context.resultado = False
        context.error = str(e)


@then(u'la tarea se marca como completada exitosamente')
def step_impl(context):
    assert context.error is None, \
        f'Se esperaba que la tarea se marcara como completada exitosamente, pero se obtuvo el error: {context.error}'
    assert context.resultado is True, \
        'Se esperaba que el resultado fuera True'


@then(u'la operación devuelve {resultado}')
def step_impl(context, resultado):
    valor_esperado = resultado.lower() == 'true'
    assert context.resultado == valor_esperado, \
        f'Se esperaba que la operación devolviera {valor_esperado}, pero devolvió {context.resultado}'


@then(u'{cantidad:d} tarea está completada')
def step_impl(context, cantidad):
    tareas_completadas = context.gestor.obtener_tareas_por_estado("completada")
    assert len(tareas_completadas) == cantidad, \
        f'Se esperaba {cantidad} tarea(s) completada(s), pero hay {len(tareas_completadas)}'


@then(u'{cantidad:d} tareas están completadas')
def step_impl(context, cantidad):
    tareas_completadas = context.gestor.obtener_tareas_por_estado("completada")
    assert len(tareas_completadas) == cantidad, \
        f'Se esperaba {cantidad} tarea(s) completada(s), pero hay {len(tareas_completadas)}'


@then(u'la tarea con ID {id:d} está en la lista de tareas completadas')
def step_impl(context, id):
    tareas_completadas = context.gestor.obtener_tareas_por_estado("completada")
    ids_completados = [tarea.id for tarea in tareas_completadas]
    assert id in ids_completados, \
        f'Se esperaba que la tarea con ID {id} estuviera completada, pero no lo está'