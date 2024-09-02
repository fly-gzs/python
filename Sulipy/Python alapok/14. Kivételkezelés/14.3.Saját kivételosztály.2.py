'''
Készíts egy programot, amely érdemjegyeket kér be a felhasználótól, és rögzíti ezeket egy listában!
A beolvasás mindaddig folytatódjon, amig a felhasználó nem ad meg jegyet, csupán ENTER-t üt!
A beolvasott értékek ellenőrzését saját kivételosztály segítségével oldja meg a program!
'''


class JegyError(Exception):
    """
    Nem megflelő érdemjegy összetevő esetén ...
    """

def jegy_ell(ertek):
    if 1 <= ertek <= 5:
        return ertek
    else:
        raise JegyError(f'{ertek}: érvénytelen érdemjegy!')

lista = []
jegy = 1
try:
    while jegy != '':
        jegy = jegy_ell(int(input('Add meg az érdemjegyeket! ')))
        lista.append(jegy)
except JegyError as e:
    print(e)
    print('A számnak a [1; 5] tartományba kell esnie!')
except ValueError as e:
    print(e)
    print('Nem számpot adtál meg!')
print(lista)