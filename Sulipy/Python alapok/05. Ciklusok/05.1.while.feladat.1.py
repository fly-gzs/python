'''
Írj egy programot, amely kiírja a páros számokat 1 és 10 között!
'''
szam = 1
while szam <= 4:
    maradek = szam % 2
    if (maradek == 0):
        print(szam)
    szam = szam + 1
print("Vége")