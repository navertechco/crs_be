try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListActivityDetail import FSListActivityDetail
from .BSListActivityDetail import BSListActivityDetail
from .DSListActivityDetail import DSListActivityDetail


class ListActivityDetail():
    def __init__(self):
        self.FSListActivityDetail = FSListActivityDetail
        self.BSListActivityDetail = BSListActivityDetail
        self.DSListActivityDetail = DSListActivityDetail