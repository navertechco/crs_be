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
            match = NewMatch().BSNewMatch(id, match)
            if len(match) > 0 and data.get('destinations') is not None:
                destinations = ProcessDestinations().BSProcessDestinations(id, input)
                if len(destinations) > 0:
                    days = ProcessDays().BSProcessDays(id, input)
                    if len(days) > 0:
                        processed = DSProcessQuote(id)
                        if len(processed) > 0:
                            days["session"].commit()
                            match["session"].commit()
                            destinations["session"].commit()
                            processed["session"].commit() 
                            return True
                        days["session"].rollback()
                        match["session"].rollback()
                        destinations["session"].rollback()
                        processed["session"].rollback() 
                    raise Exception(605, "Error de Procesamiento de días")
                raise Exception(605, "Error de Procesamiento de destinos")
            raise Exception((605, 'Error de match de cotización'))
        raise Exception((605, 'No tiene match la cotización'))
    except Exception as e:
        raise e
