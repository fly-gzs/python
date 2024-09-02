'''
Készíts egy programot, amely a felhasználótól bekér egy angol szót, és annak megfelelő tartalmú viccet jelenít meg.
Amennyiben több megfelelő vicc is elérhető, akkor ezek közül véletlenszerűen választ egyet.
Ha nincs a megadott kifejezésnek megfelelő vicc, akkor ezt jelzi a felhasználónak, de megjelenít egy tetszőleges viccet.
'''


import requests
import random

word = input('Adj meg egy angol szót! ')
headers = {
  "Accept": "application/json"
}
url = "https://icanhazdadjoke.com/search"
payload = {'term': word}
try:
  resp = requests.get(url, headers = headers, params=payload)
  joke_list = resp.json()['results']
  random_joke = random.choice(joke_list)
  joke = random_joke['joke']
  print(f'Itt egy vicc a "{word}" szónak megfelelő tartalommal: \n{joke}')
except:
  print('Nincs a megadott kifejezésnek megfelelő vicc!')


#szo = joke(input('Adj meg egy angol szót! '))