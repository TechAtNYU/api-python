import os

from pytnyu import TNYU_API_VERSION

class TNYUAPI(object):
    API_ROOT = os.path.join('https://api.tnyu.org/', TNYU_API_VERSION)
    def __init__(self, host=None, api_key=None):
        self.api_key = api_key or os.getenv('TNYU_API_KEY', '')
        self.api_root = host or self.API_ROOT
    def get_resource(self, resource_name):
        headers = {
            'content-type': 'application/vnd.api+json',
            'accept': 'application/*, text/*',
            'x-api-key': self.api_root
            }
        r = requests.get(self.api_root + '/' + resource_name, headers=headers, verify=False)
        return json.loads(r.text)
