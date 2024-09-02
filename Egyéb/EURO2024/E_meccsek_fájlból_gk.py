def gk(csapat):
    return csapat[7]
def rugott(csapat):
    return csapat[5]
def pontok(csapat):
    return csapat[-1]

tablazat = []
tablazat2 = []
tablazat3 = []
meccsek = []

E_csoport = ['Belgium', 'Szlovákia', 'Románia', 'Ukrajna']

with open('./adatok/E_csoport.txt', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        csoport_adatok = {
            'Belgium': {'meccs':int(adatok[1]), 'gyozelem':int(adatok[2]), 'dontetlen':int(adatok[3]), 'vereseg':int(adatok[4]), 'rugott_gol':int(adatok[5]), 'kapott_gol':int(adatok[6]), 'pont':int(adatok[7])},
            'Szlovákia': {'meccs':int(adatok[1]), 'gyozelem':int(adatok[2]), 'dontetlen':int(adatok[3]), 'vereseg':int(adatok[4]), 'rugott_gol':int(adatok[5]), 'kapott_gol':int(adatok[6]), 'pont':int(adatok[7])},
            'Románia':{'meccs':int(adatok[1]), 'gyozelem':int(adatok[2]), 'dontetlen':int(adatok[3]), 'vereseg':int(adatok[4]), 'rugott_gol':int(adatok[5]), 'kapott_gol':int(adatok[6]), 'pont':int(adatok[7])},
            'Ukrajna': {'meccs':int(adatok[1]), 'gyozelem':int(adatok[2]), 'dontetlen':int(adatok[3]), 'vereseg':int(adatok[4]), 'rugott_gol':int(adatok[5]), 'kapott_gol':int(adatok[6]), 'pont':int(adatok[7])}
            }


with open('./adatok/E_meccsek.txt', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok = sor.strip().split(', ')
        meccs1 = (adatok[0], adatok[1], adatok[2])
        meccsek.append(meccs1)
print(meccsek)

def meccs_feldolgozas(csapat1, csapat2, eredmeny):
    gol_csapat1, gol_csapat2 = map(int, eredmeny.split('-'))

    csoport_adatok[csapat1]['meccs'] += 1
    csoport_adatok[csapat2]['meccs'] += 1
    csoport_adatok[csapat1]['rugott_gol'] += gol_csapat1
    csoport_adatok[csapat1]['kapott_gol'] += gol_csapat2
    csoport_adatok[csapat2]['rugott_gol'] += gol_csapat2
    csoport_adatok[csapat2]['kapott_gol'] += gol_csapat1

    if gol_csapat1 > gol_csapat2:
        csoport_adatok[csapat1]['gyozelem'] += 1
        csoport_adatok[csapat2]['vereseg'] += 1
        csoport_adatok[csapat1]['pont'] += 3
    elif gol_csapat1 < gol_csapat2:
        csoport_adatok[csapat2]['gyozelem'] += 1
        csoport_adatok[csapat1]['vereseg'] += 1
        csoport_adatok[csapat2]['pont'] += 3
    else:
        csoport_adatok[csapat1]['dontetlen'] += 1
        csoport_adatok[csapat2]['dontetlen'] += 1
        csoport_adatok[csapat1]['pont'] += 1
        csoport_adatok[csapat2]['pont'] += 1


for csapat1, csapat2, eredmeny in meccsek:
    if eredmeny != '-':
        meccs_feldolgozas(csapat1, csapat2, eredmeny)
    else:
        print(f'A {csapat1} - {csapat2} meccs még nem került megrendezésre!')

print('\n--- Az "E" csoport rendezés nélkül: ---')
for csapat in E_csoport:
    print(f"{csapat}: {csoport_adatok[csapat]['meccs']}, {csoport_adatok[csapat]['gyozelem']}, {csoport_adatok[csapat]['dontetlen']}, {csoport_adatok[csapat]['vereseg']}, {csoport_adatok[csapat]['rugott_gol']}-{csoport_adatok[csapat]['kapott_gol']}, {csoport_adatok[csapat]['rugott_gol'] - csoport_adatok[csapat]['kapott_gol']}, {csoport_adatok[csapat]['pont']} ")
    
with open('./adatok/E_csoport_masolat.txt', 'w', encoding='utf-8') as celfajl:
    print('', file=celfajl)
    for csapat in E_csoport:
        print(f"{csapat},{csoport_adatok[csapat]['meccs']},{csoport_adatok[csapat]['gyozelem']},{csoport_adatok[csapat]['dontetlen']},{csoport_adatok[csapat]['vereseg']},{csoport_adatok[csapat]['rugott_gol']},{csoport_adatok[csapat]['kapott_gol']},{csoport_adatok[csapat]['rugott_gol'] - csoport_adatok[csapat]['kapott_gol']},{csoport_adatok[csapat]['pont']} ", file=celfajl)

with open('./adatok/E_csoport_masolat.txt', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        tablazat.append(adatok)
print('\n')


gkszerint = sorted(tablazat, key=gk, reverse=True)

print('\n--- Az "E" csoport gólkülönbség szerint: ---')
for csapat in gkszerint:
    print(csapat[0] + ', ' + csapat[1] + ', ' + csapat[2] + ', ' + csapat[3] + ', ' + csapat[4] + ', ' + csapat[5] + ', ' + csapat[6] + ', ' + csapat[7] + ', ' + csapat[8])
    
with open('./adatok/E_csoport_gk.txt', 'w', encoding='utf-8') as celfajl:
    print('', file=celfajl)
    for csapat in gkszerint:
        print(csapat[0] + ',' + csapat[1] + ',' + csapat[2] + ',' + csapat[3] + ',' + csapat[4] + ',' + csapat[5] + ',' + csapat[6] + ',' + csapat[7] + ', ' + csapat[8], file=celfajl)
print('\n')

with open('./adatok/E_csoport_gk.txt', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok1 = sor.strip().split(',')
        tablazat2.append(adatok1)
print(tablazat2)

rugott_gol_szerint = sorted(tablazat2, key=rugott, reverse=True)

print('\n--- Az "E" csoport rúgott gólok szerint: ---')
for csapat in rugott_gol_szerint:
    print(csapat[0] + ',' + csapat[1] + ', ' + csapat[2] + ', ' + csapat[3] + ', ' + csapat[4] + ', ' + csapat[5] + ', ' + csapat[6] + ', ' + csapat[7] + ', ' + csapat[8])
    
with open('./adatok/E_csoport_rug.txt', 'w', encoding='utf-8') as celfajl:
    print('', file=celfajl)
    for csapat in rugott_gol_szerint:
        print(csapat[0] + ',' + csapat[1] + ',' + csapat[2] + ',' + csapat[3] + ',' + csapat[4] + ',' + csapat[5] + ',' + csapat[6] + ',' + csapat[7] + ',' + csapat[8], file=celfajl)
print('\n')

with open('./adatok/E_csoport_rug.txt', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok1 = sor.strip().split(',')
        tablazat3.append(adatok1)
print(tablazat3)

pontokszerint = sorted(tablazat3, key=rugott, reverse=True)

print('\n--- Az "E" csoport pontok, gólkülönbség és rúgott gólok szerint szerint: ---')
for csapat in pontokszerint:
    print(csapat[0], ': ', ', '.join(map(str, csapat[1:])), sep='')

with open('./adatok/E_csoport_állás.txt', 'w', encoding='utf-8') as celfajl:
    print('', file=celfajl)
    for csapat in pontokszerint:
        print(csapat[0], ': ', ', '.join(map(str, csapat[1:])), sep='', file=celfajl)