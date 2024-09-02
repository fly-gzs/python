'''
Írj egy programot, amelyben van egy 'kerulet' nevű függvény,
amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is!
Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó,
és számolja ki a kerületét (0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter:
téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!

A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!
'''

def kerület(a, lista):
    return a + sum(lista)

lista = []
be_szam = 0
while be_szam >= 0:
    be_szam = int(input('Adj meg egy pozitív számot: '))
    if be_szam >= 0:
        lista.append(be_szam)

print(kerület(5,lista))
