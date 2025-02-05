import tkinter as tk
from tkinter import Frame, Label, Radiobutton, StringVar, Entry, Button


class LivroForm(tk.Frame):
    """
    Formulário para adicionar livros na biblioteca.
    """

    def __init__(self, master, livro_manager, livro_list):
        super().__init__(master)
        self.livro_manager = livro_manager
        self.livro_list = livro_list
        self.pack(padx=10, pady=10)  # Mudando para 'pack()' ao invés de 'grid()' na raiz

        self.create_widgets()

    def create_widgets(self):
        """
        Cria os widgets da interface gráfica.
        """

        # Título
        Label(self, text="Título:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.titulo_entry = Entry(self, width=40)
        self.titulo_entry.grid(row=0, column=1, padx=5, pady=5)

        # Autor
        Label(self, text="Autor:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.autor_entry = Entry(self, width=40)
        self.autor_entry.grid(row=1, column=1, padx=5, pady=5)

        # Tipo do livro (Físico/Digital)
        Label(self, text="Tipo:").grid(row=2, column=0, sticky="e", padx=5, pady=5)

        # Criando um Frame para os botões de tipo de livro
        frame_tipo = Frame(self)
        frame_tipo.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Variável para armazenar a seleção do tipo
        self.tipo_var = StringVar(value="fisico")

        # Radiobutton para Livro Físico
        self.radio_fisico = Radiobutton(
            frame_tipo, text="📖 Físico", variable=self.tipo_var, value="fisico"
        )
        self.radio_fisico.grid(row=0, column=0, padx=(0, 5))  # Mantendo os botões juntos

        # Radiobutton para Livro Digital
        self.radio_digital = Radiobutton(
            frame_tipo, text="💻 Digital", variable=self.tipo_var, value="digital"
        )
        self.radio_digital.grid(row=0, column=1, padx=(5, 0))  # Mantendo alinhamento

        # Campo para localização (Aparece para livros físicos)
        Label(self, text="Localização:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.localizacao_entry = Entry(self, width=40)
        self.localizacao_entry.grid(row=3, column=1, padx=5, pady=5)

        # Campo para o link (Para livros digitais ou referência de livros físicos)
        Label(self, text="🔗 Link:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.link_entry = Entry(self, width=40)
        self.link_entry.grid(row=4, column=1, padx=5, pady=5)

        # Botão para adicionar livro
        self.add_button = Button(self, text="Adicionar Livro", command=self.adicionar_livro)
        self.add_button.grid(row=5, column=1, pady=10)

    def adicionar_livro(self):
        """
        Adiciona um novo livro à biblioteca.
        """

        titulo = self.titulo_entry.get().strip()
        autor = self.autor_entry.get().strip()
        tipo = self.tipo_var.get()
        localizacao = self.localizacao_entry.get().strip()
        link = self.link_entry.get().strip()

        if not titulo or not autor:
            print("Erro: O título e o autor são obrigatórios.")
            return

        livro = self.livro_manager.adicionar_livro(
            titulo=titulo,
            autor=autor,
            tipo=tipo,
            localizacao=localizacao if tipo == "fisico" else "",
            link=link if link else "#"
        )

        if livro:
            self.livro_list.atualizar_lista()
            self.limpar_campos()

    def limpar_campos(self):
        """
        Limpa os campos do formulário após adicionar um livro.
        """
        self.titulo_entry.delete(0, tk.END)
        self.autor_entry.delete(0, tk.END)
        self.localizacao_entry.delete(0, tk.END)
        self.link_entry.delete(0, tk.END)
        self.tipo_var.set("fisico")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Gerenciamento de Livraria")
    app = LivroForm(root, None, None)
    root.mainloop()