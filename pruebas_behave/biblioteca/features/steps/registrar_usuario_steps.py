from behave import given, when, then
from biblioteca import Usuario, Biblioteca

@given(u'que hay un usuario registrado con ID "{id}" y con nombre "{nombre}"')
def step_impl(context, id, nombre):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    usuario = Usuario(int(id), nombre)
    context.biblioteca.registrar_usuario(usuario)

@when(u'registro el usuario con ID "{id}" y nombre "{nombre}"')
def step_impl(context, id, nombre):
    usuario = Usuario(int(id), nombre)
    context.mensaje_usuario = context.biblioteca.registrar_usuario(usuario)

@when(u'registro el usuario con ID "{id}" sin nombre')
def step_impl(context, id):
    usuario = Usuario(int(id), "")
    context.mensaje_usuario = context.biblioteca.registrar_usuario(usuario)

@when(u'registro el usuario con ID "{id}" y nombre con números "{nombre}"')
def step_impl(context, id, nombre):
    usuario = Usuario(int(id), nombre)
    context.mensaje_usuario = context.biblioteca.registrar_usuario(usuario)

@when(u'registro el usuario con ID negativo "{id}" y nombre "{nombre}"')
def step_impl(context, id, nombre):
    usuario = Usuario(int(id), nombre)
    context.mensaje_usuario = context.biblioteca.registrar_usuario(usuario)

@when(u'registro el usuario con ID no numérico "{id}" y nombre "{nombre}"')
def step_impl(context, id, nombre):
    usuario = Usuario(id, nombre)
    context.mensaje_usuario = context.biblioteca.registrar_usuario(usuario)

@when(u'registro el usuario con ID "{id}" y nombre con solo espacios')
def step_impl(context, id):
    usuario = Usuario(int(id), "   ")
    context.mensaje_usuario = context.biblioteca.registrar_usuario(usuario)

@when(u'consulto los usuarios registrados')
def step_impl(context):
    context.usuarios_consultados = context.biblioteca.consultar_usuarios()

@then(u'obtengo el mensaje de usuario "{mensaje_esperado}"')
def step_impl(context, mensaje_esperado):
    assert context.mensaje_usuario == mensaje_esperado, \
        f'Se esperaba el mensaje "{mensaje_esperado}" y se obtuvo '\
        f'"{context.mensaje_usuario}".'

@then(u'el usuario con ID "{id}" está registrado')
def step_impl(context, id):
    usuario = context.biblioteca.buscar_usuario_id(int(id))
    assert not isinstance(usuario, str), \
        f'Se esperaba un objeto Usuario, pero se obtuvo un mensaje de error: {usuario}'
    assert usuario.id == int(id), \
        f'Se esperaba encontrar el usuario con ID "{id}".'

@then(u'el usuario con ID "{id}" no está registrado')
def step_impl(context, id):
    usuario = context.biblioteca.buscar_usuario_id(int(id))
    assert isinstance(usuario, str), \
        f'Se esperaba no encontrar el usuario con ID "{id}", pero se encontró.'

@then(u'obtengo una lista con el usuario de ID "{id}"')
def step_impl(context, id):
    assert not isinstance(context.usuarios_consultados, str), \
        f'Se esperaba una lista de usuarios, pero se obtuvo: {context.usuarios_consultados}'
    usuarios_ids = [usuario.id for usuario in context.usuarios_consultados]
    assert int(id) in usuarios_ids, \
        f'Se esperaba encontrar el usuario con ID "{id}" en la lista de usuarios.'

@then(u'obtengo el mensaje de consulta de usuarios "{mensaje_esperado}"')
def step_impl(context, mensaje_esperado):
    assert context.usuarios_consultados == mensaje_esperado, \
        f'Se esperaba el mensaje "{mensaje_esperado}" y se obtuvo '\
        f'"{context.usuarios_consultados}".'

@then(u'la biblioteca tiene "{cantidad}" usuarios registrados')
def step_impl(context, cantidad):
    cantidad_actual = len(context.biblioteca.usuarios)
    assert cantidad_actual == int(cantidad), \
        f'Se esperaba que la biblioteca tuviera {cantidad} usuarios registrados '\
        f'y tiene {cantidad_actual}.'