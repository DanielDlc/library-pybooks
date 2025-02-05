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
            return (
                self.titulo.lower() == other.titulo.lower()
                and self.autor.lower() == other.autor.lower()
            )
        return False

    def __hash__(self):
        """
        Define um hash para permitir que objetos ItemBiblioteca sejam usados
        em conjuntos (set) e como chaves em dicionários.

        :return: O hash baseado no título e autor do livro.
        """
        return hash((self.titulo.lower(), self.autor.lower()))

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
        return (
            f"ItemBiblioteca(titulo='{self.titulo}', "
            f"autor='{self.autor}', link='{self.link}')"
        )

    def __add__(self, other):
        """
        Combina dois livros em um único.

        :param other: Outro livro da biblioteca.
        :return: Um novo ItemBiblioteca com título e autor combinados.
        """
        if isinstance(other, ItemBiblioteca):
            novo_titulo = f"{self.titulo} & {other.titulo}"
            novo_autor = f"{self.autor} e {other.autor}"
            return ItemBiblioteca(novo_titulo, novo_autor)
        raise TypeError(
            "Só é possível somar objetos do tipo ItemBiblioteca."
        )

    def __lt__(self, other):
        """
        Define a comparação de livros com base no título.

        :param other: Outro livro da biblioteca.
        :return: True se o título do livro atual for menor (alfabeticamente).
        """
        if isinstance(other, ItemBiblioteca):
            return self.titulo.lower() < other.titulo.lower()
        raise TypeError(
            "A comparação só pode ser feita entre objetos do tipo "
            "ItemBiblioteca."
        )

    def __len__(self):
        """
        Retorna o tamanho do título do livro.

        :return: Número de caracteres no título do livro.
        """
        return len(self.titulo)
