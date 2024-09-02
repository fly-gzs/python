import random

lotto_halmaz = set()
lista = []
while len(lotto_halmaz) < 5:
    veletlen_szam = random.randint(1,90)
    lista.append(veletlen_szam)
    lotto_halmaz.add(veletlen_szam)
lista.sort()
print('Rendezett lista: ', lista)
print('A generált számok mennyisége: ' + str(len(lista)) + ' db.')
print('Eredeti halmaz: ', lotto_halmaz)
lotto = sorted(lotto_halmaz)
print('---------------------------------------------------------------')
print('A véletlen lottószámok növekvő sorrendben: ', lotto)

