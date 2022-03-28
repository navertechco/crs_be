from src.INFRA.IMPORT.catalogs import upload_catalogs


if __name__ == '__main__':
    upload_catalogs(filename="cruises.xlsx", page=0, cid=36, tags=[
                   "ship_name", "cruise_format", "cabine_type"])