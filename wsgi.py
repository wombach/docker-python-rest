#from m4i_atlas_core import ConfigStore
# from m4i_compare import app as compare
#from m4i_data2model import app as data2model
# from m4i_lineage_model import app as lineage_model
# from werkzeug.serving import run_simple
# from werkzeug.wsgi import DispatcherMiddleware

# from m4i_atlas_config import config

# application = DispatcherMiddleware(None, {
#     '/data2model': data2model,
#     #'/compare': compare,
#     #'/lineage_model': lineage_model,
# })

# if __name__ == '__main__':
#     store = ConfigStore.get_instance()
#     store.load(config)

#     run_simple(
#         hostname='127.0.0.1',
#         port=5000,
#         application=application,
#         threaded=True
#     )
# # END IF
from app import create_app
app = create_app(metrics=True)