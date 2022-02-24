try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSCreateCatalog import DSCreateCatalog
from naver_core import *
import ast, json,re, yaml
def myconverter(o):
    if "datetime" in str(o):
        return str(o).replace(",","-").replace("datetime.date","").__str__()
    
def BSCreateCatalog(input):
    try:
        state = input.get('state')
        if state == "tour":
            value = getValue(input, 'value')  
            value = yaml.safe_load(value)
            print(value)
            value = json.dumps(value, default=myconverter)
            value = json.loads(value)
            input["data"]["value"] = value
        result = DSCreateCatalog(input)
        if len(result) > 0:
            result["session"].commit()
        return True

    except Exception as e:
        raise e
