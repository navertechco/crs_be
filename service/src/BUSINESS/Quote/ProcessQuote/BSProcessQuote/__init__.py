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
            if data.get('destinations') is not None:
                match = NewMatch().BSNewMatch(id, input)
                if len(match) > 0:
                    match["session"].commit()
                    destinations = ProcessDestinations().BSProcessDestinations(id, input)
                    if len(destinations) > 0:
                        destinations["session"].commit()
                        days = ProcessDays().BSProcessDays(id, input)
                        if len(days) > 0:
                            days["session"].commit()
                            processed = DSProcessQuote(id)
                            if len(processed) > 0:
                                processed["session"].commit()
                                return True
                            raise Exception( 605, "Error de Procesamiento de cotizaciòn")
                        raise Exception(605, "Error de Procesamiento de días")
                    raise Exception(605, "Error de Procesamiento de destinos")
                raise Exception(605, 'Error de Procesamiento de match')
            raise Exception(605, 'No tiene destinos la cotización')
        raise Exception(605, 'No tiene match la cotización')
    except Exception as e:
        raise e
