try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSGetDestination import DSGetDestination
from naver_core import *


def BSGetDestination(input):
    try:
        destination_id = getValue(input, 'destination_id')
        res = DSGetDestination(destination_id)
        return res

    except Exception as e:
        raise e
