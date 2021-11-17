try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSProccessQuote import DSProccessQuote
# from src.User.SignIn import BSSignIn
# from src.User.SignUp import BSSignUp
# from src.User.Reset import BSReset
# from src.System.ValidateUser import BSValidateUser
from naver_core import *


def BSProccessQuote(input):
    """Método que confirma registro de usuario

    Args:
        input (dict): usuario de entrada

    Raises:
        Exception:  Error de validación de usuario

    Returns:
        boolean: True si el usuario se confirma, False si no
    """
    try:
        confirmation= input.get('confirmation')
        result =  DSProccessQuote(confirmation)
        if len(result) > 0:
            result['session'].commit()
            return True
        raise Exception((605, 'Error de ProccessQuoteación'))
    except Exception as e:
        raise e
