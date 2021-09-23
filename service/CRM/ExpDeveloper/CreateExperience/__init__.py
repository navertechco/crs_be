try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateExperience import FSCreateExperience
from .BSCreateExperience import BSCreateExperience
from .DSCreateExperience import DSCreateExperience


class CreateExperience():
    def __init__(self):
        self.FSCreateExperience = FSCreateExperience
        self.BSCreateExperience = BSCreateExperience
        self.DSCreateExperience = DSCreateExperience