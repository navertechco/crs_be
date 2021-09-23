try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSUpdatePoll import FSUpdatePoll
from .BSUpdatePoll import BSUpdatePoll
from .DSUpdatePoll import DSUpdatePoll


class UpdatePoll():
    def __init__(self):
        self.FSUpdatePoll = FSUpdatePoll
        self.BSUpdatePoll = BSUpdatePoll
        self.DSUpdatePoll = DSUpdatePoll