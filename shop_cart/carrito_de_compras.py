from typing import Dict

class ProductoInfo:
    id: int
    nombre: str
    precio: float
    descripcion: str

    def __init__(self, id: int, nombre: str, precio: float, descripcion: str):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

class ProductoTienda:
    producto: ProductoInfo
    stock: int

    def __init__(self, producto: ProductoInfo, stock: int):
        self.producto = producto
        self.stock = stock

class Cliente:
    id: int
    nombre: str
    
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

class CarritoDeCompras:
    id_cliente: int
    productos: Dict[ProductoInfo, int]  # Mapea ProductoInfo a cantidad

    def __init__(self, id_cliente: int):
        self.id_cliente = id_cliente
        self.productos = {}

    def agregar_producto(self, producto: ProductoInfo, cantidad: int):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo.")
        
        if not isinstance(producto, ProductoInfo):
            raise TypeError("El producto debe ser una instancia de ProductoInfo.")
        
        producto_en_carrito = next((p for p in self.productos if p.id == producto.id), None)
        if producto_en_carrito:
            self.productos[producto_en_carrito] += cantidad
        else:
            self.productos[producto] = cantidad

    def obtener_productos(self):
        return self.productos
    
    def calcular_total(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos.items())
        return total
    
    def vaciar_carrito(self):
        self.productos.clear()
    
    def eliminar_producto(self, producto: ProductoInfo):
        if not isinstance(producto, ProductoInfo):
            raise TypeError("El producto debe ser una instancia de ProductoInfo.")
        
        producto_en_carrito = next((p for p in self.productos if p.id == producto.id), None)
        if producto_en_carrito:
            del self.productos[producto_en_carrito]
        else:
            raise ValueError("El producto no está en el carrito.")


class Tienda:
    clientes: Dict[int, Cliente]
    productos: Dict[int, ProductoTienda]
    carritos: Dict[int, CarritoDeCompras]

    id_cliente_counter: int = 1
    id_producto_counter: int = 1

    def __init__(self):
        self.clientes = {}
        self.productos = {}
        self.carritos = {}

    def agregar_cliente(self, nombre: str) -> Cliente:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del cliente debe ser una cadena no vacía.")
        cliente = Cliente(self.id_cliente_counter, nombre)
        self.clientes[self.id_cliente_counter] = cliente
        self.carritos[self.id_cliente_counter] = CarritoDeCompras(self.id_cliente_counter)
        self.id_cliente_counter += 1
        return cliente
    
    def agregar_producto_tienda(self, nombre: str, precio: float, descripcion: str, stock: int) -> ProductoTienda:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del producto debe ser una cadena no vacía.")
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser un número positivo.")
        if not isinstance(descripcion, str):
            raise ValueError("La descripción debe ser una cadena.")
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("El stock debe ser un entero no negativo.")
        
        producto_info = ProductoInfo(self.id_producto_counter, nombre, precio, descripcion)
        producto_tienda = ProductoTienda(producto_info, stock)
        self.productos[self.id_producto_counter] = producto_tienda
        self.id_producto_counter += 1
        return producto_tienda
    
    def editar_producto_tienda(self, id_producto: int, nombre: str = None, precio: float = None, descripcion: str = None, stock: int = None):
        if id_producto not in self.productos:
            raise ValueError("El producto con el ID proporcionado no existe.")
        
        producto_tienda = self.productos[id_producto]
        
        if nombre is not None:
            if not isinstance(nombre, str) or not nombre.strip():
                raise ValueError("El nombre del producto debe ser una cadena no vacía.")
            producto_tienda.producto.nombre = nombre
        
        if precio is not None:
            if not isinstance(precio, (int, float)) or precio <= 0:
                raise ValueError("El precio debe ser un número positivo.")
            producto_tienda.producto.precio = precio
        
        if descripcion is not None:
            if not isinstance(descripcion, str):
                raise ValueError("La descripción debe ser una cadena.")
            producto_tienda.producto.descripcion = descripcion
        
        if stock is not None:
            if not isinstance(stock, int) or stock < 0:
                raise ValueError("El stock debe ser un entero no negativo.")
            producto_tienda.stock = stock

    def eliminar_producto_tienda(self, id_producto: int):
        if id_producto not in self.productos:
            raise ValueError("El producto con el ID proporcionado no existe.")
        self.productos.pop(id_producto)

        # Eliminar el producto de todos los carritos
        for carrito in self.carritos.values():
            producto_en_carrito = next((p for p in carrito.productos if p.id == id_producto), None)
            if producto_en_carrito:
                carrito.eliminar_producto(producto_en_carrito)

    def consultar_productos(self):
        return list(self.productos.values())
    
    def agregar_producto_al_carrito(self, id_cliente: int, id_producto: int, cantidad: int):
        if id_cliente not in self.clientes:
            raise ValueError("El cliente con el ID proporcionado no existe.")
        if id_producto not in self.productos:
            raise ValueError("El producto con el ID proporcionado no existe.")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo.")
        
        producto_tienda = self.productos[id_producto]
        if producto_tienda.stock < cantidad:
            raise ValueError("No hay suficiente stock disponible para el producto solicitado.")
        
        carrito = self.carritos[id_cliente]
        carrito.agregar_producto(producto_tienda.producto, cantidad)

    def obtener_productos_del_carrito(self, id_cliente: int):
        if id_cliente not in self.clientes:
            raise ValueError("El cliente con el ID proporcionado no existe.")
        carrito = self.carritos[id_cliente]
        return carrito.obtener_productos()
    
    def calcular_total_del_carrito(self, id_cliente: int):
        if id_cliente not in self.clientes:
            raise ValueError("El cliente con el ID proporcionado no existe.")
        carrito = self.carritos[id_cliente]
        return carrito.calcular_total()
    
    def vaciar_carrito(self, id_cliente: int):
        if id_cliente not in self.clientes:
            raise ValueError("El cliente con el ID proporcionado no existe.")
        carrito = self.carritos[id_cliente]
        
        carrito.vaciar_carrito()

    def eliminar_producto_del_carrito(self, id_cliente: int, id_producto: int):
        if id_cliente not in self.clientes:
            raise ValueError("El cliente con el ID proporcionado no existe.")
        if id_producto not in self.productos:
            raise ValueError("El producto con el ID proporcionado no existe.")
        
        carrito = self.carritos[id_cliente]
        producto_tienda = self.productos[id_producto]

        try:
            carrito.eliminar_producto(producto_tienda.producto)
        except ValueError as e:
            raise ValueError("El producto no está en el carrito.") from e


    

