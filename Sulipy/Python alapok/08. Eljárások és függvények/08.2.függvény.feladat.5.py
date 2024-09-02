'''
Írj egy programot, ami addig kér be egész pozitív számokat,
amíg a felhasználó negtív számot nem ír!
A megadott számokat tárolja a program egy listában,
és ezt adja át paraméterként egy függvények,
amely a lista legkisebb elemével tér vissza.
A program írja ki, hogy melyik volt a megadott legkisebb szám!
'''

def legkisebb(lista):
    return min(lista)

lista = []
be_szam = 1
while be_szam >= 0:
    be_szam = int(input('Adj meg egy pozitív számot: '))
    if be_szam > 0:
        lista.append(be_szam)

print(legkisebb(lista))