"""Módulo que define o formulário para adicionar/editar livros."""

import tkinter as tk
from tkinter import filedialog, messagebox
from src.managers.livro_manager import LivroManager

class LivroForm:
    """Formulário para adicionar ou editar livros."""

    def __init__(self, master, livro_manager):
        """Cria o formulário na interface.

        :param master: O widget pai.
        :param livro_manager: O gerenciador de livros.
        """
        self.livro_manager = livro_manager

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
        self.tipo_var = tk.StringVar(value="Físico")
        tk.Radiobutton(self.frame, text='Físico', variable=self.tipo_var, value='Físico', command=self.alterar_campos).grid(row=2, column=1)
        tk.Radiobutton(self.frame, text='Digital', variable=self.tipo_var, value='Digital', command=self.alterar_campos).grid(row=2, column=2)

        # Campo de imagem
        tk.Label(self.frame, text='Imagem:').grid(row=3, column=0, padx=5, pady=5)
        self.entry_imagem = tk.Entry(self.frame, width=50)
        self.entry_imagem.grid(row=3, column=1)
        self.botao_selecionar_imagem = tk.Button(self.frame, text="Selecionar", command=self.selecionar_imagem)
        self.botao_selecionar_imagem.grid(row=3, column=2)

        # Campos dinâmicos (Localização ou Tamanho)
        self.label_extra = tk.Label(self.frame, text="Localização:")
        self.label_extra.grid(row=4, column=0, padx=5, pady=5)
        self.entry_extra = tk.Entry(self.frame, width=30)
        self.entry_extra.grid(row=4, column=1)

        # Campo de link (aparece apenas para livros digitais)
        self.label_link = tk.Label(self.frame, text="Link:")
        self.entry_link = tk.Entry(self.frame, width=50)

        # Botão de adicionar livro
        self.botao_adicionar = tk.Button(self.frame, text="Adicionar Livro", command=self.adicionar_livro)
        self.botao_adicionar.grid(row=6, column=0, columnspan=3, pady=10)

        # Atualiza os campos iniciais
        self.alterar_campos()

    def selecionar_imagem(self):
        """Abre um seletor de arquivos para selecionar uma imagem."""
        caminho_imagem = filedialog.askopenfilename(filetypes=[("Imagens PNG", "*.png"), ("Imagens JPG", "*.jpg"), ("Imagens JPEG", "*.jpeg")])
        if caminho_imagem:
            self.entry_imagem.delete(0, tk.END)
            self.entry_imagem.insert(0, caminho_imagem)

    def alterar_campos(self):
        """Altera os campos de entrada conforme o tipo de livro."""
        tipo = self.tipo_var.get()
        if tipo == "Físico":
            self.label_extra.config(text="Localização:")
            self.label_extra.grid(row=4, column=0)
            self.entry_extra.grid(row=4, column=1)

            self.label_link.grid_forget()
            self.entry_link.grid_forget()
        else:
            self.label_extra.config(text="Tamanho (MB):")
            self.label_extra.grid(row=4, column=0)
            self.entry_extra.grid(row=4, column=1)

            self.label_link.grid(row=5, column=0, padx=5, pady=5)
            self.entry_link.grid(row=5, column=1, columnspan=2, pady=5)

    def adicionar_livro(self):
        """Adiciona um novo livro à livraria."""
        titulo = self.entry_titulo.get().strip()
        autor = self.entry_autor.get().strip()
        tipo = self.tipo_var.get()
        extra = self.entry_extra.get().strip()
        imagem = self.entry_imagem.get().strip()
        link = self.entry_link.get().strip()

        if not titulo or not autor:
            messagebox.showerror("Erro", "Preencha os campos Título e Autor!")
            return

        if tipo == "Físico":
            livro = self.livro_manager.adicionar_livro(tipo="fisico", titulo=titulo, autor=autor, localizacao=extra, imagem=imagem)
        else:
            try:
                tamanho = float(extra) if extra else 0.0
            except ValueError:
                messagebox.showerror("Erro", "O tamanho do livro digital deve ser um número válido!")
                return

            livro = self.livro_manager.adicionar_livro(tipo="digital", titulo=titulo, autor=autor, formato="PDF", tamanho=tamanho, imagem=imagem, link=link)

        if livro:
            messagebox.showinfo("Sucesso", f'Livro "{titulo}" adicionado com sucesso!')
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Não foi possível adicionar o livro.")

    def limpar_campos(self):
        """Limpa os campos após adicionar um livro."""
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_extra.delete(0, tk.END)
        self.entry_imagem.delete(0, tk.END)
        self.entry_link.delete(0, tk.END)