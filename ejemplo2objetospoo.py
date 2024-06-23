class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def agregar_al_carrito(self, cantidad):
        if self.cantidad_disponible >= cantidad:
            self.cantidad_disponible -= cantidad
            print(f"Se han agregado {cantidad} {self.nombre}(s) al carrito.")
        else:
            print(f"No hay suficientes {self.nombre}(s) disponibles.")

    def calcular_total(self, cantidad):
        total = self.precio * cantidad
        return total

    def mostrar_resumen_compra(self, cantidad, total):
        print(f"Resumen de la compra:")
        print(f"Producto: {self.nombre}")
        print(f"Cantidad: {cantidad}")
        print(f"Total: {total}")


# Ejemplo de uso
producto1 = Producto("Camisa", 20, 50)
producto1.agregar_al_carrito(3)  # Se han agregado 3 Camisa(s) al carrito.

cantidad_comprada = 5
total_compra = producto1.calcular_total(cantidad_comprada)
producto1.mostrar_resumen_compra(cantidad_comprada, total_compra)
