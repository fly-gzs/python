'''
Írj egy programot, ami a felhasználótól bekér két számot, és a képernyőn megjeleníti a két szám hányadosát
három tizedesjegy pontossággal! A program adjon hibaüzenetet, ha a felhasználó nem számot adott meg,
vagy az osztás nem végezhető el! Ebben az esetben kérjen be újabb adatot mindaddig, amíg nem lép fel hiba!
'''

oszto = 0
osztando = 'a'
while str(osztando).isalpha():
    try:
        osztando = input(f'Adj meg az osztandó számot! ')
        osztando = int(osztando)
    except ValueError as e:
        print('Hiba: ', e)
        print('Nem számot adtál meg!')
while oszto == 0:
    try:
        oszto = int(input('Mennyivel osszam el az előző számot? '))
        print(f'Az eredmeny: {osztando / oszto:.3f}')
    except ZeroDivisionError as e:
        print('Hiba: ', e)
        print('Nullával nem oszthatunk!')
    except ValueError as e:
        print('Hiba: ', e)
        print('Nem számot adtál meg!')
print('A program vége')





