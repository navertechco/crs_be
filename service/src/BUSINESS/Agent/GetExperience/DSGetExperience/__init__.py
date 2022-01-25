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


def DSGetExperience(input):
    try:
        table = "EXPERIENCE"
        destination, experience, key_activities, travel_rhtythms, destination_option = input.get(
            "data").values()
        stm_ka = ""
        if len(key_activities) > 0:
            stm_ka = f" and (e.key_activity_id   ) in {str(tuple(key_activities)).replace(',)',')')}"
            stm_ka += f" and (e.key_activity2_id   ) in {str(tuple(key_activities)).replace(',)',')')}"
        stm_tr = ""
        if len(travel_rhtythms) > 0:
            stm_tr = f" and (e.travel_ritm_id ) in {str(tuple(travel_rhtythms)).replace(',)',')')}"
        stm_to = ""
        if (destination_option != None) :
            stm_to = f" and (e.destination_option_id ) =\'{destination_option}\'"
            
        stm = f"""
            select distinct  d.destination_title, e.experience_title title, e.experience_photo image, e.experience_video video, 
             (e.props)::jsonb    props 
                from entities.experience e 
                    join entities.destination d 
                        on e.destination_id =d.destination_id 
                where (d.destination_title like upper('%{destination}%') 
                and e.experience_title like upper('%{experience}%'))
        """+stm_ka+stm_tr+stm_to
        res = nbd.persistence.getQuery(stm, table)
        return res
    except Exception as e:
        raise e
