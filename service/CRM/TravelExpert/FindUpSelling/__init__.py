try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSFindUpSelling import FSFindUpSelling
from .BSFindUpSelling import BSFindUpSelling
from .DSFindUpSelling import DSFindUpSelling


class FindUpSelling():
    def __init__(self):
        self.FSFindUpSelling = FSFindUpSelling
        self.BSFindUpSelling = BSFindUpSelling
        self.DSFindUpSelling = DSFindUpSelling