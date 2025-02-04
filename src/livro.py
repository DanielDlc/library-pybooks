import os

class Livro:
    def __init__(self, titulo, autor, genero=None, ano=None, imagem=None, link=None):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano
        self.imagem = imagem  # Caminho da imagem do livro
        self.link = link  # URL para compra ou mais informações

    def exibir_detalhes(self):
        detalhes = f'Título: {self.titulo}\nAutor: {self.autor}'
        if self.genero:
            detalhes += f'\nGênero: {self.genero}'
        if self.ano:
            detalhes += f'\nAno: {self.ano}'
        if self.imagem:
            detalhes += f'\n🖼 Imagem: {self.imagem}'
        if self.link:
            detalhes += f'\n🔗 Link: {self.link}'
        return detalhes


class LivroComImagem(Livro):
    def __init__(self, titulo, autor, diretorio_imagem, **kwargs):
        super().__init__(titulo, autor, **kwargs)
        self.imagem = self._obter_caminho_imagem(diretorio_imagem, kwargs.get("imagem"))

    def _obter_caminho_imagem(self, diretorio, imagem_nome):
        """Verifica se a imagem existe e retorna o caminho correto."""
        if not imagem_nome:
            return "img/default.jpg"  # Imagem padrão

        # Se o caminho já for absoluto, não modificar
        if os.path.isabs(imagem_nome):
            return imagem_nome if os.path.exists(imagem_nome) else "img/default.jpg"

        caminho_imagem = os.path.join(diretorio, imagem_nome)

        # Retorna o caminho correto se a imagem existir, caso contrário, retorna uma imagem padrão
        return caminho_imagem if os.path.exists(caminho_imagem) else "img/default.jpg"