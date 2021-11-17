try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSClientEdit import DSClientEdit
from naver_core import *
from src.BUSINESS.Agent import CreateContact, ClientEditContact


def BSClientEdit(input):
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
            return CreateContact().BSCreateContact(input)
        if state == 'update':
            return ClientEditContact().BSClientEditContact(input)

        raise Exception((605, 'Error de Edición'))
    except Exception as e:
        raise e
