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
------------- 1. feladat -------------
A legöregebb autó: JTZ-774, Ford Fiesta, 25 éves.
'''
print('------------- 1. feladat -------------')
max_index = 0
max_kor = autok[0]['kor']
for index, kocsi in enumerate(autok):
    if kocsi['kor'] > max_kor:
        max_kor = kocsi['kor']
        max_index = index
print(f"A legöregebb autó: {autok[max_index]['rendszam']}, {autok[max_index]['marka']} {autok[max_index]['tipus']}, {autok[max_index]['kor']} éves")

# {max_kor} év, neve: {diakok[max_index]['vezeteknev']} {diakok[max_index]['keresztnev']}")
