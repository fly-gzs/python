'''
Az adott lista elemei közül a program kiírja a 3-mal osztható páros számokat!
'''
szamok = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]
for szam in szamok:
    if szam % 2 == 0 and szam % 3 == 0:
        print(szam)