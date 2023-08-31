from __future__ import print_function
import json

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/calendar.events'
]

config_file = "config.json"
with open(config_file, encoding="utf-8") as f:
    config = json.load(f)


class GoogleAPIHandler:

    def __init__(self):
        self._creds = None

    def _get_access_token(self):
        if os.path.exists('token.json'):
            self._creds = Credentials.from_authorized_user_file(
                'token.json', SCOPES)
        if not self._creds or not self._creds.valid:
            if self._creds and self._creds.expired and self._creds.refresh_token:
                self._creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self._creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(self._creds.to_json())

        return True

    def get_calendar_list(self):
        self._get_access_token()
        try:
            service = build('calendar', 'v3', credentials=self._creds)
            page_token = None
            while True:
                cal_list = service.calendarList().list(
                    pageToken=page_token
                ).execute()
                for calendar_entry in cal_list['items']:
                    print(json.dumps(calendar_entry['id'], indent=4))
                page_token = cal_list.get('nextPageToken')
                if not page_token:
                    break
        except HttpError as error:
            print(f'Something went wrong {error}')

    def add_event_when_programming_session_is_complete(self, body):
        self._get_access_token()
        try:
            service = build('calendar', 'v3', credentials=self._creds)
            event = service.events().insert(
                calendarId=config.get("calendarId", ""), body=body
            ).execute()
            print(f'Event created: {event.get("htmlLink")}')

        except HttpError as error:
            print(f"Something went wrong {error}")
