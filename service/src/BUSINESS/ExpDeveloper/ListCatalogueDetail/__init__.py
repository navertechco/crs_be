try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListCatalogueDetail import FSListCatalogueDetail
from .BSListCatalogueDetail import BSListCatalogueDetail
from .DSListCatalogueDetail import DSListCatalogueDetail


class ListCatalogueDetail():
    def __init__(self):
        self.FSListCatalogueDetail = FSListCatalogueDetail
        self.BSListCatalogueDetail = BSListCatalogueDetail
        self.DSListCatalogueDetail = DSListCatalogueDetail