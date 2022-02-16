import pandas as pd
import os
import requests

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
 
FILE_PATH_JSON = os.path.join(ROOT_DIR,"hotel.json")
FILE_PATH_XSLX = os.path.join(ROOT_DIR,"hotel.xlsx")

 
hotel_json = pd.read_json(FILE_PATH_JSON).to_dict()
hotel_xlsx = pd.read_excel(FILE_PATH_XSLX, engine='openpyxl').to_dict()
hotels = []
dto = {}
catalogs = []
for key,values in hotel_xlsx.items():
    dto[key]=None
    for index,value in values.items():
        if len(hotels)<index + 1:
            hotels.append({})
        dto[key]=value
        hotels[index]={**hotels[index],**dto}
            
i=7         
for hotel in hotels:
    hotel_name = hotel.get('hotelname')
    room_category = hotel.get('roomcategory')
    catalog = {
        
        "catalog_id":24,
        "order":0,
        "description":f"{hotel_name}-{room_category}",
        "is_active":True,
        "code":i,
        "value":hotel
        
    }
    catalogs.append(catalog)
    i+=1




print(hotels)
