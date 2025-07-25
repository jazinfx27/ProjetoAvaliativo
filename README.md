# 🧾 Projeto Avaliador - Sistema de Controle de Loja de Roupas

## 💡 Objetivo

Desenvolver um sistema desktop para o controle de vendas, clientes e produtos de uma loja de roupas, utilizando Python com Tkinter, banco de dados MySQL e arquitetura MVC.

---

## ⚙️ Funcionalidades

- ✅ Login com autenticação de usuário
- ✅ Cadastro, listagem, edição e exclusão de **clientes**
- ✅ Cadastro, listagem, edição e exclusão de **produtos**
- ✅ Registro de **vendas** com múltiplos itens
- ✅ Interface gráfica amigável com **Tkinter**
- ✅ Conexão segura com banco de dados via **arquivo .env**
- ✅ Organização em camadas: `models`, `views`, `controllers`

---

## 🧱 Estrutura do Projeto

projeto_avaliador/
├── app/
│ ├── controllers/ # Lógica entre views e models
│ ├── database/ # Conexão e scripts SQL
│ ├── models/ # Acesso ao banco
│ ├── views/ # Interface Tkinter
│ └── main.py # Ponto de entrada
├── docs/ # Documentação
├── .env # Configurações de ambiente
├── .gitignore # Arquivos ignorados pelo Git
├── README.md # Este arquivo

yaml
Copiar
Editar

---

## 🗃 Banco de Dados

- Banco de dados MySQL
- Tabelas principais:
  - `usuarios`
  - `clientes`
  - `produtos`
  - `vendas`
  - `itens_venda`
- O modelo do banco (DER) está disponível em `docs/modelo_banco.png`

---

## 🔐 Configuração do Ambiente

1. Instale as dependências:
   ```bash
   pip install mysql-connector-python python-dotenv bcrypt
Copie o arquivo .env:

ini
Copiar
Editar

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=loja_roupas

Execute o script SQL:

Abra o MySQL e rode app/database/setup.sql para criar as tabelas

📄 Documentação
A documentação completa está na pasta /docs:

requisitos.txt: Requisitos funcionais e não funcionais

algoritmo.txt: Descrição das funcionalidades

DER.txt: Relacionamentos entre as tabelas

modelo_banco.png: Imagem do banco (DER)

🧑‍💻 Autor
Desenvolvido por: [JOÃO ARTHUR]

Coautoria de suporte técnico com ChatGPT (OpenAI)

