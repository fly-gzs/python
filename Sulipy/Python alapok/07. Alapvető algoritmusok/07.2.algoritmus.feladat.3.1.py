'''
Torpedó játék egyszerűsített változata. A játéktér legyen egy 3x3-as négyzetalakú rács,
amiben az oszlopokat betűk (A, B, C), a sorokat számok (1, 2, 3) jelölik.
A program helyezzen el egy darab egy egység kiterjedésű hajót
a játéktérben véletlenszerűen (Pl: B2).
A játékos próbálja meg kitalálni a hajó pozícióját újabb és újabb tippek megadásával.
A játék végén a program azt is írja ki a képernyőre,
hogy hány próbálkozásból tudta a játékos kitalálni a pozíciót!
'''
import random
jatekter = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
hajo = random.choice(jatekter)
print('A hajó helyzete: ', hajo)
rossz_tipp_lista = []
ervenytelen_tipp_lista = []
helyes_tipp_lista = []
ervenyes_tipp = []
osszes_tipp = []
tipp_szam = 0
while tipp_szam < len(jatekter):
    tipp = input('Tippelj egyet: ')
    if not tipp in jatekter:
        print('Hiba! Ez a mező nem létezik a játéktérben!')
        ervenytelen_tipp_lista.append(tipp)
    elif tipp == hajo:
        print('Talált, süllyedt!')
        helyes_tipp_lista.append(tipp)
        break
    else:
        print('Nem talált!')
        rossz_tipp_lista.append(tipp)
    tipp_szam += 1
print('A találat helye: ', ('').join(helyes_tipp_lista))    
print('Rossz tippek: ', (', ').join(rossz_tipp_lista))
print('Érvénytelen tippek: ', (', ').join(ervenytelen_tipp_lista))