try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllMedia import FSListAllMedia
from .BSListAllMedia import BSListAllMedia
from .DSListAllMedia import DSListAllMedia


class ListAllMedia():
    def __init__(self):
        self.FSListAllMedia = FSListAllMedia
        self.BSListAllMedia = BSListAllMedia
        self.DSListAllMedia = DSListAllMedia