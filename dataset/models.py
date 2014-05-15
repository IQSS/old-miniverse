import os
from hashlib import md5
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db import models
from dataverse.models import Dataverse

class Dataset(models.Model):
    """Expects a .zip file upload
    Modify in the future for shapefiles loaded separately
    """
    name = models.CharField(max_length=255)
    dataverse = models.ForeignKey(Dataverse)

    metadata_text = models.TextField(blank=True)
        
    md5 = models.CharField(max_length=40, blank=True, db_index=True, help_text='auto-filled on save')
    
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    
    
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
        return self.singlefile_set.all()
        
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',  )
        #verbose_name = 'COA File Load Log'

     
class SingleFile(models.Model):
    """Used for working with a selected shapefile, specifically using the extensions specified in WORLDMAP_MANDATORY_IMPORT_EXTENSIONS
    
    """
    dataset_file = models.FileField(upload_to='datafile/%Y/%m/%d')# max_length=255)
    dataset = models.ForeignKey(Dataset)
    
    has_gis_data = models.BooleanField(default=False)
    #mime_type = models.CharField(max_length=255, blank=True)
    
    md5 = models.CharField(max_length=40, blank=True, db_index=True, help_text='auto-filled on save')
    
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def get_mapit_link(self):
        return 'http://127.0.0.1:8000/shapefile/examine-dvn-file/%s/%s' % (self.dataset.id, self.id)

    def dataverse_name(self):
        return self.dataset.dataverse.name
    dataverse_name.allow_tags = True
    
    def get_basename(self):
        return os.path.basename(self.dataset_file.name)

    def save(self, *args, **kwargs):
        if not self.id:
            super(SingleFile, self).save(*args, **kwargs)
        self.md5 = md5('%s%s' % (self.id, self.dataset_file)).hexdigest()

        super(SingleFile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.get_basename()

    class Meta:
        ordering = ('dataset_file',)

