from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import google.auth
from googleapiclient.discovery import build
import base64
from email.message import EmailMessage
from pprint import pprint
import json
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def get_service():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('./google/token_send.json'):
        creds = Credentials.from_authorized_user_file('./google/token_send.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './google/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('./google/token_send.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    return service


def send_message(service):
    message = EmailMessage()

    message.set_content('alma\n'
                        'barack\n'
                        'dinnye\n')

    message['To'] = 'zsolt.gondocs@forrodrot.hu'
    message['From'] = 'zsolt.gondocs@gmail.com'
    message['Subject'] = 'Próba üzenet!'

    print(message)

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    with open('./adatok/encoded_message.json', 'w') as kimenet:
        json.dump(encoded_message, kimenet, indent=2)

    create_message = {
        'raw': encoded_message
    }

    with open('./adatok/create_message.json', 'w') as kimenet:
        json.dump(create_message, kimenet, indent=2)

    send_message = (service.users().messages().send(userId="me", body=create_message).execute())
    print(F'Message Id: {send_message["id"]}')


def main():
    service = get_service()
    send_message(service)


main()
