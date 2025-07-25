import tkinter as tk
from app.views.cliente_view import ClienteView
from app.views.produto_view import ProdutoView
from app.views.venda_view import VendaView

class MenuView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu Principal")

        tk.Button(self.root, text="Clientes", width=20, command=self.abrir_clientes).pack(pady=5)
        tk.Button(self.root, text="Produtos", width=20, command=self.abrir_produtos).pack(pady=5)
        tk.Button(self.root, text="Vendas", width=20, command=self.abrir_vendas).pack(pady=5)

        self.root.mainloop()

    def abrir_clientes(self):
        janela = tk.Toplevel(self.root)
        ClienteView(janela)

    def abrir_produtos(self):
        janela = tk.Toplevel(self.root)
        ProdutoView(janela)

    def abrir_vendas(self):
        janela = tk.Toplevel(self.root)
        VendaView(janela)
