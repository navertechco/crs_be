"""catalogs module."""
import os
import json
import pandas as pd
import requests
from src.INFRA.WEB.App.libs import app


def load_file(**kwargs):
    """
    load_file Function
    ~~~~~~~~~~~~~~~~~~~~~

    Requests is an HTTP library, written in Python, for human beings.
    Basic usage:

    """
    [filename, page] = {**kwargs}
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    rows_xlsx = pd.ExcelFile(file_path, engine='openpyxl')
    data = rows_xlsx.parse(rows_xlsx.sheet_names[page]).to_dict()
    return data


def get_rows(**kwargs):
    """_summary_

    Returns:
        _type_: _description_
    """
    data = load_file(**kwargs)
    rows = []
    for col, values in data.items():
        dto = {}
        dto[col] = None
        for row, value in values.items():
            if len(rows) <= row:
                rows.append({})
            dto[col] = value
            rows[row] = {**rows[row], **dto}
    return rows


def get_tag(row, tags):
    """_summary_

    Args:
        row (_type_): _description_
        tags (_type_): _description_

    Returns:
        _type_: _description_
    """
    res = ""
    for tag in tags:
        res += row.get(tag)+"-"
    return res


def get_catalogs(**kwargs):
    """_summary_

    Returns:
        _type_: _description_
    """
    [cid, tags] = {**kwargs}
    rows = get_rows(**kwargs)
    catalogs = []
    i = 7
    for row in rows:
        tag = get_tag(row, tags)
        catalog = {
            "catalog_id": cid,
            "order": 0,
            "description": f"{tag}-{i}",
            "is_active": True,
            "code": i,
            "value": row
        }
        catalogs.append(catalog)
        i += 1
    return catalogs


def upload_catalogs(**kwargs):
    """_summary_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
    """
    server = os.environ.get('SERVER')
    catalogs = get_catalogs(**kwargs)
    print(catalogs[0])
    for catalog in catalogs:
        try:
            data = {}
            data = {
                "data": catalog
            }
            res = requests.post(
                f'{server}/Admin/CreateCatalog', data=json.dumps(data))
            status = res.status_code
            # response = r.json()
            return status == 200
        except Exception as error:
            print(error)
            raise error


if __name__ == '__main__':
    upload_catalogs(filename="experience.xlsx", page=2, cid=35, tags=[
                   "experienceName", "keyActivityType_fk", "keyActivityType_fk2"])
