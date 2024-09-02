'''
Készíts egy programot, amely a RandomUser API felhasználásával véletlenszerűen megjelenít egy nevet,
és a felhasználónak ki kell találnia, hogy férfiről vagy nőröl van-e szó.
A program természetesen értékelje a választ!
'''


import requests
from pprint import pprint


url = 'https://randomuser.me/api/'
resp = requests.get(url)
name = resp.json()['results']
print(f"{name[0]['name']['title']} {name[0]['name']['first']} {name[0]['name']['last']}")
gender = name[0]['gender']
print(gender)

print('---')
print(f"A véletlen generátor a következő keresznevet adja: {name[0]['name']['first']}")
gender_tipp = input('Tippeld meg a személy nemét! ')
if gender_tipp == 'férfi':
    gender_tipp = 'male'
elif gender_tipp == 'nő':
    gender_tipp = 'female'
else:
    print('Hibás tipp!')

print(f'{"Eltaláltad!" if gender_tipp == gender else "Nem talált!"}')




