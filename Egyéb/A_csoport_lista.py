A_csoport = ['Németország', 'Skócia', 'Magyarország', 'Svájc']

Németország = ['Németország']
Skócia = ['Skócia']
Magyarország = ['Magyarország']
Svájc = ['Svájc']

A_csoport_meccsek = [('Németország', 'Skócia', input('Németország - Skócia: ')),
          ('Magyarország', 'Svájc', input('Magyarország - Svájc: ')),
          ('Németország', 'Magyarország', input('Németország - Magyarország: ')),
          ('Skócia', 'Svájc', input('Skócia - Svájc: ')),
          ('Skócia', 'Magyarország', input('Skócia - Magyarország: ')),
          ('Svájc', 'Németország', input('Svájc - Németország: '))
]

meccs_csapat1 = 0
def meccs_feldolgozas(csapat1, csapat2, eredmeny):
    gol_csapat1, gol_csapat2 = map(int, eredmeny.split('-'))
    
    csapat1[1].append(meccs_csapat1)
    A_csoport_adatok[csapat1]['meccs'] += 1
    A_csoport_adatok[csapat2]['meccs'] += 1
    A_csoport_adatok[csapat1]['rugott_gol'] += gol_csapat1
    A_csoport_adatok[csapat1]['kapott_gol'] += gol_csapat2
    A_csoport_adatok[csapat2]['rugott_gol'] += gol_csapat2
    A_csoport_adatok[csapat2]['kapott_gol'] += gol_csapat1
    
    if gol_csapat1 > gol_csapat2:
        A_csoport_adatok[csapat1]['gyozelem'] += 1
        A_csoport_adatok[csapat2]['vereseg'] += 1
        A_csoport_adatok[csapat1]['pont'] += 3
    elif gol_csapat1 < gol_csapat2:
        A_csoport_adatok[csapat2]['gyozelem'] += 1
        A_csoport_adatok[csapat1]['vereseg'] += 1
        A_csoport_adatok[csapat2]['pont'] += 3
    else:
        A_csoport_adatok[csapat1]['dontetlen'] += 1
        A_csoport_adatok[csapat2]['dontetlen'] += 1
        A_csoport_adatok[csapat1]['pont'] += 1
        A_csoport_adatok[csapat2]['pont'] += 1
    
for csapat1, csapat2, eredmeny in A_csoport_meccsek:
    if eredmeny:
        meccs_feldolgozas(csapat1, csapat2, eredmeny)
    else:
        print(f'A {csapat1} - {csapat2} meccs még nem került megrendezésre!')
        
print('\n--- Az "A" csoport állása ---')
for csapat in A_csoport:
    print(f"{csapat}: {A_csoport_adatok[csapat]['meccs']}, {A_csoport_adatok[csapat]['gyozelem']}, {A_csoport_adatok[csapat]['dontetlen']}, {A_csoport_adatok[csapat]['vereseg']}, {A_csoport_adatok[csapat]['rugott_gol']}-{A_csoport_adatok[csapat]['kapott_gol']}, {A_csoport_adatok[csapat]['pont']} ")