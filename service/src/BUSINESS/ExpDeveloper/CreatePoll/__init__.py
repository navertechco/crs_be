try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreatePoll import FSCreatePoll
from .BSCreatePoll import BSCreatePoll
from .DSCreatePoll import DSCreatePoll


class CreatePoll():
    def __init__(self):
        self.FSCreatePoll = FSCreatePoll
        self.BSCreatePoll = BSCreatePoll
        self.DSCreatePoll = DSCreatePoll