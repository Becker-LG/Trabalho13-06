from flask import Flask, render_template, request, redirect
import sqlite3
import io
from PIL import Image

# Conectar ao banco de dados
conexao = sqlite3.connect("testes.db")
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS teste (
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               imagem BLOB NOT NULL)''')

#with open('./testes/imagem.jpg', 'rb') as f:
#    imagem_bytes = f.read()
#
#cursor.execute("INSERT INTO teste (imagem) VALUES (?)", (imagem_bytes,))
#conexao.commit()
#
#cursor.execute("SELECT imagem FROM teste WHERE id = 1")
#imagem_recuperada = cursor.fetchone()[0]
#
#imagem_recuperada_io = io.BytesIO(imagem_recuperada)
#imagem = Image.open(imagem_recuperada_io)
#imagem.save('./testes/imagem_recuperada.jpg')

conexao.close()

app = Flask(__name__)

@app.route("/teste")
def teste():
    imagem = request.args.get("imagem")
    return render_template("teste.html", imagem = imagem)

app.run()