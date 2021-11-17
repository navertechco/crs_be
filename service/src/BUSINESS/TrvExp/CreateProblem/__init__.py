try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateProblem import FSCreateProblem
from .BSCreateProblem import BSCreateProblem
from .DSCreateProblem import DSCreateProblem


class CreateProblem():
    def __init__(self):
        self.FSCreateProblem = FSCreateProblem
        self.BSCreateProblem = BSCreateProblem
        self.DSCreateProblem = DSCreateProblem