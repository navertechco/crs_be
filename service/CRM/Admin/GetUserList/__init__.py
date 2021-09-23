try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetUserList import FSGetUserList
from .BSGetUserList import BSGetUserList
from .DSGetUserList import DSGetUserList


class GetUserList():
    def __init__(self):
        self.FSGetUserList = FSGetUserList
        self.BSGetUserList = BSGetUserList
        self.DSGetUserList = DSGetUserList