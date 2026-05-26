from flask import Flask, render_template
import mysql.connector


app = Flask(__name__)

@app.route('/pag.login/login.html')
def login():
    return render_template('/pag.login/login.html')

@app.route('/pag.cadastro/cad.html', methods=['POST'])
def cadastro():
    conexao = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='almoxarifado')

        
    cursor = conexao.cursor(dictionary=True)
    query = "INSERT INTO almoxarifado(nome, qntd, tipo) VALUES ('"+ dado_nome +"','"+ dado_qntd +"','"+ dado_tipo +"'"
    cursor.execute(query)
    resultado = cursor.fetchall()
    resultado = cursor

    cursor.close()
    conexao.close()
    dado_nome = request.form['nome']
    dado_qntd = request.form['qntd']
    dado_tipo = request.form['tipo']


    return render_template('/pag.cadastro/cad.html', dado_nome=dado_nome, dado_qntd=dado_qntd, dado_tipo=dado_tipo)

@app.route('/pag.estoque/consultaestoque.html')
def estoque():
    conexao = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='almoxarifado')

        
    cursor = conexao.cursor(dictionary=True)
        
    cursor.execute('SELECT * FROM almoxarifado')
    resultado = cursor.fetchall()
    resultado = cursor

    cursor.close()
    conexao.close()




    return render_template('/pag.estoque/consultaestoque.html')

@app.route('/pag.solicitaçoes/index.html')
def solicitacoes():
    return render_template('/pag.solicitaçoes/index.html')

@app.route('/pag.devolver/devolver.html')
def devolver():
    return render_template('/pag.devolver/devolver.html')



if __name__ == '__main__':
    app.run( host='0.0.0.0', port=80, debug=True)
    