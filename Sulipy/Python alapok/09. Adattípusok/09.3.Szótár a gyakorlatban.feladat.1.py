'''
Írj egy programot, amelyben könyvek adatait (szerző, cím) tudja rögzíteni a felhasználó.
A könyvek adatainak tárolására használjon a program szótárakat,
amelyek egy lista elemei legyenek! Az adatbekérés addig folytatódjon,
amíg a felhasználó a szerző megadásakor nem gépel be adatot, csupán ENTER-t üt!
A program ekkor listázza ki a már bevitt adatokat, és fejezze be a működését!
'''
from pprint import pprint
from pprint import pformat

konyv = {}
konyvtar = []
szerzo = None
while szerzo != '':
    szerzo = input('Add meg a szerző nevét! ')
    if szerzo == '':
        break
    cim = input('Add meg a mű címét nevét! ')
    konyv['szerzo'] = szerzo
    konyv['cim'] = cim
    konyvtar.append(konyv)
    konyv = {}
    
pprint(konyvtar, sort_dicts = False, width = 30)