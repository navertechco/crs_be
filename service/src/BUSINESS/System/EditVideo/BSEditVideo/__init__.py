try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSEditVideo import DSEditVideo
from naver_core import *
from src.infra.video.youtube import *


def BSEditVideo(input):
    try:
        state = input.get('state')
        resources = DSEditVideo(input)

        if state == 'create':
            title = getValue(input, 'title')
            description = getValue(input, 'description')
            playlistId = create_playlist(title, description)["id"]
            for resourceId in resources:
                insert_playlist_items(resourceId, playlistId)
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
