import os
import requests

from . import TNYU_API_VERSION

API_URL = "https://api.tnyu.org/"


class TNYUAPI(object):
    api_root = os.path.join(API_URL, TNYU_API_VERSION)

    def __init__(self, host=None, api_key=None):
        self.api_key = api_key or os.getenv('TNYU_API_KEY', '')
        self.api_root = host or self.api_root

    def get_resource(self, resource_name):
        headers = {
            'content-type': 'application/vnd.api+json',
            'accept': 'application/*, text/*',
            'x-api-key': self.api_key
        }

        r = requests.get(
            self.api_root + '/' + resource_name, headers=headers, verify=False)
        return r.json()
