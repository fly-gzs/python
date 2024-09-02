'''
A program generáljon 10 darab véletlenszámot [1;3] intervallumon,
ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre!
A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon,
és a program törölje ennek a számnak valamennyi előfordulását a listából,
majd írja ki a módosított listát a képernyőre!
'''
import random

lista = []
szamlalo = 1
szamlalo2 = 1
while szamlalo <= 10:
    random_szam = random.randint(1, 3)
    lista.append(random_szam)
    szamlalo += 1
#     print(random_szam)
delete_lista = lista.copy()
print(lista)
szam = int(input('Adj meg egy számot [1;3] intervallumon belül: '))
# print(delete_lista)
db = delete_lista.count(szam)
print('A listában ' + str(delete_lista.count(szam)) + ' db "' + str(szam) + '" szám található.')
while szamlalo2 <= db:
    delete_lista.remove(szam)
    szamlalo2 += 1
print('A listából kivettük a megadott "' + str(szam) + '" számokat.')
print('A lista maradék elemei: ', delete_lista)
    