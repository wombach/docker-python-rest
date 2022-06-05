from flask import Flask, Blueprint
from flask_restful import Api
#from api import controllers
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from prometheus_flask_exporter import RESTfulPrometheusMetrics
from flask_restful import Resource, abort
from flask_apispec.views import MethodResource
from flask_apispec import doc


class Equipmentlist(MethodResource, Resource):
    @doc(
        description='Equipment properties are provided as a list of all equipment properties that belong to the equipment.', 
        tags=['equipment'],
        summary="Returns a list of all available equipment.",
        security=[{"basicAuth": []}],
        responses={
            200: { "description": "Successful operation", "content": { "application/json": {"schema": {
                  "type": "array"
                }}}},
            401: { "description": "Not authorized. Please provide elastic credentials with read access to the equipment index.", "content": {}}
        })
    def get(self):
        es = auth.current_user()

        query_body = {
            "size": 5000,
            "_source": {
                "exclude": [ "properties" ]
            },
            "query" : {
                "match_all": {}
            }
        }

        #es_query = es.search(config['ES_INDEX'], query_body)
        return "OK"

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
    api.add_resource(Equipmentlist, '/equipment')
    docs.register(Equipmentlist)
    # api.add_resource(controllers.Equipment, '/equipment/<string:eqt_code>')
    # docs.register(controllers.Equipment)

    return app

if __name__ == '__main__':
    app = create_app(metrics=True)
    app.run(host='0.0.0.0', port=5000)
