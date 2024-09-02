'''
Készíts egy programot, ami a rendszámokban előforduló karkatereket helyettesíti
'|' jellel a betűket,
'*' jellel a számokat
az alábbiaknak megfelelően:
Alakítsd át a fenti programot úgy, hogy a leképezés map() fügvénnyel történjen!

rendszamok = ['ABC123', 'ABCD777', 'WN25L']
atalakitva = ['|||***', '||||***', '||**|']
'''

def uj_rendszam(rendszam):
    atalakitott_rendszamok = ''
    for karakter in rendszam:
        if karakter.isalpha():
            atalakitott_rendszamok += '|'
        elif karakter.isdigit():
            atalakitott_rendszamok += '*'
    return atalakitott_rendszamok
    
rendszamok = ['ABC123', 'ABCD777', 'WN25L']
modositott_rendszamok = list(map(uj_rendszam, rendszamok))
        
print(f'{modositott_rendszamok = }')
