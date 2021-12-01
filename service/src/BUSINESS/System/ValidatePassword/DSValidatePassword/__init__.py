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

def DSValidatePassword(username, password):
    try:
        pp = ""
        stm = """ SELECT * FROM "USER" WHERE USERNAME = \'{0}\'
        
        """.format(username)
        table = "USER"
        user = nbd.persistence.getQuery(stm, table)
        if len(user) > 0:
            pp = str(user[0]['password']).strip()
        else:
            raise Exception("No Existe usuario")    
        
        stm = """ SELECT CAST(DIGEST(\'{0}\','SHA256') AS BPCHAR) = \'{1}\' as VALID
                
        """.format(password, pp) 
        table = "USER"
        res = nbd.persistence.getQuery(stm, table)
        return res  

    except Exception as e:
        raise e