import pandas as pd
import os
import requests
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
 
 
FILE_PATH_XSLX = os.path.join(ROOT_DIR,"experience.xlsx")

  
experience_xlsx = pd.read_excel(FILE_PATH_XSLX, engine='openpyxl')
data = experience_xlsx.to_dict()
experiences = []

catalogs = []

for col,values in data.items():
    dto = {}
    dto[col]=None
    for row,value in values.items():
        if len(experiences)<=row:
            experiences.append({})
        dto[col]=value
        experiences[row]={**experiences[row],**dto}
i=7         
for experience in experiences:
    experience_name = experience.get('experienceName')
    keyActivityType_fk = experience.get('keyActivityType_fk')
    keyActivityType_fk2 = experience.get('keyActivityType_fk2')
    catalog = {
        
        "catalog_id":35,
        "order":0,
        "description":f"{experience_name}-{keyActivityType_fk}-{keyActivityType_fk2}-{i}",
        "is_active":True,
        "code":i,
        "value":experience
        
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
