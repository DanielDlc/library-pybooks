"""Módulo com botões de ações (Editar, Excluir, Exibir livros)."""

import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import webbrowser
from PIL import Image, ImageTk
from src.models.livro_fisico import LivroFisico
from src.models.livro_digital import LivroDigital

# Diretórios padrão para imagens
IMG_DIR_FISICOS = os.path.join("img", "fisicos")
DEFAULT_IMAGE_PATH = os.path.join(IMG_DIR_FISICOS, "default.jpg")

class LivroActions:
    """Botões de ação para manipular os livros."""

    def __init__(self, master, lista_livros, livro_manager):
        """Cria os botões e vincula as ações."""
        self.lista_livros = lista_livros
        self.livro_manager = livro_manager

        frame_botoes = tk.Frame(master)
        frame_botoes.pack(pady=5)

        self.botao_editar = tk.Button(frame_botoes, text='Editar', command=self.editar_livro)
        self.botao_editar.pack(side=tk.LEFT, padx=5)

        self.botao_excluir = tk.Button(frame_botoes, text='Excluir', command=self.excluir_livro)
        self.botao_excluir.pack(side=tk.LEFT, padx=5)

        self.botao_exibir = tk.Button(frame_botoes, text='Exibir', command=self.exibir_livro)
        self.botao_exibir.pack(side=tk.LEFT, padx=5)

    def editar_livro(self):
        """Edita um livro selecionado e salva as alterações no JSON."""
        selecao = self.lista_livros.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um livro para editar!")
            return

        index = selecao[0]
        livro = self.livro_manager.listar_livros()[index]

        novo_titulo = simpledialog.askstring("Editar Livro", "Novo título:", initialvalue=livro.titulo)
        novo_autor = simpledialog.askstring("Editar Livro", "Novo autor:", initialvalue=livro.autor)

        if isinstance(livro, LivroFisico):
            nova_localizacao = simpledialog.askstring("Editar Livro", "Nova localização:", initialvalue=livro.localizacao)
            livro_editado = LivroFisico(novo_titulo, novo_autor, localizacao=nova_localizacao, diretorio_imagem=livro.imagem)
        else:
            novo_tamanho = simpledialog.askfloat("Editar Livro", "Novo tamanho (MB):", initialvalue=livro.tamanho)
            livro_editado = LivroDigital(novo_titulo, novo_autor, formato="PDF", tamanho=novo_tamanho, imagem=livro.imagem, link=livro.link)

        self.livro_manager.livraria.livros[index] = livro_editado
        self.livro_manager.salvar_dados()
        self.lista_livros.delete(index)
        self.lista_livros.insert(index, f"{livro_editado.titulo} - {livro_editado.autor}")

        messagebox.showinfo("Sucesso", "Livro editado com sucesso!")

    def excluir_livro(self):
        """Exclui um livro selecionado e atualiza o JSON."""
        selecao = self.lista_livros.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um livro para excluir!")
            return

        index = selecao[0]
        livro = self.livro_manager.listar_livros()[index]
        confirmacao = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir '{livro.titulo}'?")

        if confirmacao:
            self.livro_manager.livraria.livros.pop(index)
            self.livro_manager.salvar_dados()
            self.lista_livros.delete(index)
            messagebox.showinfo("Sucesso", "Livro excluído com sucesso!")

    def exibir_livro(self):
        """Exibe a imagem do livro ou abre o link no navegador."""
        selecao = self.lista_livros.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um livro para exibir!")
            return

        index = selecao[0]
        livro = self.livro_manager.listar_livros()[index]

        if isinstance(livro, LivroFisico):
            self.exibir_imagem_fisica(livro)
        elif hasattr(livro, "link") and livro.link and livro.link != "#":
            self.abrir_link(livro.link)
        else:
            messagebox.showwarning("Aviso", "O livro selecionado não possui um link ou imagem para exibir.")

    def exibir_imagem_fisica(self, livro):
        """Tenta exibir a imagem de um livro físico."""
        caminho_imagem = livro.imagem

        # Se a imagem estiver vazia, buscar pelo nome do livro
        if not caminho_imagem or not os.path.exists(caminho_imagem):
            caminho_imagem = os.path.join(IMG_DIR_FISICOS, f"{livro.titulo}.jpg")

        # Se ainda não existir, usar a imagem padrão
        if not os.path.exists(caminho_imagem):
            caminho_imagem = DEFAULT_IMAGE_PATH

        if os.path.exists(caminho_imagem):
            self.abrir_imagem(caminho_imagem)
        else:
            messagebox.showwarning("Aviso", "Nenhuma imagem disponível para este livro.")

    def abrir_imagem(self, caminho_imagem):
        """Exibe a imagem do livro em uma nova janela."""
        try:
            img = Image.open(caminho_imagem)
            img.thumbnail((300, 300))

            janela_imagem = tk.Toplevel()
            janela_imagem.title("Imagem do Livro")

            img_tk = ImageTk.PhotoImage(img)
            label_imagem = tk.Label(janela_imagem, image=img_tk)
            label_imagem.image = img_tk  # Manter referência
            label_imagem.pack()

            janela_imagem.mainloop()

        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir a imagem: {e}")

    def abrir_link(self, link):
        """Abre o link no navegador."""
        try:
            webbrowser.open(link)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o link: {e}")