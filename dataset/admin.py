from django.contrib import admin
from dataset.models import Dataset, SingleFile


class SingleFileInline(admin.TabularInline):
    model = SingleFile
    extra= 1
    readonly_fields = ('update_time', 'create_time', 'md5', )
    fields = ('dataset_file', 'has_gis_data')
    
class DatasetAdmin(admin.ModelAdmin):
    inlines = (SingleFileInline, )
    save_on_top = True
    search_fields = ('name',  )
    list_filter = ('dataverse', )    
    readonly_fields = ('update_time', 'create_time', 'md5', 'view_dataset_list')
    list_display = ('name', 'dataverse', 'view_dataset_list', 'metadata_text', 'update_time' )
admin.site.register(Dataset, DatasetAdmin)

class SingleFileAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ('dataset__name', 'dataset_file'  )
    list_filter = ('has_gis_data', 'dataset', )    
    readonly_fields = ('update_time', 'create_time', 'md5', 'dataverse_name')
    list_display = ('dataset_file', 'dataset', 'dataverse_name', 'has_gis_data', 'update_time'  )
admin.site.register(SingleFile, SingleFileAdmin)

