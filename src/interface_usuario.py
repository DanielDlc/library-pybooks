import tkinter as tk
from tkinter import messagebox

from livro_digital import LivroDigital
from livro_fisico import LivroFisico


class Interface:
    def __init__(self, livraria):
        self.livraria = livraria
        self.janela = tk.Tk()
        self.janela.title('Sistema de Gerenciamento de Livraria')

        # Labels e campos de entrada
        tk.Label(self.janela, text='Título:', anchor='w').grid(
            row=0, column=0, sticky='w', padx=10, pady=5
        )
        self.entry_titulo = tk.Entry(self.janela, width=50)  # Tamanho maior
        self.entry_titulo.grid(row=0, column=1, columnspan=2, pady=5)

        tk.Label(self.janela, text='Autor:', anchor='w').grid(
            row=1, column=0, sticky='w', padx=10, pady=5
        )
        self.entry_autor = tk.Entry(self.janela, width=50)  # Tamanho maior
        self.entry_autor.grid(row=1, column=1, columnspan=2, pady=5)

        # Escolha do tipo de livro
        tk.Label(self.janela, text='Tipo:', anchor='w').grid(
            row=2, column=0, sticky='w', padx=10, pady=5
        )
        self.tipo_var = tk.StringVar(value='Físico')
        tk.Radiobutton(
            self.janela,
            text='Físico',
            variable=self.tipo_var,
            value='Físico',
            command=self.alterar_campos,
        ).grid(row=2, column=1)
        tk.Radiobutton(
            self.janela,
            text='Digital',
            variable=self.tipo_var,
            value='Digital',
            command=self.alterar_campos,
        ).grid(row=2, column=2)

        # Campos adicionais dinâmicos
        self.label_extra = tk.Label(
            self.janela, text='Localização:', anchor='center'
        )
        self.label_extra.grid(row=3, column=0, padx=10, pady=5)
        self.entry_extra = tk.Entry(self.janela, width=20)  # Localização menor
        self.entry_extra.grid(row=3, column=1, pady=5, sticky='we')

        # Condição (para livros físicos)
        self.label_condicao = tk.Label(
            self.janela, text='Condição:', anchor='center'
        )
        self.label_condicao.grid(row=4, column=0, padx=10, pady=5)
        self.entry_condicao = tk.Entry(self.janela, width=20)
        self.entry_condicao.grid(row=4, column=1, pady=5, sticky='we')

        # Botões
        self.botao_adicionar = tk.Button(
            self.janela, text='Adicionar Livro', command=self.adicionar_livro
        )
        self.botao_adicionar.grid(row=5, column=0, columnspan=3, pady=10)

        self.botao_listar = tk.Button(
            self.janela,
            text='Listar Todos os Livros',
            command=self.listar_livros,
        )
        self.botao_listar.grid(row=6, column=0, columnspan=3, pady=5)

        self.botao_listar_fisicos = tk.Button(
            self.janela,
            text='Listar Livros Físicos',
            command=self.listar_livros_fisicos,
        )
        self.botao_listar_fisicos.grid(row=7, column=0, columnspan=3, pady=5)

        self.botao_listar_digitais = tk.Button(
            self.janela,
            text='Listar Livros Digitais',
            command=self.listar_livros_digitais,
        )
        self.botao_listar_digitais.grid(row=8, column=0, columnspan=3, pady=5)

    def alterar_campos(self):
        """Altera os campos adicionais com base no tipo de livro."""
        tipo = self.tipo_var.get()
        if tipo == 'Físico':
            self.label_extra.config(text='Localização:')
            self.entry_condicao.config(
                state='normal'
            )  # Condição visível para físicos
            self.entry_extra.delete(0, tk.END)
            self.entry_extra.config(state='normal')
        else:  # Digital
            self.label_extra.config(text='Tamanho (MB):')
            self.entry_condicao.delete(0, tk.END)
            self.entry_condicao.config(state='disabled')  # Desativar condição
            self.entry_extra.delete(0, tk.END)

    def adicionar_livro(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        tipo = self.tipo_var.get()
        extra = self.entry_extra.get()
        condicao = self.entry_condicao.get()

        if not titulo or not autor:
            messagebox.showerror('Erro', 'Preencha os campos Título e Autor!')
            return

        if tipo == 'Físico':
            livro = LivroFisico(
                titulo,
                autor,
                localizacao=extra or 'Desconhecida',
                condicao=condicao or 'novo',
            )
        else:  # Livro Digital
            try:
                tamanho = float(extra) if extra else 0.0
                livro = LivroDigital(titulo, autor, tamanho=tamanho)
            except ValueError:
                messagebox.showerror(
                    'Erro',
                    'O tamanho deve ser um número válido (ex.: 5.0 MB).',
                )
                return

        mensagem = self.livraria.adicionar_livro(livro)
        messagebox.showinfo('Resultado', mensagem)

    def listar_livros(self):
        livros = self.livraria.listar_livros()
        if livros:
            messagebox.showinfo('Livros Cadastrados', livros)
        else:
            messagebox.showinfo(
                'Livros Cadastrados', 'Nenhum livro cadastrado.'
            )

    def listar_livros_fisicos(self):
        livros_fisicos = self.livraria.listar_livros_fisicos()
        if livros_fisicos:
            messagebox.showinfo('Livros Físicos', livros_fisicos)
        else:
            messagebox.showinfo(
                'Livros Físicos', 'Nenhum livro físico cadastrado.'
            )

    def listar_livros_digitais(self):
        livros_digitais = self.livraria.listar_livros_digitais()
        if livros_digitais:
            messagebox.showinfo('Livros Digitais', livros_digitais)
        else:
            messagebox.showinfo(
                'Livros Digitais', 'Nenhum livro digital cadastrado.'
            )

    def iniciar(self):
        self.janela.mainloop()
