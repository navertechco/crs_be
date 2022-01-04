try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSProcessOptions import BSProcessOptions
import logging

def FSProcessOptions(input):
    try:
         
        result = BSProcessOptions(input)
        return result

    except Exception as e:
        logging.error(e)