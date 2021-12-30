try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSTourEdit import BSTourEdit
from naver_core import *
from flask import render_template, make_response

def FSTourEdit	(input):
    """Método para editar un Cliente.

    Args:
        input (dict): Diccionario con los datos del Cliente.

    Returns:
        json: Resultado del API.
    """
    try:
        result = BSTourEdit(input)
        return Ok(result)
    except Exception as e:
        return ErrorResponse(e) 