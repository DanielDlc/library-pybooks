"""Módulo que define a classe LivroDigital."""

import os
from src.models.livro import LivroComImagem

# Caminho correto para armazenar imagens de livros digitais
IMG_DIR = os.path.abspath(os.path.join("img", "digitais"))

class LivroDigital(LivroComImagem):
    """Representa um livro digital na biblioteca."""

    def __init__(
        self, titulo: str, autor: str, formato: str,
        tamanho: float, imagem: str = None, link: str = "#", **kwargs
    ) -> None:
        """
        Inicializa um livro digital.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param formato: O formato do livro digital (PDF, EPUB, etc.).
        :param tamanho: O tamanho do arquivo em MB.
        :param imagem: Caminho da imagem da capa do livro (opcional).
        :param link: Link para acessar o livro digital (padrão: "#").
        """
        # Define o caminho padrão para a imagem se não for fornecido
        diretorio_imagem = imagem or os.path.join(IMG_DIR, "default.jpg")

        # Chama o construtor da superclasse
        super().__init__(titulo, autor, diretorio_imagem, **kwargs)

        # Atributos específicos do livro digital
        self.formato = formato
        self.tamanho = tamanho
        self.link = link

    def __str__(self) -> str:
        """Retorna uma string formatada com os detalhes do livro digital."""
        return f"{self.titulo} - {self.autor} ({self.formato}, {self.tamanho}MB)"