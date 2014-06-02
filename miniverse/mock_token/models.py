from hashlib import md5, sha224
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db import models
from dataset.models import DataFile
from datetime import date, datetime
from django.utils.timezone import utc
from django.contrib.auth.models import User
import shutil
import urllib


#class APIPermission
#    name = models.CharField(max_length=255, unique=True)
#    url_name = models.CharField(max_length=255, unique=True)
#    def does_url_name_exist
    
class ApplicationInfo(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(help_text='contact info, etc')
    contact_email = models.EmailField()
    
    hostname = models.CharField(max_length=255, blank=True)
    ip_address = models.CharField(max_length=15, blank=True)
    
    mapit_link = models.URLField(help_text='http://geoconnect.harvard.edu')
    #api_permissions = models.ManyToManyField(APIPermission, blank=True, null=True)
    
    time_limit_minutes = models.IntegerField(default=30, help_text='in minutes')
    time_limit_seconds = models.IntegerField(default=0, help_text='autofilled on save')
    
    md5 = models.CharField(max_length=40, blank=True, db_index=True, help_text='auto-filled on save')
    
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        if not self.id:
            super(ApplicationInfo, self).save(*args, **kwargs)
        
        self.md5 = md5('%s%s' % (self.id, self.name)).hexdigest()
        self.time_limit_seconds = self.time_limit_minutes * 60  
        super(ApplicationInfo, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Application information'
        verbose_name_plural = verbose_name


class DataverseToken(models.Model):
    """Superclass for a GIS File "Helper"
    - Examples of GIS files: shapefiles, GeoTiffs, spreadsheets or delimited text files with lat/lng, GeoJSON etc
    """
    token = models.CharField(max_length=255, blank=True, help_text = 'auto-filled on save', db_index=True)
    application = models.ForeignKey(ApplicationInfo)

    dataverse_user = models.ForeignKey(User)
    data_file = models.ForeignKey(DataFile)
    
    has_expired = models.BooleanField(default=False)
    #dataset_version = models.IntegerField()
    
    last_refresh_time =  models.DateTimeField(auto_now_add=True)
           
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s (%s)' % (self.dataverse_user, self.data_file)


    def has_token_expired(self, current_time=None):
        """Check if the token has expired.
        Find the difference between the current time and the token's "last_refresh_time"
        Compare it to the ApplicationInfo "time_limit_seconds" attribute
        
        :current_time   datetime object that is timezone aware or None
        """
        if current_time is None:
            current_time = datetime.utcnow().replace(tzinfo=utc)
        
        try:
            mod_time = current_time - self.last_refresh_time
        except:
            return True
            
        if mod_time.seconds > self.application.time_limit_seconds:
            self.has_expired = True
            self.save()
            return True
        
        return False
        
    def refresh_token(self):
        current_time = datetime.utcnow().replace(tzinfo=utc)
        if self.has_token_expired(current_time):
            return False            
        self.last_refresh_time = current_time
        self.save()
        return True
        
    def save(self, *args, **kwargs):
        if not self.id:
            super(DataverseToken, self).save(*args, **kwargs)
        
        if not self.token:
            self.token = sha224('[id:%s][sf:%s]' % (self.id, self.data_file.md5)).hexdigest()

        super(DataverseToken, self).save(*args, **kwargs)
    
    def get_mapit_link_with_token(self, request):
        #metadata_url = reverse('view_data_file_metadata', kwargs={'dv_token' : self.token})
        
        d = {}
        metadata_url = reverse('view_data_file_metadata_base_url', kwargs={})
        d['cb'] = request.build_absolute_uri(metadata_url) #request.get_host()
        callback_url = urllib.urlencode(d)
        return self.application.mapit_link + '%s/?%s' % (self.token, callback_url)
    
    def file_metadata(self):
        lnk = reverse('view_data_file_metadata', kwargs={ 'dv_token' : self.token })
        return '<a href="%s">metadata api</a>' % lnk
    file_metadata.allow_tags = True
    
    @staticmethod
    def get_new_token(user, application, data_file):
        if user is None:
            raise Exception('no user') 
        if application is None:
            raise Exception('no application') 
        if data_file is None:
            raise Exception('no data_file_id') 

        dv_token = DataverseToken(application=application\
                                , dataverse_user=user\
                                , data_file=data_file\
                                )
        dv_token.save()
        
        return dv_token