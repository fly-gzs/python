'''
Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel
alapján eldönti milyen fajtájú! (kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)
Az előbbi programot módosítsd úgy, hogy újabb és újabb mondatot kérjen be a program
(amig a felhasználó csak egy ENTER-t nem üt),
majd állapítsa meg, és írja ki mineden egyes alkalommal a mondat fajtáját!
'''
mondat = None
while mondat != '':
    mondat = input('Írj egy mondatot: ')
    if mondat != '' and mondat[-1] == '.':
        print('Ez egy KIJELENTŐ mondat.')
    elif mondat != '' and mondat[-1] == '?':
        print('Ez egy KÉRDŐ mondat.')
    elif mondat != '' and mondat[-1] == '!':
        print('Ez egy FELKIÁLTÓ/FELSZÓLÍTÓ/ÓHAJTÓ mondat.')
    elif mondat == '':
        print('Entert ütöttél!')
    else:
        print('Nincs írásjel a mondat végén!')
print('Vége')