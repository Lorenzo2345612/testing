class Libro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

class Usuario:
    def __init__(self, id, nombre):
        self.id: int = id
        self.nombre: str = nombre

class Prestamo:
    def __init__(self, libro: Libro, usuario: Usuario):
        self.libro = libro
        self.usuario = usuario

class Biblioteca:
    def __init__(self):
        self.libros: list[Libro] = []
        self.usuarios: list[Usuario] = []
        self.prestamos: list[Prestamo] = []
    def registrar_libro(self, libro: Libro):
        # Validar id negativo o no entero
        if not isinstance(libro.id, int) or libro.id <= 0:
            return "El id debe ser un número positivo entero"
        # Verificar si el libro ya está registrado
        for l in self.libros:
            if l.id == libro.id:
                return "Ya se encuentra registrado ese libro"
        # Valida campos vacíos
        if not libro.titulo and not libro.autor:
            mensaje = "Completa los campos: título y autor"
            libro.titulo = mensaje
            libro.autor = mensaje
        elif not libro.titulo:
            libro.titulo = "Completa el título del libro"
        elif not libro.autor:
            libro.autor = "Completa el nombre del autor"
        # Agregar libro
        self.libros.append(libro)
        return "Se ha registrado correctamente"

    # Consultar libros disponibles o no disponibles
    def consultar_libros(self):
        disponibles = [libro for libro in self.libros if libro.disponible]
        if not disponibles:
            return "No hay libros disponibles"
        return disponibles
    
    # Buscar libro por id
    def buscar_libro_id(self, id_libro: int):
        for libro in self.libros:
            if libro.id == id_libro:
                return libro
        return "No existe ese libro"

    # Buscar libro por título
    def buscar_libro(self, titulo: str):
        encontrados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        if not encontrados:
            return "No existe ese libro"
        return encontrados
    
    # Seleccionar libro por id y verificar disponibilidad
    def seleccionar_libro(self, id_libro: int):
        for libro in self.libros:
            if libro.id == id_libro:
                if libro.disponible:
                    return "Está disponible"
                else:
                    return "Está prestado"
        return "No existe ese libro"

    def registrar_usuario(self, usuario: Usuario):
        # Validar id negativo o no entero
        if not isinstance(usuario.id, int) or usuario.id <= 0:
            return "El id debe ser un número positivo entero"
        # Verificar si el usuario ya está registrado
        for u in self.usuarios:
            if u.id == usuario.id:
                return "Ya existe un usuario con ese identificador"
        # Validar nombre vacío o solo espacios en blanco
        if not usuario.nombre:
            return "Completa el nombre del usuario"
        
        if usuario.nombre.strip() == "":
            return "El nombre no puede estar vacío o contener solo espacios"
        
        # Validar que el nombre no contenga números
        if any(char.isdigit() for char in usuario.nombre):
            return "El nombre no puede contener números"
        
        # Agregar usuario
        self.usuarios.append(usuario)
        return "Usuario registrado correctamente"
    
    def consultar_usuarios(self):
        if not self.usuarios:
            return "No hay usuarios registrados"
        return self.usuarios
    
    def buscar_usuario_id(self, id_usuario: int):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                return usuario
        return "No existe ese usuario"

    def prestar_libro(self, id_libro, id_usuario):
        libro_consultado = self.buscar_libro_id(id_libro)
        usuario_consultado = self.buscar_usuario_id(id_usuario)
        if isinstance(libro_consultado, str):
            return libro_consultado
        if isinstance(usuario_consultado, str):
            return usuario_consultado
        prestamo_existente = self.buscar_prestamo_libro(id_libro)
        if isinstance(prestamo_existente, Prestamo):
            return "El libro ya está prestado"
        libro_consultado.disponible = False
        prestamo = Prestamo(libro_consultado, usuario_consultado)
        self.prestamos.append(prestamo)
        return "El libro se ha prestado con éxito"
    
    
    def consultar_prestamos(self):
        if not self.prestamos:
            return "No hay préstamos registrados"
        return self.prestamos
    
    def buscar_prestamo(self, id_libro, id_usuario):
        for prestamo in self.prestamos:
            if prestamo.libro.id == id_libro and prestamo.usuario.id == id_usuario:
                return prestamo
        return "No existe ese préstamo"
    
    def buscar_prestamo_libro(self, id_libro):
        for prestamo in self.prestamos:
            if prestamo.libro.id == id_libro:
                return prestamo
        return "No existe ese préstamo"

    def devolver_libro(self, id_libro, id_usuario):
        libro = self.buscar_libro_id(id_libro)
        if isinstance(libro, str):
            return libro
        prestamo = self.buscar_prestamo(id_libro, id_usuario)
        if isinstance(prestamo, str):
            return prestamo
        self.prestamos.remove(prestamo)
        libro.disponible = True
        return "El libro se ha devuelto con éxito"
