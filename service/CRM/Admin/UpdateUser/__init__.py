try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSUpdateUser import FSUpdateUser
from .BSUpdateUser import BSUpdateUser
from .DSUpdateUser import DSUpdateUser


class UpdateUser():
    def __init__(self):
        self.FSUpdateUser = FSUpdateUser
        self.BSUpdateUser = BSUpdateUser
        self.DSUpdateUser = DSUpdateUser