import tkinter as tk
from tkinter import messagebox
from app.models.usuario_model import UsuarioModel

class LoginView:
    def __init__(self, root, abrir_menu_callback):
        self.model = UsuarioModel()
        self.root = root
        self.root.title("Login")

        self.label_usuario = tk.Label(root, text="Usuário:")
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()

        self.label_senha = tk.Label(root, text="Senha:")
        self.label_senha.pack()
        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.pack()

        self.btn_login = tk.Button(root, text="Entrar", command=self.login)
        self.btn_login.pack()

        self.abrir_menu_callback = abrir_menu_callback

    def login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        if self.model.autenticar(usuario, senha):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.root.destroy()
            self.abrir_menu_callback()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")
