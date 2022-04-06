try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
# from ..DSConnect import DSConnect
try:
    from naver_core import *
    from naver_config import *
    from src.INFRA.WEB.App.routes import app
    from src.BUSINESS.System import ValidateUser, LogConnection, FindCatalog
    from src.BUSINESS.Agent import GetExperience
    from src.BUSINESS.User import SignUp, SignIn, Logout, Reset, UpdateProfile
except Exception as e:
    print(e)
    pass

config = NaverConfig(app)


class BS():
    def __init__(self):
        self.LogConnection = LogConnection()
        self.Logout = Logout()
        self.SignUp = SignUp()
        self.SignIn = SignIn()
        self.Reset = Reset
        self.FindCatalog = FindCatalog()
        self.GetExperience = GetExperience()
        self.ValidateUser = ValidateUser()
        self.UpdateProfile = UpdateProfile


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
        self = BS()
        if input is None:
            res = self.LogConnection.BSLogConnection(config)
            return res
        state = input.get("state")
        if state == "logout":
            result = self.Logout.BSLogout(input)
            return result
        if state == "signup":
            result = self.SignUp.BSSignUp(input)
            return result
        if state == "forgot":
            result = self.Reset.BSReset(input)
            return result
        validuser = self.ValidateUser.BSValidateUser(input)
        if validuser:
            if state == "signin":
                result = self.SignIn.BSSignIn(input)
                if len(result) > 0:
                    catalogs = self.FindCatalog.BSFindCatalog(
                        {"data": {"catalogs": ["ALL"]}})
                    return catalogs
            if state == "update":
                result = self.UpdateProfile.BSUpdateProfile(input)
                return result

        raise Exception(605, 'Error de Login')
    except Exception as e:
        raise e
