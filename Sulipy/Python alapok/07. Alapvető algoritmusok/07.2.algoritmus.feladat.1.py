'''
Írj egy programot, amely 5 darab véletlenszámot generál [1;7] intervallumon,
és ezeket eltárolja egy listában. Kérjen be a felhasználótól egy számot,
és vizsgálja meg, hogy ez előfordul-e a listában!
Az eredményről tájékoztassa a felhasználót, és írja ki a lista elemeit a képernyőre!
'''

import random
szamlalo =1
lista = []
while szamlalo <= 5:
    random_szam = random.randint(1,7)
#     print(random_szam)
    lista.append(random_szam)
    szamlalo += 1
print(lista)
talalat = False
index = 0
szam = int(input('Adj meg egy számot: '))
while index < 5 and not talalat:
    if lista[index] == szam:
        talalat = True
    index += 1
if talalat:
    print('A megadott szám (' + str(szam) + ') szerepel a listában!')
else:
    print('A megadott szám (' + str(szam) + ') NEM szerepel a listában!')

    
    