import os
import requests

from . import TNYU_API_VERSION
from .serializer import Resource

API_URL = "https://api.tnyu.org/"


class TNYUAPI(object):
    api_root = os.path.join(API_URL, TNYU_API_VERSION)

    def __init__(self, host=None, api_key=None):
        self.api_key = api_key or os.getenv('TNYU_API_KEY', '')
        self.api_root = host or self.api_root
        self.headers = {
            'content-type': 'application/vnd.api+json',
            'accept': 'application/*, text/*',
            'authorization': 'Bearer ' + self.api_key
        }

    def get_resource(self, resource_name):
        r = requests.get(
            self.api_root + '/' + resource_name, headers=self.headers, verify=False)
        return r.json()

    def post_resource(self, resource_name, data):
        r = requests.post(self.api_root + '/' + resource_name,
                          data=data.to_json(), headers=self.headers, verify=False)
        return r.json()
