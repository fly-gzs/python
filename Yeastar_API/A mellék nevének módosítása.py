import requests
import json
import hashlib

ip = input('IP (192.168.2.150): ')
if ip == '':
    ip = '192.168.2.150'
print(ip)
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
# Kielo2ph = "password": "453e4dac79acb3fe87590b24e1a26dd7"
# Jelszo1590 = "password": "1ed5697871c128ad8050309c1923fecf"
ext_number = input('Mellékszám: ')
ext_username = input('Név: ')


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

if login_response.status_code == 200:
    token = login_response.json().get("token")
    print("Sikeres kapcsolat a telefonközponttal! Token:", token)
    if token == None:
        print('Hibás logon password! Nincs token!')
else:
    print(f"Hiba történt bejelentkezéskor: {login_response.status_code} - {login_response.text}")
    token = None

# Ha sikerült a bejelentkezés, folytatjuk a mellék módosítását
if token:
    # API végpont a mellék módosításához
    update_url = f"http://{ip}/api/v2.0.0/extension/update?token={token}"
    update_headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    # Adatok a mellék módosításához
    update_payload = {
        "number": ext_number,                         # API v1.1.0 esetén: "extid"
        "username": ext_username
    }

    # POST kérés küldése a mellék módosításához
    update_response = requests.post(update_url, headers=update_headers, data=json.dumps(update_payload))


    # Az API válaszának kiértékelése
    if update_response.json()['status'] == 'Success':
        print(f"Az {update_payload['number']} számú mellék átnevezve: {update_payload['username']}")
    else:
        print(f"Hiba történt a mellék módosításakor")
