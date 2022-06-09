try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSFindCatalog import DSFindCatalog
from ..DSFindTableCatalog import DSFindTableCatalog
from naver_core import *
from naver_core import *
from src.business.Dto import CatalogDetailDto


def BSFindCatalog(input):
    try:
        results = DSFindCatalog(input)
        catalog_list = {"catalogs": {}}
        catalogs = getValue(input, 'catalogs')
        for catalog in catalogs:
            for result in results:
                if result["catalog"] == catalog or catalog == "ALL":
                    catalogDto = CatalogDetailDto(result)
                    if catalogDto.catalog not in list(catalog_list["catalogs"]):
                        catalog_list["catalogs"][catalogDto.catalog] = []
                    catalog_list["catalogs"][catalogDto.catalog].append(
                        catalogDto.__dict__())

        tables = getValue(input, 'tables')
        if tables is not None:
            for table in tables:
                name = table.get('name')
                result = DSFindTableCatalog(table)
                # catalogDto = CatalogDetailDto(result)
                catalog_list["catalogs"][name] = (result)
            pass

        return catalog_list

    except Exception as e:
        raise e
