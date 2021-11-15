from .GetTheme import GetTheme
from .GetScreen import GetScreen
from .ListAllCatalogue import ListAllCatalogue
from .ListAllAlert import ListAllAlert
from .EditProfile import EditProfile
from .ListParam import ListParam
from .ListMenu import ListMenu
from .ListPermission import ListPermission
from .Forgot import Forgot
from .Reset import Reset
from .SingUp import SingUp
from .SingIn import SingIn
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class User():
    def __init__(self):
        self.SingIn = SingIn()
        self.SingUp = SingUp()
        self.Reset = Reset()
        self.Forgot = Forgot()
        self.ListPermission = ListPermission()
        self.ListMenu = ListMenu()
        self.ListParam = ListParam()
        self.EditProfile = EditProfile()
        self.ListAllAlert = ListAllAlert()
        self.ListAllCatalogue = ListAllCatalogue()
        self.GetScreen = GetScreen()
        self.GetTheme = GetTheme()
        self.attributes={self.user_id: None , self.props: None , self.user_type: None }
