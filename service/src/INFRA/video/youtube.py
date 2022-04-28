#!/usr/bin/python

import httplib2
import sys
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
import google_auth_oauthlib.flow


FILE_PATH = os.path.abspath(__file__)
VIDEO_DIR = os.path.dirname(FILE_PATH)
INFRA_DIR = os.path.dirname(VIDEO_DIR)
SRC_DIR = os.path.dirname(INFRA_DIR)
ROOT_DIR = os.path.dirname(SRC_DIR)
CLIENT_SECRETS_FILE = os.path.join(ROOT_DIR, ("client_secrets.json"))
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


scopes = ["https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl",
          "https://www.googleapis.com/auth/youtube.readonly",
          "https://www.googleapis.com/auth/youtubepartner"]

# ////////////////////////////////////////////////////////////////////////////// PLAYLIST //////////////////////////////////////////////////////////////////////////////


def list_playlist():
    youtube = initialize_api()
    request = youtube.playlists().list(part="id, snippet, status",
                                       channelId="UCmePd2U1QGDYQysI8xqe1XA", maxResults=50)
    response = request.execute()
    print(response)


def delete_playlist(id):
    youtube = initialize_api()
    request = youtube.playlists().delete(id=id)
    response = request.execute()
    print(response)


def create_playlist(title, description):
    youtube = initialize_api()
    response = youtube.playlists().insert(
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
    print(response['id'])

# ////////////////////////////////////////////////////////////////////////////// PLAYLIST ITEMS //////////////////////////////////////////////////////////////////////////////


def list_playlist_items(playlistId):
    youtube = initialize_api()
    request = youtube.playlistItems().list(part="id, snippet, contentDetails, status",
                                           playlistId=f"{playlistId}", maxResults=50)
    response = request.execute()
    print(response)


def insert_playlist_items(videoId, playlistId):
    youtube = initialize_api()
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": f"{playlistId}",
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": f"{videoId}"
                }}}
    )

    response = request.execute()
    print(response)


def update_playlist_items(videoId, playlistId):
    youtube = initialize_api()
    request = youtube.playlistItems().update(
        part="snippet",
        body={
            "snippet": {
                "playlistId": f"{playlistId}",
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": f"{videoId}"
                }}}
    )

    response = request.execute()
    print(response)


def delete_playlist_items(id):
    youtube = initialize_api()
    request = youtube.playlistItems().delete(id=id)
    response = request.execute()
    print(response)


if __name__ == '__main__':
    pass
