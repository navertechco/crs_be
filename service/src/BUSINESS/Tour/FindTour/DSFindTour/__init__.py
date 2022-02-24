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
 
        #TOUR QUERY
        tour_stm=f"SELECT detail"
        tour_stm+=f" FROM {schema}.{table}" 
        tour_stm+=f" WHERE tour_id=\'{tour_id}\'"
        res = {"tour":"", "customer":""}
        result = nbd.persistence.getQuery(tour_stm, table)[0].get("detail")
        res["tour"] = result
         
        #CLIENT QUERY
        client_stm = """
                select c.* from entities.tour t join entities.client c 
                on t.client_id = c.client_id 
        """
        client_stm+=f" WHERE tour_id=\'{tour_id}\'"
        res["customer"] = nbd.persistence.getQuery(client_stm, table)[0]
      
        return result  

    except Exception as e:
        raise e