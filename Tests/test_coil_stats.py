import urllib.parse
import urllib.request
import json
from utils import config_parser

config = config_parser('../config.txt')

base_url = f'http://{config['SERVER_HOST']}:{config['SERVER_PORT']}/api/coil/stats'

params = {'date_start': '2024-05-20', 'date_end': '2024-05-21'}

query_string = urllib.parse.urlencode(params)

url = base_url + '?' + query_string

response = urllib.request.urlopen(url)

data = response.read()

json_data = json.loads(data)

print(json_data)
