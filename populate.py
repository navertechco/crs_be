import pandas as pd
from faker import Faker
from collections import defaultdict 
from sqlalchemy import create_engine
fake = Faker()
fake_data = defaultdict(list)
for _ in range(10):
    fake_data["id_destination"].append(1)
    fake_data["id_supplier"].append(1)
    fake_data["id_key_activity"].append(1)
    fake_data["id_service_type"].append(1)
    fake_data["id_budget"].append(1)
    fake_data["id_delimiter"].append(1)
    fake_data["me"].append(True)
    fake_data["open_days"].append("L,M,X,J,V,S,D")
    fake_data["close_time"].append("23:59")
    fake_data["open_time"].append("0:00")
    fake_data["cost"].append(9)
    fake_data["selling_price"].append(10)
    fake_data["name"].append(fake.name())
    fake_data["description"].append("")
    fake_data["time"].append(60)
    fake_data["id_age_friendly_range"].append(1)
    fake_data["child_frendly"].append(True)
    fake_data["infant_friendly"].append(True)
    fake_data["observation"].append("")
    fake_data["max_capacity"].append(10)
    fake_data["pet_friendly"].append(True)


    df_fake_data = pd.DataFrame(fake_data)
    df_fake_data

    engine = create_engine('postgresql://postgres:postgres@172.16.0.129:5432/CRS', echo=False)
    df_fake_data.to_sql('service', con=engine,index=False, if_exists='append')



