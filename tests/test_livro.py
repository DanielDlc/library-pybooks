"""Testes para a lista de livros na interface (livro_list.py)"""

import tkinter as tk
from unittest.mock import MagicMock

import pytest

from src.gui.livro_list import LivroList
from src.models.livro_digital import LivroDigital
from src.models.livro_fisico import LivroFisico


@pytest.fixture
def mock_livro_manager():
    """Mock do gerenciador de livros."""
    return MagicMock()


@pytest.fixture
def livro_list(mock_livro_manager):
    """Cria uma instância do LivroList com mock sem destruir root prematuramente."""
    root = tk.Tk()
    lista = LivroList(root, mock_livro_manager)
    yield lista  # Usa yield para manter a instância viva durante o teste
    root.destroy()  # Destrói após o teste


def test_adicionar_livro_fisico(livro_list, mock_livro_manager):
    """Testa se um livro físico aparece na interface após ser adicionado."""
    livro = LivroFisico(
        "Python Fluente",
        "Luciano Ramalho",
        localizacao="Estante A"
    )
    mock_livro_manager.listar_livros.return_value = [livro]

    livro_list.atualizar_lista()

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
        tamanho=10.0
    )
    mock_livro_manager.listar_livros.return_value = [livro]

    livro_list.atualizar_lista()

    assert livro_list.lista_livros.size() == 1
    assert (
        livro_list.lista_livros.get(0)
        == "Automate the Boring Stuff - Al Sweigart (💻 Digital)"
    )


def test_atualizar_lista(livro_list, mock_livro_manager):
    """Testa a atualização da lista de livros na interface."""
    livros = [
        LivroFisico(
            "Python Fluente",
            "Luciano Ramalho",
            localizacao="Estante A"
        ),
        LivroDigital(
            "Automate the Boring Stuff",
            "Al Sweigart",
            formato="PDF",
            tamanho=10.0
        ),
    ]
    mock_livro_manager.listar_livros.return_value = livros

    livro_list.atualizar_lista()

    TOTAL_LIVROS = len(livros)  # Substitui valor mágico
    assert livro_list.lista_livros.size() == TOTAL_LIVROS
    assert (
        livro_list.lista_livros.get(0)
        == "Python Fluente - Luciano Ramalho (📖 Físico)"
    )
    assert (
        livro_list.lista_livros.get(1)
        == "Automate the Boring Stuff - Al Sweigart (💻 Digital)"
    )
