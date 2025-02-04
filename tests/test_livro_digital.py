from src.livro_digital import LivroDigital


def test_criar_livro_digital():
    """Utilizo para testar condição de livros digitais."""

    TITULO = "Data Structures & Algorithms in Python"
    AUTOR = "Michael T. Goodrich"
    FORMATO_ESPERADO = "PDF"
    TAMANHO_ESPERADO = 12.5

    livro = LivroDigital(TITULO,
                         AUTOR,
                         formato=FORMATO_ESPERADO,
                         tamanho=TAMANHO_ESPERADO
                         )

    assert livro.titulo == TITULO
    assert livro.autor == AUTOR
    assert livro.formato == FORMATO_ESPERADO
    assert livro.tamanho == TAMANHO_ESPERADO
