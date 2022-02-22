import pandas as pd
import os
import requests
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
 
 
FILE_PATH_XSLX = os.path.join(ROOT_DIR,"cruises.xlsx")

  
cruise_xlsx = pd.read_excel(FILE_PATH_XSLX, engine='openpyxl')
data = cruise_xlsx.to_dict()
cruises = []

catalogs = []

for col,values in data.items():
    dto = {}
    dto[col]=None
    for row,value in values.items():
        if len(cruises)<=row:
            cruises.append({})
        dto[col]=value
        cruises[row]={**cruises[row],**dto}
i=7         
for cruise in cruises:
    ship_name = cruise.get('ship_name')
    category = cruise.get('category') 
    catalog = {
        
        "catalog_id":36,
        "order":0,
        "description":f"{ship_name}-{category}-{i}",
        "is_active":True,
        "code":i,
        "value":cruise
        
    }
    catalogs.append(catalog)
    i+=1

for catalog in catalogs:
    
    try:
        data = {}
        data={
        "data":catalog
    }
        r = requests.post('http://192.168.101.4:9999/Admin/CreateCatalog', data=json.dumps(data))
        status = r.status_code
        response = r.json()
        s=1
    except Exception as e:
        print(e)
        raise e
    
     



print(catalogs[0])
