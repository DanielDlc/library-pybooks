from livro import Livro


class LivroDigital(Livro):
    def __init__(self, titulo, autor, **kwargs):
        super() .__init__(titulo, autor)
        self.genero = kwargs.get("genero")
        self.ano = kwargs.get("ano")
        self.formato = kwargs.get("formato", "PDF")
        self.tamanho = kwargs.get("tamanho", 0)

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        detalhes += f'\nFormato: {self.formato}'
        detalhes += f'\nTamanho: {self.tamanho} MB'
        return detalhes
