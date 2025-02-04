from src.livro import Livro


def test_criar_livro():
    """Testa a criação de um livro com dados reais."""

    TITULO = "Clean Code"
    AUTOR = "Robert C. Martin"
    GENERO = "Programação"
    ANO_ESPERADO = 2008

    livro = Livro(TITULO, AUTOR, GENERO, ANO_ESPERADO)

    assert livro.titulo == TITULO
    assert livro.autor == AUTOR
    assert livro.genero == GENERO
    assert livro.ano == ANO_ESPERADO
