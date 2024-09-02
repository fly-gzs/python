import json

szotar = {}
filmlista = []
with open('./adatok/lista.txt', encoding='utf-8') as forrasfajl:
    sorok = forrasfajl.readlines()

teljes_lista = []
for i in range(0,len(sorok),5):
    elem = {
        'datum': sorok[i].strip(),
        'sorozat': sorok[i+1].strip(),
        'epizod': sorok[i+2].strip(),
        'hossz': sorok[i+3].strip(),
    }
    if sorok[i+4].strip() == '1':
        elem['latta'] = True
    else:
        elem['latta'] = False

    teljes_lista.append(elem)
print(teljes_lista)
szotar['sorozatok'] = teljes_lista
print(szotar)

for sorozat in szotar['sorozatok']:
    print(sorozat)

with open('./adatok/json_lista.txt', 'w', encoding='utf-8') as celfajl:
  json.dump(szotar, celfajl, indent=2)

