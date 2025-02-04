import json

from livro_digital import LivroDigital
from livro_fisico import LivroFisico


class Livraria:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        for livro_existente in self.livros:
            if (
                livro_existente.titulo == livro.titulo
                and livro_existente.autor == livro.autor
                ):
                return 'Livro já cadastrado.'
        self.livros.append(livro)
        return 'Livro adicionado com sucesso.'

    def listar_livros(self):
        if not self.livros:
            return 'Nenhum livro cadastrado.'
        return '\n\n'.join([livro.exibir_detalhes() for livro in self.livros])

    def listar_livros_fisicos(self):
        livros_fisicos = [
            livro for livro in self.livros if isinstance(livro, LivroFisico)
        ]
        if not livros_fisicos:
            return 'Nenhum livro físico cadastrado.'
        return '\n\n'.join([
            livro.exibir_detalhes() for livro in livros_fisicos
        ])

    def listar_livros_digitais(self):
        livros_digitais = [
            livro for livro in self.livros if isinstance(livro, LivroDigital)
        ]
        if not livros_digitais:
            return 'Nenhum livro digital cadastrado.'
        return '\n\n'.join([
            livro.exibir_detalhes() for livro in livros_digitais
        ])

    def salvar_dados(self, arquivo='livraria.json'):
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(
                [livro.__dict__ for livro in self.livros],
                f,
                ensure_ascii=False,
                indent=4,
            )

    def carregar_dados(self, arquivo='livraria.json'):
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            for item in dados:
                if 'localizacao' in item:
                    self.adicionar_livro(LivroFisico(**item))
                elif 'formato' in item:
                    self.adicionar_livro(LivroDigital(**item))
        except FileNotFoundError:
            print(
                'Arquivo de dados não encontrado. '
                'Iniciando com uma livraria vazia.'
            )
