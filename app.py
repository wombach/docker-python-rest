from flask import Flask, Blueprint
from flask_restful import Api
from api import controllers
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from prometheus_flask_exporter import RESTfulPrometheusMetrics
from flask_restful import Resource, abort
from flask_apispec.views import MethodResource
from flask_apispec import doc

def create_app(metrics):
    app = Flask(__name__) 
    api = Api(app, prefix='/api/v1')

    # node exporter, metrics
    if metrics:
        metrics = RESTfulPrometheusMetrics(app, api, excluded_paths=["^(?:(?!\/api\/v1\/.*).)*$"])

    # swagger
    spec = APISpec(
      title='DMP Equipment',
      info=dict(description='This is an API for retrieving equipment information from the Van Oord Data Management Platform'),
      version='1.0.3',
      plugins=[MarshmallowPlugin()],
      openapi_version='3.0.2'
    )

    authSchema = {"type": "http", "scheme": "basic"}
    spec.components.security_scheme("basicAuth", authSchema)
    api_key_scheme = {"type": "apiKey", "in": "header", "name": "X-API-Key"}
    spec.components.security_scheme("ApiKeyAuth", api_key_scheme)

    app.config.update({
        'APISPEC_SPEC': spec,
        'APISPEC_SWAGGER_URL': '/api/v1/',  # URI to access API Doc JSON 
        'APISPEC_SWAGGER_UI_URL': '/'  # URI to access UI of API Doc
    })

    docs = FlaskApiSpec(app)

    # endpoints
    api.add_resource(controllers.Equipmentlist, '/equipment')
    docs.register(controllers.Equipmentlist)
    # api.add_resource(controllers.Equipment, '/equipment/<string:eqt_code>')
    # docs.register(controllers.Equipment)

    return app

if __name__ == '__main__':
    app = create_app(metrics=True)
    app.run(host='0.0.0.0', port=5000)
