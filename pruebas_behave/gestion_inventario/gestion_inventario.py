class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


class GestionProductos:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, id, nombre, precio, cantidad):
        if not id or not nombre or precio is None or cantidad is None:
            raise ValueError("Todos los campos son obligatorios")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser un número positivo")
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero no negativo")
        if not isinstance(id, int) or id < 0:
            raise ValueError("El ID debe ser un entero no negativo")
        if any(p.id == id for p in self.productos):
            raise ValueError("El ID del producto ya existe")
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        nuevo_producto = Producto(id, nombre, precio, cantidad)
        self.productos.append(nuevo_producto)

    def obtener_producto(self, id):
        return next((p for p in self.productos if p.id == id), None)

    def buscar_producto_por_nombre(self, nombre: str):
        nombre_normalizado = nombre.strip().lower()
        return next((p for p in self.productos
                     if p.nombre.lower() == nombre_normalizado), None)

    def actualizar_stock(self, id, cantidad):
        if not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un entero")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        producto = self.obtener_producto(id)
        if not producto:
            raise ValueError("Producto no encontrado")
        producto.cantidad = cantidad

    def eliminar_producto(self, id):
        producto = self.obtener_producto(id)
        if not producto:
            raise ValueError("Producto no encontrado")
        self.productos.remove(producto)

    def disminuir_stock(self, id, cantidad):
        producto = self.obtener_producto(id)
        if not producto:
            raise ValueError("Producto no encontrado")
        if cantidad < 0:
            raise ValueError("La cantidad a disminuir no puede ser negativa")
        if producto.cantidad < cantidad:
            raise ValueError("Stock insuficiente")
        producto.cantidad -= cantidad

    def aumentar_stock(self, id, cantidad):
        producto = self.obtener_producto(id)
        if not producto:
            raise ValueError("Producto no encontrado")
        if cantidad < 0:
            raise ValueError("La cantidad a aumentar no puede ser negativa")
        producto.cantidad += cantidad


class GestionInventario:
    def __init__(self):
        self.gestion_productos = GestionProductos()

    def agregar_producto(self, id, nombre, precio, cantidad):
        try:
            self.gestion_productos.agregar_producto(
                id, nombre, precio, cantidad)
        except Exception as e:
            raise e

    def obtener_productos(self):
        return self.gestion_productos.productos

    def buscar_producto(self, nombre):
        return self.gestion_productos.buscar_producto_por_nombre(nombre)

    def actualizar_stock(self, id, cantidad):
        try:
            self.gestion_productos.actualizar_stock(id, cantidad)
        except Exception as e:
            raise e

    def eliminar_producto(self, id):
        try:
            self.gestion_productos.eliminar_producto(id)
        except Exception as e:
            raise e

    def registrar_venta(self, id_producto, cantidad):
        try:
            self.gestion_productos.disminuir_stock(id_producto, cantidad)
        except Exception as e:
            raise e

    def registrar_compra(self, id_producto, cantidad):
        try:
            self.gestion_productos.aumentar_stock(id_producto, cantidad)
        except Exception as e:
            raise e
