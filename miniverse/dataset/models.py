import os
from hashlib import md5

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db import models
from django.template.defaultfilters import slugify

from dataverse.models import Dataverse
from core.models import TimeStampedModel


class DatasetState(models.Model):
    """
    Version states for the DatasetVersion object
    DRAFT, IN REVIEW, RELEASED, ARCHIVED, DEACCESSIONED
    
    """    
    name = models.CharField(max_length=70)
    sort_order = models.IntegerField()
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(DatasetState, self).save(*args, **kwargs)
        
        
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('sort_order', 'name',)
        

class Dataset(TimeStampedModel):
    """Expects a .zip file upload
    Modify in the future for shapefiles loaded separately
    """
    name = models.CharField(max_length=255)
    dataverse = models.ForeignKey(Dataverse)

    version_state = models.ForeignKey(DatasetState)
    
    version_number =  models.IntegerField(default=1)
    minor_version_number = models.IntegerField(default=0)
    
    description = models.TextField(blank=True)
        
    md5 = models.CharField(max_length=40, blank=True, db_index=True, help_text='auto-filled on save')
    
    
    def get_dv_api_params(self):
        if not self.id:
            return {}
            
        p = { 'dataset_id' : self.id\
                , 'dataset_version_id' : self.version_number\
                , 'dataset_name' : self.name\
                , 'dataset_description' : self.description\
                }
        p.update(self.dataverse.get_dv_api_params())
        return p
        
    def save(self, *args, **kwargs):
        if not self.id:
            super(Dataset, self).save(*args, **kwargs)
        self.md5 = md5('%s%s' % (self.id, self.name)).hexdigest()

        super(Dataset, self).save(*args, **kwargs)
    
    def natural_key(self):
            return '%s-%s' % (self.name, self.dataverse)
            
    def view_dataset_list(self):
        lnk = reverse('view_dataset_list', kwargs={})
        return '<a href="%s">view dataset</a>' % lnk
    view_dataset_list.allow_tags = True
    
    def get_files(self):
        return self.datafile_set.all()
        
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',  )
        #verbose_name = 'COA File Load Log'

        
    
class DataFile(TimeStampedModel):
    """Used for working with a selected shapefile, specifically using the extensions specified in WORLDMAP_MANDATORY_IMPORT_EXTENSIONS
    
    """
    dataset_file = models.FileField(upload_to='datafile/%Y/%m/%d')# max_length=255)
    dataset = models.ForeignKey(Dataset)
    
    has_gis_data = models.BooleanField(default=False)

    file_checksum = models.CharField(max_length=40, blank=True, db_index=True, help_text='auto-filled on save')
    
    #mime_type = models.CharField(max_length=255, blank=True)
    
    md5 = models.CharField(max_length=40, blank=True, db_index=True, help_text='auto-filled on save')
    

    def get_dv_api_params(self, request=None):
        """
        Params to respond to API call from GeoConnect
        """
        if not self.id:
            return {}
        
        # Params from Datafile
        p = { 'datafile_id' : self.id\
                , 'datafile_label': self.get_basename()\
                #, 'has_gis_data' : self.has_gis_data
                ,'filename' : self.get_basename()\
                ,'filesize' : self.dataset_file.size\
                ,'created' : str(self.created)\
                ,'datafile_type': '--file-type--'\
                ,'datafile_expected_md5_checksum': self.file_checksum\
            }        
                        
        # Full url to file, if available
        if request:
            p['datafile_download_url'] = request.build_absolute_uri(self.dataset_file.url)
        
        # Add params from owning Dataset and Dataverse
        p.update(self.dataset.get_dv_api_params())    
            
        return p
        
    def get_mapit_link(self):
        return 'http://127.0.0.1:8000/shapefile/examine-dvn-file/%s/%s' % (self.dataset.id, self.id)

    def dataverse_name(self):
        return self.dataset.dataverse.name
    dataverse_name.allow_tags = True
    
    def get_basename(self):
        return os.path.basename(self.dataset_file.name)

    def save(self, *args, **kwargs):
        if not self.id:
            super(DataFile, self).save(*args, **kwargs)
        self.md5 = md5('%s%s' % (self.id, self.dataset_file)).hexdigest()

        self.file_checksum = self.md5   # fake, need to add real md5
        
        super(DataFile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.get_basename()

    class Meta:
        ordering = ('dataset_file',)

