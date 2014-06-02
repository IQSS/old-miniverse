from django.contrib import admin
from dataset.models import Dataset, DataFile


class DataFileInline(admin.TabularInline):
    model = DataFile
    extra= 1
    readonly_fields = ('update_time', 'create_time', 'md5', )
    fields = ('dataset_file', 'has_gis_data')
    
class DatasetAdmin(admin.ModelAdmin):
    inlines = (DataFileInline, )
    save_on_top = True
    search_fields = ('name',  )
    list_filter = ('dataverse', )    
    readonly_fields = ('update_time', 'create_time', 'md5', 'view_dataset_list')
    list_display = ('name', 'dataverse', 'view_dataset_list', 'description', 'update_time' )
admin.site.register(Dataset, DatasetAdmin)

class DataFileAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ('dataset__name', 'dataset_file'  )
    list_filter = ('has_gis_data', 'dataset', )    
    readonly_fields = ('update_time', 'create_time', 'md5', 'dataverse_name')
    list_display = ('dataset_file', 'dataset', 'dataverse_name', 'has_gis_data', 'update_time'  )
admin.site.register(DataFile, DataFileAdmin)

