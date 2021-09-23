try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateUpSelling import FSCreateUpSelling
from .BSCreateUpSelling import BSCreateUpSelling
from .DSCreateUpSelling import DSCreateUpSelling


class CreateUpSelling():
    def __init__(self):
        self.FSCreateUpSelling = FSCreateUpSelling
        self.BSCreateUpSelling = BSCreateUpSelling
        self.DSCreateUpSelling = DSCreateUpSelling