from src.livraria import Livraria
from src.livro_digital import LivroDigital
from src.livro_fisico import LivroFisico


def test_adicionar_livro():
    """Testa a adição de um livro físico na livraria."""
    livraria = Livraria()
    livro = LivroFisico("Python Fluente",
                        "Luciano Ramalho",
                        localizacao="Estante A"
                        )

    resultado = livraria.adicionar_livro(livro)
    assert resultado == "Livro adicionado com sucesso."
    assert len(livraria.livros) == 1


def test_nao_adicionar_livro_duplicado():
    """Testa a tentativa de adicionar um livro duplicado na livraria."""
    livraria = Livraria()
    livro = LivroFisico("Python Fluente",
                        "Luciano Ramalho",
                        localizacao="Estante A"
                        )

    livraria.adicionar_livro(livro)
    resultado = livraria.adicionar_livro(livro)  # adicionando o mesmo livro

    assert resultado == "Livro já cadastrado."
    assert len(livraria.livros) == 1  # deve ter apenas 1 livro na coleção


def test_listar_livros():
    """Testa a listagem de livros na livraria."""
    livraria = Livraria()

    assert livraria.listar_livros() == "Nenhum livro cadastrado."

    livro = LivroDigital("Automate the Boring Stuff with Python",
                         "Al Sweigart",
                         formato="PDF",
                         tamanho=8.5
                         )
    livraria.adicionar_livro(livro)

    assert "Automate the Boring Stuff with Python" in livraria.listar_livros()


def test_salvar_e_carregar_livros():
    """Testa a persistência de livros no JSON."""
    livraria = Livraria()
    livro = LivroFisico("Effective Python",
                        "Brett Slatkin",
                        localizacao="Escritório"
                        )

    livraria.adicionar_livro(livro)
    livraria.salvar_dados("test_livraria.json")

    nova_livraria = Livraria()
    nova_livraria.carregar_dados("test_livraria.json")

    assert len(nova_livraria.livros) == 1
    assert nova_livraria.livros[0].titulo == "Effective Python"


