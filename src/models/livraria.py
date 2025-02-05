"""Módulo que gerencia a coleção de livros na livraria."""

from src.models.livro_digital import LivroDigital
from src.models.livro_fisico import LivroFisico


class Livraria:
    """Gerencia os livros da biblioteca (sem persistência)."""

    def __init__(self) -> None:
        """Inicializa a livraria como uma coleção vazia."""
        self.livros = []

    def adicionar_livro(self, livro) -> str:
        """Adiciona um livro à coleção.

        :param livro: Objeto do tipo LivroFisico ou LivroDigital.
        :return: Mensagem de sucesso ou erro.
        """
        if not isinstance(livro, (LivroFisico, LivroDigital)):
            return "Erro: O objeto adicionado não é um livro válido."

        self.livros.append(livro)
        return f'Livro "{livro.titulo}" adicionado com sucesso!'

    def listar_livros(self):
        """Retorna a lista de livros."""
        return self.livros
