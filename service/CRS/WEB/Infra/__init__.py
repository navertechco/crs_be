try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from flask_mysqldb import MySQLdb

inframessage = "hola desde infra"
db = MySQLdb.connect("dentalmedical.app", "zaq12wsx",
                     "D1c13mbr31234.", "dentalmedicaldb")
                     
def query_db(query, args=()):
    cur = db.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return r


def execute_db(query, args=()):
    cur = db.cursor()
    try:
        cur.execute(query, args)
        cur.connection.close()
        return True
    except cur.Error:
        cur.connection.close()
        return False
