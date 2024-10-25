class Producto:
    # Precio debe ser mayor a 0 // Cantidad >= 0
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad



class Inventario:
    def __init__(self, productos=[]):
        self.productos = productos
        pass

    # 3.Eliminar un producto: Quitar un producto del inventario. 
    def borrar_producto(self, dni=None):
        for i, prod in enumerate(self.productos):
            if prod.dni == dni:
                del(self.clientes[i])
                print(str(prod),"> BORRADO")
                return
        print("Cliente no encontrado")