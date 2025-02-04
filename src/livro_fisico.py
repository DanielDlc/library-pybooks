from src.livro import LivroComImagem
import os

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "img", "fisicos")

class LivroFisico(LivroComImagem):
    def __init__(self, titulo, autor, localizacao=None, condicao="Novo", diretorio_imagem=None, **kwargs):
        # Define o caminho padrão para a imagem se não for fornecido
        if diretorio_imagem is None:
            diretorio_imagem = os.path.join(IMG_DIR, "default.jpg")

        # Armazena os atributos específicos do LivroFisico ANTES de chamar super()
        self.localizacao = localizacao if localizacao else "Desconhecida"
        self.condicao = condicao

        # Remove "localizacao" e "condicao" de kwargs para evitar que cheguem em LivroComImagem
        kwargs.pop("localizacao", None)
        kwargs.pop("condicao", None)

        # Chama o construtor da superclasse
        super().__init__(titulo, autor, diretorio_imagem, **kwargs)

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        detalhes += f'\n📍 Localização: {self.localizacao}'
        detalhes += f'\n📌 Condição: {self.condicao}'
        return detalhes