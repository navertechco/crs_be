try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSFindUpSelling import DSFindUpSelling
import logging

def BSFindUpSelling(uupselling_id, uprops):
    try:
        result = DSFindUpSelling(uupselling_id, uprops)
        return result

    except Exception as e:
        logging.error(e)