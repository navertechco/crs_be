try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSDeleteUpSelling import DSDeleteUpSelling
import logging

def BSDeleteUpSelling(uupselling_id):
    try:
        result = DSDeleteUpSelling(uupselling_id)
        return result

    except Exception as e:
        logging.error(e)