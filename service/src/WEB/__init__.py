try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__) 
from .App.routes import app 

from os import system

 
def main(host,port):
    app.run(host=host, port=port)
 