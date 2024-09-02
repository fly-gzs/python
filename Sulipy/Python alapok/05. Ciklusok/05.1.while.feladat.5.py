'''
Írj egy programot, amely a felhasználótól páros számot kér be.
Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig,
amíg végül páros számot nem ad meg a felhasználó.
'''
szam = int(input("Adj meg egy páros számot: "))
while szam % 2 == 1:
    szam = int(input("Adj meg egy páros számot: "))
print("Igen a " + str(szam) + " páros.")