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

def DSProcessQuote(id):
    """Método para validar si existe una cotización

    Args:
        id (int): id de la cotización

    Raises:
        e: Error de conexión a la base de datos

    Returns:
        res: Resultado de la consulta
    """       
    try:
        table = "QUOTE"
        stm = " UPDATE "
        stm += table 
        stm += " SET ID_QUOTE_STATE = 2 "
        stm += " WHERE id_quote = \'{}\'".format(id)
        stm += " AND id_quote_state >= 1"
        res = nbd.persistence.setWrite(stm, table)
        return res  

    except Exception as e:
        raise e