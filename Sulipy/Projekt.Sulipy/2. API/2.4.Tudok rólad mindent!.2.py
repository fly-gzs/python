'''
Írj egy programot, amely az IPinfo nevű API segítségével adatokat ír ki a felhasználó által megadott IP címről.
'''


import requests
from pprint import pprint

def ip_address(ip_):
    url = 'https://ipinfo.io/' + ip_ + '/geo'
    resp = requests.get(url)
    ip = resp.json()['ip']
    hostname = resp.json()['hostname']
    city = resp.json()['city']
    region = resp.json()['region']
    country = resp.json()['country']
    loc = resp.json()['loc']
    org = resp.json()['org']
    postal = resp.json()['postal']
    timezone = resp.json()['timezone']
    readme = resp.json()['readme']
    return ip, hostname, city, region, country, loc, org, postal, timezone, readme

ip_cim = input('Add meg az IP címet!: ')
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

