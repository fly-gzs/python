'''
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig,
amíg az csupán ENTER-t nem üt! A számokat tárolja el a program egy listában!
Az adatbekérés befejezte után írja ki a program a lista elemeit,
a legkisebb és a legnagyobb számot!
Alakítsd át úgy az előbbi programot, hogy az 'X' vagy 'x' megadása eredményezze az adatbekérés végét!
'''
lista = []
szam = input('Adj meg egy számot! ')
while szam != 'X' and szam != 'x':
    lista.append(szam)
    szam = input('Adj meg egy számot! ')
print(lista)
print(f'A lista elemei: ', ' | '.join(lista))
legkisebb = lista[0]
legnagyobb = lista[0]
for i in lista:
    if i < legkisebb:
        legkisebb = i
    if i > legnagyobb:
        legnagyobb = i
print('A lista legkisebb eleme: ', legkisebb)
print('A lista legnagyobb eleme: ', legnagyobb)