from behave import given, when, then
from gestor_tareas import GestorTareas


@given(u'que el gestor tiene tareas con diferentes estados')
def step_impl(context):
    context.gestor = GestorTareas()
    # Agregar varias tareas
    id1 = context.gestor.agregar_tarea("Tarea pendiente 1", "Descripción 1")
    id2 = context.gestor.agregar_tarea("Tarea pendiente 2", "Descripción 2")
    id3 = context.gestor.agregar_tarea("Tarea completada 1", "Descripción 3")
    id4 = context.gestor.agregar_tarea("Tarea pendiente 3", "Descripción 4")

    # Marcar algunas como completadas
    context.gestor.marcar_completada(id3)


@given(u'que el gestor tiene {cantidad_pendientes:d} tareas pendientes y {cantidad_completadas:d} tareas completadas')
def step_impl(context, cantidad_pendientes, cantidad_completadas):
    context.gestor = GestorTareas()

    # Agregar tareas pendientes
    for i in range(cantidad_pendientes):
        context.gestor.agregar_tarea(f"Tarea pendiente {i+1}", f"Descripción pendiente {i+1}")

    # Agregar y completar tareas
    for i in range(cantidad_completadas):
        id = context.gestor.agregar_tarea(f"Tarea completada {i+1}", f"Descripción completada {i+1}")
        context.gestor.marcar_completada(id)


@when(u'obtengo las tareas con estado "{estado}"')
def step_impl(context, estado):
    try:
        context.tareas_filtradas = context.gestor.obtener_tareas_por_estado(estado)
        context.error = None
    except Exception as e:
        context.tareas_filtradas = []
        context.error = str(e)


@when(u'intento obtener las tareas con estado "{estado}"')
def step_impl(context, estado):
    try:
        context.tareas_filtradas = context.gestor.obtener_tareas_por_estado(estado)
        context.error = None
    except Exception as e:
        context.tareas_filtradas = []
        context.error = str(e)


@then(u'obtengo {cantidad:d} tarea')
def step_impl(context, cantidad):
    assert len(context.tareas_filtradas) == cantidad, \
        f'Se esperaba obtener {cantidad} tarea(s), pero se obtuvieron {len(context.tareas_filtradas)}'


@then(u'obtengo {cantidad:d} tareas')
def step_impl(context, cantidad):
    assert len(context.tareas_filtradas) == cantidad, \
        f'Se esperaba obtener {cantidad} tarea(s), pero se obtuvieron {len(context.tareas_filtradas)}'


@then(u'la lista contiene la tarea con ID {id:d}')
def step_impl(context, id):
    ids_encontrados = [tarea.id for tarea in context.tareas_filtradas]
    assert id in ids_encontrados, \
        f'Se esperaba encontrar la tarea con ID {id} en la lista, pero no está. IDs encontrados: {ids_encontrados}'


@then(u'la lista no contiene la tarea con ID {id:d}')
def step_impl(context, id):
    ids_encontrados = [tarea.id for tarea in context.tareas_filtradas]
    assert id not in ids_encontrados, \
        f'No se esperaba encontrar la tarea con ID {id} en la lista, pero está presente'


@then(u'todas las tareas tienen estado "{estado}"')
def step_impl(context, estado):
    for tarea in context.tareas_filtradas:
        assert tarea.estado == estado, \
            f'Se esperaba que todas las tareas tuvieran estado "{estado}", pero la tarea {tarea.id} tiene estado "{tarea.estado}"'


@then(u'obtengo una lista vacía')
def step_impl(context):
    assert len(context.tareas_filtradas) == 0, \
        f'Se esperaba una lista vacía, pero se obtuvieron {len(context.tareas_filtradas)} tarea(s)'