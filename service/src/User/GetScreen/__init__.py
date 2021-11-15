try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetScreen import FSGetScreen
from .BSGetScreen import BSGetScreen
from .DSGetScreen import DSGetScreen


class GetScreen():
    def __init__(self):
        self.FSGetScreen = FSGetScreen
        self.BSGetScreen = BSGetScreen
        self.DSGetScreen = DSGetScreen