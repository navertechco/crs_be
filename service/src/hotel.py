import pandas as pd
import os
import requests
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
 
FILE_PATH_JSON = os.path.join(ROOT_DIR,"hotel.json")
FILE_PATH_XSLX = os.path.join(ROOT_DIR,"hotel.xlsx")

 
hotel_json = pd.read_json(FILE_PATH_JSON).to_dict()
hotel_xlsx = pd.ExcelFile(FILE_PATH_XSLX, engine='openpyxl')
data = hotel_xlsx.parse(hotel_xlsx.sheet_names[0]).to_dict()
hotels = []

catalogs = []

for col,values in data.items():
    dto = {}
    dto[col]=None
    for row,value in values.items():
        if len(hotels)<=row:
            hotels.append({})
        dto[col]=value
        hotels[row]={**hotels[row],**dto}
i=7         
for hotel in hotels:
    hotel_name = hotel.get('hotelname')
    room_category = hotel.get('roomcategory')
    catalog = {
        
        "catalog_id":24,
        "order":0,
        "description":f"{hotel_name}-{room_category}-{i}",
        "is_active":True,
        "code":i,
        "value":hotel
        
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
