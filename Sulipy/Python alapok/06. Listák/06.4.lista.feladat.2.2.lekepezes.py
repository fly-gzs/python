'''
Adott egy függvény. Értelmezési tartománya: [-3; 4] intervallumon az egész számok halmaza.
Hozzárendelési szabálya: y = 2x-3.
A program egy lista formájában tárolja az értelmezési tartomány elemeit.
Listaelemek leképezésével állítsa elő, tárolja listában és írja ki az értékkészlet elemeit.
Az előző programot alakítsuk most úgy át, hogy a listaelemek leképezése
az értelemezési tartomány nemnegatív elemire korlátozódjon!
'''

x = []
for ert_tart in range(-3,5):
    x.append(ert_tart)
y = [2*ert_tart-3 for ert_tart in x if ert_tart >= 0]
print('Az y = 2x-3 függvény értelmezési tartománya: ', x)
print('Az y = 2x-3 függvény érték készlete: ', y)

