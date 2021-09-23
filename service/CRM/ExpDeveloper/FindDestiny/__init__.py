try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSFindDestiny import FSFindDestiny
from .BSFindDestiny import BSFindDestiny
from .DSFindDestiny import DSFindDestiny


class FindDestiny():
    def __init__(self):
        self.FSFindDestiny = FSFindDestiny
        self.BSFindDestiny = BSFindDestiny
        self.DSFindDestiny = DSFindDestiny