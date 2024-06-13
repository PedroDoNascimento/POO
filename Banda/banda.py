from musico import Musico

class Banda:
    def __init__(self, nome):
        self.nome = nome
        self.musicos = []

    def adicionar_musico(self, musico):
        self.musicos.append(musico)

    def mostrar_musicos(self):
        print(f'Banda: {self.nome}')
        for musico in self.musicos:
            musico.mostrar_info()
