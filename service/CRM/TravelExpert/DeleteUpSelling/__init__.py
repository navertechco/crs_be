try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSDeleteUpSelling import FSDeleteUpSelling
from .BSDeleteUpSelling import BSDeleteUpSelling
from .DSDeleteUpSelling import DSDeleteUpSelling


class DeleteUpSelling():
    def __init__(self):
        self.FSDeleteUpSelling = FSDeleteUpSelling
        self.BSDeleteUpSelling = BSDeleteUpSelling
        self.DSDeleteUpSelling = DSDeleteUpSelling