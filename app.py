from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flasgger import Swagger
import sys, asyncio

from resources import LoginResource, ProductionResource, ProcessamentoResource, ComercializacaoResource, ImportacaoResource, ExportacaoResource

if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = Flask(__name__)
app.config.from_object('config.Config')

jwt = JWTManager(app)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "TECH Changeler G10",
        "description": "API de consulta EMBRAPA",
        "version": "1.0.0"
    },
    "host": "localhost:5000",
    "basePath": "/",
    "schemes": [
        "http"
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        }
    },
}



swagger = Swagger(app, template=swagger_template)
#swagger = Swagger(app)




api = Api(app)
api.add_resource(LoginResource, '/login')
api.add_resource(ProductionResource, '/producao')
api.add_resource(ProcessamentoResource, '/processamento')
api.add_resource(ComercializacaoResource, '/comercializacao')
api.add_resource(ImportacaoResource, '/importacao')
api.add_resource(ExportacaoResource, '/exportacao')

if __name__ == '__main__':
    app.run(debug=True)