try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSGetExperienceDetail import BSGetExperienceDetail
import logging

def FSGetExperienceDetail(uexperience_id):
    try:
        result = BSGetExperienceDetail(uexperience_id)
        return result

    except Exception as e:
        logging.error(e)