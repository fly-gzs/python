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

result = genius.album_tracks(185717, per_page=None, page=None, text_format=None)
with open('./adatok/eredmeny_választott_album.json', 'w', encoding='utf-8') as kimenet:
    json.dump(result, kimenet, indent=2)
list = result['tracks']
# pprint(result['sections'][0]['hits'][0]['result']['title_with_featured'])
album_track_list = []
album_track_dict = {}
album_track_dict_list = []
for idx, track in enumerate(list):
    print(idx + 1, track['song']['title_with_featured'])
    album_track_dict['sorszam'] = idx + 1
    album_track_dict['dal'] = track['song']['title_with_featured']
    album_track_dict_list.append(album_track_dict)
    album_track_list.append(track['song']['title_with_featured'])
    album_track_dict = {}
pprint(album_track_list)
pprint(album_track_dict_list)
