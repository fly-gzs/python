'''
Készíts egy programot, amely az IPinfo és a IPify nevű API-ok együttes felhasználásával adatokat
ír ki a felhasználó akktuális IP címéről.
'''


import requests
from pprint import pprint


import requests
from pprint import pprint

def ip_address(ip_):
    url = 'https://ipinfo.io/' + ip_ + '/geo'
    resp = requests.get(url)
    ip = resp.json()['ip']
    try:
        hostname = resp.json()['hostname']
    except:
        hostname = 'Nincs adat!'
    city = resp.json()['city']
    region = resp.json()['region']
    country = resp.json()['country']
    loc = resp.json()['loc']
    org = resp.json()['org']
    postal = resp.json()['postal']
    timezone = resp.json()['timezone']
    readme = resp.json()['readme']
    return ip, hostname, city, region, country, loc, org, postal, timezone, readme

url = 'https://api.ipify.org/?format=json'
resp = requests.get(url)
ip_cim = resp.json()['ip']

with open(f'./adatok/Own_IP_{ip_cim}.txt', 'w', encoding='utf-8') as celfajl:
    print(f'Az általad megadott IP cím adatai:', file=celfajl)
    print(f'IP cím: {ip_address(ip_cim)[0]}', file=celfajl)
    print(f'Hostnév: {ip_address(ip_cim)[1]}', file=celfajl)
    print(f'Város: {ip_address(ip_cim)[2]}', file=celfajl)
    print(f'Megye: {ip_address(ip_cim)[3]}', file=celfajl)
    print(f'Ország kód: {ip_address(ip_cim)[4]}', file=celfajl)
    print(f'Földrajzi koordináták: {ip_address(ip_cim)[5]}', file=celfajl)
    print(f'Szolgáltató: {ip_address(ip_cim)[6]}', file=celfajl)
    print(f'Irányítószám: {ip_address(ip_cim)[7]}', file=celfajl)
    print(f'Időzóna: {ip_address(ip_cim)[8]}', file=celfajl)
    print(f'Info: {ip_address(ip_cim)[9]}', file=celfajl)

print(f'Az általad megadott IP cím adatai:')
print(f'IP cím: {ip_address(ip_cim)[0]}')
print(f'Hostnév: {ip_address(ip_cim)[1]}')
print(f'Város: {ip_address(ip_cim)[2]}')
print(f'Megye: {ip_address(ip_cim)[3]}')
print(f'Ország kód: {ip_address(ip_cim)[4]}')
print(f'Földrajzi koordináták: {ip_address(ip_cim)[5]}')
print(f'Szolgáltató: {ip_address(ip_cim)[6]}')
print(f'Irányítószám: {ip_address(ip_cim)[7]}')
print(f'Időzóna: {ip_address(ip_cim)[8]}')
print(f'Info: {ip_address(ip_cim)[9]}')
