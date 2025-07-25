from app.database.conexao import conectar
import bcrypt

class UsuarioModel:
    def __init__(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()

    def criar_usuario(self, nome, usuario, senha):
        senha_criptografada = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        sql = "INSERT INTO usuarios (nome, usuario, senha) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (nome, usuario, senha_criptografada.decode()))
        self.conn.commit()

    def autenticar(self, usuario, senha):
        sql = "SELECT senha FROM usuarios WHERE usuario = %s"
        self.cursor.execute(sql, (usuario,))
        resultado = self.cursor.fetchone()
        if resultado:
            return bcrypt.checkpw(senha.encode(), resultado[0].encode())
        return False
