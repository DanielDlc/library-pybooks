"""Módulo que define a classe base LivroComImagem."""

import os
from typing import Optional
from src.models.livro import Livro

class LivroComImagem(Livro):
    """Classe base para livros que possuem imagens associadas."""

    def __init__(self, titulo: str, autor: str, diretorio_imagem: str, imagem: Optional[str] = None, **kwargs) -> None:
        """
        Inicializa um livro com imagem.

        :param titulo: O título do livro.
        :param autor: O autor do livro.
        :param diretorio_imagem: Diretório onde a imagem está armazenada.
        :param imagem: Nome ou caminho da imagem (opcional).
        :param kwargs: Argumentos adicionais.
        """
        super().__init__(titulo, autor, **kwargs)
        self.imagem = self._obter_caminho_imagem(diretorio_imagem, imagem)

    def _obter_caminho_imagem(self, diretorio: str, imagem_nome: Optional[str]) -> Optional[str]:
        """
        Verifica se a imagem existe e retorna o caminho correto.

        :param diretorio: Diretório onde a imagem deve estar.
        :param imagem_nome: Nome do arquivo da imagem.
        :return: Caminho correto da imagem, ou None se não for encontrada.
        """
        imagem_padrao = os.path.join(diretorio, "default.jpg")

        if not imagem_nome:
            return imagem_padrao  # Se nenhuma imagem for fornecida, usa uma padrão

        # Se o caminho já for absoluto, verifica se o arquivo existe
        if os.path.isabs(imagem_nome):
            return imagem_nome if os.path.exists(imagem_nome) else imagem_padrao

        # Constrói o caminho baseado no diretório fornecido
        caminho_imagem = os.path.join(diretorio, imagem_nome)

        return caminho_imagem if os.path.exists(caminho_imagem) else imagem_padrao