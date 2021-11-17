try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllExperience import FSListAllExperience
from .BSListAllExperience import BSListAllExperience
from .DSListAllExperience import DSListAllExperience


class ListAllExperience():
    def __init__(self):
        self.FSListAllExperience = FSListAllExperience
        self.BSListAllExperience = BSListAllExperience
        self.DSListAllExperience = DSListAllExperience