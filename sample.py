from pytnyu import TNYUAPI

if __name__ == '__main__':
    api = TNYUAPI()
    print api.get_resource('events')
