"""Testes para o módulo livro_actions.py"""

from tkinter import messagebox
from unittest.mock import MagicMock

import pytest

from src.gui.livro_actions import LivroActions


@pytest.fixture
def mock_livro_manager():
    """Mock do gerenciador de livros."""
    return MagicMock()


@pytest.fixture
def mock_lista_livros():
    """Mock da lista de livros."""
    lista_mock = MagicMock()
    lista_mock.curselection.return_value = [0]  # Simula um livro selecionado
    return lista_mock


@pytest.fixture
def livro_actions(mock_lista_livros, mock_livro_manager):
    """Cria uma instância do LivroActions com mocks."""
    return LivroActions(
        mock_lista_livros, mock_lista_livros, mock_livro_manager
        )


def mock_askstring(*args, **kwargs):
    """Mock para substituir tkinter.simpledialog.askstring."""
    return "Novo Título"


@pytest.mark.parametrize("novo_titulo", ["Novo Título"])
def test_editar_livro(
    monkeypatch, livro_actions, mock_livro_manager, novo_titulo
    ):
    """Testa a edição de um livro."""
    monkeypatch.setattr("tkinter.simpledialog.askstring", mock_askstring)

    livro_actions.lista_livros.curselection.return_value = [0]
    livro_actions.editar_livro()

    mock_livro_manager.salvar_dados.assert_called_once()


def test_excluir_livro(monkeypatch, livro_actions, mock_livro_manager):
    """Testa a exclusão de um livro."""
    monkeypatch.setattr(messagebox, "askyesno", lambda *args: True)

    livro_actions.lista_livros.curselection.return_value = [0]
    livro_actions.excluir_livro()

    mock_livro_manager.salvar_dados.assert_called_once()


def test_abrir_link(mock_webbrowser, livro_actions, mock_livro_manager):
    """Testa se o link do livro é aberto corretamente no navegador."""
    livro_actions.lista_livros.curselection.return_value = [1]
    livro_actions.abrir_link()

    mock_webbrowser.assert_called_once_with(
        "https://automatetheboringstuff.com/"
        )
