import os
from src.livro import Livro

class LivroComImagem(Livro):
    def __init__(self, titulo, autor, diretorio_imagem, **kwargs):
        super().__init__(titulo, autor)
        self.imagem = self._obter_caminho_imagem(diretorio_imagem, kwargs.get("imagem"))

    def _obter_caminho_imagem(self, diretorio, imagem_nome):
        """Verifica se a imagem existe e retorna o caminho correto."""
        if not imagem_nome:
            return None
        caminho_imagem = os.path.join(diretorio, imagem_nome)
        return caminho_imagem if os.path.exists(caminho_imagem) else None