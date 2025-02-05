"""Módulo que define o formulário para adicionar livros."""

import tkinter as tk
from tkinter import messagebox, simpledialog
from src.managers.livro_manager import LivroManager

class LivroForm:
    """Formulário para adicionar livros."""

    def __init__(self, master, livro_manager, livro_list):
        """Cria o formulário na interface.

        :param master: O widget pai.
        :param livro_manager: O gerenciador de livros.
        :param livro_list: O widget da lista de livros.
        """
        self.livro_manager = livro_manager
        self.livro_list = livro_list

        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        # Campos de entrada
        tk.Label(self.frame, text='Título:').grid(row=0, column=0, padx=5, pady=5)
        self.entry_titulo = tk.Entry(self.frame, width=50)
        self.entry_titulo.grid(row=0, column=1)

        tk.Label(self.frame, text='Autor:').grid(row=1, column=0, padx=5, pady=5)
        self.entry_autor = tk.Entry(self.frame, width=50)
        self.entry_autor.grid(row=1, column=1)

        tk.Label(self.frame, text='Tipo:').grid(row=2, column=0, padx=5, pady=5)
        self.tipo_var = tk.StringVar(value="fisico")
        tk.Radiobutton(self.frame, text='📖 Físico', variable=self.tipo_var, value='fisico', command=self.alterar_campos).grid(row=2, column=1)
        tk.Radiobutton(self.frame, text='💻 Digital', variable=self.tipo_var, value='digital', command=self.alterar_campos).grid(row=2, column=2)

        # Campo de localização/tamanho
        self.label_extra = tk.Label(self.frame, text="Localização:")
        self.label_extra.grid(row=3, column=0, padx=5, pady=5)
        self.entry_extra = tk.Entry(self.frame, width=50)
        self.entry_extra.grid(row=3, column=1)

        # Campo de link
        tk.Label(self.frame, text='🔗 Link:').grid(row=4, column=0, padx=5, pady=5)
        self.entry_link = tk.Entry(self.frame, width=50)
        self.entry_link.grid(row=4, column=1)

        # Botão de adicionar livro
        self.botao_adicionar = tk.Button(self.frame, text="Adicionar Livro", command=self.adicionar_livro)
        self.botao_adicionar.grid(row=5, column=0, columnspan=2, pady=10)

        self.alterar_campos()

    def alterar_campos(self):
        """Altera os campos de entrada conforme o tipo de livro."""
        tipo = self.tipo_var.get()
        if tipo == "fisico":
            self.label_extra.config(text="Localização:")
        else:
            self.label_extra.config(text="Tamanho (MB):")

    def adicionar_livro(self):
        """Adiciona um novo livro à livraria."""
        titulo = self.entry_titulo.get().strip()
        autor = self.entry_autor.get().strip()
        tipo = self.tipo_var.get()
        extra = self.entry_extra.get().strip()
        link = self.entry_link.get().strip()

        if not titulo or not autor:
            messagebox.showerror("Erro", "Preencha os campos Título e Autor!")
            return

        if tipo == "fisico":
            livro = self.livro_manager.adicionar_livro(
                tipo="fisico",
                titulo=titulo,
                autor=autor,
                localizacao=extra if extra else "Desconhecido",
                link=link if link else "#"
            )
        else:
            try:
                tamanho = float(extra) if extra else 0.0
            except ValueError:
                messagebox.showerror("Erro", "O tamanho do livro digital deve ser um número válido!")
                return

            livro = self.livro_manager.adicionar_livro(
                tipo="digital",
                titulo=titulo,
                autor=autor,
                formato="PDF",
                tamanho=tamanho,
                link=link if link else "#"
            )

        if livro:
            messagebox.showinfo("Sucesso", f'Livro "{titulo}" adicionado com sucesso!')
            self.livro_list.atualizar_lista()  # Atualiza a lista após adicionar
        else:
            messagebox.showerror("Erro", "Não foi possível adicionar o livro.")