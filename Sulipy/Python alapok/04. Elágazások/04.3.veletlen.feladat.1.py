'''
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot,
majd összehasonlítja ezt a felhasználó által megadott,
szintén ebbe a tartományba eső számmal!
Az összehasonlítás eredményéről tájékoztassa a felhasználót!
'''

import random
random_szam = random.randint(1,3)
# print(random_szam)
bekert_szam = int(input("Kérek egy számot 1 és 3 között: "))
# print(bekert_szam)
if (random_szam == bekert_szam):
    print("A két szám egyenlő egymással:", bekert_szam)
else:
    print("A véleten szám (", random_szam, ") és a bekért szám (", bekert_szam, ") nem egyenlő egymással!")
    if (random_szam > bekert_szam):
        print("Véletlen szám nagyobb mint a bekért szám.")
    else:
        print("Véletlen szám kisebb mint a bekért szám.")