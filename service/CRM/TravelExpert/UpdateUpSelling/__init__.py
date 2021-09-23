try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSUpdateUpSelling import FSUpdateUpSelling
from .BSUpdateUpSelling import BSUpdateUpSelling
from .DSUpdateUpSelling import DSUpdateUpSelling


class UpdateUpSelling():
    def __init__(self):
        self.FSUpdateUpSelling = FSUpdateUpSelling
        self.BSUpdateUpSelling = BSUpdateUpSelling
        self.DSUpdateUpSelling = DSUpdateUpSelling