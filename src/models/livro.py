"""Módulo que define a classe base Livro."""


class Livro:
    """Classe base para representar um livro."""

    def __init__(
            self,
            titulo: str,
            autor: str,
            link: str = "#"
            ) -> None:
        """
        Inicializa um livro.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param link: URL para referência ou compra (opcional, padrão "#").
        """
        self.titulo = titulo
        self.autor = autor
        self.link = link  # URL para compra ou mais informações

    def exibir_detalhes(self) -> str:
        """Retorna uma string formatada com os detalhes do livro."""
        detalhes = f"Título: {self.titulo}\nAutor: {self.autor}"
        if self.link and self.link != "#":
            detalhes += f"\n🔗 Link: {self.link}"
        return detalhes


class LivroFisico(Livro):
    """Representa um livro físico com localização."""

    def __init__(
            self,
            titulo: str,
            autor: str,
            localizacao: str,
            link: str = "#"
            ) -> None:
        """
        Inicializa um livro físico.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param localizacao: Localização do livro na estante.
        :param link: URL para referência (opcional, padrão "#").
        """
        super().__init__(titulo, autor, link)
        self.localizacao = localizacao

    def exibir_detalhes(self) -> str:
        """Retorna uma string formatada com os detalhes do livro físico."""
        detalhes = super().exibir_detalhes()
        detalhes += f"\n📍 Localização: {self.localizacao}"
        return detalhes


class LivroDigital(Livro):
    """Representa um livro digital com um link de acesso."""

    def __init__(self, titulo: str, autor: str, link: str) -> None:
        """
        Inicializa um livro digital.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param link: URL para acessar ou baixar o livro.
        """
        super().__init__(titulo, autor, link)

    def exibir_detalhes(self) -> str:
        """Retorna uma string formatada com os detalhes do livro digital."""
        detalhes = super().exibir_detalhes()
        detalhes += "\n💻 Formato: Digital"
        return detalhes
