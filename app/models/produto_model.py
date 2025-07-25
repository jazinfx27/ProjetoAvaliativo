from app.database.conexao import conectar

class ProdutoModel:
    def __init__(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()

    def inserir(self, nome, preco, estoque):
        sql = "INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (nome, preco, estoque))
        self.conn.commit()

    def listar(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

    def atualizar(self, produto_id, nome, preco, estoque):
        sql = "UPDATE produtos SET nome=%s, preco=%s, estoque=%s WHERE id=%s"
        self.cursor.execute(sql, (nome, preco, estoque, produto_id))
        self.conn.commit()

    def deletar(self, produto_id):
        self.cursor.execute("DELETE FROM produtos WHERE id=%s", (produto_id,))
        self.conn.commit()
