from app.database.conexao import conectar

class VendaModel:
    def __init__(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()

    def registrar_venda(self, cliente_id, itens):
        sql_venda = "INSERT INTO vendas (cliente_id) VALUES (%s)"
        self.cursor.execute(sql_venda, (cliente_id,))
        venda_id = self.cursor.lastrowid

        sql_item = "INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)"
        for item in itens:
            self.cursor.execute(sql_item, (venda_id, item['produto_id'], item['quantidade'], item['preco']))

        self.conn.commit()
        return venda_id

    def listar_vendas(self):
        self.cursor.execute("SELECT * FROM vendas")
        return self.cursor.fetchall()
