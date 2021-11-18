try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSProcessQuote import DSProcessQuote
from ...NewMatch import NewMatch
from ...ProcessDestinations import ProcessDestinations
from ...ProcessDays import ProcessDays
from naver_core import *


def BSProcessQuote(id, input):
    """Método de Procesamiento de Cotización

    Args:
        id (int): Identificador de la Cotización
        input (dict): Diccionario con los datos de la Cotización

    Raises:
        Exception: Cuando no se puede procesar la Cotización
        Exception: Cuando no se puede procesar los destinos
        Exception: Cuando no se puede procesar los días
        Exception: Cuando no se puede crear el Match
        e: Todas las expeciones

    Returns:
        bool: [description]
    """
    try:
        data = input.get('data')
        if data.get('match') is not None:
            match = data.get('match')
            res = NewMatch().BSNewMatch(id, match)
            if res and data.get('destinations') is not None:
                res = ProcessDestinations().BSProcessDestinations(id, input)
                if res:
                    res = ProcessDays().BSProcessDays(id, input)
                    if res:
                        res = DSProcessQuote(id)
                    return res
                raise Exception(605, "Error de Procesamiento de días")
            raise Exception(605, "Error de Procesamiento de destinos")
        raise Exception((605, 'Error de match de cotización'))
    except Exception as e:
        raise e
