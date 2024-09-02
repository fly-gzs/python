'''
A mellékelt táblázat tartalmát először másold át egy Google-táblázatba! Készíts egy programot, amely ezt a
Google-táblázatot kiegészíti a felhasználók automatikusan generált e-mail címével,
melyben az ékezetes betűk ékezet nélkülivé vannak alakítva.
Az e-mail cím felépítése: vezeteknev.keresztnev@x_mail.com
Az adatbeolvasás dinamikusan történjen, tehát a program maga határozza meg az adatsorok számát!
Ügyelj arra is, hogy optimalizáld az API-hívások számát!
'''


import gspread
from pprint import pprint

gc = gspread.service_account(filename='./google/projektsulipy-f9eed1f76c3d.json')

sheet1 = gc.open('diakok').worksheet('Munkalap1')

tablazat_lista = sheet1.get_all_records()
e_mail_lista_rossz = []
for nev in tablazat_lista:
    vezeteknev = nev['vezetéknév']
    keresztnev = nev['keresztnév']
    e_mail_rossz = f'{vezeteknev}.{keresztnev}@x-mail.com'
    e_mail_lista_rossz.append(e_mail_rossz)
# print(e_mail_lista_rossz)

def nincs_ekezet(nev):
    ekezet_nelkul = ''
    for betu in nev:
        if betu == 'á':
            betu = 'a'
        if betu == 'é':
            betu = 'e'
        if betu == 'í':
            betu = 'i'
        if betu == 'ó':
            betu = 'o'
        if betu == 'ö':
            betu = 'o'
        if betu == 'ő':
            betu = 'o'
        if betu == 'ú':
            betu = 'u'
        if betu == 'ü':
            betu = 'u'
        if betu == 'ű':
            betu = 'u'
        ekezet_nelkul += betu
    return ekezet_nelkul

e_mail_lista = []
for e_mail_jo in e_mail_lista_rossz:
    e_mail_jo = e_mail_jo.lower()
    e_mail_lista.append(nincs_ekezet(e_mail_jo))
# print(e_mail_lista)

sheet1.update_cell(1, 3, 'e_mail')
for idx, e_mail in enumerate(e_mail_lista):
    print(idx, e_mail)
    sheet1.update_cell(idx+2, 3, e_mail)

