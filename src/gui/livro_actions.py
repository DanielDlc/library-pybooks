"""Módulo com botões de ações (Editar, Excluir, Exibir livros)."""

import tkinter as tk
import webbrowser
from tkinter import messagebox, simpledialog

from src.models.livro_digital import LivroDigital
from src.models.livro_fisico import LivroFisico


class LivroActions:
    """Botões de ação para manipular os livros."""

    def __init__(self, master, lista_livros, livro_manager):
        """Cria os botões e vincula as ações."""
        self.lista_livros = lista_livros
        self.livro_manager = livro_manager

        frame_botoes = tk.Frame(master)
        frame_botoes.pack(pady=5)

        self.botao_editar = tk.Button(
            frame_botoes, text="Editar", command=self.editar_livro
        )
        self.botao_editar.pack(side=tk.LEFT, padx=5)

        self.botao_excluir = tk.Button(
            frame_botoes, text="Excluir", command=self.excluir_livro
        )
        self.botao_excluir.pack(side=tk.LEFT, padx=5)

        self.botao_exibir = tk.Button(
            frame_botoes, text="Abrir Link", command=self.abrir_link
        )
        self.botao_exibir.pack(side=tk.LEFT, padx=5)

    def editar_livro(self):
        """Edita um livro selecionado e salva as alterações no JSON."""
        selecao = self.lista_livros.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um livro para editar!")
            return

        index = selecao[0]
        livro = self.livro_manager.listar_livros()[index]

        novo_titulo = simpledialog.askstring(
            "Editar Livro", "Novo título:", initialvalue=livro.titulo
        )
        novo_autor = simpledialog.askstring(
            "Editar Livro", "Novo autor:", initialvalue=livro.autor
        )
        novo_link = simpledialog.askstring(
            "Editar Livro", "Novo link:",
            initialvalue=getattr(livro, "link", "")
        )

        if isinstance(livro, LivroFisico):
            nova_localizacao = simpledialog.askstring(
                "Editar Livro",
                "Nova localização:",
                initialvalue=livro.localizacao,
            )
            livro_editado = LivroFisico(
                novo_titulo, novo_autor,
                localizacao=nova_localizacao, link=novo_link
            )
        else:
            novo_tamanho = simpledialog.askfloat(
                "Editar Livro",
                "Novo tamanho (MB):",
                initialvalue=livro.tamanho,
            )
            livro_editado = LivroDigital(
                novo_titulo,
                novo_autor,
                formato="PDF",
                tamanho=novo_tamanho,
                link=novo_link,
            )

        self.livro_manager.livraria.livros[index] = livro_editado
        self.livro_manager.salvar_dados()
        self.lista_livros.delete(index)
        self.lista_livros.insert(
            index, f"{livro_editado.titulo} - {livro_editado.autor}"
        )

        messagebox.showinfo("Sucesso", "Livro editado com sucesso!")

    def excluir_livro(self):
        """Exclui um livro selecionado e atualiza o JSON."""
        selecao = self.lista_livros.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um livro para excluir!")
            return

        index = selecao[0]
        livro = self.livro_manager.listar_livros()[index]
        confirmacao = messagebox.askyesno(
            "Confirmar",
            f"Tem certeza que deseja excluir '{livro.titulo}'?",
        )

        if confirmacao:
            self.livro_manager.livraria.livros.pop(index)
            self.livro_manager.salvar_dados()
            self.lista_livros.delete(index)
            messagebox.showinfo("Sucesso", "Livro excluído com sucesso!")

    def abrir_link(self):
        """Abre o link do livro no navegador."""
        selecao = self.lista_livros.curselection()
        if not selecao:
            messagebox.showwarning(
                "Aviso", "Selecione um livro para abrir o link!"
            )
            return

        index = selecao[0]
        livro = self.livro_manager.listar_livros()[index]

        if hasattr(livro, "link") and livro.link and livro.link != "#":
            webbrowser.open(livro.link)
        else:
            messagebox.showwarning(
                "Aviso", "O livro selecionado não possui um link válido."
            )
