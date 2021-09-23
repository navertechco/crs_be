try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSDeleteVideo import BSDeleteVideo
import logging

def FSDeleteVideo(uvideo_id):
    try:
        result = BSDeleteVideo(uvideo_id)
        return result

    except Exception as e:
        logging.error(e)