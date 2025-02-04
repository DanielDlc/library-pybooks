import json
from src.livro_fisico import LivroFisico
from src.livro_digital import LivroDigital

class Livraria:
    def __init__(self):
        self.livros = []

    def carregar_dados(self, arquivo="livraria.json"):
        """Carrega os dados do JSON e adiciona os livros na livraria."""
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)

            for item in dados:
                try:
                    if "formato" in item and "tamanho" in item:
                        # Livro Digital precisa de formato e tamanho
                        livro = LivroDigital(
                            titulo=item.get("titulo", "Título Desconhecido"),
                            autor=item.get("autor", "Autor Desconhecido"),
                            formato=item.get("formato", "PDF"),
                            tamanho=item.get("tamanho", 0),
                            imagem=item.get("imagem", "img/digitais/default.jpg"),
                            link=item.get("link", "#")
                        )
                    else:
                        # Livro Físico precisa de localização e imagem
                        livro = LivroFisico(
                            titulo=item.get("titulo", "Título Desconhecido"),
                            autor=item.get("autor", "Autor Desconhecido"),
                            localizacao=item.get("localizacao", "Desconhecido"),
                            diretorio_imagem=item.get("imagem", "img/fisicos/default.jpg")
                        )
                    
                    self.livros.append(livro)

                except TypeError as e:
                    print(f"Erro ao processar um livro: {e}")

        except FileNotFoundError:
            print(f"Arquivo {arquivo} não encontrado. Criando nova livraria.")
            self.livros = []
        except json.JSONDecodeError:
            print(f"Erro: O arquivo {arquivo} está corrompido ou mal formatado.")

    def adicionar_livro(self, livro):
        """Adiciona um livro à livraria e salva no JSON."""
        if not isinstance(livro, (LivroFisico, LivroDigital)):
            return "Erro: O objeto adicionado não é um livro válido."

        self.livros.append(livro)
        self.salvar_dados()
        return f'Livro "{livro.titulo}" adicionado com sucesso!'

    def salvar_dados(self, arquivo="livraria.json"):
        """Salva os livros no JSON."""
        try:
            with open(arquivo, "w", encoding="utf-8") as f:
                json.dump([livro.__dict__ for livro in self.livros], f, indent=4, ensure_ascii=False)
            print(f"Dados salvos com sucesso em {arquivo}.")
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")