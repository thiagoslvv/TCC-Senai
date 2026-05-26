from flask import Flask, render_template1

app = Flask(__name__)

@app.route('/pag.login/login.html')
def login():
    return render_template('/pag.login/login.html')

@app.route('/pag.cadastro/cad.html')
def cadastro():
    return render_template('/pag.cadastro/cad.html')
@app.route('/pag.redicionamento/red.html')
def redirecionamento():
    return render_template('/pag.redicionamento/red.html')

@app.route('/pag.estoque/consultaestoque.html')
def estoque():
    return render_template('/pag.estoque/consultaestoque.html')

@app.route('/pag.solicitaçoes/index.html')
def solicitacoes():
    return render_template('/pag.solicitaçoes/index.html')



if __name__ == '__main__':
    app.run( host='0.0.0.0', port=80, debug=True)