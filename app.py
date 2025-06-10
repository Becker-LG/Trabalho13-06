'''
Baseado no modelo 10 - completo

1) A nova tabela criada, deve conter no mínimo 10 campos diversos, mas deve ter campos do tipo inteiro, string, data, valores decimais, entre outros. Também deve ter Chave Primária.
FEEEITOOOOOOOOOOOO

2) A página WEB deve ter no mínimo 4 caminhos (/about, /cadastro, etc).
VAI TER: cadastro, listagem de filmes, página inicial, FALTA UMA

3) Dentro da página WEB, deve ter a listagem separada da página do cadastro. Também deve ter no mínimo 3 elementos diferentes, tipo ComboBox, DropDown, CheckBox, etc.

4) Deve ter na página a opção para carregar/trocar a imagem de fundo da página.

5) uma atividade extra  (se fizer os 4 acima, já garante o 10.0 - Dez)

Salvar o caminho da imagem de fundo, na base de dados (tabela).

Já que esta salva, pode adicionar ela na listagem e ter uma imagem para cada cadastro.

E se agora, está na listagem, criar um botão ao lado da listagem para poder trocar a imagem para cada registro cadastrado
'''

######### VAI SER SOBRE FILMEEEESSSS ##########

#Imports
from flask import Flask, render_template
import sqlite3
import io
from PIL import Image
#tem que dar
# <!--
'''pip install Pillow'''
# -->

# Conectar ao banco de dados
conexao = sqlite3.connect("filmes.db")
cursor = conexao.cursor()

comandoSQL = '''CREATE TABLE IF NOT EXISTS filme (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(200) NOT NULL,
                diretor VARCHAR(200) NOT NULL,
                genero VARCHAR(200),
                dataLanca DATE,
                duracao INTEGER NOT NULL,
                avalIMDB FLOAT,
                avalRotten FLOAT,
                ganho FLOAT,
                claEtaria BOOLEAN)'''

cursor.execute(comandoSQL)

comandoSQL = '''CREATE TABLE IF NOT EXISTS imagem (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                imagem BLOB NOT NULL)'''

# Funções =========================================================================================================================================================

###### CRUD FILMES ######

def F_Insert(nome, diretor, genero, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria):
    cursor.execute('''INSERT INTO filmes (nome, diretor, genero, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (nome, diretor, genero, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria))
    return

def F_SelectNome(nome):
    cursor.execute('''SELECT nome, diretor, genero, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria FROM filmes
                   WHERE nome = ?''', nome)
    registros = cursor.fetchall()
    nome, diretor, genero, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria = registros[0]
    return [nome, diretor, genero, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria]

def F_SelectGenero(genero):
    cursor.execute('''SELECT nome, diretor, genero, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria FROM filmes
                   WHERE genero = ?''', genero)
    registros = cursor.fetchall()
    nome, diretor, genero, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria = registros[0]
    return [nome, diretor, genero, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria]

def F_SelectClaEtaria(claEtaria):
    cursor.execute('''SELECT nome, diretor, genero, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria FROM filmes
                   WHERE claEtaria = ?''', claEtaria)
    registros = cursor.fetchall()
    nome, diretor, genero, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria = registros[0]
    return [nome, diretor, genero, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria]

def F_DeleteId(id):
    cursor.execute('''DELETE FROM filmes WHERE id = ?''', id)
    return

###### CRUD IMAGENS ######

def I_Insert(imagem):
    cursor.execute('''INSERT INTO imagem (imagem) VALUES (?)''', imagem)
    return

def I_Select():
    cursor.execute('''SELECT id, imagem FROM imagem''')
    registros = cursor.fetchall()
    id, imagem = registros[0]
    return [id, imagem]

'''
conexao = sqlite3.connect("./testes/testes.db")
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS teste (
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               imagem BLOB NOT NULL)")

with open('./testes/imagem.jpg', 'rb') as f:
    imagem_bytes = f.read()

cursor.execute("INSERT INTO teste (imagem) VALUES (?)", (imagem_bytes,))
conexao.commit()

cursor.execute("SELECT imagem FROM teste WHERE id = 1")
imagem_recuperada = cursor.fetchone()[0]

imagem_recuperada_io = io.BytesIO(imagem_recuperada)
imagem = Image.open(imagem_recuperada_io)
imagem.save('./testes/imagem_recuperada.jpg')

conexao.close()'''

# Routes =========================================================================================================================================================

app = Flask(__name__)

@app.route("/")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/table")
def table():
    return render_template("table.html")

@app.route("/tableAval")
def tableAval():
    return render_template("tableAval.html")

app.run()

#conexao.commit()
