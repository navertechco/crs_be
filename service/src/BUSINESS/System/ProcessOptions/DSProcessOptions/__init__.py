try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.INFRA.WEB.App.routes import app 


config = NaverConfig(app)
nbd = NaverDB(app,config)

def DSProcessOptions(input):
    """Método para procesar opciones de inclusión

    Args:
        input (dict): Entrada del método

    Raises:
        e: error del proceso

    Returns:
        res: resultadod de la operación
    """        
    try:
        res = input  
        return res  

    except Exception as e:
        raise e