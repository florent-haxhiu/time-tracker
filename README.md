# Programming Tracker

This is orginally a programming tracker for myself but can be used for anything really just by changing the summary.

## Steps to Start

If you've never used the google apis, I would highly suggest going through their docs as they are pretty good.
This is the [link](https://developers.google.com/calendar/api/quickstart/python). This is for Python but can also be done in a number of other languages.

When downloading the creds, add them to the root dir and name it to `credentials.json`.

Once everything is installed.

1. Clone the repo and create a virtualenv (makes life a lot easier) `python -m venv venv`
2. Install these packages if not already installed
`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
3. Create a config.json in the src folder
    - Within the config.json, create a calendarId key and add the id for the calendar you want to use, it may be your email address but it may also differ
    - To find out, your calendarId if you don't know go into the code and uncomment line 57 and comment out line 56, this will print out all the ids that exist.
    - Choose the one that looks the most familiar.
4. Comment the line 57 and uncomment line 56 and run the code.

You will probably want to open a new terminal session as this will just stay until you enter 'y' and it will then add it onto your calendar

## Tips if you get stuck on the token section

- If you are getting an error about having incorrect permissions, you will need to modify scopes in the code and in the web console.
- Once you modified the SCOPES in the `google_api_handler.py`, you will want to remove token.json and re-run the code.
