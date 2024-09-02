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
genius = lyricsgenius.Genius(os.getenv('GENIUS_TOKEN'), verbose=False)

result = genius.search_song(title='Rio', artist='Tankcsapda',
                            get_full_info=False)

print(result.lyrics)

