'''
Készíts egy programot, ami a rendszámokban előforduló karkatereket helyettesíti
'|' jellel a betűket,
'*' jellel a számokat
az alábbiaknak megfelelően:

rendszamok = ['ABC123', 'ABCD777', 'WN25L']
atalakitva = ['|||***', '||||***', '||**|']
'''

modositott_rendszamok = []

rendszamok = ['ABC123', 'ABCD777', 'WN25L']
for elem in rendszamok:
    uj_rendszam = ''
    for karakter in elem:
        if karakter.isdecimal():
            uj_rendszam += '*'
        else:
            uj_rendszam += '|'
    modositott_rendszamok.append(uj_rendszam)
        
print(f'{modositott_rendszamok = }')
