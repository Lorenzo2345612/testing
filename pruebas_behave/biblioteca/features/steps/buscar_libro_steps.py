from behave import given, when, then
from biblioteca import Libro, Biblioteca

@given(u'que existen los libros con título "{titulo}" con IDs "{id1}" y "{id2}" registrados')
def step_impl(context, titulo, id1, id2):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    libro1 = Libro(int(id1), titulo, "J. K. Rowling")
    libro2 = Libro(int(id2), titulo, "J. K. Rowling")
    context.biblioteca.registrar_libro(libro1)
    context.biblioteca.registrar_libro(libro2)

@when(u'busco el libro por título "{titulo}"')
def step_impl(context, titulo):
    context.libros_encontrados = context.biblioteca.buscar_libro(titulo)

@when(u'busco el libro por ID "{id}"')
def step_impl(context, id):
    context.libro_encontrado = context.biblioteca.buscar_libro_id(int(id))

@then(u'obtengo una lista con "{cantidad}" libros')
def step_impl(context, cantidad):
    assert not isinstance(context.libros_encontrados, str), \
        f'Se esperaba una lista de libros, pero se obtuvo: {context.libros_encontrados}'
    cantidad_actual = len(context.libros_encontrados)
    assert cantidad_actual == int(cantidad), \
        f'Se esperaba encontrar {cantidad} libros y se encontraron {cantidad_actual}.'

@then(u'la lista contiene el libro con ID "{id}"')
def step_impl(context, id):
    assert not isinstance(context.libros_encontrados, str), \
        f'Se esperaba una lista de libros, pero se obtuvo: {context.libros_encontrados}'
    libros_ids = [libro.id for libro in context.libros_encontrados]
    assert int(id) in libros_ids, \
        f'Se esperaba encontrar el libro con ID "{id}" en la lista de resultados.'

@then(u'obtengo el mensaje de búsqueda "{mensaje_esperado}"')
def step_impl(context, mensaje_esperado):
    assert context.libros_encontrados == mensaje_esperado, \
        f'Se esperaba el mensaje "{mensaje_esperado}" y se obtuvo '\
        f'"{context.libros_encontrados}".'

@then(u'obtengo el libro con ID "{id}" y título "{titulo}"')
def step_impl(context, id, titulo):
    libro = context.libro_encontrado
    assert not isinstance(libro, str), \
        f'Se esperaba un objeto Libro, pero se obtuvo un mensaje de error: {libro}'
    assert libro.id == int(id), \
        f'Se esperaba el libro con ID "{id}" y se obtuvo ID "{libro.id}".'
    assert libro.titulo == titulo, \
        f'Se esperaba el libro con título "{titulo}" y se obtuvo "{libro.titulo}".'

@then(u'obtengo el mensaje de búsqueda por ID "{mensaje_esperado}"')
def step_impl(context, mensaje_esperado):
    assert context.libro_encontrado == mensaje_esperado, \
        f'Se esperaba el mensaje "{mensaje_esperado}" y se obtuvo '\
        f'"{context.libro_encontrado}".'