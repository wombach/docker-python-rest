from elasticsearch import Elasticsearch
from flask import Flask
from m4i_atlas_core import ConfigStore
from m4i_backend_core.auth import requires_auth

app = Flask(__name__)

store = ConfigStore.get_instance()


def write_to_elastic(index_name: str, message: dict):
    username, password, url_with_port = store.get_many('elastic_username', 'elastic_password', 'elastic_host')
    connection = Elasticsearch(
        url_with_port,
        basic_auth=(username, password),
        # verify_certs=False
    )
    response = connection.index(index=index_name, document=message)
    return response


@app.route('/log', methods=['POST'])
@requires_auth(transparent=True)
def logging_to_elastic(message, access_token=None):
    """
    This is the endpoint /log which is used to push logs to elastic index "atlas-logging".
    For the frontend the path will be /repository/api/log.

    :param message: The message or log to be pushed
    :param access_token: the bearer token of the frontend used to verify where this request is coming from.
    :return: The elastic api response.
    """
    index_name: str = 'atlas-logging'
    response = write_to_elastic(index_name, message)

    return 200, response
# END logging_to_elastic
