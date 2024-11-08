
# Implementar una clase Producto con los siguientes atributos:

class Producto:
    # Precio debe ser mayor a 0 // Cantidad >= 0
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre # nombre: El nombre del producto.
        self.categoria = categoria # categoria: La categoría a la que pertenece el producto.
        self.precio = precio # precio: El precio del producto (debe ser mayor que 0).
        self.cantidad = cantidad # cantidad: La cantidad en stock (debe ser mayor o igual que 0).


# Implementar una clase Inventario que maneje una lista de productos y permita las siguientes operaciones:

# 1.Agregar un producto: Verificar que el producto no exista previamente en el inventario.



# 4.Mostrar inventario: Listar todos los productos disponibles.
# 5.Buscar un producto: Permitir buscar un producto por nombre.

class Inventario:
    def __init__(self, productos=[]):
        self.productos = productos
        pass

    # 2.Actualizar un producto: Modificar el precio o la cantidad en stock de un producto ya existente.
    def modificar_Precio(self):
        nuevoPrecio = int(input('Introduce el nuevo precio para el producto:'))
        self.precio = nuevoPrecio
   
    def modificar_Cantidad(self):
        nuevaCantidad = int(input('Introduce las unidades actuales del producto:'))
        self.cantidad = nuevaCantidad

    # 3.Eliminar un producto: Quitar un producto del inventario. 
    def borrar_producto(self, dni=None):
        for i, prod in enumerate(self.productos):
            if prod.dni == dni:
                del(self.clientes[i])
                print(str(prod),"> BORRADO")
                return
        print("Cliente no encontrado")


"""
Ejercicio Final - Enunciado
Descripción: Crea una aplicación en Python para la gestión de un inventario de productos, usando programación orientada a objetos (POO). El sistema debe permitir agregar, actualizar, eliminar y mostrar productos en un inventario, cada uno de los cuales es representado como un objeto de la clase Producto.

1.Clases y Objetos:




1.Agregar un producto: Verificar que el producto no exista previamente en el inventario.

2.Actualizar un producto: Modificar el precio o la cantidad en stock de un producto ya existente.
3.Eliminar un producto: Quitar un producto del inventario.
4.Mostrar inventario: Listar todos los productos disponibles.
5.Buscar un producto: Permitir buscar un producto por nombre.

2.Validaciones:
El precio debe ser siempre mayor que 0.
La cantidad debe ser mayor o igual que 0.
Manejar correctamente las excepciones y validar entradas (evitar que el usuario ingrese datos no válidos).

3.Funciones y Métodos:
Todos los atributos deben ser privados, utilizando getters y setters para acceder y modificar los valores.
Deben implementarse métodos para cada una de las funcionalidades mencionadas (agregar, actualizar, eliminar, etc.).

4.Organización del Código:
El código debe estar estructurado de manera que sea legible y modular.
Cada funcionalidad debe estar en un método de la clase correspondiente.
No se deben utilizar variables globales fuera de las clases.

Requisitos de Entrega (POR FAVOR, CUMPLE ESTOS REQUISITOS, EL EJERCICIO FINAL NO SERÁ VALORADO)
1.El archivo debe ser un script en Python con las clases Producto e Inventario correctamente implementadas.
2.Las clases deben estar organizadas siguiendo los principios de POO (atributos privados, getters, setters, encapsulamiento).
3.El código debe estar bien estructurado y comentado.
"""