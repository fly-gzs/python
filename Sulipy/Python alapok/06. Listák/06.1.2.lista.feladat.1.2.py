'''
Készíts egy programot, amely a felhasználótól keresztneveket kér be egészen addig,
amíg az ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)!
A program a bekért neveket írja ki a képernyőre!
A 3. név megadása után tájékoztassa a program a felhasználót,
hogy már nincs lehetősége újabb adat bevitelére,
írja ki az addig megadott neveket, és lépjen ki.
'''
szavak  = []
keresztnev = None
db = 1
while keresztnev != '' and db <= 3:
    keresztnev = input('Adj meg egy keresztnevet!\t')
    if keresztnev != '':
        szavak.append(keresztnev)
    db = db + 1
print("Max. 3 név megadására van lehetőség!")
print(szavak)
