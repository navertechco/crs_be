try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllPoll import FSListAllPoll
from .BSListAllPoll import BSListAllPoll
from .DSListAllPoll import DSListAllPoll


class ListAllPoll():
    def __init__(self):
        self.FSListAllPoll = FSListAllPoll
        self.BSListAllPoll = BSListAllPoll
        self.DSListAllPoll = DSListAllPoll