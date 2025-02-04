"""Módulo que gerencia a persistência de livros no JSON."""

import json
import os
from src.models.livro_fisico import LivroFisico
from src.models.livro_digital import LivroDigital
from src.models.livraria import Livraria

# Caminho do banco de dados JSON
LIVRARIA_JSON = os.path.abspath(os.path.join("src", "database", "livraria.json"))

class LivroManager:
    """Gerencia a persistência de livros no arquivo JSON."""

    def __init__(self):
        """Inicializa a gerência de livros carregando do JSON."""
        self.livraria = Livraria()
        self.carregar_dados()

    def carregar_dados(self) -> None:
        """Carrega os dados do JSON e adiciona os livros na livraria."""
        if not os.path.exists(LIVRARIA_JSON):
            print(f"Arquivo {LIVRARIA_JSON} não encontrado. Criando novo arquivo.")
            self.salvar_dados()
            return

        try:
            with open(LIVRARIA_JSON, "r", encoding="utf-8") as f:
                dados = json.load(f)

            for item in dados:
                try:
                    if "formato" in item and "tamanho" in item:
                        livro = LivroDigital(
                            titulo=item.get("titulo", "Título Desconhecido"),
                            autor=item.get("autor", "Autor Desconhecido"),
                            formato=item.get("formato", "PDF"),
                            tamanho=item.get("tamanho", 0.0),
                            imagem=item.get("imagem", "img/digitais/default.jpg"),
                            link=item.get("link", "#")
                        )
                    else:
                        livro = LivroFisico(
                            titulo=item.get("titulo", "Título Desconhecido"),
                            autor=item.get("autor", "Autor Desconhecido"),
                            localizacao=item.get("localizacao", "Desconhecido"),
                            diretorio_imagem=item.get("imagem", "img/fisicos/default.jpg")
                        )
                    
                    self.livraria.adicionar_livro(livro)

                except TypeError as e:
                    print(f"Erro ao processar um livro: {e}")

        except json.JSONDecodeError:
            print(f"Erro: O arquivo {LIVRARIA_JSON} está corrompido ou mal formatado.")

    def salvar_dados(self) -> None:
        """Salva os livros no arquivo JSON."""
        try:
            with open(LIVRARIA_JSON, "w", encoding="utf-8") as f:
                json.dump([livro.__dict__ for livro in self.livraria.livros], f, indent=4, ensure_ascii=False)
            print(f"Dados salvos com sucesso em {LIVRARIA_JSON}.")
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")

    def adicionar_livro(self, **kwargs):
        """Adiciona um novo livro e salva no JSON."""
        tipo = kwargs.get("tipo", "fisico").lower()

        if tipo == "fisico":
            livro = LivroFisico(
                titulo=kwargs.get("titulo", "Título Desconhecido"),
                autor=kwargs.get("autor", "Autor Desconhecido"),
                localizacao=kwargs.get("localizacao", "Desconhecido"),
                diretorio_imagem=kwargs.get("imagem", "img/fisicos/default.jpg")
            )
        elif tipo == "digital":
            livro = LivroDigital(
                titulo=kwargs.get("titulo", "Título Desconhecido"),
                autor=kwargs.get("autor", "Autor Desconhecido"),
                formato=kwargs.get("formato", "PDF"),
                tamanho=kwargs.get("tamanho", 0.0),
                imagem=kwargs.get("imagem", "img/digitais/default.jpg"),
                link=kwargs.get("link", "#")
            )
        else:
            return None

        self.livraria.adicionar_livro(livro)
        self.salvar_dados()
        return livro

    def listar_livros(self):
        """Retorna a lista de livros."""
        return self.livraria.listar_livros()