"""Interface principal da aplicação."""

import tkinter as tk
from src.gui.livro_form import LivroForm
from src.gui.livro_list import LivroList
from src.managers.livro_manager import LivroManager

class Interface:
    """Janela principal do sistema de gerenciamento de livros."""

    def __init__(self):
        """Inicializa a interface principal."""
        self.janela = tk.Tk()
        self.janela.title('Sistema de Gerenciamento de Livraria')

        # Criar o gerenciador de livros (Singleton)
        self.livro_manager = LivroManager()

        # Frame principal para a organização dos elementos
        self.container = tk.Frame(self.janela)
        self.container.pack(padx=20, pady=20)

        # Criar a lista de livros
        self.livro_list = LivroList(self.container, self.livro_manager)

        # Criar o formulário de cadastro de livros (agora passando `livro_list`)
        self.livro_form = LivroForm(self.container, self.livro_manager, self.livro_list)

        # Atualizar a lista de livros no início
        self.livro_list.atualizar_lista()

        self.janela.mainloop()