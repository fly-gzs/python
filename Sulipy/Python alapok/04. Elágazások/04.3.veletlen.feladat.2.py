'''
A program a pénzfeldobást modellezi.
Kérdezze meg a felhasználótól a választását (fej vagy írás),
majd adjon tájékoztatást, hogy eltalálta-e!
'''

import random
random_szam = random.randint(1,2)
# print(random_szam)
gep=0
ember=0
rossz_tipp=0
for i in range(0,3):
    if (random_szam == 1):
        print("A pénzfeldobás eredménye: FEJ")
    else:
        print("A pénzfeldobás eredménye: ÍRÁS")
    print("Tippelj! Fej vagy írás? Fej estén írj 1-t, írás esetén 2-t!")
    tipp = int(input("Fej vagy írás? "))
    # print(tipp)
    if (random_szam == tipp):
    #     print("Eltaláltad!")
        if (tipp == 1):
            print("Eltaláltad! FEJ")
            print("\n")
            ember=ember+1
        else:
            print("Eltaláltad! ÍRÁS")
            print("\n")
            ember=ember+1
    elif (tipp < 1 or tipp > 2):
        print("Hééé! Tippelj rendesen, az anyád szentségit!!!")
        print("\n")
        rossz_tipp=rossz_tipp+1
    else:
        print("Nem talált!")
        print("\n")
        gep=gep+1
    print("A meccs állása: Gép - Ember", gep, "-", ember)
    print("\n")
print("A hibás tippek száma: ", rossz_tipp)
print("A meccs végeredménye: Gép - Ember", gep, "-", ember)