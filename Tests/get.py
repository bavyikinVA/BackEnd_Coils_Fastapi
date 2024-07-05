import urllib.request
from utils import config_parser

config = config_parser('../config.txt')

url = f'http://{config['SERVER_HOST']}:{config['SERVER_PORT']}/api/coil?id_min=3&id_max=15'

headers = {'Content-Type': 'application/json'}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode())
