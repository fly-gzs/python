'''
Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot!
A képernyőre kizárólag csak a 3-mal oszthatóakat írja ki,
és a végén informálja a felhasználót arról is, hány darab ilyen szám volt.
'''
import random

random_szam=1
huszig_mehet=0
szamlalo=0
while huszig_mehet <= 20:
    random_szam=random.randint(1,12)
#     print(random_szam)
    if (random_szam % 3 == 0):
        print("(",random_szam,")")
        szamlalo += 1
    huszig_mehet += 1
    if (huszig_mehet == 20):
        break
print("A " + str(huszig_mehet) + " db véletlen szám között " + str(szamlalo) + " db hárommal osztható szám volt.")