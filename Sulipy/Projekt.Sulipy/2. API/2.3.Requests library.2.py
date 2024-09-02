'''
A program írja ki képernyőre, hogy a SuliPY oldal mikor frissült utoljára!
Tipp: Ez az információ is a response header részében található.
'''

import requests
from pprint import pprint

# A cél URL
url = "https://sulipy.hu/"

# GET kérés küldése az oldalra
response = requests.get(url)

# A "Last-Modified" header értékének kiolvasása
last_modified = response.headers.get('Last-Modified')
print(response.text)

if last_modified:
    print(f"Az oldal utoljára frissítve: {last_modified}")
else:
    print("Nem található 'Last-Modified' header az oldal válaszában.")


