from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import base64
import mimetypes
import os
from email.message import EmailMessage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://mail.google.com/']

def get_service():
    creds = None
    if os.path.exists('./google/token_send.json'):
        creds = Credentials.from_authorized_user_file('./google/token_send.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './google/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('./google/token_send.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    return service


def send_draft(service, draft_id):
    """Send an existing draft."""
    try:
        # Send the draft
        sent_message = service.users().drafts().send(userId="me", body={"id": draft_id}).execute()
        print(f'Sent message ID: {sent_message["id"]}')
        return sent_message
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None


def gmail_create_and_send_draft_with_attachment(service):
    """Create and send a draft email with attachment."""
    try:
        mime_message = EmailMessage()

        # headers
        mime_message["To"] = "zsolt.gondocs@forrodrot.hu"
        mime_message["From"] = "zsolt.gondocs@gmail.com"
        mime_message["Subject"] = "Üzenet csatolmánnyal"

        # text
        mime_message.set_content(
            "Hi, this is an automated mail with an attachment. Please do not reply."
        )

        # attachment
        attachment_filename = "./adatok/OpenWRT.txt"
        type_subtype, _ = mimetypes.guess_type(attachment_filename)
        maintype, subtype = type_subtype.split("/")

        with open(attachment_filename, "rb") as fp:
            attachment_data = fp.read()
        mime_message.add_attachment(attachment_data, maintype, subtype)

        # Create the draft
        encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()
        create_draft_request_body = {"message": {"raw": encoded_message}}
        draft = service.users().drafts().create(userId="me", body=create_draft_request_body).execute()

        # Send the draft
        send_draft(service, draft["id"])

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    service = get_service()
    gmail_create_and_send_draft_with_attachment(service)
