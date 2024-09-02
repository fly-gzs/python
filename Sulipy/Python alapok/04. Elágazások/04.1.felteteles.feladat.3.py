'''
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között,
vagyis egy változóban tárolj egy ilyen számot!
Azután a program bekér egy számot a felhasználótól, majd kiírja,
hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
'''

import random
random_szam = random.randint(1,5)
# print(random_szam)
bekert_szam = int(input("Kérek egy számot 1 és 5 között: "))
# print(bekert_szam)
if (random_szam == bekert_szam):
    print("A két szám egyenlő egymással:", bekert_szam)
else:
    print("A véleten szám (", random_szam, ") és a bekért szám (", bekert_szam, ") nem egyenlő egymással!")
    if (random_szam > bekert_szam):
        print("Véletlen szám nagyobb mint a bekért szám.")
    else:
        print("Véletlen szám kisebb mint a bekért szám.")