from flask import Flask,request, jsonify,abort
from datetime import datetime
from controllers import Embrapa
import sys, asyncio
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from controllers.login import Login


if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = Flask(__name__)

app.config.from_object('config.Config')

jwt = JWTManager(app)


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    result = Login().validade_user(username,password)

    if(result == True):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Bad username or password"}), 401



@app.route('/producao')
@jwt_required()
async def getProduction():
    ano = request.args.get('ano', default=None)
    if ano is None:
        ano=datetime.now().year
    
    dados = Embrapa().getProductionDados(ano)

    return jsonify([e.serialize() for e in dados])

@app.route('/processamento')
@jwt_required()
async def getProcessamento():
    ano = request.args.get('ano', default=None)
    tipo = request.args.get('tipo', default=None)   
    if ano is None:
        ano=datetime.now().year

    if tipo is None:
        tipo=1
    
    try:
        tipoAux=int(tipo)
        if(tipoAux<=0 or tipoAux>4):
            abort(404)
            return
    except:
        abort(404)
    
    dados = Embrapa().getProcessamentoDados(ano,tipo)

    return jsonify([e.serialize() for e in dados])


@app.route('/comercializacao')
@jwt_required()
async def getComercializacao():
    ano = request.args.get('ano', default=None)
    if ano is None:
        ano=datetime.now().year

    dados = Embrapa().getComercializacaoDados(ano)

    return jsonify([e.serialize() for e in dados])


@app.route('/importacao')
@jwt_required()
async def getImportacao():
    ano = request.args.get('ano', default=None)
    tipo = request.args.get('tipo', default=None)   
    if ano is None:
        ano=datetime.now().year

    if tipo is None:
        tipo=1
    
    try:
        tipoAux=int(tipo)
        if(tipoAux<=0 or tipoAux>4):
            abort(404)
            return
    except:
        abort(404)
    
    dados = Embrapa().getImportacaoDados(ano,tipo)

    return jsonify([e.serialize() for e in dados])

@app.route('/exportacao')
@jwt_required()
async def getExportacao():
    ano = request.args.get('ano', default=None)
    tipo = request.args.get('tipo', default=None)   
    if ano is None:
        ano=datetime.now().year

    if tipo is None:
        tipo=1
    
    try:
        tipoAux=int(tipo)
        if(tipoAux<=0 or tipoAux>4):
            abort(404)
            return
    except:
        abort(404)
    
    dados = Embrapa().getExportacaoDados(ano,tipo)

    return jsonify([e.serialize() for e in dados])


if __name__ == '__main__':
    app.run()
