try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSFindActivity import DSFindActivity
import logging

def BSFindActivity(uactivity_id, ucontact_id, uprops):
    try:
        result = DSFindActivity(uactivity_id, ucontact_id, uprops)
        return result

    except Exception as e:
        logging.error(e)