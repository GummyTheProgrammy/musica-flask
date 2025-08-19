# app.py

import os
from flask import Flask, render_template, send_from_directory

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Define o caminho para a pasta de músicas
MUSICAS_FOLDER = os.path.join(os.getcwd(), 'musicas')

# 1. Rota da página principal
@app.route('/')
def index():
    # Obtém uma lista de todos os arquivos na pasta 'musicas'
    # o 'musicas' aqui é o nome do diretório
    lista_musicas = os.listdir(MUSICAS_FOLDER)
    # Renderiza a página HTML e passa a lista de músicas para ela
    return render_template('songplayer.html', musicas=lista_musicas)

# 2. Rota para servir os arquivos de música
# A rota recebe o nome do arquivo como um parâmetro
@app.route('/musicas/<nome_arquivo>')
def get_musica(nome_arquivo):
    # Envia o arquivo solicitado da pasta de músicas
    return send_from_directory(MUSICAS_FOLDER, nome_arquivo)

if __name__ == '__main__':
    # Inicia o servidor com o modo de depuração ativado
    app.run(debug=True)