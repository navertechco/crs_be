import json
class CatalogDetailDto():
    def __init__(self, data):
 
        self.catalog = data.get("catalog")
        self.order = data.get("order")
        self.description = data.get("description")
        self.code = data.get("code")
        self.value = json.loads(data.get("value"))

    def __dict__(self):
        return {
 
            "catalog": self.catalog, 
            "order": self.order,
            "description": self.description,
            "code": self.code,
            "value": self.value,
        }
