import urllib.request
import json
from utils import config_parser

config = config_parser('config.txt')

url = f'http://{config['SERVER_HOST']}:{config['SERVER_PORT']}/api/coil'
headers = {'Content-Type': 'application/json'}
data = {'length': 50, 'weight': 12300}
data_json = json.dumps(data)
data_bytes = data_json.encode('utf-8')
request = urllib.request.Request(url, data=data_bytes, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode())
