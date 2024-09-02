'''
A mellékelt fájl néhány sorozat adásba kerülésének dátumát, a sorozat angol címét,
az évadot és az epizód számát, az epizód hosszát percben és egy jelzést tartalmaz,
hogy a lista készítője megnézte-e már azt az epizódot.
Ezek az adatok egymás után külön sorokban szerepelnek.

Készíts egy programot amely beolvassa a fájlban tárolt adatokat egy szótárba.
A szótárnak egyetlen kulcs-érték párja legyen, a kulcs a 'sorozatok' tartalmú sztring,
az ehhez rendelt érték pedig egy lista. Ezen lsitának az elemei legyenek szótárak,
amelyek tartalmazzák az egyes epizódokra vonatkozó adatokat az alábbiak szerint.
A program a beolvasott, majd szótár típusba mentett adatokat írja ki egy JSON fájlba!
'''


from pprint import pprint
from pprint import pformat

szotar = {}
filmlista = []
with open('./adatok/lista.txt', encoding='utf-8') as forrasfajl:
    sorok = forrasfajl.readlines()

teljes_lista = []
for i in range(0,len(sorok),5):
    elem = {
        'datum': sorok[i].strip(),
        'sorozat': sorok[i+1].strip(),
        'epizod': sorok[i+2].strip(),
        'hossz': sorok[i+3].strip(),
    }
    if sorok[i+4].strip() == '1':
        elem['latta'] = True
    else:
        elem['latta'] = False

    teljes_lista.append(elem)

print(teljes_lista)
print(len(teljes_lista))

y =[]
x = 0
while x < len(teljes_lista):
    if teljes_lista[x]['latta'] == True:
        y.append(x)
        x += 1
    else:
        x += 1

print(teljes_lista)
print(len(teljes_lista))


szoveg = pformat(teljes_lista, sort_dicts = False)
eltavolitando_karakterek = [' [','[',']','{','}',"'"]
for karakter in eltavolitando_karakterek:
    szoveg = szoveg.replace(karakter, "")
# print(szoveg)
with open('../adatok/modosított_lista.txt', 'w', encoding='utf-8') as celfajl:
    print(szoveg, file=celfajl)
