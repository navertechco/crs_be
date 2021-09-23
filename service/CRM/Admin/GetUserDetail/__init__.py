try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetUserDetail import FSGetUserDetail
from .BSGetUserDetail import BSGetUserDetail
from .DSGetUserDetail import DSGetUserDetail


class GetUserDetail():
    def __init__(self):
        self.FSGetUserDetail = FSGetUserDetail
        self.BSGetUserDetail = BSGetUserDetail
        self.DSGetUserDetail = DSGetUserDetail