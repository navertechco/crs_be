from django.db import models



def CatalogField(name, Master, Detail):
   try:
        catalog = Master.objects.values_list('catalog_id', 'description').filter(description=name)
        # print(name)
        # print(catalog)
        # print(catalog[0][0])
        
        if len(catalog)>0:
            catalog_id = catalog[0][0]
            if len(Detail.objects.values_list('catalog_detail_id','catalog_id', 'description'))> 0:
                
                catalog_detail = list(Detail.objects.values_list('catalog_detail_id','catalog_id', 'description').filter(catalog_id=catalog_id))
                # print(catalog_detail) 
                return catalog_detail
        return []        
   except Exception as e:
       print(e)
       pass

 