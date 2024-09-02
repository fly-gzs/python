meccsek = []
with open('./adatok/B_meccsek.txt', 'r', encoding='utf-8') as forrasfajl:
    forrasfajl.readline()
    for sor in forrasfajl:
        adatok = sor.strip().split(', ')
        meccs1 = [adatok[0], adatok[1], adatok[2]]
        meccsek.append(meccs1)
print(meccsek)

szamlalo = 0
for csapat1, csapat2, eredmeny in meccsek:
    szamlalo += 1
    if eredmeny == '-':
        x = input(f'{csapat1} - {csapat2}: ')
        meccsek[szamlalo-1][2] = x

print(meccsek)

with open('./adatok/B_meccsek.txt', 'w', encoding='utf-8') as celfajl:
    print('', file=celfajl)
    for csapat1, csapat2, eredmeny in meccsek:
        if eredmeny != '-':
            print(f"{csapat1}, {csapat2}, {eredmeny}", file=celfajl)
        else:
            print(f"{csapat1}, {csapat2}, {eredmeny}", file=celfajl)
            print(f'A {csapat1} - {csapat2} meccs még nem került megrendezésre!')

