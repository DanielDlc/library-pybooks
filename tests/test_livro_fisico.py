from src.models.livro_fisico import LivroFisico


def test_criar_livro_fisico():
    """ Estou testando livro físico com dados reais"""
    livro = LivroFisico(
        "Python Fluente",
        "Luciano Ramalho",
        localizacao="Estande B",
        condicao="Novo"
        )

    assert livro.titulo == "Python Fluente"
    assert livro.autor == "Luciano Ramalho"
    assert livro.localizacao == "Estande B"
    assert livro.condicao == "Novo"
