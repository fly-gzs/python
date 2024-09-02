"""
Készíts egy programot, amely a felhasználótól bekér egy páros számot,
majd ennek megfelelően rajzol ki a képernyőre
egy pocak szerű alakzatot az alábbiak szerint!
"""
paros_szam = int(input('Adj meg egy páros számot: '))
darab_karakter = 1
sor = 1
if (paros_szam % 2 == 1):
    print('Ez nem páros szám volt')
else:
    while sor <= paros_szam/2:
      oszlop = 1
      while oszlop <= darab_karakter:
          print('O ', end='')
          oszlop = oszlop + 1
      print('')
      darab_karakter = darab_karakter + 1
      sor = sor + 1
    darab_karakter = paros_szam/2
    while paros_szam/2 < sor <= paros_szam:
      oszlop = 1
      while oszlop <= darab_karakter:
          print('O ', end='')
          oszlop = oszlop + 1
      print('')
      darab_karakter = darab_karakter - 1
      sor = sor + 1
