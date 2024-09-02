'''
Készíts egy programot, amely megkérdezi a felhasználó kedvenc előadójának a nevét,
a Genius API felhasználásával letötli az előadó albumainak címeit, amelyből a felhasználó választ egyet!
A megadott album egy véletlenszerűen kiválasztott számának a szövegét a program megjeleníti a képernyőn,
és a felhasználónak kell kitalálnia ennek a számnak a címét!
'''


import os
import lyricsgenius
import json
import random

band = input('Melyik a kedvenc rock/metal zenekarod? ')
# os.getenv(): a környezeti változó értékének kiolvasása
genius = lyricsgenius.Genius(os.getenv('GENIUS_TOKEN'), verbose=False)

result = genius.search_albums(band, per_page=49, page=None)
with open('./adatok/eredmeny_albumok.json', 'w') as kimenet:
    json.dump(result, kimenet, indent=2)
lista = result['sections'][0]['hits']

print('---')
print(f'Kilistázom neked a {band} albumait.')
all_albums_list = []
all_albums_id_list = []
for idx, album in enumerate(lista):
    print(idx + 1, album['result']['name'], album['result']['id'])
    all_albums_list.append(album['result']['name'])
    all_albums_id_list.append(album['result']['id'])

print('---')
favorite_album = int(input(f'Melyik a kedvenc albumod a {band} zenekertól? Add meg a sorszámát! '))
favorite_id = all_albums_id_list[favorite_album-1]

result = genius.album_tracks(favorite_id, per_page=None, page=None, text_format=None)
with open('./adatok/eredmeny_választott_album.json', 'w', encoding='utf-8') as kimenet:
    json.dump(result, kimenet, indent=2)
list = result['tracks']

album_track_list = []
print('---')
print(f'A kedvenc albumodon ({all_albums_list[favorite_album-1]}) a következő dalok vannak!')
for idx, track in enumerate(list):
    print(idx + 1, track['song']['title_with_featured'])
    album_track_list.append(track['song']['title_with_featured'])

random_track = random.choice(album_track_list)
print('---')
print(f'Véletlenszerűen választok neked egy dalt a(z) {all_albums_list[favorite_album-1]} albumról: {random_track}')
print('---')
print(f'A(z) {random_track} dal szövege:')

result = genius.search_song(title=random_track, artist=band,
                            get_full_info=False)
print(result.lyrics)

