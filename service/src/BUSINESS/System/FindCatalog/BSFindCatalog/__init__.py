try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSFindCatalog import DSFindCatalog
import logging
from naver_core import *
from src.BUSINESS.Dto import CatalogDetailDto


def BSFindCatalog(input):
    try:
        results = DSFindCatalog(input)
        catalog_list = {"catalogs": {}}
        catalogs = getValue(input, 'catalogs')
        for catalog in catalogs:
            catalog_list["catalogs"][catalog]=[]
            for result in results:
                catalogDto = CatalogDetailDto(result)
                if catalogDto.catalog==catalog:
                    catalog_list["catalogs"][catalog].append(catalogDto.__dict__())
                    
        return catalog_list

    except Exception as e:
        raise e