# Ejemplos de constructores y destructores
# tienda don Juan

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        print(f'Se ha registrado el producto {self.nombre} con precio ${self.precio:.2f}')

    def __del__(self):
        print(f'Se ha agotado el producto {self.nombre}. Gracias por su compra.')

# Ejemplo de uso
def ejemplo_tienda_abastos():
    producto1 = Producto('Manzanas', 2.50)
    producto2 = Producto('Leche', 1.80)