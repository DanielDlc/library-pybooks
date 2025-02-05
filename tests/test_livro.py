from src.models.livro import Livro
from src.models.livro_digital import LivroDigital

# 🔹 Definir constantes para valores mágicos
TAMANHO_ESPERADO = 8.7


def test_comparar_livros():
    """Testa se dois livros com o mesmo título e autor
    são considerados iguais.
    """
    livro1 = Livro("Python Fluente", "Luciano Ramalho")
    livro2 = Livro("Python Fluente", "Luciano Ramalho")
    livro3 = Livro("Clean Code", "Robert C. Martin")

    # 🔹 Uso das variáveis nos asserts
    assert livro1 == livro2  # Livros iguais
    assert livro1 != livro3  # Livros diferentes


def test_somar_livros_digitais():
    """Testa a sobrecarga de operador para
    somar tamanhos de livros digitais.
    """
    livro1 = LivroDigital(
        "Automate the Boring Stuff",
        "Al Sweigart",
        tamanho=5.5
    )
    livro2 = LivroDigital(
        "Python Crash Course",
        "Eric Matthes",
        tamanho=3.2
    )

    # 🔹 Criando um novo livro com a soma dos tamanhos
    resultado = livro1 + livro2

    # 🔹 Quebrando linha longa para legibilidade
    assert resultado.titulo == (
        "Automate the Boring Stuff + Python Crash Course"
    )
    assert resultado.autor == "Múltiplos Autores"
    assert resultado.tamanho == TAMANHO_ESPERADO  # Usando constante
