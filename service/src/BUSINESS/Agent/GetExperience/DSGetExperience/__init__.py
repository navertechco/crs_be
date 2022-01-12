try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from src.BUSINESS.Dto import ClientDto
from src.INFRA.WEB.App.routes import app
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSGetExperience(name):
    try:
        table = "DESTINATION"
        stm = """
            select distinct e.experience_title title, e.experience_photo image, e.experience_video video 
                from entities.experience e 
                    join entities.destination d 
                        on e.destination_id =d.destination_id 
                where d.destination_title like upper(\'{}\') 
        """.format(name)
        res = nbd.persistence.getQuery(stm, table) 
        return res
    except Exception as e:
        raise e
