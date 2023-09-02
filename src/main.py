import time
from google_api_handler import GoogleAPIHandler


google_api_handler = GoogleAPIHandler()


def ask_user_when_to_start():
    started_seconds = time.time()

    while True:
        user_input = input('Do you want to end (y/n): ').lower()
        if user_input == 'y':
            break
    stopped_seconds = time.time()

    return started_seconds, stopped_seconds


def convert_time_to_required_datetime():

    summary = input('What are you gonna be doing today: ')

    started, stopped = ask_user_when_to_start()

    started_date = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(started))
    stopped_date = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(stopped))

    body = {
        'summary': summary,
        'start': {
            'dateTime': started_date,
            'timeZone': 'Europe/London'
        },
        'end': {
            'dateTime': stopped_date,
            'timeZone': 'Europe/London'
        }
    }

    print(f"Started {summary} session")

    google_api_handler.add_event_when_session_is_complete(body)


convert_time_to_required_datetime()
