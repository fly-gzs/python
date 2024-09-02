'''
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig,
amíg az csupán ENTER-t nem üt! A számokat tárolja el a program egy listában!
Az adatbekérés befejezte után írja ki a program a lista elemeit,
a legkisebb és a legnagyobb számot!
'''
lista = []
szam = input('Adj meg egy számot! ')
while szam != '':
    lista.append(szam)
    szam = input('Adj meg egy számot! ')
print(f'A lista elemei: ', ' | '.join(lista))
legkisebb = lista[0]
legnagyobb = lista[0]
for x in lista:
    if x < legkisebb:
        legkisebb = x
    if x > legnagyobb:
        legnagyobb = x
print('A lista legkisebb eleme: ', legkisebb)
print('A lista legnagyobb eleme: ', legnagyobb)