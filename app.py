from flask import Flask,request, jsonify,abort
from datetime import datetime
from getDataFromEmbrapa import getProductionDados,getProcessamentoDados,getComercializacaoDados,getImportacaoDados
import sys, asyncio

if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = Flask(__name__)


@app.route('/producao')
async def getProduction():
    ano = request.args.get('ano', default=None)
    if ano is None:
        ano=datetime.now().year
    
    dados = getProductionDados(ano)

    return jsonify([e.serialize() for e in dados])

@app.route('/processamento')
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
    
    dados = getProcessamentoDados(ano,tipo)

    return jsonify([e.serialize() for e in dados])


@app.route('/comercializacao')
async def getComercializacao():
    ano = request.args.get('ano', default=None)
    if ano is None:
        ano=datetime.now().year

    dados = getComercializacaoDados(ano)

    return jsonify([e.serialize() for e in dados])


@app.route('/importacao')
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
    
    dados = getImportacaoDados(ano,tipo)

    return jsonify([e.serialize() for e in dados])


