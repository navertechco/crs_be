try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSDeleteExperience import DSDeleteExperience
import logging

def BSDeleteExperience(uexperience_id):
    try:
        result = DSDeleteExperience(uexperience_id)
        return result

    except Exception as e:
        logging.error(e)