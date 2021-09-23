try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSUpdateVideo import DSUpdateVideo
import logging

def BSUpdateVideo(udata):
    try:
        result = DSUpdateVideo(udata)
        return result

    except Exception as e:
        logging.error(e)