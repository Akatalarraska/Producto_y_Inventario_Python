# Implementar una clase Producto con los siguientes atributos:
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre # nombre: El nombre del producto.
        self.categoria = categoria # categoria: La categoría a la que pertenece el producto.
        self.precio = precio # precio: El precio del producto (debe ser mayor que 0).
        self.cantidad = cantidad # cantidad: La cantidad en stock (debe ser mayor o igual que 0).
    
    @property
    def precio(self):
        return self._precio
    # Precio debe ser mayor a 0
    @precio.setter
    def precio(self, euros):
        if euros >= 0:
            self._precio  = euros
        else:
            raise ValueError(f'El precio del producto {self.nombre} debe ser mayor o igual que 0.')
    
    @property
    def cantidad(self):
                return self._cantidad
       
    # CantidadPrecio debe ser mayor a 0 
    @cantidad.setter
    def cantidad(self, unidades):
        if unidades >= 0:
            self._cantidad  = unidades
        else:
            raise ValueError(f'La cantidad del producto {self.nombre} debe ser mayor o igual que 0.')

    def __str__(self):
        return f"Producto: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}€, Cantidad: {self.cantidad}u"



# Implementar una clase Inventario que maneje una lista de productos y permita las siguientes operaciones:
class Inventario:
    def __init__(self):
        self._productos = []  #Se crea una lisa vacia para manejar los productos.

    # 1.Agregar un producto: 
    def añadir_producto(self, producto):
        # Verificar que el producto no exista previamente en el inventario.
        for x in self._productos:
            if x.nombre == producto.nombre:
                print('Error: Este ya producto ya se encuentra actualmente en el inventario.')
                return
            self._productos.append(producto)
            print(f"El producto: '{producto.nombre}' se ha añadido al inventario.")

    # 2.Actualizar un producto: Modificar el precio o la cantidad en stock de un producto ya existente.
    def actualizar_producto(self, nombre, precio=None, cantidad=None):
        for x in self._productos:
            if x.nombre == nombre:
                if precio is not None:
                    x.precio = precio
                if x.cantidad is not None:
                    x.cantidad = cantidad
                print(f"El producto '{nombre}' se ha actualizado.")
                return
        print(f'Error, no se ha encontrado este producto: "{nombre}" en el inventario')

    # 3.Eliminar un producto: Quitar un producto del inventario. 
    def borrar_producto(self, nombre):
        for x in self._productos:
            if x.nombre == nombre:
                self._productos.remove(x)
                print(f"El producto: '{nombre}' se ha eliminado del inventario.")
                return
        print(f"El producto: '{nombre}' no se encuentra en el inventario.")


# 4.Mostrar inventario: Listar todos los productos disponibles.
    def mostrar_inventario(self):
        if not self._productos:
            print('La lista de prodcutos del inventario está vacia.')
        else:
            print('Productos en el inventario:')
            for x in self._productos:
                print(x)

# 5.Buscar un producto: Permitir buscar un producto por nombre.
    def buscar_producto(self, nombre):
        for x in self._productos:
            if x.nombre == nombre:
                print('Producto:', x)
                return
        print('Error, no se ha encontrado el producto en el inventario.')
            
        

p1 = Producto("madalenas", "bolleria", 2, 10)
p2 = Producto("Patatas", "Verdura", 2.30, 2 )
p3 = Producto('Bicicleta', 'Deporte', 900, 7)
print(p1)
print(p2)
print(p3)