import random
from pprint import pprint
from pprint import pformat
import datetime


lotto_halmaz = set()
lista = []
szamlalo = 0
while szamlalo < 5:
    while len(lotto_halmaz) < 5:
        veletlen_szam = random.randint(1,90)
        lista.append(veletlen_szam)
        lotto_halmaz.add(veletlen_szam)
    szamlalo += 1
    lista.sort()
    print(f'--- {szamlalo}. jaték ---')
    print('Rendezett lista: ', lista)
    print('A generált számok mennyisége: ' + str(len(lista)) + ' db.')
    print('Eredeti halmaz: ', lotto_halmaz)
    lotto = sorted(lotto_halmaz)
    print('A véletlen lottószámok növekvő sorrendben: ', lotto)
    datum = datetime.datetime.now()
    print(datum)
    szoveg = pformat(lotto, sort_dicts=False)
    eltavolitando_karakterek = [' [', '[', ']', '{', '}', "'"]
    for karakter in eltavolitando_karakterek:
        szoveg = szoveg.replace(karakter, "")
    print(szoveg)

    with open('../adatok/lotto.txt', 'a', encoding='utf-8') as celfajl:
        print(f'--- {szamlalo}. jaték ---', file=celfajl)
        print('Rendezett lista: ', lista, file=celfajl)
        print('A generált számok mennyisége: ' + str(len(lista)) + ' db.', file=celfajl)
        print('Eredeti halmaz: ', lotto_halmaz, file=celfajl)
        lotto = sorted(lotto_halmaz)
        print('A véletlen lottószámok növekvő sorrendben: ', lotto, file=celfajl)
        print(datum, file=celfajl)
        print(f'Ötöslottó nyerőszámok: {szoveg}', file=celfajl)
        print('\n', file=celfajl)
    print('\n')
    lotto_halmaz = set()
    lista = []
