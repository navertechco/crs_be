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

def DSFindTour(input):
    """"""
    try:
        tour_id = getValue(input, 'tour_id')
        table = "TOUR"
        schema = "entities"
        stm=f"SELECT *"
        stm+=f" FROM {schema}.{table}" 
        stm+=f" WHERE tour_id=\'{tour_id}\'"
        res = nbd.persistence.getQuery(stm, table)
        return res  

    except Exception as e:
        raise e