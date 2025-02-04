from livro import Livro


class LivroFisico(Livro):
    def __init__(self, titulo, autor, **kwargs):
        super().__init__(titulo, autor)
        self.genero = kwargs.get("genero")
        self.ano = kwargs.get("ano")
        self.localizacao = kwargs.get("localizacao")
        self.condicao = kwargs.get("condicao", "novo")

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        detalhes += f'\nLocalização: {self.localizacao or "Desconhecida"}'
        detalhes += f'\nCondição: {self.condicao}'
        return detalhes
