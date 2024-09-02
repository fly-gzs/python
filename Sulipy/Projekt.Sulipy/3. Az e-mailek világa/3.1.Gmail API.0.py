from __future__ import print_function

import os.path
from pprint import pprint

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Ha az a scopes módosításra kerül, törölni kell a token.json fájlt.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """A Gmail API alapvető használatát mutatja.
    Felsorolja a felhasználó Gmail-címkéit.
    """
    creds = None
    '''
    A token.json fájl tárolja a felhasználó hozzáférési és frissítési jogkivonatait, 
    és automatikusan létrejön, amikor az engedélyezési folyamat első alkalommal befejeződik.
    '''
    if os.path.exists('./google/token.json'):
        creds = Credentials.from_authorized_user_file('./google/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './google/credentials.json', SCOPES)    # credentials.json (hitelesítő adatok) bármiéyen név lehet
            creds = flow.run_local_server(port=0)
        # Mentsed el a hitelesítő adatokat a következő futtatáshoz
        with open('./google/token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # A Gmail API hívása
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return
        print('Labels:')
        pprint(labels)
        for label in labels:
            print(label['name'])

    except HttpError as error:
        # TODO(developer) - A Gmail API-ból származó hibák kezelése.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()