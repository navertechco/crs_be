try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListExperienceDetail import FSListExperienceDetail
from .BSListExperienceDetail import BSListExperienceDetail
from .DSListExperienceDetail import DSListExperienceDetail


class ListExperienceDetail():
    def __init__(self):
        self.FSListExperienceDetail = FSListExperienceDetail
        self.BSListExperienceDetail = BSListExperienceDetail
        self.DSListExperienceDetail = DSListExperienceDetail