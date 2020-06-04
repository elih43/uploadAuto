import pickle
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests


from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build



scopes = ["https://www.googleapis.com/auth/youtube.upload"]

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
CLIENT_SECRET = "client_secret.json"
def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    youtube = get_authenticated_service()
    request = youtube.videos().insert(
        part="snippet,status",
        body={
         
          "snippet": {
            "categoryId": "22",
            "description": "Description of uploaded video.",
            "title": "Test vid."
            
          },
          "status": {
            "privacyStatus": "unlisted"
          }
        },
        
        # TODO: For this request to work, you must replace "YOUR_FILE"
        #       with a pointer to the actual file you are uploading.
        media_body=MediaFileUpload("vid.mp4")
    )
    response = request.execute()

    print(response)


def get_authenticated_service():
    credentials = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    #  Check if the credentials are invalid or do not exist
    if not credentials or not credentials.valid:
        # Check if the credentials have expired
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET, scopes)
            credentials = flow.run_console()

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)
    CRED = credentials
    
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)


if __name__ == "__main__":
    get_authenticated_service()
    main()