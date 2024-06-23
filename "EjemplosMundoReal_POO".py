# Oclass Hotel:
    def __init__(self, nombre, ubicacion, habitaciones_disponibles):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.habitaciones_disponibles = habitaciones_disponibles

    def reservar_habitacion(self, cantidad):
        if self.habitaciones_disponibles >= cantidad:
            self.habitaciones_disponibles -= cantidad
            print(f"Se han reservado {cantidad} habitaciones en {self.nombre}.")
        else:
            print("No hay suficientes habitaciones disponibles.")

    def cancelar_reserva(self, cantidad):
        self.habitaciones_disponibles += cantidad
        print(f"Se han cancelado {cantidad} habitaciones en {self.nombre}.")

    def mostrar_disponibilidad(self):
        print(f"Habitaciones disponibles en {self.nombre}: {self.habitaciones_disponibles}")


# Ejemplo de uso
hotel1 = Hotel("Hotel ABC", "Ciudad XYZ", 50)
hotel1.mostrar_disponibilidad()  # Habitaciones disponibles en Hotel ABC: 50

hotel1.reservar_habitacion(10)  # Se han reservado 10 habitaciones en Hotel ABC.
hotel1.mostrar_disponibilidad()  # Habitaciones disponibles en Hotel ABC: 40

hotel1.cancelar_reserva(5)  # Se han cancelado 5 habitaciones en Hotel ABC.
hotel1.mostrar_disponibilidad()  # Habitaciones disponibles en Hotel ABC: 45nline Python - IDE, Editor, Compiler, Interpreter

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
