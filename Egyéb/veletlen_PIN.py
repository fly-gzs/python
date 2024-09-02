import random

PIN_halmaz = set()
PIN_lista = []
while len(PIN_halmaz) < 10:
    veletlen_szam = random.randint(1000,9999)
    PIN_lista.append(veletlen_szam)
    PIN_halmaz.add(veletlen_szam)
PIN_lista.sort()
# print('Rendezett lista: ', PIN_lista)
# print('A generált számok mennyisége: ' + str(len(PIN_lista)) + ' db.')
# print('Eredeti halmaz: ', PIN_halmaz)
PIN = sorted(PIN_halmaz)
print('---------------------------------------------------------------')
print('Az eredeti PIN lista növekvő sorrendben: ', PIN)
print('A generált számok mennyisége: ' + str(len(PIN)) + ' db.')
print('---------------------------------------------------------------')
print('5 db PIN kód hozzáfűzése:')
while len(PIN_halmaz) < 15:
    veletlen_szam = random.randint(1000,9999)
    PIN_lista.append(veletlen_szam)
    PIN_halmaz.add(veletlen_szam)
PIN = sorted(PIN_halmaz)
print('A bővített PIN lista növekvő sorrendben: ', PIN)
print('A PIN kódok száma a bővítés után: ' + str(len(PIN)) + ' db.')