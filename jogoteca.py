from flask import Flask, flash, render_template, request, redirect, session

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
app.secret_key = 'alura'

@app.route('/')
def inicio():    
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo='Crie um novo Jogo:')

@app.route('/criar', methods=['POST'])
def criar():
    
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'aloha' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + 'Logado com Sucesso')
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuario nao Logado')
        return redirect('/login')
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuario Logado')
    return redirect('/')

app.run(debug=True)