class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __eq__(self, value):
        if not isinstance(value, Producto):
            return False
        return (self.id == value.id and self.nombre == value.nombre and
                self.cantidad == value.cantidad and
                self.precio == value.precio)


class Inventario:
    def __init__(self):
        self.productos: list[Producto] = []

    def comprobar_id_valido(self, id):
        if not self.comprobar_es_numerico(id):
            return "ERROR: El ID del producto debe ser un número."
        if (not self.comprobar_es_entero(id) or
                not self.comprobar_numero_positivo(id)):
            return (
                "ERROR: El ID del producto debe ser "
                "un número entero positivo."
            )
        return None

    def comprobar_nombre_valido(self, nombre):
        if not isinstance(nombre, str):
            return (
                "ERROR: El nombre del producto debe ser una cadena de texto."
            )
        if nombre.strip() == "":
            return "ERROR: El nombre del producto no puede estar vacío."
        return None

    def comprobar_cantidad_valida(self, cantidad):
        if not self.comprobar_es_numerico(cantidad):
            return "ERROR: La cantidad debe ser un número."
        if not self.comprobar_es_entero(cantidad):
            return "ERROR: La cantidad debe ser un número entero."
        if not self.comprobar_numero_positivo(cantidad):
            return "ERROR: La cantidad no puede ser negativa."
        if cantidad == 0:
            return "ERROR: La cantidad no puede ser cero."
        return None

    def comprobar_precio_valido(self, precio):
        if not self.comprobar_es_numerico(precio):
            return "ERROR: El precio debe ser un número."
        if not self.comprobar_numero_positivo(precio):
            return "ERROR: El precio no puede ser negativo."
        if precio == 0:
            return "ERROR: El precio no puede ser cero."
        return None

    def comprobar_es_numerico(self, valor):
        return isinstance(valor, (int, float))

    def comprobar_numero_positivo(self, valor):
        return valor >= 0

    def comprobar_es_entero(self, valor):
        return isinstance(valor, int)

    def comprobar_producto_valido(self, id, nombre, cantidad, precio):
        id_valido = self.comprobar_id_valido(id)
        if id_valido is not None:
            return id_valido

        producto_existente = self.consultar_producto_id(id)
        if producto_existente is not None:
            return "ERROR: El ID del producto ya existe."

        nombre_valido = self.comprobar_nombre_valido(nombre)
        if nombre_valido is not None:
            return nombre_valido

        cantidad_valida = self.comprobar_cantidad_valida(cantidad)
        if cantidad_valida is not None:
            return cantidad_valida

        precio_valido = self.comprobar_precio_valido(precio)
        if precio_valido is not None:
            return precio_valido

        return None

    def registrar_producto(self, id, nombre, cantidad, precio):
        resultado = self.comprobar_producto_valido(
            id, nombre, cantidad, precio)
        if resultado is not None:
            return resultado

        nuevo_producto = Producto(id, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        return "Producto registrado exitosamente."

    def listar_productos(self):
        return self.productos

    def consultar_producto_id(self, id):
        id_valido = self.comprobar_id_valido(id)
        if id_valido is not None:
            return id_valido

        for producto in self.productos:
            if producto.id == id:
                return producto
        return None

    def consultar_producto_nombre(self, nombre):
        nombre_valido = self.comprobar_nombre_valido(nombre)
        if nombre_valido is not None:
            return nombre_valido

        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def actualizar_stock(self, id, nueva_cantidad):
        id_valido = self.comprobar_id_valido(id)
        if id_valido is not None:
            return id_valido

        cantidad_valida = self.comprobar_cantidad_valida(nueva_cantidad)
        if cantidad_valida is not None:
            return cantidad_valida

        for producto in self.productos:
            if producto.id == id:
                producto.cantidad = nueva_cantidad
                return "Stock actualizado exitosamente."
        return "ERROR: Producto no encontrado."

    def eliminar_producto(self, id):
        id_valido = self.comprobar_id_valido(id)
        if id_valido is not None:
            return id_valido
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                return "Producto eliminado exitosamente."
        return "ERROR: Producto no encontrado."

    def registrar_venta(self, id, cantidad_vendida):
        id_valido = self.comprobar_id_valido(id)
        if id_valido is not None:
            return id_valido

        cantidad_valida = self.comprobar_cantidad_valida(cantidad_vendida)
        if cantidad_valida is not None:
            return cantidad_valida
        for producto in self.productos:
            if producto.id == id:
                if producto.cantidad < cantidad_vendida:
                    return "ERROR: Stock insuficiente."
                producto.cantidad -= cantidad_vendida
                return "Venta registrada exitosamente."
        return "ERROR: Producto no encontrado."

    def registrar_compra(self, id, cantidad_comprada):
        id_valido = self.comprobar_id_valido(id)
        if id_valido is not None:
            return id_valido

        cantidad_valida = self.comprobar_cantidad_valida(cantidad_comprada)
        if cantidad_valida is not None:
            return cantidad_valida
        for producto in self.productos:
            if producto.id == id:
                producto.cantidad += cantidad_comprada
                return "Compra registrada exitosamente."
        return "ERROR: Producto no encontrado."

    def consultar_total_inventario(self):
        total = 0.00
        for producto in self.productos:
            total += producto.cantidad * producto.precio
        return total
