try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditExperience import FSEditExperience
from .BSEditExperience import BSEditExperience
from .DSEditExperience import DSEditExperience


class EditExperience():
    def __init__(self):
        self.FSEditExperience = FSEditExperience
        self.BSEditExperience = BSEditExperience
        self.DSEditExperience = DSEditExperience