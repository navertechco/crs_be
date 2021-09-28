try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditProblem import FSEditProblem
from .BSEditProblem import BSEditProblem
from .DSEditProblem import DSEditProblem


class EditProblem():
    def __init__(self):
        self.FSEditProblem = FSEditProblem
        self.BSEditProblem = BSEditProblem
        self.DSEditProblem = DSEditProblem