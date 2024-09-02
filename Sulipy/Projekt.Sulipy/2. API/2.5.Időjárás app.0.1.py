import requests
from pprint import pprint

API_KEY = '87f63b2c81f27ab2a23ce00e97a37557'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

payload = {'lat': 35, 'lon': 139, 'appid': API_KEY}
resp = requests.get(API_URL, params=payload)
resp = resp.json()
pprint(resp)