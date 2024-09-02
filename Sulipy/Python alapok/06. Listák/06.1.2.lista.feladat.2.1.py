'''
Készíts egy programot, amely a felhasználótól kis "a" betűvel kezdődő szavakat kér be és ezeket tárolja.
Ha a felhasználó nem "a" betűvel kezdődő szót ad meg, akkor azt hagyja figyelmen kívül és ne tárolja.
A bekérés egészen addig folytatódjon, amíg a felhasználó ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)!
A program a bekért neveket írja ki a képernyőre!
A program tájékoztatássa a felhasználót a működéséről, és az elvárt adatokról!
'''
a_betus  = []
a_szo = None
while a_szo != '':
    a_szo = input('Adj meg egy kis "a" betüvel kezdődő szót!\t')
    if a_szo != '' and a_szo[0] != 'a':
        print('')
        print('Csak kis "a" betüvel kezdődő szavakat tároljuk!')
    if a_szo != '' and a_szo[0] == 'a':
        a_betus.append(a_szo)
print('A következő szavakat tároltuk le: ' + ' | '.join(a_betus))
