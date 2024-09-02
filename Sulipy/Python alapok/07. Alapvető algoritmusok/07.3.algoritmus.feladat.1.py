'''
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot
és ezeket tárolja el egy listában! A program számolja össze,
és képernyőre írja ki a listában tárolt páros számok számát, valamint a lista elemeit!
'''
import random
db = 0
szamlalo = 0
lista = []
paros = []
while db < 5:
    szam = random.randint(1,10)
    if szam % 2 == 0:
        paros.append(szam)
        szamlalo += 1
    lista.append(szam)
    db += 1
#     print(szam)
print('A véletlen számok listája: ', lista)
# print(paros)
print(f'A véletlen számok között {szamlalo} db páros szám van: ', paros)