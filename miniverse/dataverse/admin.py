from django.contrib import admin
from dataverse.models import Dataverse

class DataverseAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ('name',  )
    list_filter = ('parent_dataverse', )    
    readonly_fields = ('update_time', 'create_time', 'md5', 'breadcrumb',)
    list_display = ('name', 'parent_dataverse', 'breadcrumb',  )
admin.site.register(Dataverse, DataverseAdmin)

