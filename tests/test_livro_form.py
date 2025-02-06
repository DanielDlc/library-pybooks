"""Testes para o formulário de adição de livros (livro_form.py)"""

from unittest.mock import MagicMock

import pytest

from src.gui.livro_form import LivroForm


@pytest.fixture
def mock_livro_manager():
    """Mock do gerenciador de livros."""
    return MagicMock()


@pytest.fixture
def mock_livro_list():
    """Mock da lista de livros."""
    return MagicMock()


@pytest.fixture
def livro_form(mock_livro_manager, mock_livro_list):
    """Cria uma instância do LivroForm com mocks."""
    return LivroForm(MagicMock(), mock_livro_manager, mock_livro_list)


def test_adicionar_livro_fisico(livro_form, mock_livro_manager):
    """Testa se um livro físico é adicionado corretamente."""
    livro_form.titulo_entry.insert(0, "Python Fluente")
    livro_form.autor_entry.insert(0, "Luciano Ramalho")
    livro_form.tipo_var.set("fisico")
    livro_form.localizacao_entry.insert(0, "Estante A")

    livro_form.adicionar_livro()

    mock_livro_manager.adicionar_livro.assert_called_once_with(
        titulo="Python Fluente",
        autor="Luciano Ramalho",
        tipo="fisico",
        localizacao="Estante A",
        link="#",
    )


def test_adicionar_livro_digital(livro_form, mock_livro_manager):
    """Testa se um livro digital é adicionado corretamente."""
    livro_form.titulo_entry.insert(0, "Automate the Boring Stuff")
    livro_form.autor_entry.insert(0, "Al Sweigart")
    livro_form.tipo_var.set("digital")
    livro_form.link_entry.insert(0, "https://automatetheboringstuff.com/")

    livro_form.adicionar_livro()

    mock_livro_manager.adicionar_livro.assert_called_once_with(
        titulo="Automate the Boring Stuff",
        autor="Al Sweigart",
        tipo="digital",
        localizacao="",
        link="https://automatetheboringstuff.com/",
    )


def test_nao_adicionar_livro_vazio(livro_form, mock_livro_manager):
    """Testa se um livro não é adicionado quando os campos estão vazios."""
    livro_form.adicionar_livro()

    mock_livro_manager.adicionar_livro.assert_not_called()


def test_limpar_campos_apos_adicionar(livro_form, mock_livro_manager):
    """Testa se os campos do formulário são limpos após adicionar um livro."""
    livro_form.titulo_entry.insert(0, "Python Fluente")
    livro_form.autor_entry.insert(0, "Luciano Ramalho")
    livro_form.localizacao_entry.insert(0, "Estante A")
    livro_form.link_entry.insert(0, "https://example.com")
    livro_form.tipo_var.set("digital")

    livro_form.adicionar_livro()

    assert not livro_form.titulo_entry.get()
    assert not livro_form.autor_entry.get()
    assert not livro_form.localizacao_entry.get()
    assert not livro_form.link_entry.get()
    assert livro_form.tipo_var.get() == "fisico"  # O valor padrão "fisico"
