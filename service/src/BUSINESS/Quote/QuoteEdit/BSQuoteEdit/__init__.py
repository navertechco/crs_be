try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSQuoteEdit import DSQuoteEdit
from naver_core import *
from ... import NewQuote, NewMatch, ProcessQuote, PromoteQuote, UpdateQuote, ProcessDestinations


def BSQuoteEdit(input):
    """Método que se encarga de ejecutar el comando edit.

    Args:
        input (dict): usuario de entrada

    Raises:
        Exception:  Error de validación de usuario

    Returns:
        boolean: True si el usuario se confirma, False si no
    """
    try:
        state = getValue(input, 'state')

        if state == 'new':
            res = DSQuoteEdit(input)
            if len(res) > 0:
                res = NewQuote().BSNewQuote(input)
                if res:
                    res = ProcessQuote().BSProcessQuote(input)
                    if res:
                        return True
                    raise Exception('Error al procesar la cotización')
                raise Exception('Error al crear la cotización')
            raise Exception('Ya tiene una cotización activa')

        if state == 'update':
            return UpdateQuote().BSUpdateQuote(input)

        raise Exception((605, 'Error de Edición'))
    except Exception as e:
        raise e
