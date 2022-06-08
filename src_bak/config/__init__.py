import os, json, sys

def open_json(filename):
    try:
        filename=json.load(open(filename))
        return filename
    except Exception as e:
        return None

def lookup_env(config):
    for key, value in config.items():
        if value is None:
            env_value = os.getenv(key)
            if env_value:
                config[key] = env_value
            else:
                print('[ERROR] Missing config parameter:', key)
                sys.exit(4)

    return config

def get_config(filename='config.json'):
    config_list = { 'ES_URL' : None, 'ES_INDEX' : None, }
    json = open_json(filename)

    if json is not None:
        config_list = dict(list(config_list.items()) + list(json.items()))

    # lookup variables in envirement if not found in jsonfile
    if None in config_list.values():
        config_list = lookup_env(config_list)

    return config_list