rendszamok = ['ABC123', 'ABCD777', 'WN25L']

atalakitas = []
for elem in rendszamok:
    uj_rendszam = ''
    for karakter in elem:
        if karakter in '0123456789':
            uj_rendszam += '*'
        else:
            uj_rendszam += '|'
    atalakitas.append(uj_rendszam)
print(atalakitas)