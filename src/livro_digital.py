class LivroDigital:
    def __init__(self, titulo, autor, formato, tamanho, imagem=None, link=None, **kwargs):
        self.titulo = titulo
        self.autor = autor
        self.formato = formato
        self.tamanho = tamanho
        self.imagem = imagem if imagem else "img/digitais/default.jpg"  # Imagem padrão
        self.link = link if link else "#"  # Link padrão

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.formato}, {self.tamanho}MB)"