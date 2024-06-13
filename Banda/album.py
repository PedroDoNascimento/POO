class Album:
    def __init__(self, titulo, ano_lancamento):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento

    def mostrar_info(self):
        print(f'Álbum: {self.titulo}, Ano: {self.ano_lancamento}')
        
