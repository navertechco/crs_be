try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSDeleteVideo import DSDeleteVideo
import logging

def BSDeleteVideo(uvideo_id):
    try:
        result = DSDeleteVideo(uvideo_id)
        return result

    except Exception as e:
        logging.error(e)