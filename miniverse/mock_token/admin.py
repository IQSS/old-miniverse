from django.contrib import admin
from mock_token.models import ApplicationInfo, DataverseToken


"""
class DataverseTokenInline(admin.TabularInline):
    model = SingleFile
    extra= 1
    readonly_fields = ('update_time', 'create_time', 'md5', )
    fields = ('dataverse_user', 'single_file', 'application')
"""

class ApplicationInfoAdmin(admin.ModelAdmin):
    #inlines = (DataverseTokenInline)
    save_on_top = True
    list_display = ('name', 'ip_address', 'hostname', 'time_limit_minutes', 'contact_email', 'description' )
    readonly_fields = ('update_time', 'create_time', 'md5', )
admin.site.register(ApplicationInfo, ApplicationInfoAdmin)


class DataverseTokenAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('dataverse_user', 'single_file', 'application', 'last_refresh_time', 'file_metadata', 'token', 'update_time' )
    list_filter = ('application', )    
    readonly_fields = ('update_time', 'create_time', 'token', 'file_metadata' )
admin.site.register(DataverseToken, DataverseTokenAdmin)

