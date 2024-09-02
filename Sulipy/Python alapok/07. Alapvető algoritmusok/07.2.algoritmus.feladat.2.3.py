"""
A program tároljon el egy szót egy változóban. 
A felhasználó adjon meg egy betűt, amiről a program döntse el, hogy előfordul-e a szóban! 
Az eredményről tájékoztassa a felhasználót, és írja ki a tárolt szót is!
Fejlesszük tovább a 2.2 programot úgy, hogy a felhasználónak többször is legyen lehetősége
újabb tippet megadnia.
A bekérés addig folytatódjon, amíg a felhasználó nem ad meg betűt, csupán egy ENTER-t üt!

Igyekezz minél felhasználóbarátabbá tenni a programot!
A programnak lehetnek egyéb hasznos funkciói,
például gyűjtheti és kiírhatja a jó és a rossz tippeket (betűket).
"""

szo = input('Adj meg egy szót: ')
print('Tippelj, milyen betük szerepelnek a szóban!')
print('A kilépéshez csak egy ENTER-t üss!')
betu = None
lista_igen = []
lista_nem = []
while betu != '':
    talalat = False
    index = 0
    betu = input('Adj meg egy betüt: ')
    while index < len(szo):
        if szo[index] == betu:
            talalat = True
        index += 1
    if talalat:
        lista_igen.append(betu)
    elif betu == '':
        print('ENTER-t ütöttél. Vége a játéknak!')
    else:
        lista_nem.append(betu)
print('Jó tippek: ', ', '.join(lista_igen))
print('Rossz tippek: ', ', '.join(lista_nem))