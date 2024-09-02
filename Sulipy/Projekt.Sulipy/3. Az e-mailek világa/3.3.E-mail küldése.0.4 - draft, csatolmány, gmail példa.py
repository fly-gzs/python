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


def gmail_create_draft_with_attachment(service):
    """Create and insert a draft email with attachment.
    Print the returned draft's message and id.
    Returns: Draft object, including draft id and message meta data.

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    try:
        # create gmail api client
        mime_message = EmailMessage()

        # headers
        mime_message["To"] = "zsolt.gondocs@forrodrot.hu"
        mime_message["From"] = "zsolt.gondocs@gmail.com"
        mime_message["Subject"] = "Üzenet csatolmánnyal"

        # text
        mime_message.set_content(
            "Hi, this is automated mail with attachment.Please do not reply."
        )

        # attachment
        attachment_filename = "./adatok/OpenWRT.txt"
        # guessing the MIME type
        type_subtype, _ = mimetypes.guess_type(attachment_filename)
        maintype, subtype = type_subtype.split("/")

        with open(attachment_filename, "rb") as fp:
            attachment_data = fp.read()
        mime_message.add_attachment(attachment_data, maintype, subtype)

        encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()

        create_draft_request_body = {"message": {"raw": encoded_message}}

        # pylint: disable=E1101
        draft = (
            service.users()
            .drafts()
            .create(userId="me", body=create_draft_request_body)
            .execute()
        )
        print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')
        sent_message = service.users().drafts().send(userId="me", body={"id": draft['id']}).execute()
        print(f'Sent message ID: {sent_message["id"]}')
    except HttpError as error:
        print(f"An error occurred: {error}")
        draft = None

    return draft


def build_file_part(file):
    """Creates a MIME part for a file.

    Args:
    file: The path to the file to be attached.

    Returns:
    A MIME part that can be attached to a message.
    """
    content_type, encoding = mimetypes.guess_type(file)

    if content_type is None or encoding is not None:
        content_type = "application/octet-stream"
    main_type, sub_type = content_type.split("/", 1)
    if main_type == "text":
        with open(file, "rb"):
            msg = MIMEText("r", _subtype=sub_type)
    elif main_type == "image":
        with open(file, "rb"):
            msg = MIMEImage("r", _subtype=sub_type)
    elif main_type == "audio":
        with open(file, "rb"):
            msg = MIMEAudio("r", _subtype=sub_type)
    else:
        with open(file, "rb"):
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(file.read())
    filename = os.path.basename(file)
    msg.add_header("Content-Disposition", "attachment", filename=filename)
    return msg


if __name__ == "__main__":
    service = get_service()
    gmail_create_draft_with_attachment(service)