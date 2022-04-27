#!/usr/bin/python

import httplib2
import sys, os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

ROUTES_PATH = os.path.abspath(__file__)
APP_DIR = os.path.dirname(ROUTES_PATH)
web_DIR = os.path.dirname(APP_DIR)
infra_DIR = os.path.dirname(web_DIR)
SRC_DIR = os.path.dirname(infra_DIR)
ROOT_DIR = os.path.dirname(SRC_DIR)
STATIC = os.path.join(web_DIR, ("static/"))
TEMPLATE_FOLDER = os.path.join(STATIC, ("templates/"))
UPLOAD_FOLDER = os.path.join(STATIC, ("uploads/"))
ALLOWED_EXTENSIONS = {"xlsx", "csv"}
ENV_PATH = os.path.join(ROOT_DIR, (".env"))
 
CLIENT_SECRETS_FILE = "client_secrets.json" 
MISSING_CLIENT_SECRETS_MESSAGE = ""  
YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def initialize_api():
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                   message=MISSING_CLIENT_SECRETS_MESSAGE,
                                   scope=YOUTUBE_READ_WRITE_SCOPE)

    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        flags = argparser.parse_args()
        credentials = run_flow(flow, storage, flags)

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    http=credentials.authorize(httplib2.Http()))
    return youtube


def create_playlist(title, description):
    youtube = initialize_api()
    # This code creates a new, private playlist in the authorized user's channel.
    playlists_insert_response = youtube.playlists().insert(
        part="snippet,status",
        body=dict(
            snippet=dict(
                title=f"{title}",
                description=f"{description}"
            ),
            status=dict(
                privacyStatus="private"
            )
        )
    ).execute()

    print(f"New playlist id: {playlists_insert_response['id']}")
