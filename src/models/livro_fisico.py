"""Módulo que define a classe LivroFisico."""

from src.models.item_biblioteca import ItemBiblioteca


class LivroFisico(ItemBiblioteca):
    """Representa um livro físico na biblioteca."""

    def __init__(
            self,
            titulo: str,
            autor: str,
            localizacao: str,
            condicao: str = "Novo",
            link: str = "Sem link"
            ) -> None:
        """
        Inicializa um livro físico.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param localizacao: Localização onde o livro está armazenado.
        :param condicao: Condição física do livro (novo, usado, etc.).
        :param link: Link de compra ou referência do livro.
        """
        super().__init__(titulo, autor, link)
        self.localizacao = localizacao
        self.condicao = condicao
        self.tipo = "Físico"

    def __str__(self) -> str:
        return f"{self.titulo} - {self.autor} (📖 {self.tipo})"
