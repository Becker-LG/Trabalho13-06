'''
Baseado no modelo 10 - completo

1) A nova tabela criada, deve conter no mínimo 10 campos diversos, mas deve ter campos do tipo inteiro, string, data, valores decimais, entre outros. Também deve ter Chave Primária.
FEEEITOOOOOOOOOOOO

2) A página WEB deve ter no mínimo 4 caminhos (/about, /cadastro, etc).
VAI TER: cadastro, listagem de filmes, página inicial, tabelaAvaliação

3) Dentro da página WEB, deve ter a listagem separada da página do cadastro. Também deve ter no mínimo 3 elementos diferentes, tipo ComboBox, DropDown, CheckBox, etc.
Radio = classe etária
CheckBox = Gênero
DataList = idioma

4) Deve ter na página a opção para carregar/trocar a imagem de fundo da página.
FEITOOOOOO

5) uma atividade extra  (se fizer os 4 acima, já garante o 10.0 - Dez)

Salvar o caminho da imagem de fundo, na base de dados (tabela).
FEITOOOOOOOOOOOO

Já que esta salva, pode adicionar ela na listagem e ter uma imagem para cada cadastro.

E se agora, está na listagem, criar um botão ao lado da listagem para poder trocar a imagem para cada registro cadastrado
'''

######### VAI SER SOBRE FILMEEEESSSS ##########

#Imports
from flask import Flask, render_template, request
import sqlite3
import io
from PIL import Image
#tem que dar
# <!-- NÃO PRECISA MAIS DO PILLOW ##############################
'''pip install Pillow'''
# -->
import requests
# <!--
'''pip install requests'''
# -->
import os

# Conectar ao banco de dados
conexao = sqlite3.connect("filmes.db", check_same_thread=False)
cursor = conexao.cursor()

comandoSQL = '''CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(200) NOT NULL,
                diretor VARCHAR(200) NOT NULL,
                genero VARCHAR(200),
                idioma VARCHAR(45),
                dataLanca DATE,
                duracao INTEGER NOT NULL,
                avalIMDB FLOAT,
                avalRotten FLOAT,
                ganho FLOAT,
                claEtaria INTEGER)'''

cursor.execute(comandoSQL)

comandoSQL = '''CREATE TABLE IF NOT EXISTS imagem (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                imagem VARCHAR(500) NOT NULL)'''

cursor.execute(comandoSQL)

# Funções =========================================================================================================================================================

###### CRUD FILMES ######

def F_Insert(nome, diretor, genero, idioma, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria):
    cursor.execute('''INSERT INTO filmes (nome, diretor, genero, idioma, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (nome, diretor, genero, idioma, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria))
    
    conexao.commit()
    return 'Feito!'

def F_SelectTudo():
    cursor.execute('''SELECT nome, diretor, genero, idioma, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria FROM filmes''')
    registros = cursor.fetchall()

    return registros

def F_SelectNome(nome):
    cursor.execute('''SELECT nome, diretor, genero, idioma, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria FROM filmes
                   WHERE nome = ?''', nome)
    registros = cursor.fetchall()
    nome, diretor, genero, idioma, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria = registros[0]

    return [nome, diretor, genero, idioma, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria]

def F_SelectMelhores():
    cursor.execute('''SELECT nome, diretor, genero, idioma, dataLanca, duracao, avalIMDB, avalRotten, ganho, claEtaria FROM filmes
                   WHERE avalIMDB >= 70 OR avalRotten >= 70
                   ORDER BY avalIMDB, avalRotten''')
    registros = cursor.fetchall()
    return registros

def F_DeleteId(id):
    cursor.execute('''DELETE FROM filmes WHERE id = ?''', id)
    return

###### CRUD IMAGENS ######

def I_Insert(imagem):
    cursor.execute('''INSERT INTO imagem (imagem) VALUES (?)''', (imagem,))
    conexao.commit()
    return 'Feito!'

def I_Select():
    cursor.execute('''SELECT id, imagem FROM imagem''')
    registros = cursor.fetchall()
    return registros


###### BAIXAR IMAGEM ######

def BaixarImagem(url, pasta_destino, nome_arquivo):
    try:
        # Garante que a pasta existe
        os.makedirs(pasta_destino, exist_ok=True)
        
        caminho_completo = os.path.join(pasta_destino, nome_arquivo)
        
        resposta = requests.get(url)
        resposta.raise_for_status()

        with open(caminho_completo, 'wb') as arquivo:
            arquivo.write(resposta.content)
        print(f"Imagem salva em: {caminho_completo}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar a imagem: {e}")


'''
IDEIA INICIAL DE COMO COLOCAR IMAGEM NO SITE

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
    link = request.args.get('link') if request.args.get('link') else ""
    if link != '':
        BaixarImagem(link, 'static', 'background.jpg')
        imagens = I_Select()
        x = 0
        for i in imagens:
            if i[1] == link:
                x += 1

        if x == 0:
            I_Insert(link)

    #print(F_Insert('Teste', 'Teste', 'Teste', 'Teste', '12-12-1212', 200, 100, 100, 1000000, 12))

    return render_template("about.html")

@app.route("/register")
def register():
    valores = []
    valores.append(request.args.get('campoNome') if request.args.get('campoNome') else "")
    valores.append(request.args.get('campoDiretor') if request.args.get('campoDiretor') else "")
    valores.append(request.args.get('campoIdioma') if request.args.get('campoIdioma') else "")
    valores.append(request.args.get('campoDataLanc') if request.args.get('campoDataLanc') else "")
    valores.append(request.args.get('campoDuracao') if request.args.get('campoDuracao') else "")
    valores.append(request.args.get('campoAvalIMDB') if request.args.get('campoAvalIMDB') else "")
    valores.append(request.args.get('campoAvalRotten') if request.args.get('campoAvalRotten') else "")
    valores.append(request.args.get('campoGanho') if request.args.get('campoGanho') else "")
    valores.append(request.args.get('campoClaEtaria') if request.args.get('campoClaEtaria') else "")

    s = ""
    s += " " + request.args.get('campoSuspense') if request.args.get('campoSuspense') else ""
    s += " " + request.args.get('campoDrama') if request.args.get('campoDrama') else ""
    s += " " + request.args.get('campoAcao') if request.args.get('campoAcao') else ""
    valores.append(s)

    if valores[0] != "":
        print(valores)
        F_Insert(valores[0], valores[1], valores[9], valores[2], valores[3], valores[4], valores[5], valores[6], valores[7], valores[8])

    return render_template("register.html", valores = valores)

@app.route("/table")
def table():
    filmes = F_SelectTudo()

    return render_template("table.html", filmes = filmes)

@app.route("/tableAval")
def tableAval():
    filmes = F_SelectMelhores()

    return render_template("tableAval.html", filmes = filmes)

app.run()

#conexao.commit()
