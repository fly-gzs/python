"""
A program tároljon el egy szót egy változóban. 
A felhasználó adjon meg egy betűt, amiről a program döntse el, hogy előfordul-e a szóban! 
Az eredményről tájékoztassa a felhasználót, és írja ki a tárolt szót is!
"""

szo = input('Adj meg egy szót: ')
betu = input('Adj meg egy betüt: ')
index = 0
talalat = False
while index < len(szo) and not talalat:
    if szo[index] == betu:
        talalat = True
    index += 1
if talalat:
    print('A szóban szerepel a megadott "' + betu + '" betü.')
    print('A tárolt szó:', szo)
else:
    print('A szóban NEM szerepel a megadott "' + betu + '" betü.')
    print('A tárolt szó:', szo)    