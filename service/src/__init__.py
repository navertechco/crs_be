try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
    
from .BUSINESS import *
from .INFRA.WEB import *
from .INFRA.NET import *
class CRS():
    def __init__(self):
        self.User = User()
        self.Agent = Agent()
        self.Client = Client()
        self.File = File()
        self.ExpDeveloper = ExpDeveloper()
        self.Itinerary = Itinerary()
        self.TrvExp = TrvExp()
        self.Admin = Admin()
        self.System = System()