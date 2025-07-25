from app.database.conexao import conectar

class ClienteModel:
    def __init__(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()

    def inserir(self, nome, email):
        sql = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
        self.cursor.execute(sql, (nome, email))
        self.conn.commit()

    def listar(self):
        self.cursor.execute("SELECT * FROM clientes")
        return self.cursor.fetchall()

    def atualizar(self, cliente_id, nome, email):
        sql = "UPDATE clientes SET nome=%s, email=%s WHERE id=%s"
        self.cursor.execute(sql, (nome, email, cliente_id))
        self.conn.commit()

    def deletar(self, cliente_id):
        self.cursor.execute("DELETE FROM clientes WHERE id=%s", (cliente_id,))
        self.conn.commit()
