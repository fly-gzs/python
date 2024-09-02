'''
Készíts egy programot, amely a felhasználótól keresztneveket kér be egészen addig,
amíg az ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)!
A program a bekért neveket írja ki a képernyőre!
'''
szavak  = []
keresztnev = None
db = 1
while keresztnev != '':
    keresztnev = input('Adj meg egy keresztnevet!\t')
    if keresztnev != '':
        szavak.append(keresztnev)
print(szavak)
