'''
Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel
alapján eldönti milyen fajtájú! (kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)
'''
mondat = input('Írj egy mondatot: ')
if mondat[-1] == '.':
    print('Ez egy KIJELENTŐ mondat.')
elif mondat[-1] == '?':
    print('Ez egy KÉRDŐ mondat.')
elif mondat[-1] == '!':
    print('Ez egy FELKIÁLTÓ/FELSZÓLÍTÓ/ÓHAJTÓ mondat.')
else:
    print('Nincs írásjel a mondat végén!')