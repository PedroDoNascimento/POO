class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor

    def mostrar_info(self):
        print(f'Marca: {self.marca}, Potência do Motor: {self.motor.potencia}HP')

motor = Motor(150)
carro = Carro('Toyota', motor)
carro.mostrar_info() 