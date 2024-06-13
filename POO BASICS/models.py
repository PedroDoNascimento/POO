import random

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_info(self):
        print(f'nome: {self.nome}, idade: {self.idade}')

idade = random.randint(10, 50)

pessoa1 = Pessoa('joséfe', idade)
pessoa1.mostrar_info()

pessoa2 = Pessoa('gabriel', idade)
pessoa2.mostrar_info()

pessoa3 = Pessoa('andré', idade)
pessoa3.mostrar_info()