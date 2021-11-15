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

def DSLogout(indetification):
    """Método de persistencia para desconectar usuario

    0.- NEW: El usuario es nuevo, no se ha registrado en la base de datos
    1.- UNCONFIRMED: El usuario esta en la base de datos pero no ha confirmado su cuenta
    2.- REGITERED: El usuario esta en la base de datos y ha confirmado su cuenta
    3.- FORGOT: El usuario esta en la base de datos pero ha olvidado su contraseña
    4.- BLOCK: El usuario esta en la base de datos pero ha sido bloqueado
    5.- DISCONNECTED: El usuario esta en la base de datos y ha cerrado sesion
    6.- CONNECTED: El usuario esta en la base de datos y ha iniciado sesion

    Args:
        indetification (int): identificador de usuario

    Raises:
        e: Error de conexión a base de datos

    Returns:
        dict: respuesta de conexión a base de datos
    """    
    try:
        stm = """UPDATE GAMER
                    SET
                        STATE = 5  -- DISCONNECTED
                        WHERE IDENTIFICATION = \'{}\'
                        AND STATE = 6 -- CONNECTED
                            """.format(indetification)
        table = "GAMER"
        res = nbd.persistence.setWrite(stm, table)
        return res  

    except Exception as e:
        raise e