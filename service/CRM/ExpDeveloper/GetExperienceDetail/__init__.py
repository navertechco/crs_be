try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetExperienceDetail import FSGetExperienceDetail
from .BSGetExperienceDetail import BSGetExperienceDetail
from .DSGetExperienceDetail import DSGetExperienceDetail


class GetExperienceDetail():
    def __init__(self):
        self.FSGetExperienceDetail = FSGetExperienceDetail
        self.BSGetExperienceDetail = BSGetExperienceDetail
        self.DSGetExperienceDetail = DSGetExperienceDetail