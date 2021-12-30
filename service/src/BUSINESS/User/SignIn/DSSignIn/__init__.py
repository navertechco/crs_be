try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.INFRA.WEB.App.routes import app

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSSignIn(username):
    """Método para iniciar sesión en el sistema
    0.- NEW: El usuario es nuevo, no se ha registrado en la base de datos
    1.- UNCONFIRMED: El usuario esta en la base de datos pero no ha confirmado su cuenta
    2.- REGISTERED: El usuario esta en la base de datos y ha confirmado su cuenta
    3.- FORGOT: El usuario esta en la base de datos pero ha olvidado su contraseña
    4.- BLOCK: El usuario esta en la base de datos pero ha sido bloqueado
    5.- DISCONNECTED: El usuario esta en la base de datos y ha cerrado sesion
    6.- CONNECTED: El usuario esta en la base de datos y ha iniciado sesion

    Args:
        username (str): Nombre de usuario

    Raises:
        e: Error de conexión a la base de datos

    Returns:
        [lst]: Lista con los datos del usuario
    """
    try:
        table = "USER"
        schema = "entities"
        update_stm = """ UPDATE {0}.{1} \n""".format(schema, table)
        set_stm = update_stm + """ SET STATE = 6  """
        where_stm = set_stm +  """ WHERE USERNAME = \'{0}\' """.format(username)
        and_stm = where_stm + """  AND (STATE = 5  OR STATE = 2 ) """
        res = nbd.persistence.setWrite(and_stm, table)['session']
        if isinstance(res, object):
            res.commit()
            select_stm = """   SELECT * """
            from_stm = select_stm + """ FROM {0}.{1} """.format(schema, table)
            where_stm =  from_stm + """      WHERE USERNAME = \'{0}\' """.format(username)
            and_stm =  where_stm +  """      AND STATE = 6; -- CONNECTED \n"""
         
        res = nbd.persistence.getQuery(and_stm, table)
        return res

    except Exception as e:
        raise e
