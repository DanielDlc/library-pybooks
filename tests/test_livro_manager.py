"""Testes para o gerenciador de livros (livro_manager.py)"""

import json
from unittest.mock import mock_open, patch

import pytest

from src.managers.livro_manager import LivroManager
from src.models.livro_digital import LivroDigital
from src.models.livro_fisico import LivroFisico


@pytest.fixture
def livro_manager():
    """Cria uma instância do LivroManager para testes."""
    return LivroManager()


@patch("builtins.open", new_callable=mock_open, read_data="[]")
@patch("os.path.exists", return_value=True)
def test_carregar_dados(mock_exists, mock_file, livro_manager):
    """Testa se a carga inicial do JSON funciona corretamente."""
    livro_manager.carregar_dados()
    assert livro_manager.listar_livros() == []  # Deve iniciar vazio


@patch("builtins.open", new_callable=mock_open)
def test_salvar_dados(mock_file, livro_manager):
    """Testa se os dados são salvos corretamente no JSON."""
    livro = LivroFisico(
        "Python Fluente",
        "Luciano Ramalho",
        localizacao="Estante A",
    )

    livro_manager.adicionar_livro(
        titulo=livro.titulo,
        autor=livro.autor,
        localizacao=livro.localizacao,
        tipo="fisico",
    )

    livro_manager.salvar_dados()

    # Verifica se o arquivo foi aberto para escrita
    mock_file.assert_called_once_with(
        livro_manager.LIVRARIA_JSON, "w", encoding="utf-8"
    )


def test_adicionar_livro_fisico(livro_manager):
    """Testa se um livro físico é adicionado corretamente."""
    livro = LivroFisico(
        "Clean Code",
        "Robert C. Martin",
        localizacao="Prateleira B",
    )

    livro_adicionado = livro_manager.adicionar_livro(
        titulo=livro.titulo,
        autor=livro.autor,
        localizacao=livro.localizacao,
        tipo="fisico",
    )

    assert livro_adicionado is not None
    assert livro_adicionado.titulo == "Clean Code"
    assert livro_adicionado.autor == "Robert C. Martin"
    assert len(livro_manager.listar_livros()) == 1


def test_adicionar_livro_digital(livro_manager):
    """Testa se um livro digital é adicionado corretamente."""
    livro = LivroDigital(
        "Automate the Boring Stuff",
        "Al Sweigart",
        formato="PDF",
        tamanho=10.0,
    )

    livro_adicionado = livro_manager.adicionar_livro(
        titulo=livro.titulo,
        autor=livro.autor,
        formato="PDF",
        tamanho=10.0,
        tipo="digital",
    )

    assert livro_adicionado is not None
    assert livro_adicionado.titulo == "Automate the Boring Stuff"
    assert livro_adicionado.autor == "Al Sweigart"
    assert len(livro_manager.listar_livros()) == 1


def test_nao_adicionar_livro_duplicado(livro_manager):
    """Testa se um livro duplicado não é adicionado."""
    livro_manager.adicionar_livro(
        titulo="Python Fluente",
        autor="Luciano Ramalho",
        localizacao="Estante A",
        tipo="fisico",
    )

    resultado = livro_manager.adicionar_livro(
        titulo="Python Fluente",
        autor="Luciano Ramalho",
        localizacao="Estante A",
        tipo="fisico",
    )

    assert resultado is None  # O segundo livro não deve ser adicionado
    assert len(livro_manager.listar_livros()) == 1


@patch("builtins.open", new_callable=mock_open)
@patch("os.path.exists", return_value=True)
def test_carregar_livros_do_json(mock_exists, mock_file, livro_manager):
    """Testa se o LivroManager carrega corretamente os livros do JSON."""
    dados_falsos = json.dumps([
        {
            "titulo": "Effective Python",
            "autor": "Brett Slatkin",
            "localizacao": "Escritório",
            "tipo": "fisico",
        },
        {
            "titulo": "Python Tricks",
            "autor": "Dan Bader",
            "formato": "EPUB",
            "tamanho": 5.0,
            "tipo": "digital",
        },
    ])

    mock_file.return_value.read.return_value = dados_falsos

    livro_manager.carregar_dados()
    livros = livro_manager.listar_livros()

    TOTAL_LIVROS = len(dados_falsos)  # Remove valor mágico
    assert len(livros) == TOTAL_LIVROS
    assert livros[0].titulo == "Effective Python"
    assert livros[1].titulo == "Python Tricks"
