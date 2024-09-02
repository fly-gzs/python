import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Kedvelt dalok listájának lekérése
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

# Felhasználói adatok lekérése
user = sp.current_user()
pprint(user)
