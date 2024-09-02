'''
Készíts egy programot, amely a felhasználótól bekér egy egész számot,
majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót.
'''
szam = int(input("Adj meg egy számot: "))
maradek = szam % 2
if (szam > 0 and maradek == 0):
    print("A megadott szám (" + str(szam) + ") pozitív páros.")
elif (szam < 0 and maradek == 1):
    print("A megadott szám (" + str(szam) + ") negatív páratlan.")
else:
    print("A megadott szám (" + str(szam) + ") se nem pozitív páros, se nem negatív páratlan.")
