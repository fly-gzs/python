'''
Írj egy programot, ami a felhasználótól három egész számot számot kér be egyesével, ezeket eltárolja egy listában,
majd a képernyőre kiírja a lista tartalmát! Ha a felhasználó nem számot ad meg, kapjon hibaüzenetet,
és ismétlődjön meg a bekérés!
'''

lista = []
x = 1
while len(lista) < 3:
    try:
        szam = int(input(f'Adj meg a(z) {x}. számot! '))
        lista.append(szam)
        x += 1
    except:
        print('Nem számot adtál meg!')
print('A program vége')
print(lista)
print(len(lista))



