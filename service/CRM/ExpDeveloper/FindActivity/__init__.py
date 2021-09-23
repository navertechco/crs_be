try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSFindActivity import FSFindActivity
from .BSFindActivity import BSFindActivity
from .DSFindActivity import DSFindActivity


class FindActivity():
    def __init__(self):
        self.FSFindActivity = FSFindActivity
        self.BSFindActivity = BSFindActivity
        self.DSFindActivity = DSFindActivity