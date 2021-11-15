from .EditProfile import EditProfile
from .ListAllTournament import ListAllTournament
from .ListTopWinner import ListTopWinner
from .ListAllWinner import ListAllWinner
from .ListParam import ListParam
from .ListMenu import ListMenu
from .ListPermission import ListPermission
from .Logout import Logout
from .Forgot import Forgot
from .Reset import Reset
from .SignUp import SignUp
from .SignIn import SignIn
from .Connect import Connect
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class User():
    def __init__(self):
        self.Connect = Connect()
        self.SignIn = SignIn()
        self.SignUp = SignUp()
        self.Reset = Reset()
        self.Forgot = Forgot()
        self.Logout = Logout()
        self.ListPermission = ListPermission()
        self.ListMenu = ListMenu()
        self.ListParam = ListParam()
        self.ListAllWinner = ListAllWinner()
        self.ListTopWinner = ListTopWinner()
        self.ListAllTournament = ListAllTournament()
        self.EditProfile = EditProfile()
        self.attributes={'id_user': None , 'id_user_type': None , 'props': None }
