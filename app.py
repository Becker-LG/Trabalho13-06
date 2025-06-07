'''
Baseado no modelo 10 - completo

1) A nova tabela criada, deve conter no mínimo 10 campos diversos, mas deve ter campos do tipo inteiro, string, data, valores decimais, entre outros. Também deve ter Chave Primária.
FEEEITOOOOOOOOOOOO

2) A página WEB deve ter no mínimo 4 caminhos (/about, /cadastro, etc).
VAI TER: cadastro, listagem de filmes, página inicial, edição dos filmes prontos

3) Dentro da página WEB, deve ter a listagem separada da página do cadastro. Também deve ter no mínimo 3 elementos diferentes, tipo ComboBox, DropDown, CheckBox, etc.

4) Deve ter na página a opção para carregar/trocar a imagem de fundo da página.

5) uma atividade extra  (se fizer os 4 acima, já garante o 10.0 - Dez)

Salvar o caminho da imagem de fundo, na base de dados (tabela).

Já que esta salva, pode adicionar ela na listagem e ter uma imagem para cada cadastro.

E se agora, está na listagem, criar um botão ao lado da listagem para poder trocar a imagem para cada registro cadastrado
'''

######### VAI SER SOBRE FILMEEEESSSS ##########

import sqlite3 
#import pandas as pd

# Conectar ao banco de dados
conexao = sqlite3.connect("firmes.db")
cursor = conexao.cursor()

comandoSQL = '''CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(200) NOT NULL,
                diretor VARCHAR(200) NOT NULL),
                genero VARCHAR(200) PRIMARY KEY AUTOINCREMENT,
                dataLanca DATE NOT NULL,
                duracao INTEGER NOT NULL,
                avaliacaoIMDB FLOAT NOT NULL,
                avaliacaoRotten FLOAT NOT NULL,
                ganho FLOAT NOT NULL,
                classificacaoEtaria BOOLEAN NOT NULL)'''

cursor.execute(comandoSQL)