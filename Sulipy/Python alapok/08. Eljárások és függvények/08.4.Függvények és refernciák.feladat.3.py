'''
Írj egy programot, amely egy ötbetűs főneveket tartalamzó listából véletelenszerűen választ
egyet, amit a játékosnak egy-egy betű megadásával kell kitalálnia!
A főprogramot a main() függvény tartalmazza, és ezen kívűl legyen még minimum 2
- részfeladatokat megvalósító - függvény! A program az alábbiak szerint műdködjön:
'''

import random

def szovalaszto():
    szotar = ['kalap', 'tégla', 'lámpa', 'tábla', 'kocsi']
    return random.choice(szotar)

def nem_megoldott(jatekos):
    return '_' in jatekos

def tipp_bekero():
    return input('Adj meg egy betűt! ')

def ertekel(gep, karakter, jatekos, nem_jo):
    talalat = False
    for index, betu in enumerate(gep):
        if karakter == betu:
            jatekos[index] = karakter
            talalat = True
    if talalat:
        print('Talalat!')
    else:
        print('Sajnos nem talált!')
        nem_jo.append(karakter)
    print(f'Jelenlegi állás: {"".join(jatekos)}')
    print(f'Rossz tippek: {", ".join(nem_jo)}')
    print('---------------------------------------\n')

def main():
    print('Találd ki melyik ötbetűs szóra gondoltam!')
    kitalalando = szovalaszto()
    allas = ['_', '_', '_', '_', '_']
    rossz_tippek = []
    probalkozasok = 0
    while nem_megoldott(allas):
        probalkozasok += 1
        tipp = tipp_bekero()
        ertekel(kitalalando, tipp, allas, rossz_tippek)
    print(f'Garatulálok! Kitalaltad {probalkozasok} próbálkozásból.')
   
main()

