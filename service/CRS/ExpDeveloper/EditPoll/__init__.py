try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditPoll import FSEditPoll
from .BSEditPoll import BSEditPoll
from .DSEditPoll import DSEditPoll


class EditPoll():
    def __init__(self):
        self.FSEditPoll = FSEditPoll
        self.BSEditPoll = BSEditPoll
        self.DSEditPoll = DSEditPoll