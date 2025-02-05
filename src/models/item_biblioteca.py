"""Módulo que define a classe base ItemBiblioteca e suas subclasses."""

class ItemBiblioteca:
    """Classe base para representar um item da biblioteca."""

    def __init__(self, titulo: str, autor: str, link: str = "#") -> None:
        """
        Inicializa um item da biblioteca.

        :param titulo: O título do item.
        :param autor: O autor do item.
        :param link: Link opcional para informações sobre o livro.
        """
        self.titulo = titulo
        self.autor = autor
        self.link = link  # Adicionado para corrigir o erro


class LivroFisico(ItemBiblioteca):
    """Representa um livro físico na biblioteca."""

    def __init__(self, titulo: str, autor: str, localizacao: str, condicao: str, link: str = "#") -> None:
        """
        Inicializa um livro físico.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param localizacao: Localização onde o livro está armazenado.
        :param condicao: Condição física do livro (novo, usado, etc.).
        :param link: Link opcional para informações sobre o livro.
        """
        super().__init__(titulo, autor, link)  # Agora aceita link corretamente
        self.localizacao = localizacao
        self.condicao = condicao


class LivroDigital(ItemBiblioteca):
    """Representa um livro digital na biblioteca."""

    def __init__(self, titulo: str, autor: str, formato: str, tamanho: float, link: str = "#") -> None:
        """
        Inicializa um livro digital.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param formato: O formato do livro digital (PDF, EPUB, etc.).
        :param tamanho: O tamanho do arquivo em MB.
        :param link: Link para acesso ao livro digital.
        """
        super().__init__(titulo, autor, link)  # Agora aceita link corretamente
        self.formato = formato
        self.tamanho = tamanho