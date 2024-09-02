import requests
import json

# API végpont és fejlécek beállítása
url = "http://192.168.2.150/api/v2.0.0/login"
headers = {
    "Content-Type": "application/json; charset=utf-8"
}

# Adatok a kérés törzsében
payload = {
    "username": "api",
    "password": "1ed5697871c128ad8050309c1923fecf",
    "port": "8260",
    "version": "2.0.0",
}

# POST kérés küldése az API végpontra
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.text)

# Az API válaszának kiértékelése
if response.status_code == 200:
    print("Sikeres bejelentkezés!")
    print("Válasz:", response.json())
else:
    print(f"Hiba történt: {response.status_code} - {response.text}")
