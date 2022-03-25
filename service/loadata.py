from src.INFRA.IMPORT.catalogs import upload_catalogs


if __name__ == '__main__':
    upload_catalogs(filename="experiences.xlsx", page=0, cid=35, tags=[
                   "experienceName", "keyActivityType_fk", "keyActivityType_fk2"])