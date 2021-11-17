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

def DSReset(email):
    try:
        stm = "SELECT * from public.USER where email = '"+email+"'"
        table = "USER"
        res = nbd.persistence.getQuery(stm, table)
        return res  

    except Exception as e:
        raise e