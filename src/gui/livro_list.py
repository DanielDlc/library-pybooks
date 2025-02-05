"""Módulo que exibe a lista de livros cadastrados."""

import tkinter as tk

from src.gui.livro_actions import LivroActions
from src.managers.livro_manager import LivroManager
from src.models.livro_fisico import LivroFisico


class LivroList:
    """Lista de livros cadastrados."""

    def __init__(self, master, livro_manager: LivroManager):
        """
        Inicializa a lista de livros.

        :param master: O widget pai.
        :param livro_manager: O gerenciador de livros (LivroManager).
        """
        self.livro_manager = livro_manager

        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        tk.Label(self.frame, text='📚 Livros cadastrados:').pack(anchor='w')

        # Lista de livros
        self.lista_livros = tk.Listbox(self.frame, width=60, height=10)
        self.lista_livros.pack()

        # Adicionar botões de ação (Editar, Excluir, Abrir)
        self.actions = LivroActions(
            self.frame,
            self.lista_livros,
            self.livro_manager
        )

        # Atualiza a lista ao iniciar
        self.atualizar_lista()

    def atualizar_lista(self):
        """Atualiza a lista de livros exibidos na interface."""
        self.lista_livros.delete(0, tk.END)

        for livro in self.livro_manager.listar_livros():
            if isinstance(livro, LivroFisico):
                tipo = "📖 Físico"
            else:  # Se não for físico, assume que é digital
                tipo = "💻 Digital"

            self.lista_livros.insert(
                tk.END, f"{livro.titulo} - {livro.autor} ({tipo})"
            )
