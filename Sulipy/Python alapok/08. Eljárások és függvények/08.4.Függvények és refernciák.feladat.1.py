'''
Írj egy programot, amely a main() függvényben generál egy véletlenszámot [1; 10] 
intervallumon és eltárolja azt egy változóban.
Egy másik függvény kérjen be a felhasználótól egy számot, ezzel térjen vissza, 
és így írja felül a main() függvényben a változó értékét.
A bekérés és felülírás mindaddig folytatódjon, amíg a felhasználó 0-t nem ad meg! 
(A bekérést megvalósító függvény újra és újra történő meghívását, valamint annak vizsgálatát, hogy a felhasználó 0-t adott-e meg, a main() függvénynnek kell vezérelnie!)
'''

def bekeres():
    y = int(input('Adj meg egy számot! '))
    return y

import random

def main():
    szam = random.randint(1,10)
    print(f'A véletlen szám: {szam}')
    szam = bekeres()
    if szam != 0:
        print(f'A felülírt véletlen szám: {szam}')
        print('')
        main()
    else:
        print('Vége!')
   
main()

