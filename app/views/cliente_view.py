import tkinter as tk
from tkinter import messagebox
from app.models.cliente_model import ClienteModel

class ClienteView:
    def __init__(self, root):
        self.model = ClienteModel()
        self.root = root
        self.root.title("Cadastro de Clientes")

        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        self.label_email = tk.Label(root, text="Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(root)
        self.entry_email.pack()

        self.btn_salvar = tk.Button(root, text="Salvar", command=self.salvar_cliente)
        self.btn_salvar.pack()

        self.btn_listar = tk.Button(root, text="Listar Clientes", command=self.listar_clientes)
        self.btn_listar.pack()

    def salvar_cliente(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        if nome and email:
            self.model.inserir(nome, email)
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")

    def listar_clientes(self):
        clientes = self.model.listar()
        for cliente in clientes:
            print(cliente)
