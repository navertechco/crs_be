try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from src.BUSINESS.Dto import QuoteDto
from src.INFRA.WEB.App.routes import app
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *

config = NaverConfig(app)
nbd = NaverDB(app, config)

def DSQuoteEdit(input):
    """Método para validar una cotizacion

    Args:
        input (dict): Diccionario con los datos de la cotizacion

    Raises:
        e: Error de conexion con la base de datos

    Returns:
        res: Resultado de la operacion
    """      
    try:
        data = input.get('data')
        quote = QuoteDto(data).getAllDict()
        
        
        return True if quote.get("id_quote") is None or 'NULL' or '' else False

    except Exception as e:
        return True