import os
import lyricsgenius

# os.getenv(): a környezeti változó értékének kiolvasása
genius = lyricsgenius.Genius(os.getenv('GENIUS_TOKEN'), verbose=True)

result = genius.search_song(title='Alive', artist='Snak The Ripper',
                            get_full_info=False)

print(type(result))
print(result.to_dict()['lyrics'])
