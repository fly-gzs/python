'''
Készíts egy programot, amely egy-egy listában tárol 5 db egymástól
különböző véletlenszámot [-5; 5] intervallumon!
A program írja ki a képernyőre a két lista elemeit, a
két lista közös elemeit, valamint a két lista összes elemét az
esetleges ismétlődések mellőzésével!
  
'''

import random
halmaz1 = set()
halmaz2 = set()
while len(halmaz1) < 5:
    random_szam1 = random.randint(-5,5)
    halmaz1.add(random_szam1)
while len(halmaz2) < 5:
    random_szam2 = random.randint(-5,5)
    halmaz2.add(random_szam2)

print(f'{halmaz1=}')
print(f'{halmaz2=}')

kozos = halmaz1 & halmaz2
unio = halmaz1 | halmaz2

print(f'{kozos=}')
print(f'{unio=}')