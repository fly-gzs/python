'''
Írj egy programot, amely a felhasználó által megadott két pont koordinátái alapján három
tizedesjegy pontossággal meghatározza a két pont távolságát, és azt,
hogy melyikük van közelebb az origóhoz! A pontok koordinátáit tuple-ök tárolják,
a programban az egyes részfeladatokat függvények valósítsák meg!
'''

# pont1 = (5,8)
# pont2 = (9,2)
# 
# tavolsag = ((9-5)**2 + (2-8)**2)**0.5
# print(tavolsag)
# print(type(tavolsag))

def calculate_distance(pont1, pont2):
    tavolsag = ((pont2[0]-pont1[0])**2 + (pont2[1]-pont1[1])**2)**0.5
    return round(tavolsag,3)

def origo(pont1, pont2):
    origo_tav1 = (pont1[0]**2 + pont1[1]**2)**0.5
    origo_tav2 = (pont2[0]**2 + pont2[1]**2)**0.5
    if origo_tav1 < origo_tav2:
        return "Az első pont közelebb van origóhoz."
    elif origo_tav2 < origo_tav1:
        return "Az második pont közelebb van origóhoz."
    else:
        return "A két pont egyenlő távolságra van az origótól."

def main():
    x1 = int(input('Add meg az 1. x koordinátát! '))
    y1 = int(input('Add meg az 1. y koordinátát! '))
    x2 = int(input('Add meg az 2. x koordinátát! '))
    y2 = int(input('Add meg az 2. y koordinátát! '))
    pont1 = (x1, y1)
    pont2 = (x2, y2)
    print(pont1)
    print(pont2)
    origo_kozelebb = origo(pont1, pont2)
    tavolsag = calculate_distance(pont1, pont2)
    print(f'A két pont közötti távolság: {tavolsag}')
    print(f'A két pont közötti távolság: {origo_kozelebb}')

main()
