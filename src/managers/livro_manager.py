"""Módulo que gerencia a persistência de livros no JSON."""

import json
import os

from src.models.livraria import Livraria
from src.models.livro_digital import LivroDigital
from src.models.livro_fisico import LivroFisico

# Caminho do banco de dados JSON
LIVRARIA_JSON = os.path.join("src", "database", "livraria.json")


class LivroManager:
    """Gerencia a persistência de livros no arquivo JSON."""

    def __init__(self):
        """Inicializa a gerência de livros carregando do JSON."""
        self.livraria = Livraria()
        self.carregar_dados()

    def carregar_dados(self) -> None:
        """Carrega os dados do JSON e adiciona os livros na livraria."""
        if not os.path.exists(LIVRARIA_JSON):
            print(f"⚠ Arquivo {LIVRARIA_JSON} não encontrado. Criando novo...")
            self.salvar_dados()
            return

        try:
            with open(LIVRARIA_JSON, "r", encoding="utf-8") as f:
                dados = json.load(f)

            for item in dados:
                livro = self._criar_livro(item)
                if livro:
                    self.livraria.adicionar_livro(livro)

        except json.JSONDecodeError:
            print(f"❌ Erro: O arquivo {LIVRARIA_JSON} está corrompido.")

    def salvar_dados(self) -> None:
        """Salva os livros no arquivo JSON."""
        try:
            with open(LIVRARIA_JSON, "w", encoding="utf-8") as f:
                json.dump(
                    [livro.__dict__ for livro in self.livraria.livros],
                    f,
                    indent=4,
                    ensure_ascii=False,
                )
            print(f"✅ Dados salvos em {LIVRARIA_JSON}.")
        except Exception as e:
            print(f"❌ Erro ao salvar os dados: {e}")

    def adicionar_livro(self, **kwargs):
        """Adiciona um novo livro e salva no JSON."""
        livro = self._criar_livro(kwargs)

        if livro:
            self.livraria.adicionar_livro(livro)
            self.salvar_dados()
            return livro
        return None

    def listar_livros(self):
        """Retorna a lista de livros."""
        return self.livraria.listar_livros()

    # Ignorar o aviso PLR6301 do Ruff para este método
    def _criar_livro(self, dados: dict):  # noqa: PLR6301
        """Cria um livro físico ou digital baseado nos dados recebidos."""
        tipo = dados.get("tipo", "fisico").lower()

        if tipo == "digital" or ("formato" in dados and "tamanho" in dados):
            return LivroDigital(
                titulo=dados.get("titulo", "Título Desconhecido"),
                autor=dados.get("autor", "Autor Desconhecido"),
                formato=dados.get("formato", "PDF"),
                tamanho=dados.get("tamanho", 0.0),
                link=dados.get("link", "#"),
            )

        return LivroFisico(
            titulo=dados.get("titulo", "Título Desconhecido"),
            autor=dados.get("autor", "Autor Desconhecido"),
            localizacao=dados.get("localizacao", "Desconhecido"),
            condicao=dados.get("condicao", "Novo"),
            link=dados.get("link", "#"),
        )
