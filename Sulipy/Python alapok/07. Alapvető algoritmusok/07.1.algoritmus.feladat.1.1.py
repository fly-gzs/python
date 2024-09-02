'''
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot,
és ezeket tárolja el egy listában! A program adja össze a lista elemeit,
írja ki a képernyőre az összegüket és a lista elemeit!
'''
import random
szamlalo = 1
lista = []
osszeg = 0
while szamlalo <= 5:
    random_szam = random.randint(1,10)
    szamlalo += 1
    lista.append(random_szam)
print(lista)
for szam in lista:
    osszeg = osszeg + szam
print('Az 5 db véletlen szám összege: ', osszeg)
