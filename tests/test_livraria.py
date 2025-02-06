"""Módulo que gerencia a coleção de livros na livraria."""

import json

from src.models.livro_digital import LivroDigital
from src.models.livro_fisico import LivroFisico


class Livraria:
    """Gerencia os livros da biblioteca (com persistência)."""

    def __init__(self) -> None:
        """Inicializa a livraria como uma coleção vazia."""
        self.livros: list[LivroFisico | LivroDigital] = []

    def adicionar_livro(self, livro) -> str:
        """Adiciona um livro à coleção."""
        if not isinstance(livro, (LivroFisico, LivroDigital)):
            return "Erro: O objeto adicionado não é um livro válido."

        for livro_existente in self.livros:
            if (
                livro_existente.titulo == livro.titulo
                and livro_existente.autor == livro.autor
                and isinstance(livro_existente, livro.__class__)
            ):
                return f'Livro "{livro.titulo}" já cadastrado!'

        self.livros.append(livro)
        return f'Livro "{livro.titulo}" adicionado com sucesso!'

    def listar_livros(self) -> str:
        """Retorna a lista de livros ou informa não ter livros cadastrados."""
        if not self.livros:
            return "Nenhum livro cadastrado."

        return "\n".join(
            f"{livro.titulo} - {livro.autor}"
            for livro in self.livros
        )

    def salvar_dados(self, arquivo: str = "livraria.json") -> None:
        """Salva os livros no formato JSON."""
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump([livro.__dict__ for livro in self.livros], f, indent=4)

    def carregar_dados(self, arquivo: str = "livraria.json") -> None:
        """Carrega os livros a partir de um arquivo JSON."""
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                livros = json.load(f)

            self.livros = [
                LivroFisico(**livro)
                if "localizacao" in livro
                else LivroDigital(**livro)
                for livro in livros
            ]
        except FileNotFoundError:
            self.livros = []
