'''
Készíts egy programot, amely a RandomUser API felhasználásával véletlenszerűen megjelenít egy nevet,
és a felhasználónak ki kell találnia, hogy férfiről vagy nőröl van-e szó.
A program természetesen értékelje a választ!
'''


import requests
from pprint import pprint

def get_gender(tipp):
    url = 'https://randomuser.me/api/'
    resp = requests.get(url)
    name = resp.json()['results']
    if tipp == 'férfi':
        tipp = 'male'
    elif tipp == 'nő':
        tipp = 'female'
    elif tipp == '':
        first_name = name[0]['name']['first']
    else:
        print('Hibás tipp!')
    print(f"{name[0]['name']['title']} {name[0]['name']['first']} {name[0]['name']['last']}")

    gender = name[0]['gender']
    print(gender)
    if gender == tipp:
        eredmeny = 'OK'
    else:
        eredmeny = 'nem OK'
    return first_name, eredmeny

nev = get_gender('')[0]
print(nev)
gender_tipp = input('Tippeld meg a személy nemét! ')

print(f'{"Eltaláltad!" if get_gender(gender_tipp)[1] == "OK" else "Nem talált!"}')



