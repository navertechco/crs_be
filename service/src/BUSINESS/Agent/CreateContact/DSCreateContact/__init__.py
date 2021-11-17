try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from src.Dto import ClientDto
from src.WEB.App.routes import app
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *

config = NaverConfig(app)
nbd = NaverDB(app, config)

def DSCreateContact(input):
    try:
        client = ClientDto(input.get('data'))
        stm = """   INSERT INTO CLIENT
                    (     
                        NAME_CONTACT,
                        NAME_CONTACT_2,
                        ID_LEGAL_CLIENT_TYPE,
                        ID_CLIENT_TYPE,
                        DNI,
                        IS_OWNER,
                        EMAIL,
                        ID_ORIGIN,
                        PHONE,
                        ADDRESS
                    )
                    VALUES  ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9})
                        
        
        """.format(
            client.name_contact,
            client.name_contact_2,
            client.id_legal_client_type,
            client.id_client_type,
            client.dni,
            client.is_owner,
            client.email,
            client.id_origin,
            client.phone,
            client.address
        )
        table = "CLIENT"
        res = nbd.persistence.setWrite(stm, table)
        return res 
    except Exception as e:
        raise e