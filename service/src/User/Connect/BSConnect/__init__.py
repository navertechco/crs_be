try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
# from ..DSConnect import DSConnect
 
from naver_core import * 
from naver_config import *
from src.WEB.App.routes import * 
from src.System import ValidateUser, LogConnection 
from ... import SignUp, SignIn, UpdateProfile, Reset
config = NaverConfig(app) 
 

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
        if input is None:
            res = LogConnection.BSLogConnection(config)
            return res        
        state = getValue(input, 'state')
        if state == "signup":
            result = SignUp().BSSignUp(input)
            return result
        if state == "forgot":
            result =  Reset().BSReset(input)
            return result
        validuser = ValidateUser.BSValidateUser(input)
        if validuser:
            if state == "signin":
                result =  SignIn().BSSignIn(input)
                return result
            if state == "update":
                result =  UpdateProfile().BSUpdateProfile(input)
                return result

        raise Exception((605, 'Error de Login'))
    except Exception as e:
        raise e
