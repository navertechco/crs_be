try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSDeleteActivity import BSDeleteActivity
import logging

def FSDeleteActivity(uactivity_id):
    try:
        result = BSDeleteActivity(uactivity_id)
        return result

    except Exception as e:
        logging.error(e)