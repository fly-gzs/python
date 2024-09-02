from lyricsgenius import Genius
import os                               # Nem kell telepíteni, része a standard library.nak

genius = Genius(os.getenv('GENIUS_TOKEN'), verbose=False)
artist = genius.search_artist("Black Sabbath", max_songs=10)
# artist = genius.search_artist("Led Zeppelin", max_songs=3, sort="title")
print(artist.songs)

