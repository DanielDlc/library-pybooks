from src.livro import Livro
from src.livro_digital import LivroDigital

def test_comparar_livros():
    livro1 = Livro("Python Fluente", "Luciano Ramalho")
    livro2 = Livro("Python Fluente", "Luciano Ramalho")
    livro3 = Livro("Clean Code", "Robert C. Martin")

    assert livro1 == livro2  # São iguais
    assert livro1 != livro3  # São diferentes

def test_somar_livros_digitais():
    livro1 = LivroDigital("Automate the Boring Stuff", "Al Sweigart", tamanho=5.5)
    livro2 = LivroDigital("Python Crash Course", "Eric Matthes", tamanho=3.2)

    resultado = livro1 + livro2

    assert resultado.titulo == "Automate the Boring Stuff + Python Crash Course"
    assert resultado.autor == "Múltiplos Autores"
    assert resultado.tamanho == 8.7  # Soma dos tamanhos dos arquivos