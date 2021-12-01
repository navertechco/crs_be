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

def DSPlayTour	(slug):
    """Método para reproducir una lista de videos del Tour.

    Args:
        slug (str): Slug del Tour.
        
    Returns:
        res: Resultado de la operación.
    """
    try:
        table = "ITINERARY"
        Command = "SELECT "
        From = " * FROM {}".format(table)
        Where = " WHERE playlist_slug = \'{}'".format( slug) 
        stm = Command + From + Where
        itinerary = nbd.persistence.getQuery(stm, table)
        if len(itinerary) > 0:
            reproductions = itinerary[0]['reproductions']
            if reproductions > 0:
                Command = "UPDATE "
                Table = "{}".format(table)
                Set = " SET reproductions={}".format(reproductions-1)
                Where = " WHERE playlist_slug = \'{}'".format( slug) 
                stm = Command + Table + Set + Where
                update = nbd.persistence.setWrite(stm, table)
                if len(update) > 0:
                    update['session'].commit()
                    return itinerary[0]['playlist']
                raise Exception("No se pudo actualizar la cantidad de reproducciones.")
            raise Exception("No se puede reproducir el Tour porque ya se ha reproducido 2 veces")
        raise Exception("No se encontró el Tour")    

    except Exception as e:
        raise e