class Animal:
    def __init__(self, nome):
        self.nome = nome 

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print('Au Au!')

class Gato(Animal):
    def fazer_som(self):
         print('Miau!')

cachorro = Cachorro('thor')
gato = Gato('Din')

cachorro.fazer_som()
gato.fazer_som()  