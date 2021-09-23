try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSDeleteDestiny import DSDeleteDestiny
import logging

def BSDeleteDestiny(udestiny_id):
    try:
        result = DSDeleteDestiny(udestiny_id)
        return result

    except Exception as e:
        logging.error(e)