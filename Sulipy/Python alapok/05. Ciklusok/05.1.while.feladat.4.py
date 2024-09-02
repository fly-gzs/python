'''
Írj egy programot, amely a felhasználó által meghatározott alkalommal írja ki
a bekért szöveget!
'''
szoveg = input("Adj meg egy szöveget! ")
mennyi = int(input("Hányszor írjuk ki? "))
szam = 1
while szam <= mennyi:
    print(szoveg)
    szam += 1
print(str(szam-1) + " " + szoveg + " nyomtatást kértél!")
    
