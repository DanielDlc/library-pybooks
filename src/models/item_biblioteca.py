class ItemBiblioteca:
    """
    Classe base para representar um item da biblioteca.
    """

    def __init__(self, titulo: str, autor: str, link: str = "#"):
        """
        Inicializa um item da biblioteca.

        :param titulo: O título do livro.
        :param autor: O nome do autor do livro.
        :param link: O link para acessar informações sobre o livro (opcional).
        """
        self.titulo = titulo
        self.autor = autor
        self.link = link

    def __eq__(self, other):
        """
        Compara dois livros para verificar se são iguais.

        Dois livros são considerados iguais se possuem o mesmo título e autor.

        :param other: Outro objeto a ser comparado.
        :return: True se forem iguais, False caso contrário.
        """
        if isinstance(other, ItemBiblioteca):
            return self.titulo.lower() == other.titulo.lower() and self.autor.lower() == other.autor.lower()
        return False

    def __str__(self):
        """
        Retorna uma representação em string do objeto.

        :return: Uma string representando o item da biblioteca.
        """
        return f"{self.titulo} - {self.autor} ({self.__class__.__name__})"

    def __repr__(self):
        """
        Retorna uma representação detalhada do objeto para depuração.

        :return: Uma string detalhada do item da biblioteca.
        """
        return f"ItemBiblioteca(titulo='{self.titulo}', autor='{self.autor}', link='{self.link}')"