'''
Egyenlő vs azonos
'''


# str - immutábilis (megváltoztathatatlan)
szo_1 = 'alma'
szo_2 = 'alma'

print('szo_1 id:', id(szo_1))  # szo_1 id: 2809970279600
print('szo_2 id:', id(szo_2))  # szo_2 id: 2809970279600

print('szo_1 == szo_2', szo_1 == szo_2)  # szo_1 == szo_2 True
print('szo_1 is szo_2', szo_1 is szo_2)  # szo_1 is szo_2 True
print()


# list - mutábilis (megváltoztatatható)
lista_1 = ['alma', 'körte']
lista_2 = ['alma', 'körte']

print('lista_1 id:', id(lista_1))  # lista_1 id: 2809970241408
print('lista_2 id:', id(lista_2))  # lista_2 id: 2809970681088

print('lista_1 == lista_2', lista_1 == lista_2)  # lista_1 == lista_2 True
print('lista_1 is lista_2', lista_1 is lista_2)  # lista_1 is lista_2 False