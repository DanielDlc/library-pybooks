"""Módulo que define a classe base Livro e a classe LivroComImagem."""

import os

class Livro:
    """Classe base para representar um livro."""

    def __init__(
        self,
        titulo: str,
        autor: str,
        genero: str = None,
        ano: int = None,
        imagem: str = None,
        link: str = None
    ) -> None:
        """
        Inicializa um livro.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param genero: O gênero literário do livro (opcional).
        :param ano: O ano de publicação (opcional).
        :param imagem: Caminho da imagem do livro (opcional).
        :param link: URL para compra ou mais informações (opcional).
        """
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano
        self.imagem = imagem  # Caminho da imagem do livro
        self.link = link  # URL para compra ou mais informações

    def exibir_detalhes(self) -> str:
        """Retorna uma string formatada com os detalhes do livro."""
        detalhes = f"Título: {self.titulo}\nAutor: {self.autor}"
        if self.genero:
            detalhes += f"\nGênero: {self.genero}"
        if self.ano:
            detalhes += f"\nAno: {self.ano}"
        if self.imagem:
            detalhes += f"\n🖼 Imagem: {self.imagem}"
        if self.link:
            detalhes += f"\n🔗 Link: {self.link}"
        return detalhes


class LivroComImagem(Livro):
    """Representa um livro com uma imagem associada."""

    def __init__(self, titulo: str, autor: str, diretorio_imagem: str, **kwargs) -> None:
        """
        Inicializa um livro com imagem.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param diretorio_imagem: Diretório onde a imagem está armazenada.
        :param kwargs: Argumentos adicionais que podem ser passados.
        """
        super().__init__(titulo, autor, **kwargs)
        self.imagem = self._obter_caminho_imagem(diretorio_imagem, kwargs.get("imagem"))

    def _obter_caminho_imagem(self, diretorio: str, imagem_nome: str) -> str:
        """
        Verifica se a imagem existe e retorna o caminho correto.

        :param diretorio: Diretório onde a imagem deve estar.
        :param imagem_nome: Nome do arquivo da imagem.
        :return: Caminho correto da imagem, ou uma imagem padrão se não encontrada.
        """
        imagem_padrao = os.path.join("img", "default.jpg")

        if not imagem_nome:
            return imagem_padrao  # Se não houver imagem definida, usa uma padrão

        # Se o caminho já for absoluto, verifica a existência
        if os.path.isabs(imagem_nome):
            return imagem_nome if os.path.exists(imagem_nome) else imagem_padrao

        # Constrói o caminho baseado no diretório fornecido
        caminho_imagem = os.path.join(diretorio, imagem_nome)

        return caminho_imagem if os.path.exists(caminho_imagem) else imagem_padrao