try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSDeletePoll import FSDeletePoll
from .BSDeletePoll import BSDeletePoll
from .DSDeletePoll import DSDeletePoll


class DeletePoll():
    def __init__(self):
        self.FSDeletePoll = FSDeletePoll
        self.BSDeletePoll = BSDeletePoll
        self.DSDeletePoll = DSDeletePoll