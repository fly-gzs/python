'''
Adott egy függvény. Értelmezési tartománya: [-3; 4] intervallumon az egész számok halmaza.
Hozzárendelési szabálya: y = 2x-3.
A program egy lista formájában tárolja az értelmezési tartomány elemeit.
Listaelemek leképezésével állítsa elő, tárolja listában és írja ki az értékkészlet elemeit.
'''

x = []
y = []
# ert_keszl = 0
for ert_tart in range(-3,5):
#     print(ert_tart)
    x.append(ert_tart)
    ert_keszl = (ert_tart * 2) - 3
    y.append(ert_keszl)
print('Az y = 2x-3 függvény értelmezési tartománya: ', x)
print('Az y = 2x-3 függvény érték készlete: ', y)

