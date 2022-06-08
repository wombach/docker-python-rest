from flask_restful import Resource, abort
from flask_httpauth import MultiAuth, HTTPBasicAuth, HTTPTokenAuth
from tasks import CallElastic
from config import get_config
from flask_apispec.views import MethodResource
from flask_apispec import doc
from api.docs import response_json, response_json_base

# basicAuth = HTTPBasicAuth()
# tokenAuth = HTTPTokenAuth('ApiKey')
# auth = MultiAuth(basicAuth, tokenAuth)
config = get_config()

def get_raw_result(query_result):
    query_result = query_result['hits']['hits']
    document_list = []
    for doc_ in query_result:
        document_list.append(doc_['_source'])
    return document_list

# @basicAuth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    else:
        es = CallElastic(config['ES_URL'], username, password)
    es_auth = es.validate_authentication(config['ES_INDEX'])
    if es_auth:
        return es
    else:
        return False

# @tokenAuth.verify_token
def verify_token(token):
    if token:
        es = CallElastic(config['ES_URL'], token=token)
    es_auth = es.validate_authentication(config['ES_INDEX'])
    if es_auth:
        return es
    else:
        return False
    

class Equipmentlist(MethodResource, Resource):
    @doc(
        description='Equipment properties are provided as a list of all equipment properties that belong to the equipment.', 
        tags=['equipment'],
        summary="Returns a list of all available equipment.",
        security=[{"basicAuth": []}],
        responses={
            200: { "description": "Successful operation", "content": { "application/json": {"schema": {
                  "type": "array",
                  "items": response_json_base
                }}}},
            401: { "description": "Not authorized. Please provide elastic credentials with read access to the equipment index.", "content": {}}
        })
    #@auth.login_required
    def get(self):
        #es = auth.current_user()

        # query_body = {
        #     "size": 5000,
        #     "_source": {
        #         "exclude": [ "properties" ]
        #     },
        #     "query" : {
        #         "match_all": {}
        #     }
        # }

        # es_query = es.search(config['ES_INDEX'], query_body)
        return "OK"
        # return get_raw_result(es_query)

# class Equipment(MethodResource, Resource):
#     @doc(
#         description='Specify the equipment by providing its equipment code. Equipment properties are keyed by their property id.', 
#         tags=['equipment'],
#         summary="Returns a specific equipment and its properties.",
#         security=[{"basicAuth": []}],
#         params = {
#             "eqt_code": {"description": "Unique code that identifies the equipment.", "schema": {"type": "string"}}
#         },
#         responses={
#             200: { "description": "Successful operation", "content": { "application/json": {"schema": response_json}}},
#             401: { "description": "Not authorized. Please provide elastic credentials with read access to the equipment index.", "content": {}},
#             404: { "description": "No equipment was found with the given equipment code.", "content": {}}
#         }
#         )
#     @auth.login_required
#     def get(self, eqt_code):

#         es = auth.current_user()

#         query_body = {
#             "size": 1,
#             "query": {
#                 "match": {
#                     "eqt_code": eqt_code
#                 }
#             }
#         }

#         es_query = es.search(config['ES_INDEX'], query_body)
#         if es_query['hits']['hits']:
#             return get_raw_result(es_query)[0]
#         else:
#             abort(404, message="Equipment code {} doesn't exist".format(eqt_code))
