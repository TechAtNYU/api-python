from pytnyu import TNYUAPI

if __name__ == '__main__':
    api = TNYUAPI()
    events = api.get_resource('events')
