from behave import given, when, then
from biblioteca import Libro, Usuario, Prestamo, Biblioteca

@given(u'que hay un libro registrado con ID "{id_libro}" y un usuario registrado con ID "{id_usuario}"')
def step_impl(context, id_libro, id_usuario):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    libro = Libro(int(id_libro), "El ingenioso hidalgo Don Quijote de la Mancha", "Miguel de Cervantes")
    usuario = Usuario(int(id_usuario), "Juan")
    context.biblioteca.registrar_libro(libro)
    context.biblioteca.registrar_usuario(usuario)

@given(u'que hay un libro registrado con ID "{id_libro}" y título "{titulo}"')
def step_impl(context, id_libro, titulo):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    libro = Libro(int(id_libro), titulo, "J.R.R. Tolkien")
    context.biblioteca.registrar_libro(libro)

@given(u'que el libro con ID "{id_libro}" está prestado al usuario con ID "{id_usuario}"')
def step_impl(context, id_libro, id_usuario):
    context.biblioteca.prestar_libro(int(id_libro), int(id_usuario))

@when(u'presto el libro con ID "{id_libro}" al usuario con ID "{id_usuario}"')
def step_impl(context, id_libro, id_usuario):
    context.resultado_prestamo = context.biblioteca.prestar_libro(int(id_libro), int(id_usuario))

@then(u'obtengo el mensaje de préstamo "{mensaje_esperado}"')
def step_impl(context, mensaje_esperado):
    assert context.resultado_prestamo == mensaje_esperado, \
        f'Se esperaba el mensaje "{mensaje_esperado}" y se obtuvo '\
        f'"{context.resultado_prestamo}".'

@then(u'el libro con ID "{id}" no está disponible')
def step_impl(context, id):
    libro = context.biblioteca.buscar_libro_id(int(id))
    assert not isinstance(libro, str), \
        f'Se esperaba un objeto Libro, pero se obtuvo un mensaje de error: {libro}'
    assert not libro.disponible, \
        f'Se esperaba que el libro con ID "{id}" no estuviera disponible.'

@then(u'el libro con ID "{id}" está disponible')
def step_impl(context, id):
    libro = context.biblioteca.buscar_libro_id(int(id))
    assert not isinstance(libro, str), \
        f'Se esperaba un objeto Libro, pero se obtuvo un mensaje de error: {libro}'
    assert libro.disponible, \
        f'Se esperaba que el libro con ID "{id}" estuviera disponible.'

@then(u'existe un préstamo del libro con ID "{id_libro}" al usuario con ID "{id_usuario}"')
def step_impl(context, id_libro, id_usuario):
    prestamo = context.biblioteca.buscar_prestamo(int(id_libro), int(id_usuario))
    assert isinstance(prestamo, Prestamo), \
        f'Se esperaba un objeto Prestamo, pero se obtuvo: {prestamo}'

@then(u'no existe un préstamo del libro con ID "{id_libro}" al usuario con ID "{id_usuario}"')
def step_impl(context, id_libro, id_usuario):
    prestamo = context.biblioteca.buscar_prestamo(int(id_libro), int(id_usuario))
    assert isinstance(prestamo, str), \
        f'Se esperaba no encontrar el préstamo, pero se encontró.'

@given(u'que existen dos usuarios con IDs "{id1}" y "{id2}" registrados')
def step_impl(context, id1, id2):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    usuario1 = Usuario(int(id1), "Marta")
    usuario2 = Usuario(int(id2), "Sofía")
    context.biblioteca.registrar_usuario(usuario1)
    context.biblioteca.registrar_usuario(usuario2)

@given(u'que hay un libro registrado con ID "{id_libro}"')
def step_impl(context, id_libro):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    libro = Libro(int(id_libro), "La Divina Comedia", "Dante Alighieri")
    context.biblioteca.registrar_libro(libro)