try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
# from ..DSConnect import DSConnect

from naver_core import *
from naver_config import *
from src.WEB.App.routes import app
from src.BUSINESS.System import ValidateUser, LogConnection
from ... import SignUp, SignIn, UpdateProfile, Reset
config = NaverConfig(app)


class BS():
    def __init__(self):
        self.ValidateUser = ValidateUser()
        self.LogConnection = LogConnection() 
        self.SignUp = SignUp.SignUp()
        self.SignIn = SignIn.SignIn()
        self.UpdateProfile = UpdateProfile.UpdateProfile()
        self.Reset = Reset.Reset()

        # super().__init__()


def BSConnect(input):
    """
    Método que se encarga de realizar la conexión de un usuario.

    Args:
        input (dict input): JSON de entrada con datos de usuario y contraseña para iniciar sesión

    Raises:
        Exception: Error de validación de datos de entrada de usuario o error de conexión con base de datos

    Returns:
        boolean: True si el usuario se ha conectado correctamente, False en caso contrario o si el usuario no existe en la base de datos o si la contraseña es incorrecta
    """
    try:
        bs = BS()
        if input is None:
            res = bs.LogConnection.BSLogConnection(config)
            return res
        state = getValue(input, 'state')
        if state == "signup":
            result = bs.SignUp.BSSignUp(input)
            return result
        if state == "forgot":
            result = bs.Reset.BSReset(input)
            return result
        validuser = bs.ValidateUser.BSValidateUser(input)
        if validuser:
            if state == "signin":
                result = bs.SignIn.BSSignIn(input)
                return result
            if state == "update":
                result = bs.UpdateProfile.BSUpdateProfile(input)
                return result

        raise Exception((605, 'Error de Login'))
    except Exception as e:
        raise e
