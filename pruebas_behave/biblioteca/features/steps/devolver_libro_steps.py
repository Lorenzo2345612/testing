from behave import given, when, then
from biblioteca import Libro, Usuario, Prestamo, Biblioteca

@given(u'que existe el libro con ID "{id_libro}" título "{titulo}" autor "{autor}" registrado y el usuario con ID "{id_usuario}" nombre "{nombre}" registrado')
def step_impl(context, id_libro, titulo, autor, id_usuario, nombre):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    libro = Libro(int(id_libro), titulo, autor)
    usuario = Usuario(int(id_usuario), nombre)
    context.biblioteca.registrar_libro(libro)
    context.biblioteca.registrar_usuario(usuario)

@given(u'que el libro con ID "{id_libro}" fue prestado al usuario con ID "{id_usuario}"')
def step_impl(context, id_libro, id_usuario):
    context.biblioteca.prestar_libro(int(id_libro), int(id_usuario))

@when(u'devuelvo el libro con ID "{id_libro}" del usuario con ID "{id_usuario}"')
def step_impl(context, id_libro, id_usuario):
    context.resultado_devolucion = context.biblioteca.devolver_libro(int(id_libro), int(id_usuario))

@then(u'obtengo el mensaje de devolución "{mensaje_esperado}"')
def step_impl(context, mensaje_esperado):
    assert context.resultado_devolucion == mensaje_esperado, \
        f'Se esperaba el mensaje "{mensaje_esperado}" y se obtuvo '\
        f'"{context.resultado_devolucion}".'

@given(u'que existen tres usuarios con IDs "{id1}", "{id2}" y "{id3}" registrados')
def step_impl(context, id1, id2, id3):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    usuario1 = Usuario(int(id1), "Bob")
    usuario2 = Usuario(int(id2), "Clara")
    usuario3 = Usuario(int(id3), "Ana")
    context.biblioteca.registrar_usuario(usuario1)
    context.biblioteca.registrar_usuario(usuario2)
    context.biblioteca.registrar_usuario(usuario3)

@given(u'que existe el libro con ID "{id_libro}" título "{titulo}" registrado')
def step_impl(context, id_libro, titulo):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    libro = Libro(int(id_libro), titulo, "Jane Austen")
    context.biblioteca.registrar_libro(libro)

@given(u'que existe el usuario con ID "{id_usuario}" registrado')
def step_impl(context, id_usuario):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    usuario = Usuario(int(id_usuario), "Eva")
    context.biblioteca.registrar_usuario(usuario)

@given(u'que existe el libro con ID "{id_libro}" y usuario con ID "{id_usuario}" registrados')
def step_impl(context, id_libro, id_usuario):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    libro = Libro(int(id_libro), "La Odisea", "Homero")
    usuario = Usuario(int(id_usuario), "Luis")
    context.biblioteca.registrar_libro(libro)
    context.biblioteca.registrar_usuario(usuario)

@given(u'que existen el libro con ID "{id_libro}" y dos usuarios con IDs "{id_usuario1}" y "{id_usuario2}" registrados')
def step_impl(context, id_libro, id_usuario1, id_usuario2):
    if not hasattr(context, 'biblioteca'):
        context.biblioteca = Biblioteca()
    libro = Libro(int(id_libro), "Don Juan Tenorio", "José Zorrilla")
    usuario1 = Usuario(int(id_usuario1), "Ana")
    usuario2 = Usuario(int(id_usuario2), "Pedro")
    context.biblioteca.registrar_libro(libro)
    context.biblioteca.registrar_usuario(usuario1)
    context.biblioteca.registrar_usuario(usuario2)