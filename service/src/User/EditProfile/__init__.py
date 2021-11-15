try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditProfile import FSEditProfile
from .BSEditProfile import BSEditProfile
from .DSEditProfile import DSEditProfile


class EditProfile():
    def __init__(self):
        self.FSEditProfile = FSEditProfile
        self.BSEditProfile = BSEditProfile
        self.DSEditProfile = DSEditProfile