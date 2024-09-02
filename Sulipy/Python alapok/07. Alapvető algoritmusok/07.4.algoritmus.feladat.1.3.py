'''
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig,
amíg az csupán ENTER-t nem üt! A számokat tárolja el a program egy listában!
Az adatbekérés befejezte után írja ki a program a lista elemeit,
a legkisebb és a legnagyobb számot!
Alakítsd át úgy az előbbi programot, hogy az 'X' vagy 'x' megadása eredményezze az adatbekérés végét!
Alakítsd át úgy az előbbi programot, hogy a legkisebb és legnagyobb páros számot határozza meg!
'''
lista = []
szam = input('Adj meg egy számot! ')
if szam != 'X' and szam != 'x':
    szam = int(szam)
    while szam != 'X' and szam != 'x':
        lista.append(szam)
        szam = input('Adj meg egy számot! ')
        if szam != 'X' and szam != 'x':
            szam = int(szam)
    print(f'A lista elemei: ',lista)
    paros_lista = []
    paros_szamlalo = 0
    for pp in lista:
        if pp % 2 == 0:
            paros_lista.append(pp)
            paros_szamlalo += 1
#     print(paros_lista)    
    if paros_szamlalo != 0:
        legkisebb = paros_lista[0]
        legnagyobb = paros_lista[0]
        for i in paros_lista:
            if i < legkisebb:
                legkisebb = i
            if i > legnagyobb:
                legnagyobb = i
        print('A lista legkisebb páros eleme: ', legkisebb)
        print('A lista legnagyobb páros eleme: ', legnagyobb)
    else:
        print('Nincs páros szám a listában!')
