"""Módulo que define a classe base ItemBiblioteca e suas subclasses."""

class ItemBiblioteca:
    """Classe base para representar um item da biblioteca."""

    def __init__(self, titulo: str, autor: str) -> None:
        """
        Inicializa um item da biblioteca.

        :param titulo: O título do item.
        :param autor: O autor do item.
        """
        self.titulo = titulo
        self.autor = autor


class LivroFisico(ItemBiblioteca):
    """Representa um livro físico na biblioteca."""

    def __init__(self, titulo: str, autor: str, localizacao: str, condicao: str) -> None:
        """
        Inicializa um livro físico.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param localizacao: Localização onde o livro está armazenado.
        :param condicao: Condição física do livro (novo, usado, etc.).
        """
        super().__init__(titulo, autor)
        self.localizacao = localizacao
        self.condicao = condicao


class LivroDigital(ItemBiblioteca):
    """Representa um livro digital na biblioteca."""

    def __init__(self, titulo: str, autor: str, formato: str, tamanho: float) -> None:
        """
        Inicializa um livro digital.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param formato: O formato do livro digital (PDF, EPUB, etc.).
        :param tamanho: O tamanho do arquivo em MB.
        """
        super().__init__(titulo, autor)
        self.formato = formato
        self.tamanho = tamanho