from flask import Flask, request, jsonify
from flask_cors import CORS
from dbUsuario import dbUser
import time
p = dbUser('postgresql-9732-0.cloudclusters.net','facens','V!ctor01','facensapi')
#import requests
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return 'Facens API Healthy Safe'

@app.route("/login", methods=["POST"])
def login():
    if request.method == 'POST':
        dados = request.get_json()
        print('dados', dados)
        login = dados.get('email')
        senha = dados.get('senha')
        if senha != None and login !=None:
            try:
                res = p.loginUsuario(login,senha)
                usuario = res[0]
                if res != []:
                    return jsonify(
                    {
                        'id':str(usuario[0]),
                    }
                    )
                else:
                    return jsonify({'id':'Login Invalido'})
            except Exception as e:
                return str(e)
        else:
            return jsonify({'erro':'Parametros invalidos'})
    else:
        return jsonify({'aguardando':'Parametros'})

@app.route("/cadastro", methods=["POST"])
def cadastroUsuario():
    dados = request.get_json(force=True)
    nome = dados['nome']
    email = dados['email']
    telefone = dados['telefone']
    empresa = dados['empresa']
    senha = dados['senha']
    print(dados)
    print(nome,email,telefone,empresa,senha)
    try:
        findEmail = p.findUsuario_by_EMAIL(email)
        if len(findEmail) == 0:
            p.insertUsuario(nome,email,telefone,empresa,senha)
            time.sleep(5)
            res = p.findUsuario_by_EMAIL(email)
            iD = res[0]
            return jsonify({'mensagem':'Cadastro feito com sucesso','id':str(iD[0])})
        else:
            return jsonify({'mensagem':'Email ja em uso'})
    except Exception as e:
        print(e)
        return jsonify({'erro':e})

if __name__ == '__main__':
  app.run(debug=True)
