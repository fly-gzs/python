'''
Adott két függvény (y=2x+3 és y=3x+1), mindkettő értelmezési tartománya az egész számok [0;10]
intervallumon. A program készítsen egy-egy halmazt a függvények értékkészleteivel,
írja ki ezeket a képernyőre, majd jelenítse meg a halmazok metszetét, unióját és különbségét!
'''
x = 0
halmaz1 = set()
halmaz2 = set()
while x <= 10:
    y1 = 2*x + 3
    y2 = 3*x + 1
    halmaz1.add(y1)
    halmaz2.add(y2)
    x += 1
print(halmaz1)
print(halmaz2)
print('---------------------------')
print('Metszet:')
print(halmaz1 & halmaz2)
print('---------------------------')
print('Unió:')
print(halmaz1 | halmaz2)
print('---------------------------')
print('Különbség:')
print(halmaz1 - halmaz2)