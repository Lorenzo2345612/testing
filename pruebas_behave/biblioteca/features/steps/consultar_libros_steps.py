from behave import given, when, then
from biblioteca import Libro, Biblioteca

@when(u'consulto los libros disponibles')
def step_impl(context):
    context.libros_consultados = context.biblioteca.consultar_libros()

@then(u'obtengo una lista con el libro de ID "{id}"')
def step_impl(context, id):
    assert not isinstance(context.libros_consultados, str), \
        f'Se esperaba una lista de libros, pero se obtuvo: {context.libros_consultados}'
    libros_ids = [libro.id for libro in context.libros_consultados]
    assert int(id) in libros_ids, \
        f'Se esperaba encontrar el libro con ID "{id}" en la lista de libros disponibles.'

@then(u'obtengo el mensaje de consulta "{mensaje_esperado}"')
def step_impl(context, mensaje_esperado):
    assert context.libros_consultados == mensaje_esperado, \
        f'Se esperaba el mensaje "{mensaje_esperado}" y se obtuvo '\
        f'"{context.libros_consultados}".'

@when(u'selecciono el libro con ID "{id}"')
def step_impl(context, id):
    context.resultado_seleccion = context.biblioteca.seleccionar_libro(int(id))

@then(u'obtengo la disponibilidad "{disponibilidad_esperada}"')
def step_impl(context, disponibilidad_esperada):
    assert context.resultado_seleccion == disponibilidad_esperada, \
        f'Se esperaba el resultado "{disponibilidad_esperada}" y se obtuvo '\
        f'"{context.resultado_seleccion}".'

@given(u'que existe el libro con ID "{id}" con título "{titulo}", con autor "{autor}" y no disponible')
def step_impl(context, id, titulo, autor):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    libro = Libro(int(id), titulo, autor)
    libro.disponible = False
    context.biblioteca.libros.append(libro)