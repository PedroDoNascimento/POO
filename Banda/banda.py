from musico import Musico

class Banda:
    def __init__(self, nome):
        self.nome = nome
        self.musicos = []
        self.albums = []
#  Adicionar/Remover Músicos
    def adicionar_musico(self, musico):
        self.musicos.append(musico)
    def remover_musico(self, musico):
        self.musicos.remove(musico)
#  Adicionar/Remover Albuns
    def adicionar_album(self, album):
        self.albums.append(album)
    def remover_album(self, album):
        self.albums.remove(album)
