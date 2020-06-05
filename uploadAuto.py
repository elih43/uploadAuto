import pickle
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests



from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from Video import Video



scopes = ["https://www.googleapis.com/auth/youtube.upload"]

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
CLIENT_SECRET = "client_secret.json"

TITLE = input("Enter a title for the video.")
CATEGORYID = input("Enter a category id.")
STATUS = input("Enter: Private, Public, or Unlisted")
def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    

    vid = Video(TITLE, CATEGORYID, STATUS)
    youtube = get_authenticated_service()
    request = youtube.videos().insert(
        part="snippet,status",
        body={
         
          "snippet": {
            "categoryId": vid.getCategoryId(),
            "description": "Description of uploaded video.",
            "title": vid.getTitle()
            
          },
          "status": {
            "privacyStatus": vid.getStatus()
          }
        },
        
        # Pointer to video file
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
        
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET, scopes)
        credentials = flow.run_console()

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)
    
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)


if __name__ == "__main__":
    get_authenticated_service()
    main()