import tkinter as tk
from tkinter import messagebox
from app.models.produto_model import ProdutoModel

class ProdutoView:
    def __init__(self, root):
        self.model = ProdutoModel()
        self.root = root
        self.root.title("Cadastro de Produtos")

        self.label_nome = tk.Label(root, text="Nome do Produto:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        self.label_preco = tk.Label(root, text="Preço:")
        self.label_preco.pack()
        self.entry_preco = tk.Entry(root)
        self.entry_preco.pack()

        self.label_estoque = tk.Label(root, text="Estoque:")
        self.label_estoque.pack()
        self.entry_estoque = tk.Entry(root)
        self.entry_estoque.pack()

        self.btn_salvar = tk.Button(root, text="Salvar", command=self.salvar_produto)
        self.btn_salvar.pack()

    def salvar_produto(self):
        nome = self.entry_nome.get()
        preco = self.entry_preco.get()
        estoque = self.entry_estoque.get()
        try:
            self.model.inserir(nome, float(preco), int(estoque))
            messagebox.showinfo("Sucesso", "Produto cadastrado!")
        except:
            messagebox.showerror("Erro", "Verifique os dados inseridos.")
