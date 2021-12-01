try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSNewItinerary import DSNewItinerary
# from src.BUSINESS.User.SignIn import BSSignIn
# from src.BUSINESS.User.SignUp import BSSignUp
# from src.BUSINESS.User.Reset import BSReset
# from src.BUSINESS.System.ValidateUser import BSValidateUser
from naver_core import *


def BSNewItinerary(input):
    """Método para crear una nueva cotización

    Args:
        input (dict): Contiene los datos de la cotización
        
    Raises:
        Exception: Cuando no se creó la cotización
        e: Cuando no se creó la cotización

    Returns:
        bool: True si se creó la cotización, False si no se creó
    """    
    try:
 
        res =  DSNewItinerary(input)
        if len(res) > 0:
            res['session'].commit()
            new_intinerarys = res['cursor'].fetchall()
            if len(new_intinerarys) > 0:
                id = new_intinerarys[0]['id_intinerary']
                return id
            raise Exception('No se creó la cotización, pruebe los datos ingresados')
        raise Exception(605, 'Error de NewItineraryación')
    except Exception as e:
        raise e
