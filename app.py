from flask import Flask,request, jsonify
from datetime import datetime
from getDataFromEmbrapa import getProductionDados
import sys, asyncio

if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = Flask(__name__)


@app.route('/production')
async def getProduction():
    ano = request.args.get('ano', default=None)
    if ano is None:
        ano=datetime.now().year
    
    dados = getProductionDados(ano)

    return jsonify(eqtls=[e.serialize() for e in dados])