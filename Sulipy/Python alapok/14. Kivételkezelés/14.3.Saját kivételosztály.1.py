'''
Módosítsd a videóban látott, példák részben olvasható kódot úgy, hogy a program a három RGB összetevő értékét
egy lépésben kérje be például úgy, hogy a felhasználónak az értékeket egymástól vesszővel és szóközzel kell
elválasztania! Hozz létre két saját kivételosztályt! Az egyik formai szempontból ellenőrzze a választ, a másik
pedig vizsgálja azt, hogy az értékekek a megfelelő intervallumba esenek-e!
'''


class RGBError(Exception):
    """
    Nem megflelő RGB összetevő esetén ...
    """

def rgb_osszetevo_ell(ertek):
    if 0 <= ertek <= 255:
        return ertek
    else:
        raise RGBError(f'{ertek}: érvénytelen RGB összetevő!')

rgb_lista_int = []
while len(rgb_lista_int) != 3:
    rgb_lista_int = []
    rgb_osszetevok = input('Add meg a három RGB összetevőt egymástól vesszővel és szóközzel elválasztva: ')
    rgb_lista = rgb_osszetevok.split(', ')
    for x in rgb_lista:
        try:
            x = int(x)
            rgb_osszetevo_ell(x)
        except RGBError as e:
            print(e)
            print('A számnak a [0; 255] tartományba kell esnie!')
        except ValueError as e:
            print(e)
            print('Hibás formátumban adtad meg az összetevőket vagy betű szerepel az összetevők között!')
        else:
            rgb_lista_int.append(x)
    print(rgb_lista_int)







#
#

#
#
# rgb = []
# srsz = 1
# while len(rgb) != 3:
#     try:
#         rgb_osszetvo = rgb_osszetevo_ell(int(input(f'Add meg a(z) {srsz}. RGB összetevőt! ')))
#     except ValueError as e:
#         print(e)
#         print('Nem számot adtál meg! Adj meg új értéket! ')
#     except RGBError as e:
#         print(e)
#         print('A számnak a [0; 255] tartományba kell esnie! Adj meg új értéket! ')
#     else:
#         rgb.append(rgb_osszetvo)
#         srsz += 1
#
# print(rgb)
