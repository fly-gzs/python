from lyricsgenius import Genius
import os                               # Nem kell telepíteni, része a standard library.nak
from pprint import pprint


# genius = Genius(os.getenv('GENIUS_TOKEN'))
genius = Genius(os.getenv('GENIUS_TOKEN'), verbose=False)
artist = genius.search_artist("Led Zeppelin", max_songs=3, sort="title")
pprint(artist.to_dict())

