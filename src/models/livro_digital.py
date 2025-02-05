"""Módulo que define a classe LivroDigital."""

from src.models.item_biblioteca import ItemBiblioteca

class LivroDigital(ItemBiblioteca):
    """Representa um livro digital na biblioteca."""

    def __init__(self, titulo: str, autor: str, formato: str, tamanho: float, link: str = "Sem link") -> None:
        """
        Inicializa um livro digital.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param formato: O formato do livro digital (PDF, EPUB, etc.).
        :param tamanho: O tamanho do arquivo em MB.
        :param link: Link de compra ou referência do livro.
        """
        super().__init__(titulo, autor, link)
        self.formato = formato
        self.tamanho = tamanho
        self.tipo = "Digital"

    def __str__(self) -> str:
        return f"{self.titulo} - {self.autor} (💻 {self.tipo})"