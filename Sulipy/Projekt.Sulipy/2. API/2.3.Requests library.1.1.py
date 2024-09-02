'''
Készíts egy programot, amely az Universities API felhasználásával megjeleníti a felhasználó által megadott
országban található egyetemek nevét és honalapcímét!
'''

import requests
from pprint import pprint

country = input('Add meg az országot! ')
URL = 'http://universities.hipolabs.com/search'
payload = {'country': country, 'name': 'pécs'}

resp = requests.get(URL, params=payload)
egyetemek = resp.json()

for egyetem in egyetemek:
    pprint(egyetem)
    pprint(egyetem['name'])
    pprint(egyetem['web_pages'])
# print(resp)