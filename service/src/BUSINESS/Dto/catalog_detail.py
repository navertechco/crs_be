class CatalogDetailDto():
    def __init__(self, data):

        self.catalog_detail_id = data.get("catalog_detail_id")
        self.catalog_id = data.get("catalog_id")
        self.created = data.get("created")
        self.updated = data.get("updated")
        self.order = data.get("order")
        self.description = data.get("description")
        self.code = data.get("code")
        self.is_active = data.get("is_active")

    def __dict__(self):
        return {

            "catalog_detail_id": self.catalog_detail_id,
            "catalog_id": self.catalog_id,
            "created": self.created,
            "updated": self.updated,
            "order": self.order,
            "description": self.description,
            "code": self.code,
            "is_active": self.is_active,
        }
