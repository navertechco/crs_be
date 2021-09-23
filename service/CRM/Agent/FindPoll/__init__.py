try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSFindPoll import FSFindPoll
from .BSFindPoll import BSFindPoll
from .DSFindPoll import DSFindPoll


class FindPoll():
    def __init__(self):
        self.FSFindPoll = FSFindPoll
        self.BSFindPoll = BSFindPoll
        self.DSFindPoll = DSFindPoll