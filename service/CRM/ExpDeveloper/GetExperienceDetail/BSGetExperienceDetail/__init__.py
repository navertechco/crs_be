try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSGetExperienceDetail import DSGetExperienceDetail
import logging

def BSGetExperienceDetail(uexperience_id):
    try:
        result = DSGetExperienceDetail(uexperience_id)
        return result

    except Exception as e:
        logging.error(e)