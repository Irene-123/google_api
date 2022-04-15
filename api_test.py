import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pickle

from apiclient.discovery import build
scopes=['https://www.googleapis.com/auth/calendar']
#file=( "client_secret.json" , 'r')

# flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
# credentials=flow.run_console()

# pickle.dump(credentials, open("token.pkl", "wb"))

credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
result = service.calendarList().list().execute()
print(result['items'][0])
