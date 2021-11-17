try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSEdit import DSEdit 
from naver_core import *
from src.Agent import CreateContact, EditContact

def BSEdit(input):
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
            return CreateContact.BsCreateContact(input)
        if state == 'update':
            return EditContact.BsEditContact(input)  
 
        raise Exception((605, 'Error de Edición'))
    except Exception as e:
        raise e
