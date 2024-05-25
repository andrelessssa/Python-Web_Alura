from flask import Flask, render_template, request

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of war', 'Rack', 'PS2')
jogo3 = Jogo('Mortal Combate', 'Luta', 'PS3')
jogo4 = Jogo('Sonic', 'Aventura', 'PS4')

lista = [jogo1, jogo2, jogo3, jogo4]

app = Flask(__name__)

@app.route('/')
def inicio():    
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Crie um novo Jogo:')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run(debug=True)