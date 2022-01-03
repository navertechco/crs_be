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

def DSGetNextVal(table, field):
    """Método para obtener el siguiente valor de la tabla

    Args:
        table (str): Nombre de la tabla
        field (str): Nombre del campo de la tabla

    Raises:
        e: error de consulta

    Returns:
        res: resultado de la consulta
    """        
    try:
         
        res = nbd.persistence.getNextVal(field, table)
        res2 = nbd.persistence.getMaxVal(field, table)
        if res2 is not None:
            return res2
        return res  

    except Exception as e:
        raise e