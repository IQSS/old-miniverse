import requests
from .models import GeographicMetadata

"""
from metadata.models import GeographicMetadata
for x in GeographicMetadata.objects.all():
    x.links_working=True
    x.save()
"""
class LinkChecker:
    
    @staticmethod
    def verify_links(meta_info):
        if not type(meta_info) is GeographicMetadata:
            return
            
        for lnk in [meta_info.layer_link, meta_info.embed_map_link]:
            if not lnk:
                continue
            r = requests.get(meta_info.layer_link)
        
            if not r.status_code == 200:
                meta_info.links_working = False
                meta_info.save()
                return
                
        meta_info.links_working = True                    
        meta_info.save()
