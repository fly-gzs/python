'''
Készíts egy listát amely 8 diák adatait tartalmazza.
A lista elemei szótárak legyenek, egy-egy szótár egy-egy diák adatait tárolja.
A szótárban lévő kulcsok és a hozzájuk tartozó értékek:
"név": a vezeteknevek és a keresztnevek nevű listából véletlenszerűen választott és párosított elemek
"életkor": véletlenszám [14;19] intervallumban
"évfolyam": véletlenszám [9;12] intervallumban
"osztály": A, B, C vagy D lehet
"cím": beágyazott szótár melynek kulcsai:
"település": telepulesek nevű listából véletlenszerűen választva
"utca": utcak nevű listából véletlenszerűen választva
"házszám": véletlenszám [1;50] intervallumban
'''
vezeteknevek = ["Kiss", "Horváth", "Szabó", "Pethő", "Szalai", "Nagy"]
keresztnevek = ["Petra", "Ádám", "Levente", "Zoé", "Hanna" ]
telepulesek = ["Sopron", "Fertőszentmiklós", "Harka", "Kópháza", "Fertőd", "Újkér" ]
utcak = ["Fő", "Kossuth", "Győri", "Petőfi", "Vadvirág", "Iskola"]
osztaly = ['A','B','C','D']

from pprint import pprint
from pprint import pformat
import random
diak = {}
cim = {}
lista = []
szamlalo = 1
while szamlalo <= 8:
    nev = random.choice(vezeteknevek) + ' ' + random.choice(keresztnevek)
    diak['Név'] = nev
    diak['Kor'] = random.randint(14,19)
    diak['Évfolyam'] = random.randint(9,12)
    diak['Osztály'] = random.choice(osztaly)
    cim['Település']  = random.choice(telepulesek)
    cim['Utca']  = random.choice(utcak)
    cim['Házszám']  = random.randint(1,50)
    diak['Cím'] = cim
    lista.append(diak)
    diak = {}
    cim = {}
    szamlalo += 1
#     print(diak)
pprint(lista, depth = 4, indent = 3, sort_dicts = False)

# szoveg = pformat(lista,  sort_dicts = False)
# eltavolitando_karakterek = ['[',']','{','}',"'"]
# for karakter in eltavolitando_karakterek:
#     szoveg = szoveg.replace(karakter, "")
# print(szoveg)
    