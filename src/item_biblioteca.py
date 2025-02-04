from .item_biblioteca import ItemBiblioteca  # Importação correta


class ItemBiblioteca:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class LivroFisico(ItemBiblioteca):
    def __init__(self, titulo, autor, localizacao, condicao):
        super().__init__(titulo, autor)
        self.localizacao = localizacao
        self.condicao = condicao

class LivroDigital(ItemBiblioteca):
    def __init__(self, titulo, autor, formato, tamanho):
        super().__init__(titulo, autor)
        self.formato = formato
        self.tamanho = tamanho