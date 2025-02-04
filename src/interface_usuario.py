import tkinter as tk
from tkinter import messagebox, filedialog
import webbrowser
import os
import shutil
from PIL import Image, ImageTk  # Certifique-se de que a biblioteca Pillow está instalada
from src.livro_digital import LivroDigital
from src.livro_fisico import LivroFisico

# Diretórios padrão para imagens
IMG_DIR_FISICOS = os.path.join("img", "fisicos")
IMG_DIR_DIGITAIS = os.path.join("img", "digitais")

# Criar diretórios se não existirem
os.makedirs(IMG_DIR_FISICOS, exist_ok=True)
os.makedirs(IMG_DIR_DIGITAIS, exist_ok=True)

class Interface:
    def __init__(self, livraria):
        self.livraria = livraria
        self.janela = tk.Tk()
        self.janela.title('Sistema de Gerenciamento de Livraria')

        # Labels e campos de entrada
        tk.Label(self.janela, text='Título:').grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.entry_titulo = tk.Entry(self.janela, width=50)
        self.entry_titulo.grid(row=0, column=1, columnspan=2, pady=5)

        tk.Label(self.janela, text='Autor:').grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.entry_autor = tk.Entry(self.janela, width=50)
        self.entry_autor.grid(row=1, column=1, columnspan=2, pady=5)

        tk.Label(self.janela, text='Tipo:').grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.tipo_var = tk.StringVar(value='Físico')
        tk.Radiobutton(self.janela, text='Físico', variable=self.tipo_var, value='Físico', command=self.alterar_campos).grid(row=2, column=1)
        tk.Radiobutton(self.janela, text='Digital', variable=self.tipo_var, value='Digital', command=self.alterar_campos).grid(row=2, column=2)

        # Campos extras (Localização ou Tamanho)
        self.label_extra = tk.Label(self.janela, text='Localização:')
        self.label_extra.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.entry_extra = tk.Entry(self.janela, width=20)
        self.entry_extra.grid(row=3, column=1, pady=5, sticky='we')

        # Campo de imagem
        tk.Label(self.janela, text='Imagem:').grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.entry_imagem = tk.Entry(self.janela, width=50)
        self.entry_imagem.grid(row=4, column=1, columnspan=2, pady=5)
        self.botao_selecionar_imagem = tk.Button(self.janela, text="Selecionar Imagem", command=self.selecionar_imagem)
        self.botao_selecionar_imagem.grid(row=4, column=3, padx=5)

        # Campo de link (somente para livros digitais)
        self.label_link = tk.Label(self.janela, text="Link:")
        self.entry_link = tk.Entry(self.janela, width=50)

        # Botão para adicionar livro
        self.botao_adicionar = tk.Button(self.janela, text='Adicionar Livro', command=self.adicionar_livro)
        self.botao_adicionar.grid(row=6, column=0, columnspan=3, pady=10)

        # Lista de livros cadastrados
        tk.Label(self.janela, text='Livros cadastrados:').grid(row=7, column=0, padx=10, pady=5, sticky='w')
        self.lista_livros = tk.Listbox(self.janela, width=60, height=10)
        self.lista_livros.grid(row=8, column=0, columnspan=3, padx=10, pady=5)

        # Botões de Ações
        self.botao_editar = tk.Button(self.janela, text='Editar Livro', command=self.editar_livro)
        self.botao_editar.grid(row=9, column=0, pady=10)

        #self.botao_excluir = tk.Button(self.janela, text='Excluir Livro', command=self.excluir_livro)
        #self.botao_excluir.grid(row=9, column=1, pady=10)

        #self.botao_abrir = tk.Button(self.janela, text='Abrir', command=self.abrir_livro)
        #self.botao_abrir.grid(row=9, column=2, pady=10)

        self.alterar_campos()
        self.atualizar_lista_livros()

    def selecionar_imagem(self):
        caminho_imagem = filedialog.askopenfilename(filetypes=[("Imagens PNG", "*.png"), ("Imagens JPG", "*.jpg"), ("Imagens JPEG", "*.jpeg")])
        if caminho_imagem:
            self.entry_imagem.delete(0, tk.END)
            self.entry_imagem.insert(0, caminho_imagem)

    def alterar_campos(self):
        """Altera os campos extras de acordo com o tipo de livro escolhido."""
        tipo = self.tipo_var.get()
        if tipo == "Físico":
            self.label_extra.config(text="Localização:")
            self.label_link.grid_forget()
            self.entry_link.grid_forget()
        else:
            self.label_extra.config(text="Tamanho (MB):")
            self.label_link.grid(row=5, column=0, padx=10, pady=5)
            self.entry_link.grid(row=5, column=1, columnspan=2, pady=5)

    def adicionar_livro(self):
        """Adiciona um livro físico ou digital e move a imagem para a pasta correta."""
        titulo, autor, tipo = self.entry_titulo.get().strip(), self.entry_autor.get().strip(), self.tipo_var.get()
        extra, imagem, link = self.entry_extra.get().strip(), self.entry_imagem.get().strip(), self.entry_link.get().strip()

        if not titulo or not autor:
            messagebox.showerror('Erro', 'Preencha os campos Título e Autor!')
            return

        pasta_destino = IMG_DIR_FISICOS if tipo == 'Físico' else IMG_DIR_DIGITAIS
        caminho_destino = os.path.join(pasta_destino, os.path.basename(imagem)) if imagem else None

        if imagem:
            try:
                shutil.copy(imagem, caminho_destino)
                imagem = caminho_destino
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível salvar a imagem: {e}")
                return

        livro = LivroFisico(titulo, autor, localizacao=extra, diretorio_imagem=imagem) if tipo == "Físico" else LivroDigital(titulo, autor, formato="PDF", tamanho=float(extra) if extra else 0, imagem=imagem, link=link)

        self.livraria.adicionar_livro(livro)
        self.atualizar_lista_livros()

    def editar_livro(self):
        """Edita um livro selecionado na lista."""
        selecao = self.lista_livros.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um livro para editar!")
            return

        livro = self.livraria.livros[selecao[0]]

        # Preenche os campos para edição
        self.entry_titulo.delete(0, tk.END)
        self.entry_titulo.insert(0, livro.titulo)

        self.entry_autor.delete(0, tk.END)
        self.entry_autor.insert(0, livro.autor)

        if isinstance(livro, LivroFisico):
            self.tipo_var.set("Físico")
            self.entry_extra.delete(0, tk.END)
            self.entry_extra.insert(0, livro.localizacao)
        else:
            self.tipo_var.set("Digital")
            self.entry_extra.delete(0, tk.END)
            self.entry_extra.insert(0, str(livro.tamanho))
            self.entry_link.delete(0, tk.END)
            self.entry_link.insert(0, livro.link)

        self.entry_imagem.delete(0, tk.END)
        self.entry_imagem.insert(0, livro.imagem if livro.imagem else "")

        self.alterar_campos()  # Atualiza os campos exibidos

        # Atualiza o botão para "Salvar Edição"
        self.botao_adicionar.config(text="Salvar Alterações", command=lambda: self.salvar_edicao(selecao[0]))    

    def salvar_edicao(self, index):
        """Salva as edições feitas no livro selecionado."""
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
            livro = LivroFisico(titulo, autor, localizacao=extra, diretorio_imagem=imagem)
        else:
            livro = LivroDigital(titulo, autor, formato="PDF", tamanho=float(extra) if extra else 0, imagem=imagem, link=link)

        self.livraria.livros[index] = livro  # Atualiza o livro na lista
        self.atualizar_lista_livros()
        messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")

        # Voltar o botão para "Adicionar Livro"
        self.botao_adicionar.config(text="Adicionar Livro", command=self.adicionar_livro)

    def atualizar_lista_livros(self):
        """Atualiza a lista de livros na interface."""
        self.lista_livros.delete(0, tk.END)
        for livro in self.livraria.livros:
            tipo = "📖 Físico" if isinstance(livro, LivroFisico) else "💻 Digital"
            self.lista_livros.insert(tk.END, f"{livro.titulo} - {livro.autor} ({tipo})")

    def iniciar(self):
        """Inicia a interface gráfica."""
        self.janela.mainloop()