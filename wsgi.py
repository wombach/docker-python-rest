from m4i_atlas_core import ConfigStore
from m4i_compare import app as compare
from m4i_consistency_metrics import app as consistency_metrics
from m4i_data2model import app as data2model
from m4i_data_governance_dashboard import app as data_governance_dashboard
from m4i_lineage_model import app as lineage_model
from m4i_logging_to_elastic import app as elastic_logging
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from m4i_atlas_config import config
from m4i_elastic_config import config as elastic_config
from flask import Flask

store = ConfigStore.get_instance()
store.load(config)
store.load(elastic_config)

app = Flask("api")

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/data2model': data2model,
    '/consistency_metrics': consistency_metrics,
    '/compare': compare,
    '/lineage_model': lineage_model,
    '/data_governance': data_governance_dashboard,
    '/logging': elastic_logging
})

