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

def DSFindCatalog(input):
           
    try:
        catalogs = str(tuple(input.get("data").get("catalogs"))).replace(",)",")")
        table = "CATALOG"
        stm="""
             
                        select  
                            (c.description)     as  catalog,
                            (cd."order")        as  order,
                            (cd.description)    as  description,
                            (cd.code)           as  code,
                            (cd.value)          as  value
             
 
                        from entities.catalog_detail cd 
                            join entities."catalog" c 
                                on c.catalog_id = cd.catalog_id 
                            where c.description in {}
                            and cd.is_active is true  
                             
                    
        """.format(catalogs)
        res = nbd.persistence.getQuery(stm, table)
 
        
        
        
        return res
    except Exception as e:
        raise e