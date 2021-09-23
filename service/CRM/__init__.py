from .Admin import Admin
from .TravelExpert import TravelExpert
from .ExpDeveloper import ExpDeveloper
from .Agent import Agent
from .User import User
try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class CRM(User):
    def __init__(self):
        self.User = User()
        self.Agent = Agent()
        self.ExpDeveloper = ExpDeveloper()
        self.TravelExpert = TravelExpert()
        self.Admin = Admin()