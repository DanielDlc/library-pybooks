class Livro:
    def __init__(self, titulo, autor, genero=None, ano=None):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano

    def exibir_detalhes(self):
        detalhes = f'Título: {self.titulo}\nAutor: {self.autor}'
        if self.genero:
            detalhes += f'\nGênero: {self.genero}'
        if self.ano:
            detalhes += f'\nAno: {self.ano}'
        return detalhes
