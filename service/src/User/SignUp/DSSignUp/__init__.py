try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.WEB.App.routes import app
from src.Dto import *

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSSignUp	(data):
    """Método para crear un nuevo Reporte.

    Args:
        data (dict): Diccionario con los datos del Reporte.

    Returns:
        res: Resultado de la operación.
    """
    try:
        user = GamerDto(data)
        stm = """
        INSERT INTO public.gamer
        (identification, username, surname, lastname, email, phone, state, user_type_fk, credits, created, updated, "password")
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', 0, 1, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '{}');
        """.format(user.identification, user.username, user.surname, user.lastname, user.email, user.phone, user.password)
        table = "GAMER"
        res = nbd.persistence.setWrite(stm, table)
        return res

    except Exception as e:
        raise e
