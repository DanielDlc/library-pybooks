"""Testes para a lista de livros (livro_list.py)"""

import tkinter as tk
from unittest.mock import MagicMock

import pytest

from src.gui.livro_list import LivroList
from src.models.livro_digital import LivroDigital
from src.models.livro_fisico import LivroFisico


@pytest.fixture
def mock_livro_manager():
    """Mock do gerenciador de livros."""
    mock = MagicMock()
    mock.listar_livros.return_value = []
    return mock


@pytest.fixture
def livro_list(mock_livro_manager):
    """Cria uma instância da lista de livros com um mock do livro_manager."""
    root = tk.Tk()
    livro_list = LivroList(root, mock_livro_manager)
    return livro_list


def test_lista_inicial_vazia(livro_list):
    """Verifica se a lista de livros inicia vazia."""
    assert livro_list.lista_livros.size() == 0


def test_adicionar_livro_fisico(livro_list, mock_livro_manager):
    """Testa se um livro físico aparece na interface após ser adicionado."""

    livro = LivroFisico(
        "Python Fluente",
        "Luciano Ramalho",
        localizacao="Estante A",
    )

    # Simula o retorno do gerenciador de livros
    mock_livro_manager.listar_livros.return_value = [livro]

    # Chama a atualização da lista
    livro_list.atualizar_lista()

    # Verifica se o livro foi adicionado à interface
    assert livro_list.lista_livros.size() == 1
    assert (
        livro_list.lista_livros.get(0)
        == "Python Fluente - Luciano Ramalho (📖 Físico)"
    )


def test_adicionar_livro_digital(livro_list, mock_livro_manager):
    """Testa se um livro digital aparece na interface após ser adicionado."""

    livro = LivroDigital(
        "Automate the Boring Stuff",
        "Al Sweigart",
        formato="PDF",
        tamanho=10.0,
    )

    mock_livro_manager.listar_livros.return_value = [livro]
    livro_list.atualizar_lista()

    assert livro_list.lista_livros.size() == 1
    assert (
        livro_list.lista_livros.get(0)
        == "Automate the Boring Stuff - Al Sweigart (💻 Digital)"
    )


def test_atualizar_lista_multiplos_livros(livro_list, mock_livro_manager):
    """Testa se múltiplos livros aparecem corretamente na lista."""

    livros = [
        LivroFisico(
            "Python Fluente",
            "Luciano Ramalho",
            localizacao="Estante A",
        ),
        LivroDigital(
            "Automate the Boring Stuff",
            "Al Sweigart",
            formato="PDF",
            tamanho=10.0,
        ),
    ]

    mock_livro_manager.listar_livros.return_value = livros
    livro_list.atualizar_lista()

    TOTAL_LIVROS = len(livros)  # Remove valor mágico
    assert livro_list.lista_livros.size() == TOTAL_LIVROS

    assert (
        livro_list.lista_livros.get(0)
        == "Python Fluente - Luciano Ramalho (📖 Físico)"
    )
    assert (
        livro_list.lista_livros.get(1)
        == "Automate the Boring Stuff - Al Sweigart (💻 Digital)"
    )
