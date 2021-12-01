try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSPromoteItinerary import BSPromoteItinerary
from naver_core import *
from flask import render_template, make_response

def FSPromoteItinerary	(data):
    """Método para crear un nuevo Reporte.

    Args:
        data (dict): Diccionario con los datos del Reporte.

    Returns:
        json: Resultado del API.
    """
    try:
        result = BSPromoteItinerary(data)
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('success.html'),200,headers) 

    except Exception as e:
        return ErrorResponse(e) 