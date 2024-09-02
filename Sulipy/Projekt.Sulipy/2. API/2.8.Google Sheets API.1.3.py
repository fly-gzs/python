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

def nincs_ekezet(nev):
    ekezet = 'áéíóöőúüű'
    no_ekezet = 'aeiooouuu'
    ekezet_nelkul = ''
    for betu in nev:
        if betu in ekezet:
            for idx1, karakter in enumerate(ekezet):
                if betu == karakter:
                    betu = no_ekezet[idx1]
                    break
        ekezet_nelkul += betu
    return ekezet_nelkul

gc = gspread.service_account(filename='./google/projektsulipy-f9eed1f76c3d.json')

sheet1 = gc.open('diakok').worksheet('Munkalap1')

tablazat_lista = sheet1.get_all_records()
e_mail_lista_kisbetus = []
for nev in tablazat_lista:
    vezeteknev = nev['vezetéknév']
    keresztnev = nev['keresztnév']
    e_mail_kisbetus = f'{vezeteknev}.{keresztnev}@x-mail.com'
    e_mail_lista_kisbetus.append(e_mail_kisbetus.lower())

e_mail_lista = []
for e_mail_jo in e_mail_lista_kisbetus:
    e_mail_lista.append(nincs_ekezet(e_mail_jo))

sheet1.update_cell(1, 3, 'e_mail')
for idx, e_mail in enumerate(e_mail_lista):
    print(idx, e_mail)
    sheet1.update_cell(idx+2, 3, e_mail)

