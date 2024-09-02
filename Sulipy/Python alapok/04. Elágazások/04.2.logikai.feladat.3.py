"""
Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
- csak 3-mal osztható,
- csak 4-gyel osztható,
- 3-mal és 4-gyel is osztható,
- sem 3-mal, sem 4-gyel nem osztható!
"""

szam = int(input("Adj meg egy számot: "))
maradek3 = szam % 3
maradek4 = szam % 4
if (maradek3 == 0 and maradek4 != 0):
    print("A szám (" + str(szam) + ") osztaható hárommal.")
elif (maradek3 != 0 and maradek4 == 0):
    print("A szám (" + str(szam) + ") osztaható néggyel.")
elif (maradek3 == 0 and maradek4 == 0):
    print("A szám (" + str(szam) + ") osztaható hárommal és néggyel is.")
else:
    print("A szám (" + str(szam) + ") nem osztaható sem hárommal, sem néggyel.")
    