from .Logout import Logout
from .ForgotPassword import ForgotPassword
from .ForgotUsername import ForgotUsername
from .ResetPassword import ResetPassword
from .Register import Register
from .SingIn import SingIn
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class User():
    def __init__(self):
        self.SingIn = SingIn()
        self.Register = Register()
        self.ResetPassword = ResetPassword()
        self.ForgotUsername = ForgotUsername()
        self.ForgotPassword = ForgotPassword()
        self.Logout = Logout()
        self.attributes={self.user_id: None , self.props: None , self.user_type: None }
