'''
Készíts egy programot, amely a felhasználótól kis "a"  és a nagy "A" betűvel kezdődő szavakat kér be és ezeket tárolja.
Ha a felhasználó nem "a" vagy "A" betűvel kezdődő szót ad meg, akkor azt hagyja figyelmen kívül és ne tárolja.
A bekérés egészen addig folytatódjon, amíg a felhasználó ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)!
A program a bekért neveket írja ki a képernyőre!
A program tájékoztatássa a felhasználót a működéséről, és az elvárt adatokról!
'''
a_betus  = []
a_szo = None
while a_szo != '':
    a_szo = input('Adj meg egy "a" vagy "A" betüvel kezdődő szót!\t')
    if a_szo != '' and a_szo[0] != 'a' and a_szo[0] != 'A':
        print('')
        print('Csak "a" vagy "A" betüvel kezdődő szavakat tároljuk!')
    elif a_szo == '':
        print('Vége!')
    else:
        a_betus.append(a_szo)
print('A következő szavakat tároltuk le: ' + str(a_betus))
