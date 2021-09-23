try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSFindUser import FSFindUser
from .BSFindUser import BSFindUser
from .DSFindUser import DSFindUser


class FindUser():
    def __init__(self):
        self.FSFindUser = FSFindUser
        self.BSFindUser = BSFindUser
        self.DSFindUser = DSFindUser