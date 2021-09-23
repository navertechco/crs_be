try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetActivityDetail import FSGetActivityDetail
from .BSGetActivityDetail import BSGetActivityDetail
from .DSGetActivityDetail import DSGetActivityDetail


class GetActivityDetail():
    def __init__(self):
        self.FSGetActivityDetail = FSGetActivityDetail
        self.BSGetActivityDetail = BSGetActivityDetail
        self.DSGetActivityDetail = DSGetActivityDetail