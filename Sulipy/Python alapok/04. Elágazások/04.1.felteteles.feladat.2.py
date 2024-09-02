"""
Készíts egy programot, ami bekér egy számot a felhasználótól,
majd kiírja, hogy a megadott szám páros-e vagy páratlan!

[Tipp] A maradékos osztás segít! Mennyivel is kell elosztanod a számot maradékosan,
hogy kiderüljön páros-e? Ebben az esetben mennyi lesz a maradék?
"""
szam = int(input("Adj meg egy számot! "))
maradek = szam % 2
# print(maradek)
if (maradek==0):
    print("A megadott szám (" + str(szam) + ") páros!")
else:
    print("A megadott szám (" + str(szam) + ") páratlan!")