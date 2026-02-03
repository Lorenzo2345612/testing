from behave import given, when, then
from gestor_tareas import GestorTareas


@given(u'que el gestor de tareas está vacío')
def step_impl(context):
    context.gestor = GestorTareas()


@given(u'que el gestor tiene una tarea con nombre "{nombre}" y descripción "{descripcion}"')
def step_impl(context, nombre, descripcion):
    context.gestor = GestorTareas()
    context.gestor.agregar_tarea(nombre, descripcion)


@when(u'agrego una tarea con nombre "{nombre}" y descripción "{descripcion}"')
def step_impl(context, nombre, descripcion):
    try:
        context.id_tarea = context.gestor.agregar_tarea(nombre, descripcion)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento agregar una tarea con nombre "{nombre}" y descripción "{descripcion}"')
def step_impl(context, nombre, descripcion):
    try:
        context.id_tarea = context.gestor.agregar_tarea(nombre, descripcion)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento agregar una tarea con nombre vacío y descripción "{descripcion}"')
def step_impl(context, descripcion):
    try:
        context.id_tarea = context.gestor.agregar_tarea("", descripcion)
        context.error = None
    except Exception as e:
        context.error = str(e)


@when(u'intento agregar una tarea con nombre "{nombre}" y descripción vacía')
def step_impl(context, nombre):
    try:
        context.id_tarea = context.gestor.agregar_tarea(nombre, "")
        context.error = None
    except Exception as e:
        context.error = str(e)


@then(u'la tarea se agrega exitosamente con ID {id:d}')
def step_impl(context, id):
    assert context.error is None, \
        f'Se esperaba que la tarea se agregara exitosamente, pero se obtuvo el error: {context.error}'
    assert context.id_tarea == id, \
        f'Se esperaba que la tarea tuviera ID {id}, pero tiene ID {context.id_tarea}'


@then(u'la tarea se agrega exitosamente')
def step_impl(context):
    assert context.error is None, \
        f'Se esperaba que la tarea se agregara exitosamente, pero se obtuvo el error: {context.error}'
    assert context.id_tarea is not None, \
        'Se esperaba que se asignara un ID a la tarea'


@then(u'el gestor tiene {cantidad:d} tarea')
def step_impl(context, cantidad):
    tareas = context.gestor.tareas
    assert len(tareas) == cantidad, \
        f'Se esperaba que el gestor tuviera {cantidad} tarea(s), pero tiene {len(tareas)}'


@then(u'el gestor tiene {cantidad:d} tareas')
def step_impl(context, cantidad):
    tareas = context.gestor.tareas
    assert len(tareas) == cantidad, \
        f'Se esperaba que el gestor tuviera {cantidad} tarea(s), pero tiene {len(tareas)}'


@then(u'la tarea con ID {id:d} tiene nombre "{nombre}"')
def step_impl(context, id, nombre):
    tarea = None
    for t in context.gestor.tareas:
        if t.id == id:
            tarea = t
            break
    assert tarea is not None, \
        f'No se encontró la tarea con ID {id} en el gestor'
    assert tarea.nombre == nombre, \
        f'Se esperaba que la tarea tuviera nombre "{nombre}", pero tiene "{tarea.nombre}"'


@then(u'la tarea con ID {id:d} tiene descripción "{descripcion}"')
def step_impl(context, id, descripcion):
    tarea = None
    for t in context.gestor.tareas:
        if t.id == id:
            tarea = t
            break
    assert tarea is not None, \
        f'No se encontró la tarea con ID {id} en el gestor'
    assert tarea.descripcion == descripcion, \
        f'Se esperaba que la tarea tuviera descripción "{descripcion}", pero tiene "{tarea.descripcion}"'


@then(u'la tarea con ID {id:d} tiene estado "{estado}"')
def step_impl(context, id, estado):
    tarea = None
    for t in context.gestor.tareas:
        if t.id == id:
            tarea = t
            break
    assert tarea is not None, \
        f'No se encontró la tarea con ID {id} en el gestor'
    assert tarea.estado == estado, \
        f'Se esperaba que la tarea tuviera estado "{estado}", pero tiene "{tarea.estado}"'


@then(u'se produce un error con mensaje "{mensaje}"')
def step_impl(context, mensaje):
    assert context.error is not None, \
        f'Se esperaba un error con mensaje "{mensaje}", pero no se produjo ningún error'
    assert mensaje in context.error, \
        f'Se esperaba el mensaje de error "{mensaje}", pero se obtuvo "{context.error}"'