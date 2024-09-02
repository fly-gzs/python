'''
A program generáljon 10 darab véletlenszámot [0;50] intervallumon, de csak a 4-gyel oszthatóakat rögzítse egy listában.
A végén jelenítse meg a listát a képernyőn, és írja ki azt is, hány elemből áll a lista.
'''

import random

lista_all = []
lista4 = []
# random_szam = random.randint(0, 50)
szamlalo = 1
while szamlalo <= 10:
    random_szam = random.randint(0, 50)
    lista_all.append(random_szam)
    if random_szam % 4 == 0:
         lista4.append(random_szam)
    szamlalo += 1
print(lista_all)
print('A lista a következő számokat tarlamazza:', lista4)
print('A listában ' + str(len(lista4)) + ' db 4-gyel osztható szám található.')