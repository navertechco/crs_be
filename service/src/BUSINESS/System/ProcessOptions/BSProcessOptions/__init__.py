try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSProcessOptions import DSProcessOptions
import logging

def BSProcessOptions(tour_id):
    try:
        result = DSProcessOptions(tour_id)
        return result

    except Exception as e:
        logging.error(e)