try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSGetExperienceList import BSGetExperienceList
import logging

def FSGetExperienceList():
    try:
        result = BSGetExperienceList()
        return result

    except Exception as e:
        logging.error(e)