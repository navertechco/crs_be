
from .Logout import Logout
from .Forgot import Forgot
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
        self.Forgot = Forgot()
        self.Logout = Logout() 
        self.attributes={'id_user': None , 'id_user_type': None , 'props': None }
