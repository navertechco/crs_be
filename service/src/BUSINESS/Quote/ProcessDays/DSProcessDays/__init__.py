try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.WEB.App.routes import app 


config = NaverConfig(app)
nbd = NaverDB(app,config)

def DSProcessDays(id, input):
    """Método para procesar días de cotización

    Args:
        id (int): Identificador de la Cotización
        input (dict): Diccionario con los datos de la Cotización

    Raises:
        e: Cuando no se puede procesar la Cotización

    Returns:
        res: Resultado de la operación
    """  
    try:
        table = "QUOTE_DAY"
        stm = "SELECT *"
        stm += "FROM {} ".format(table)
        where  = " WHERE ID_QUOTE = \'{}\'".format(id)
        stm += where
        quote_days = nbd.persistence.getQuery(stm, table)
        if len(quote_days) > 0: 
            raise Exception("Quote days already processed")         
            res = nbd.persistence.setWrite(stm, table)
            return res  

    except Exception as e:
        raise e