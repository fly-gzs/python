'''
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza.
Olvasd be a fájl tartalmát és tárold el
a, egy listában, melynek elemei szótárak,
b, egy kétdimenziós listában!
mind a két esetben az évszám int típusként kerüljön rögzítésre!
'''

lista_szotar = []
lista_2dimenzio = []
with open('./adatok/Timeline.txt', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        szotar = {'year':adatok[0], 'programming language':adatok[1], 'first name':adatok[2], 'last name of chief developer':adatok[3]}
        lista_szotar.append(szotar)
        lista_2dimenzio.append(adatok)
print(f'{lista_szotar = }')
print(f'{lista_2dimenzio = }')