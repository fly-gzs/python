'''
A kiválasztott indexű e-mail tartalmának kiíratása képernyőre. (id=msg_ids[ide beírva az indexet])
Vigyázat!!!
Az üzenet felépításe nem minden esetben azonos. E-mail-enként változhat.
A json fájlban látszik, hogy az üzenet szövege más-más lista és szótár formátumokban található.
pl: message["payload"]["parts"][0]["parts"][0]["body"]["data"]
'''

from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from pprint import pprint
import json
import base64

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


    message = service.users().messages().get(userId='me', id=msg_ids[6], format='full').execute()
    # headers = message['payload']['headers']
    with open('./adatok/uzenet.json', 'w') as kimenet:
        json.dump(message, kimenet, indent=2)

    m1 = message["payload"]["parts"][0]["body"]["data"]
    with open('./adatok/uzenet2.json', 'w') as kimenet:
        json.dump(m1, kimenet, indent=2)
    data = base64.urlsafe_b64decode(m1).decode("utf-8")
    print(data)


def main():
    service = get_service()
    get_messages(service)


main()
    