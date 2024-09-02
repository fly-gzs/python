'''
Alakítsd át a videóban látott kódot az alábbiak szerint:
- távolítsd el a kívételkezelést
- készíts egy get_service() nevű függvényt, amely biztosítja az autorizációt, és a service objektummal tér vissza
- készíts egy get_labels() nevű függvényt, amely a cimkék (labels) listájával tér vissza!
'''

from __future__ import print_function

import os.path
from pprint import pprint

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_labels(cimkek):
    cimke_lista = []
    for label in cimkek:
        cimke_lista.append(label)
    return cimke_lista

def get_service():
    creds = None
    if os.path.exists('./google/token.json'):
        creds = Credentials.from_authorized_user_file('./google/token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './google/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('./google/token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    return service

def main():
    results = get_service().users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
        return
    print('Labels:')
    
    cimke_lista_visszatero = (get_labels(labels))
    for label in cimke_lista_visszatero:
        print(label['name'])


if __name__ == '__main__':
    main()