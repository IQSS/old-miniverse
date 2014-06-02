from django.contrib import admin
from metadata.models import GeographicMetadata

class GeographicMetadataAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ('name',  )
    list_filter = ('parent_dataverse', )    
    readonly_fields = ('created', 'modified', )
    list_display = ('dataset', 'layer_name', 'worldmap_username', 'layer_link', 'bbox_min_lng', 'bbox_min_lat', 'bbox_max_lng', 'bbox_max_lat', )
admin.site.register(GeographicMetadata, GeographicMetadataAdmin)


