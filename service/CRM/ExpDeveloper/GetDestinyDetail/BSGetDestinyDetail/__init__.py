try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSGetDestinyDetail import DSGetDestinyDetail
import logging

def BSGetDestinyDetail(udestiny_id):
    try:
        result = DSGetDestinyDetail(udestiny_id)
        return result

    except Exception as e:
        logging.error(e)