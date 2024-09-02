import requests
import json
import time
from datetime import datetime
import hashlib

# A Yeastar alközpont IP címe
ip = input('IP (192.168.2.150): ')
if ip == '':
    ip = '192.168.2.150'
print(ip)

# Felhasználónév a Yeastar API-hoz (Settings > PBX > General > API)
login_username = input('Username (api): ')
if login_username == '':
    login_username = 'api'
print(login_username)

# Belépési jelszó a Yeastar API-hoz (Settings > PBX > General > API)
login_password = input('Password (Jelszo1590 - md5): ')
'''
Ha a Yeastar API belépési kódja csak egy 'ENTER', akkor a login_password automatikusan a Jelszo1590 md5 kódja lesz.
Egyéb esetben a 'hashlib' könyvtár meghívása után generálódik le a beadott
Yeastar API belépési kód hash objektumának HEXA md5 kódja.
'''

if login_password == '':
    login_password = "1ed5697871c128ad8050309c1923fecf"
    print(login_password)
else:
    result = hashlib.md5(login_password.encode())
    # A hash átalakítása HEXA kóddá
    login_password = result.hexdigest()
    print(login_password)

# A lekérdezni kívánt mellék (defaul: all)
ext_number = input('Mellékszám (all): ')
if ext_number == '':
    ext_number = 'all'
print(ext_number)

# Eltelt pillanatok 1970 január 1 12:00 óra óta
now = time.time()

# Kezdő és vége dátum/idő beállítása
start_date = input('Start dátum (mai dátum): ')
if start_date == '':
    start_date = datetime.fromtimestamp(now).strftime('%Y-%m-%d')   # Az 1970 január 1 12:00 óra óta eltelt másodpercek átalakítása
print(start_date)
start_time = input('Start idő (00:00:00): ')
if start_time == '':
    start_time = '00:00:00'
print(start_time)
starttime = start_date + ' ' + start_time
print(f'A lekérdezés kezdő időpontja: {starttime}')
end_date = input('Vége dátum (mai dátum): ')
if end_date == "":
    end_date = datetime.fromtimestamp(now).strftime('%Y-%m-%d')     # Az 1970 január 1 12:00 óra óta eltelt másodpercek átalakítása
print(end_date)
end_time = input('Vége idő (23:59:59): ')
if end_time == '':
    end_time = '23:59:59'
print(end_time)
endtime = end_date + ' ' + end_time
print(f'A lekérdezés vége időpont: {endtime}')

# API végpont és fejlécek beállítása a bejelentkezéshez
login_url = f"http://{ip}/api/v2.0.0/login"
login_headers = {
    "Content-Type": "application/json; charset=utf-8"
}

# Autentikációs adatok
login_payload = {
    "username": login_username,
    "password": login_password,
    "port": "8260",
    "version": "2.0.0"
}

# Bejelentkezés az API-ba
login_response = requests.post(login_url, headers=login_headers, data=json.dumps(login_payload))

# Sikeres válasz esetén megkapjuk az aktuális token-t
if login_response.status_code == 200:
    token = login_response.json().get("token")
    print("Sikeres bejelentkezés! Token:", token)
else:
    print(f"Hiba történt bejelentkezéskor: {login_response.status_code} - {login_response.text}")
    token = None

# Ha sikerült a bejelentkezés, folytatjuk a mellék módosítását
if token:                                             # True
    # API végpont a CDR lekéréséhez
    update_url = f"http://{ip}/api/v2.0.0/cdr/get_random?token={token}"
    update_headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    update_payload = {
        "number": ext_number,                         # összes mellék: "number": "all"
        "starttime": starttime,
        "endtime": endtime
    }

    # POST kérés küldése a CDR kéréshez
    update_response = requests.post(update_url, headers=update_headers, data=json.dumps(update_payload))

    # Az API válaszának kiértékelése
    if update_response.status_code == 200:
        print("A random kód sikeresen lekérve!")
        update_response = update_response.json()
        print(f"Állapot: {update_response['status']}")
        if update_response['status'] == 'Success':
            print(f"Mellékszám: {update_response['number']}")
            print(f"Lekérés kezdete: {update_response['starttime']}")
            print(f"Lekérés vége: {update_response['endtime']}")
            random_code = update_response['random']
            print(f"Random kód a webes letöltéshez: {random_code}")
            download_url = f'https://{ip}:8088/api/v2.0.0/cdr/download?number={ext_number}&starttime={start_date}%20{start_time}&endtime={end_date}%20{end_time}&token={token}&random={random_code}'
            print(download_url)
        else:
            print('Nincs adat!')
    else:
        print(f"Hiba történt a mellék módosításakor: {update_response.status_code} - {update_response.text}")

# A random kód lekérése után a következő url-t kell megnyitni egy bőngészőben, amely letölti a .csv fájl-t.
# A token és random kódot aktualizálni kell!
# https://192.168#.2.150:8088/api/v2.0.0/cdr/download?number=12&starttime=2024-08-09%2000:00:00&endtime=2024-08-09%2023:59:59&token=556abc0f23ecb67a1bbc3b2364ea27bf&random=556abc0f23ecb67a1bbc3b2364ea27bf