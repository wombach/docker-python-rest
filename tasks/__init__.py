from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from ssl import create_default_context
import sys, os

class CallElastic:
    def __init__(self, url=None, username=None, password=None, token=None, ca=None):
        self.url = url
        self.username = username
        self.password = password
        self.token = token
        self.ca = ca

        try:
            if self.username and self.ca:
                if not os.path.isfile(self.ca):
                    print ("[WARN] cafile not found:", self.ca)
                    sys.exit(4)
                else:    
                    context = create_default_context(cafile=self.ca)
                    es = Elasticsearch(self.url, ssl_context=context, http_auth=(self.username, self.password))
            elif self.username and not self.ca:
                es = Elasticsearch(self.url, http_auth=(self.username, self.password))
            elif self.token:
                es = Elasticsearch(self.url, api_key=self.token)
            self.es = es

        except Exception as e:
            print("[ERROR] Could not connect to:", self.url,  e)
            sys.exit(4)

    def validate_authentication(self, searchindex):
            try:
                self.es.search(index=searchindex)
                return True
            except Exception as e:
                print("[ERROR] Could not connect to:", self.url,  e)
                return False

    def search(self, searchindex, query=None):
        esquery = self.es.search(
            index=searchindex,
            body=query
        )
        return esquery
