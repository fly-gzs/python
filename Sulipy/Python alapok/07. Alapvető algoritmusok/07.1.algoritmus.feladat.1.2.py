'''
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot,
és ezeket tárolja el egy listában! A program adja össze a lista elemeit,
írja ki a képernyőre az összegüket és a lista elemeit!
Módosítsd úgy a fenti programot, hogy a program csak a páros számokat adja össze!
'''
import random
szamlalo = 1
lista = []
lista_paratlan = []
osszeg = 0
while szamlalo <= 5:
    random_szam = random.randint(1,10)
    szamlalo += 1
    lista.append(random_szam)
print(lista)
for szam in lista:
    if szam % 2 == 0:
        osszeg = osszeg + szam
    else:
        lista_paratlan.append(szam)
print('A listában szereplő páratlan számok: ', lista_paratlan)
print('Az 5 db véletlen számban lévő páros számok összege: ', osszeg)
