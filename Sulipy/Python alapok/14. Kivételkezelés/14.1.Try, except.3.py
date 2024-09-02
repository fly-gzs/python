'''
Hozz létre egy szöveges állományt, amely tartalmaz két számot egymástól tabulátorral elválasztva!
Írj egy programot, amely beolvassa a fájl tartalmát, és a képernyőn megjeleníti a két szám hányadosát!
A programot készítsd fel az esetleges hibalehetőségekre,
a felhasználó pedig kapjon a hibának megfelelő figyelmeztető üzenetet ilyen esetben!
'''

lista = []
with open('./adatok/szamok.txt', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok = sor.strip().split('\t')
        lista.append(adatok)
print(adatok)
print(lista)
print(f'Az osztandó szám: {adatok[0]}')
print(f'Az osztó szám: {adatok[1]}')

try:
    print(f'Az osztás eredmenye: {int(adatok[0]) / int(adatok[1]):.2f}')
except ZeroDivisionError as e:
    print('Hiba: ', e)
    print('Nullával nem oszthatunk!')
except ValueError as e:
    print('Hiba: ', e)
    print('Nem számot adtál meg!')
print('A program vége')