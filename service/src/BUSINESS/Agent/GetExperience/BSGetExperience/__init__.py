try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSGetExperience import DSGetExperience
from naver_core import *


def BSGetExperience(name):
    try:
         
        res = DSGetExperience(name)
        return res

    except Exception as e:
        raise e
