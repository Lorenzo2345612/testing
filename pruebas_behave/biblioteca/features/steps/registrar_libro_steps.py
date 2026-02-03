from behave import given, when, then
from biblioteca import Libro, Usuario, Biblioteca

@given(u'que la biblioteca está vacía')
def step_impl(context):
    context.biblioteca = Biblioteca()

@given(u'que registro el libro con ID "{id}", título "{titulo}" y autor "{autor}"')
def step_impl(context, id, titulo, autor):
    context.biblioteca = Biblioteca()
    libro = Libro(int(id), titulo, autor)
    context.mensaje = context.biblioteca.registrar_libro(libro)

@given(u'que existe el libro con ID "{id}" con título "{titulo}" y con autor "{autor}" registrado')
def step_impl(context, id, titulo, autor):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    libro = Libro(int(id), titulo, autor)
    context.biblioteca.registrar_libro(libro)

@when(u'registro el libro con ID "{id}", título "{titulo}" y autor "{autor}"')
def step_impl(context, id, titulo, autor):
    libro = Libro(int(id), titulo, autor)
    context.mensaje = context.biblioteca.registrar_libro(libro)

@when(u'registro el libro con ID no numérico "{id}", título "{titulo}" y autor "{autor}"')
def step_impl(context, id, titulo, autor):
    libro = Libro(id, titulo, autor)
    context.mensaje = context.biblioteca.registrar_libro(libro)

@when(u'registro el libro con ID negativo "{id}", título "{titulo}" y autor "{autor}"')
def step_impl(context, id, titulo, autor):
    libro = Libro(int(id), titulo, autor)
    context.mensaje = context.biblioteca.registrar_libro(libro)

@when(u'registro el libro con ID "{id}", sin título y sin autor')
def step_impl(context, id):
    libro = Libro(int(id), "", "")
    context.mensaje = context.biblioteca.registrar_libro(libro)

@when(u'registro el libro con ID "{id}", título "{titulo}" y sin autor')
def step_impl(context, id, titulo):
    libro = Libro(int(id), titulo, "")
    context.mensaje = context.biblioteca.registrar_libro(libro)

@then(u'obtengo el mensaje "{mensaje_esperado}"')
def step_impl(context, mensaje_esperado):
    assert context.mensaje == mensaje_esperado, \
        f'Se esperaba el mensaje "{mensaje_esperado}" y se obtuvo '\
        f'"{context.mensaje}".'

@then(u'el libro con ID "{id}" está en la biblioteca')
def step_impl(context, id):
    libro = context.biblioteca.buscar_libro_id(int(id))
    assert not isinstance(libro, str), \
        f'Se esperaba un objeto Libro, pero se obtuvo un mensaje de error: {libro}'
    assert libro.id == int(id), \
        f'Se esperaba encontrar el libro con ID "{id}".'

@then(u'el libro con ID "{id}" tiene el título "{titulo_esperado}"')
def step_impl(context, id, titulo_esperado):
    libro = context.biblioteca.buscar_libro_id(int(id))
    assert not isinstance(libro, str), \
        f'Se esperaba un objeto Libro, pero se obtuvo un mensaje de error: {libro}'
    assert libro.titulo == titulo_esperado, \
        f'Se esperaba que el libro con ID "{id}" tuviera título "{titulo_esperado}" '\
        f'y se obtuvo "{libro.titulo}".'

@then(u'el libro con ID "{id}" tiene el autor "{autor_esperado}"')
def step_impl(context, id, autor_esperado):
    libro = context.biblioteca.buscar_libro_id(int(id))
    assert not isinstance(libro, str), \
        f'Se esperaba un objeto Libro, pero se obtuvo un mensaje de error: {libro}'
    assert libro.autor == autor_esperado, \
        f'Se esperaba que el libro con ID "{id}" tuviera autor "{autor_esperado}" '\
        f'y se obtuvo "{libro.autor}".'

@then(u'el libro con ID "{id}" no está en la biblioteca')
def step_impl(context, id):
    libro = context.biblioteca.buscar_libro_id(int(id))
    assert isinstance(libro, str), \
        f'Se esperaba no encontrar el libro con ID "{id}", pero se encontró.'

@then(u'la biblioteca tiene "{cantidad}" libros registrados')
def step_impl(context, cantidad):
    cantidad_actual = len(context.biblioteca.libros)
    assert cantidad_actual == int(cantidad), \
        f'Se esperaba que la biblioteca tuviera {cantidad} libros registrados '\
        f'y tiene {cantidad_actual}.'