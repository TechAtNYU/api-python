from pytnyu import TNYU_API_VERSION

class TNYUAPI(object):
    API_ROOT = os.path.join('https://api.tnyu.org/', TNYU_API_VERSION)
    def __init__(self, auth=None, host=None):
        print API_ROOT