"""Módulo que define a classe LivroFisico."""

import os
from src.models.livro import LivroComImagem

# Caminho correto para armazenar imagens de livros físicos
IMG_DIR = os.path.abspath(os.path.join("img", "fisicos"))

class LivroFisico(LivroComImagem):
    """Representa um livro físico na biblioteca."""

    def __init__(
        self, titulo: str, autor: str, localizacao: str = None,
        condicao: str = "Novo", diretorio_imagem: str = None, **kwargs
    ) -> None:
        """
        Inicializa um livro físico.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param localizacao: Localização onde o livro está armazenado.
        :param condicao: Condição física do livro (novo, usado, etc.).
        :param diretorio_imagem: Caminho da imagem da capa do livro.
        :param kwargs: Argumentos adicionais.
        """
        # Define o caminho padrão para a imagem se não for fornecido
        diretorio_imagem = diretorio_imagem or os.path.join(IMG_DIR, "default.jpg")

        # Define os atributos específicos do LivroFisico
        self.localizacao = localizacao or "Desconhecida"
        self.condicao = condicao

        # Chama o construtor da superclasse
        super().__init__(titulo, autor, diretorio_imagem, **kwargs)

    def exibir_detalhes(self) -> str:
        """Retorna uma string formatada com os detalhes do livro físico."""
        detalhes = super().exibir_detalhes()
        detalhes += f'\n📍 Localização: {self.localizacao}'
        detalhes += f'\n📌 Condição: {self.condicao}'
        return detalhes