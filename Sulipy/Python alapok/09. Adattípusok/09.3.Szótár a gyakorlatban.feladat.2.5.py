'''
Az adatok beolvasása fájlból,
egy-egy sor az 'adatok' nevű lista egy-egy eleme
'''
adatok = []
with open('autok_listaja.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        # strip() metódus eltávolítja a sorvégi \n-t
        adatok.append(sor.strip())


'''
A 'autok' nevű lista 'auto' nevű szótár típusokat fog tartalmazni,
egy autó adatait egy szótár tárolja
'''
auto = {}  # egy auto adatai
autok = []  # szótárakat tartalmazó lista
for elem in adatok:
    auto_adatai = elem.split()
    auto['rendszam'] = auto_adatai[0]
    auto['marka'] = auto_adatai[1]
    auto['tipus'] = auto_adatai[2]
    auto['kor'] = int(auto_adatai[3])
    if auto_adatai[4] == '1':
        auto['javitva'] = True
    else:
        auto['javitva'] = False
    auto['koltseg'] = int(auto_adatai[5])

    autok.append(auto)
    auto = {}  # egy új, üres szótár objektum deklarálása ugyanazon a néven

print(autok)

'''
------------- 5. feladat -------------
Adjon meg egy betűt!    X
A megadott betű az alábbi autók márka- vagy típusmegnevezésében fordul elő:
Ford C-Max
'''
print('------------- 5. feladat -------------')
betu = input('Adj meg egy betűt: ')
lista = []
car = {}
print('A megadott betű az alábbi autók márka- vagy típusmegnevezésében fordul elő:')
for kocsi in autok:
    for karakter in kocsi['marka']:
        if karakter == betu:
            car['marka'] = kocsi['marka']
            car['tipus'] = kocsi['tipus']
            kiiras = ""
            for ertek in car.values():
                kiiras += ertek + " "
            print(kiiras)



