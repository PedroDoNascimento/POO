from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

circulo = Circulo(5)
retangulo = Retangulo(4, 6)

print(circulo.calcular_area())  # Output: 78.5
print(retangulo.calcular_area())  # Output: 24