'''
Az e-mail kiíratása az "uzenet.json" fájlba
'''
from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from pprint import pprint
import json


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_service():
    creds = None
    if os.path.exists('./google/token_read.json'):
        creds = Credentials.from_authorized_user_file('./google/token_read.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './google/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('./google/token_read.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    return service


def get_messages(service):
    results = service.users().messages().list(userId='me').execute()
    msg_ids = []
    for msg in results['messages']:
        msg_ids.append(msg['id'])
    print(msg_ids)
    print(len(msg_ids))
    for index in range(1):
        message = service.users().messages().get(userId='me', id=msg_ids[12], format='full').execute()
        # headers = message['payload']['headers']
        with open('./adatok/uzenet.json', 'w') as kimenet:
            json.dump(message, kimenet, indent=2)
        # for header in headers:
        #     if header['name'] == 'From':
        #         print(f'From: {header["value"]}')
        #     elif header['name'] == 'Subject':
        #         print(f'Subject: {header["value"]}')
        #     elif header['name'] == 'Date':
        #         print(f'\nDate: {header["value"]}')
        # print(f"Üzenet: {message['snippet']}")

def main():
    service = get_service()
    get_messages(service)


main()
    