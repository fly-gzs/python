'''
Készíts egy programot, amely TOTÓ eredményeket (1, 2, X) kér be a felhasználótól, és rögzíti ezeket egy listában!
A beolvasás mindaddig folytatódjon, amig a felhasználó nem ad meg eredményt, csupán ENTER-t üt!
A beolvasott értékek ellenőrzését saját kivételosztály segítségével oldja meg a program!
'''


class TotoError(Exception):
    """
    Nem megflelő TOTÓ eredmény esetén ...
    """

def toto_ell(ertek):
    if ertek in '12x':
        return ertek
    else:
        raise TotoError(f'{ertek}: érvénytelen TOTÓ eredmény!')

lista = []
toto = 1
try:
    while toto != '':
        toto = toto_ell(input('Add meg a TOTÓ eredményeket! '))
        if toto != '':
            if toto.isdigit():
                lista.append(int(toto))
            elif toto == 'x':
                lista.append(toto)
except TotoError as e:
    print(e)
    print('Az értékek csak [1; 2; x] lehetnek!')
print(lista)