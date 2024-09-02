def gk(csapat):
    return csapat[6]
def pontok(csapat):
    return csapat[-1]

tablazat = []
tablazat2 = []
tablazat3 = []
meccsek = []

C_csoport = ['Szlovénia', 'Dánia', 'Szerbia', 'Anglia']

with open('./adatok/C_csoport.txt', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        csoport_adatok = {
            'Szlovénia': {'meccs':int(adatok[1]), 'gyozelem':int(adatok[2]), 'dontetlen':int(adatok[3]), 'vereseg':int(adatok[4]), 'rugott_gol':int(adatok[5]), 'kapott_gol':int(adatok[6]), 'pont':int(adatok[7])},
            'Dánia': {'meccs':int(adatok[1]), 'gyozelem':int(adatok[2]), 'dontetlen':int(adatok[3]), 'vereseg':int(adatok[4]), 'rugott_gol':int(adatok[5]), 'kapott_gol':int(adatok[6]), 'pont':int(adatok[7])},
            'Szerbia':{'meccs':int(adatok[1]), 'gyozelem':int(adatok[2]), 'dontetlen':int(adatok[3]), 'vereseg':int(adatok[4]), 'rugott_gol':int(adatok[5]), 'kapott_gol':int(adatok[6]), 'pont':int(adatok[7])},
            'Anglia': {'meccs':int(adatok[1]), 'gyozelem':int(adatok[2]), 'dontetlen':int(adatok[3]), 'vereseg':int(adatok[4]), 'rugott_gol':int(adatok[5]), 'kapott_gol':int(adatok[6]), 'pont':int(adatok[7])}
            }


with open('./adatok/C_meccsek.txt', 'r', encoding='utf-8') as forrasfajl:
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

print('\n--- Az "C" csoport rendezés nélkül: ---')
for csapat in C_csoport:
    print(f"{csapat}: {csoport_adatok[csapat]['meccs']}, {csoport_adatok[csapat]['gyozelem']}, {csoport_adatok[csapat]['dontetlen']}, {csoport_adatok[csapat]['vereseg']}, {csoport_adatok[csapat]['rugott_gol']}-{csoport_adatok[csapat]['kapott_gol']}, {csoport_adatok[csapat]['rugott_gol'] - csoport_adatok[csapat]['kapott_gol']}, {csoport_adatok[csapat]['pont']} ")
    
with open('./adatok/C_csoport_masolat.txt', 'w', encoding='utf-8') as celfajl:
    print('', file=celfajl)
    for csapat in C_csoport:
        print(f"{csapat},{csoport_adatok[csapat]['meccs']},{csoport_adatok[csapat]['gyozelem']},{csoport_adatok[csapat]['dontetlen']},{csoport_adatok[csapat]['vereseg']},{csoport_adatok[csapat]['rugott_gol']}-{csoport_adatok[csapat]['kapott_gol']},{csoport_adatok[csapat]['rugott_gol'] - csoport_adatok[csapat]['kapott_gol']},{csoport_adatok[csapat]['pont']} ", file=celfajl)

with open('./adatok/C_csoport_masolat.txt', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        tablazat.append(adatok)
print('\n')


gkszerint = sorted(tablazat, key=gk, reverse=True)

print('\n--- Az "C" csoport gólkülönbség szerint: ---')
for csapat in gkszerint:
    print(csapat[0] + ', ' + csapat[1] + ', ' + csapat[2] + ', ' + csapat[3] + ', ' + csapat[4] + ', ' + csapat[5] + ', ' + csapat[6] + ', ' + csapat[7])
    
with open('./adatok/C_csoport_gk.txt', 'w', encoding='utf-8') as celfajl:
    print('', file=celfajl)
    for csapat in gkszerint:
        print(csapat[0] + ',' + csapat[1] + ',' + csapat[2] + ',' + csapat[3] + ',' + csapat[4] + ',' + csapat[5] + ',' + csapat[6] + ',' + csapat[7], file=celfajl)
print('\n')

with open('./adatok/C_csoport_gk.txt', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok1 = sor.strip().split(',')
        tablazat2.append(adatok1)

abc = sorted(tablazat2)

print('\n--- Az "C" csoport abc szerint: ---')
for csapat in abc:
    print(csapat[0] + ', ' + csapat[1] + ', ' + csapat[2] + ', ' + csapat[3] + ', ' + csapat[4] + ', ' + csapat[5] + ', ' + csapat[6] + ', ' + csapat[7])
    
with open('./adatok/C_csoport_abc.txt', 'w', encoding='utf-8') as celfajl:
    print('', file=celfajl)
    for csapat in abc:
        print(csapat[0] + ',' + csapat[1] + ',' + csapat[2] + ',' + csapat[3] + ',' + csapat[4] + ',' + csapat[5] + ',' + csapat[6] + ',' + csapat[7], file=celfajl)
print('\n')

with open('./adatok/C_csoport_abc.txt', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok1 = sor.strip().split(',')
        tablazat3.append(adatok1)

pontokszerint = sorted(tablazat3, key=pontok, reverse=True)

print('\n--- Az "C" csoport pontok, gólkülönbség és abc szerint: ---')
for csapat in pontokszerint:
    print(csapat[0], ': ', ', '.join(map(str, csapat[1:])), sep='')

with open('./adatok/C_csoport_állás.txt', 'w', encoding='utf-8') as celfajl:
    print('', file=celfajl)
    for csapat in pontokszerint:
        print(csapat[0], ': ', ', '.join(map(str, csapat[1:])), sep='', file=celfajl)