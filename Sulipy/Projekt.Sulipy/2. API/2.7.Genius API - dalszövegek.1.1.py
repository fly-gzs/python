'''
Készíts egy programot, amely megkérdezi a felhasználó kedvenc előadójának a nevét,
a Genius API felhasználásával letötli az előadó albumainak címeit, amelyből a felhasználó választ egyet!
A megadott album egy véletlenszerűen kiválasztott számának a szövegét a program megjeleníti a képernyőn,
és a felhasználónak kell kitalálnia ennek a számnak a címét!
'''


import os
import lyricsgenius
from pprint import pprint
import json

# os.getenv(): a környezeti változó értékének kiolvasása
genius = lyricsgenius.Genius(os.getenv('GENIUS_TOKEN'), verbose=True)

all_albums_list = []
all_albums_id_list = []
x = 0
szamlalo = 1
if x != None:
    result = genius.search_albums('Tankcsapda',per_page=49, page=szamlalo)
    with open('./adatok/eredmeny_albumok.json', 'w') as kimenet:
        json.dump(result, kimenet, indent=2)

    list1 = result['sections'][0]['hits']
    szamlalo += 1
    x = result['next_page']
    print(x)

    for idx, album in enumerate(list1):
        # print(idx + 1, album['result']['name'], album['result']['id'])

        all_albums_list.append(album['result']['name'])
        all_albums_id_list.append(album['result']['id'])
print(all_albums_list)
print(len(all_albums_list))
print(all_albums_id_list)
print(len(all_albums_id_list))
for idx, album1 in enumerate(all_albums_list):
    print(idx + 1, album1, album['result']['id'])