from flask import request, jsonify, abort
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required
from flasgger import swag_from
from datetime import datetime
from controllers import Embrapa
from controllers.login import Login

class LoginResource(Resource):
    @swag_from('specs/login.yml')
    def post(self):
        try:
            username = request.json.get('username', None)
            password = request.json.get('password', None)
            ret = Login().validade_user(username, password) == True
            if ret == True:
                access_token = create_access_token(identity=username)
                return jsonify(access_token=access_token)
            else:
                return {"msg": "Bad username or password"}, 401
        except:
            return {"msg": "Bad username or password"}, 401

class ProductionResource(Resource):
    @jwt_required()
    @swag_from('specs/production.yml')
    def get(self):
        try:
            ano = request.args.get('ano', default=None)
            if ano is None:
                ano = datetime.now().year
            dados = Embrapa().getProductionDados(ano)
            return jsonify([e.serialize() for e in dados])
        except:
            abort(404)


class ProcessamentoResource(Resource):
    @jwt_required()    
    @swag_from('specs/processamento.yml')
    def get(self):
        ano = request.args.get('ano', default=None)
        tipo = request.args.get('tipo', default=None)
        if ano is None:
            ano = datetime.now().year
        if tipo is None:
            tipo = 1
        try:
            tipoAux = int(tipo)
            if tipoAux <= 0 or tipoAux > 4:
                abort(404)
                return
        except:
            abort(404)
        dados = Embrapa().getProcessamentoDados(ano, tipo)
        return jsonify([e.serialize() for e in dados])


class ComercializacaoResource(Resource):
    @jwt_required()
    @swag_from('specs/comercializacao.yml')
    def get(self):
        print("bateu comercializacao")
        try:
            ano = request.args.get('ano', default=None)
            if ano is None:
                ano = datetime.now().year
            dados = Embrapa().getComercializacaoDados(ano)
            if(len(dados)>0):
                print(len(dados))
                out = [e.serialize() for e in dados]
                return jsonify(out)
            return ""
        except:
            abort(404)
class ImportacaoResource(Resource):
    @jwt_required()
    @swag_from('specs/importacao.yml')
    def get(self):
        ano = request.args.get('ano', default=None)
        tipo = request.args.get('tipo', default=None)
        if ano is None:
            ano = datetime.now().year
        if tipo is None:
            tipo = 1
        try:
            tipoAux = int(tipo)
            if tipoAux <= 0 or tipoAux > 4:
                abort(404)
                return
        except:
            abort(404)
        dados = Embrapa().getImportacaoDados(ano, tipo)
        return jsonify([e.serialize() for e in dados])

class ExportacaoResource(Resource):
    @jwt_required()
    @swag_from('specs/exportacao.yml')
    def get(self):
        ano = request.args.get('ano', default=None)
        tipo = request.args.get('tipo', default=None)
        if ano is None:
            ano = datetime.now().year
        if tipo is None:
            tipo = 1
        try:
            tipoAux = int(tipo)
            if tipoAux <= 0 or tipoAux > 4:
                abort(404)
                return
        except:
            abort(404)
        dados = Embrapa().getExportacaoDados(ano, tipo)
        return jsonify([e.serialize() for e in dados])
