try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSSignIn import DSSignIn
from naver_core import *
from src.Dto import *
from src.System.ValidatePassword import BSValidatePassword
 


def BSSignIn(input):
    """
        Método para realizar el inicio de sesion de un usuario

    Args:
        input (dict): datos de entrada del usuario

    Raises:
        Exception: Error de conexion con la base de datos

    Returns:
        boolean: True si el usuario se ha logueado correctamente, False en caso contrario
    """
    try:
        username = getValue(input, 'username') 
        user = DSSignIn(username)
        valid = BSValidatePassword(input)[0]['valid']
        if len(user) > 0: 
            dbstate = user[0]['state']
            if valid and dbstate == 6: 
                res = ProfileDto(user[0]).__dict__()
                return res
            raise Exception((601, 'Error de Login'))
        raise Exception((602, 'User is not exist'))

    except Exception as e:
        raise e
