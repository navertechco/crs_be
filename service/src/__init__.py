try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
    
from .System import *
from .Admin import Admin
from .TrvExp import TrvExp
from .ExpDeveloper import ExpDeveloper
from .Agent import Agent
from .User import User
from .WEB import *
class CRS():
    def __init__(self):
        self.User = User()
        self.Agent = Agent()
        self.ExpDeveloper = ExpDeveloper()
        self.TrvExp = TrvExp()
        self.Admin = Admin()
        self.System = System()