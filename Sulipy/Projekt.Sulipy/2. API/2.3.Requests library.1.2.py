'''
Készíts egy programot, amely az Universities API felhasználásával megjeleníti a felhasználó által megadott
országban található egyetemek nevét és honalapcímét!
Egészítsd ki a fenti programot úgy, hogy a felhasználó megadhasson egy országot vagy egy nevet,
de akár egyszerre mindkettőt is, és ennek megfelelő egyetemek neve, és országa kerüljön kilistázásra!
A felhaszanálónak többször is legyen lehetősége lekérdezésre!
'''

import requests
from pprint import pprint

country = 'Hungary'
while country != '':
    country = input('Add meg az országot! ')
    name = input('Add meg a nevet! ')
    URL = 'http://universities.hipolabs.com/search'
    payload = {'country': country, 'name': name}

    resp = requests.get(URL, params=payload)
    egyetemek = resp.json()

    if country != '':
        for egyetem in egyetemek:
            pprint(egyetem['name'])
            pprint(egyetem['country'])
    else:
        print('Vége!')
