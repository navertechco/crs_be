try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSEditVideo import DSEditVideo
from naver_core import *
from src.infra.video.youtube import *
from src.business.Tour import BSUpdatePlaylist


def BSEditVideo(input):
    try:
        state = input.get('state')

        if state == 'create':
            resources = DSEditVideo(input)
            title = getValue(input, 'title')
            description = getValue(input, 'description')
            playlists = list_playlist()["items"]

            for playlist in playlists:
                if playlist["snippet"]["title"] == title:
                    delete_playlist(playlist["id"])

            playlistId = create_playlist(title, description)["id"]
            for resourceId in resources:
                insert_playlist_items(resourceId, playlistId)
            playlist = {
                "playlist_slug": playlistId,
                "tour_id": getValue(input, 'tour_id')
            }
            res = BSUpdatePlaylist(playlist)
            return playlistId
        if state == 'delete':
            playlistId = getValue(input, 'playlistId')
            delete_playlist(playlistId)
            pass
        if state == 'insert_item':
            resourceId = getValue(input, 'resourceId')
            playlistId = getValue(input, 'playlistId')
            insert_playlist_items(resourceId, playlistId)
            pass
        if state == 'update_item':
            resourceId = getValue(input, 'resourceId')
            playlistId = getValue(input, 'playlistId')
            order = getValue(input, 'order')
            update_playlist_items(resourceId, playlistId, order)
            pass
        if state == 'delete_item':
            resourceId = getValue(input, 'resourceId')
            playlistId = getValue(input, 'playlistId')
            delete_playlist_items(resourceId, playlistId)
            pass

        return True

    except Exception as e:
        raise e
