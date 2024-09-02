'''
Írj egy programot, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között!
'''
szam = 10
while szam >= 1:
    maradek = szam % 2
    if (maradek == 1):
        print(szam)
    szam = szam - 1
print("Vége")