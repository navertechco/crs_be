try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetTourList import FSGetTourList
from .BSGetTourList import BSGetTourList
from .DSGetTourList import DSGetTourList


class GetTourList():
    def __init__(self):
        self.FSGetTourList = FSGetTourList
        self.BSGetTourList = BSGetTourList
        self.DSGetTourList = DSGetTourList