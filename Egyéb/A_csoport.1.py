A1 = 'Németország'
A2 = 'Skócia'
A3 = 'Magyarország'
A4 = 'Svájc'

A1meccs = 0
A2meccs = 0
A3meccs = 0
A4meccs = 0
A1pont = 0
A2pont = 0
A3pont = 0
A4pont = 0
A1gyozelem = 0
A2gyozelem = 0
A3gyozelem = 0
A4gyozelem = 0
A1dontetlen = 0
A2dontetlen = 0
A3dontetlen = 0
A4dontetlen = 0
A1vereseg = 0
A2vereseg = 0
A3vereseg = 0
A4vereseg = 0
A1rugott = 0
A1kapott =0
A2rugott = 0
A2kapott =0
A3rugott = 0
A3kapott =0
A4rugott = 0
A4kapott =0
germany = []
scotland = []
hungary = []
switzerland = []
allas = {}
A1A2= input(f'{A1} - {A2} ')
A3A4= input(f'{A3} - {A4} ')
A1A3= input(f'{A1} - {A3} ')
A2A4= input(f'{A2} - {A4} ')
A2A3= input(f'{A2} - {A3} ')
A4A1= input(f'{A4} - {A1} ')
if A1A2 != '':
    A1meccs += 1
    A2meccs += 1
    A1rugott += int(A1A2[0])
    A1kapott += int(A1A2[2])
    A1golkulonbseg = A1rugott - A1kapott
    A2rugott += int(A1A2[2])
    A2kapott += int(A1A2[0])
    A2golkulonbseg = A2rugott - A2kapott
    if A1A2[0] > A1A2[2]:
        A1pont += 3
        A1gyozelem += 1
        A2vereseg += 1
    elif A1A2[0] < A1A2[2]:
        A2pont += 3
        A2gyozelem += 1
        A1vereseg += 1
    else:
        A1pont += 1
        A2pont += 1
        A1dontetlen += 1
        A2dontetlen += 1
else:
    print(f'A {A1} - {A2} meccs még nem került megrendezésre!')

if A3A4 != '':
    A3meccs += 1
    A4meccs += 1
    A3rugott += int(A3A4[0])
    A3kapott += int(A3A4[2])
    A3golkulonbseg = A3rugott - A3kapott
    A4rugott += int(A3A4[2])
    A4kapott += int(A3A4[0])
    A4golkulonbseg = A4rugott - A4kapott
    if A3A4[0] > A3A4[2]:
        A3pont += 3
        A3gyozelem += 1
        A4vereseg += 1
    elif A3A4[0] < A3A4[2]:
        A4pont += 3
        A4gyozelem += 1
        A3vereseg += 1
    else:
        A3pont += 1
        A4pont += 1
        A3dontetlen += 1
        A4dontetlen += 1
else:
    print(f'A {A3} - {A4} meccs még nem került megrendezésre!')

if A1A3 != '':
    A1meccs += 1
    A3meccs += 1
    A1rugott += int(A1A3[0])
    A1kapott += int(A1A3[2])
    A1golkulonbseg = A1rugott - A1kapott
    A3rugott += int(A1A3[2])
    A3kapott += int(A1A3[0])
    A3golkulonbseg = A3rugott - A3kapott
    if A1A3[0] > A1A3[2]:
        A1pont += 3
        A1gyozelem += 1
        A3vereseg += 1
    elif A1A3[0] < A1A3[2]:
        A3pont += 3
        A3gyozelem += 1
        A1vereseg += 1
    else:
        A1pont += 1
        A3pont += 1
        A1dontetlen += 1
        A3dontetlen += 1
else:
    print(f'A {A1} - {A3} meccs még nem került megrendezésre!')

if A2A4 != '':
    A2meccs += 1
    A4meccs += 1
    if A2A4[0] > A2A4[2]:
        A2pont += 3
        A2gyozelem += 1
        A4vereseg += 1
    elif A2A4[0] < A2A4[2]:
        A4pont += 3
        A4gyozelem += 1
        A2vereseg += 1
    else:
        A2pont += 1
        A4pont += 1
        A2dontetlen += 1
        A4dontetlen += 1
else:
    print(f'A {A2} - {A4} meccs még nem került megrendezésre!')

if A2A3 != '':
    A2meccs += 1
    A3meccs += 1
    if A2A3[0] > A2A3[2]:
        A2pont += 3
        A2gyozelem += 1
        A3vereseg += 1
    elif A2A3[0] < A2A3[2]:
        A3pont += 3
        A3gyozelem += 1
        A2vereseg += 1
    else:
        A2pont += 1
        A3pont += 1
        A2dontetlen += 1
        A3dontetlen += 1
else:
    print(f'A {A2} - {A3} meccs még nem került megrendezésre!')

if A4A1 != '':
    A4meccs += 1
    A1meccs += 1
    if A4A1[0] > A4A1[2]:
        A4pont += 3
        A4gyozelem += 1
        A1vereseg += 1
    elif A4A1[0] < A4A1[2]:
        A1pont += 3
        A1gyozelem += 1
        A4vereseg += 1
    else:
        A4pont += 1
        A1pont += 1
        A4dontetlen += 1
        A1dontetlen += 1
else:
    print(f'A {A4} - {A1} meccs még nem került megrendezésre!')

germany.append(A1meccs)
germany.append(A1gyozelem)
germany.append(A1dontetlen)
germany.append(A1vereseg)
germany.append(A1pont)
scotland.append(A1meccs)
scotland.append(A2gyozelem)
scotland.append(A2dontetlen)
scotland.append(A2vereseg)
scotland.append(A2pont)
hungary.append(A3meccs)
hungary.append(A3gyozelem)
hungary.append(A3dontetlen)
hungary.append(A3vereseg)
hungary.append(A3pont)
switzerland.append(A4meccs)
switzerland.append(A4gyozelem)
switzerland.append(A4dontetlen)
switzerland.append(A4vereseg)
switzerland.append(A4pont)
print('\n')
print('--- "A" csoport ---')
print(f'Németország: {germany}')
print(f'Skócia: {scotland}')
print(f'Magyarország: {hungary}')
print(f'Svájc: {switzerland}')

print(f'{A1} gólkülönbség: {A1rugott}-{A1kapott}, {A1golkulonbseg}')