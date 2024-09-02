'''
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát, 
és másold át azt egy fájlba úgy, hogy abba már csak a nyelv és az évszám kerüljön!
'''
from pprint import pprint
from pprint import pformat

lista = []
x = 0
with open('./adatok/Timeline.txt', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        lista.append(adatok)
        del lista[x][2:4]
        x += 1

print(f'{lista}')
szoveg = pformat(lista, sort_dicts = False)
eltavolitando_karakterek = [' [','[',']','{','}',"'"]
for karakter in eltavolitando_karakterek:
    szoveg = szoveg.replace(karakter, "")
print(szoveg)
with open('./adatok/Timeline_masolat.txt', 'w', encoding='utf-8') as celfajl:
    print(szoveg, file=celfajl)