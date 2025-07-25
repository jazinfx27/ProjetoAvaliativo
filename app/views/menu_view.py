import tkinter as tk
from tkinter import messagebox
from app.models.venda_model import VendaModel

class VendaView:
    def __init__(self, root):
        self.model = VendaModel()
        self.root = root
        self.root.title("Registrar Venda")

        self.label_cliente = tk.Label(root, text="ID do Cliente:")
        self.label_cliente.pack()
        self.entry_cliente = tk.Entry(root)
        self.entry_cliente.pack()

        self.label_produto = tk.Label(root, text="ID do Produto:")
        self.label_produto.pack()
        self.entry_produto = tk.Entry(root)
        self.entry_produto.pack()

        self.label_quantidade = tk.Label(root, text="Quantidade:")
        self.label_quantidade.pack()
        self.entry_quantidade = tk.Entry(root)
        self.entry_quantidade.pack()

        self.label_preco = tk.Label(root, text="Preço Unitário:")
        self.label_preco.pack()
        self.entry_preco = tk.Entry(root)
        self.entry_preco.pack()

        self.btn_registrar = tk.Button(root, text="Registrar Venda", command=self.registrar_venda)
        self.btn_registrar.pack()

    def registrar_venda(self):
        try:
            cliente_id = int(self.entry_cliente.get())
            produto_id = int(self.entry_produto.get())
            quantidade = int(self.entry_quantidade.get())
            preco = float(self.entry_preco.get())

            itens = [{"produto_id": produto_id, "quantidade": quantidade, "preco": preco}]
            self.model.registrar_venda(cliente_id, itens)
            messagebox.showinfo("Sucesso", "Venda registrada!")
        except:
            messagebox.showerror("Erro", "Verifique os dados.")
