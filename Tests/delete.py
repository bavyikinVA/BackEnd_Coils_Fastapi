import urllib.request
from utils import config_parser

config = config_parser('../config.txt')
coil_id = 10
url = f'http://{config['SERVER_HOST']}:{config['SERVER_PORT']}/api/coil/{coil_id}'

request = urllib.request.Request(url, method='DELETE')
response = urllib.request.urlopen(request)
print(response.read().decode())
