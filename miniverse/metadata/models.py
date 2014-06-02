from django.db import models

from dataset.models import Dataset
from core.models import TimeStampedModel

# Create your models here.
class MetaDataBase(TimeStampedModel):
    
    dataset = models.ForeignKey(Dataset)
    
    metadata_type = models.CharField(max_length=255, blank=True, help_text='auto-filled on save')

    def get_type(self):
        return self.__class__.__name__
        
    def __unicode__(self):
        return '%s' % self.dataset
        
    def save(self, *args, **kwargs):
    
        #self.metadata_type = self.__class__.__name__

        super(GeographicMetadata, self).save(args, kwargs)

    class Meta:
        ordering = ('-modified', 'dataset')
        
       
        
class GeographicMetadata(MetaDataBase):
    """
    Metadata regarding a related WorldMap Layer
    """
    layer_name = models.CharField(max_length=255)
    layer_link = models.URLField()
    embed_map_link = models.URLField(blank=True)
    worldmap_username = models.CharField(max_length=255)
    
    bbox_min_lng = models.DecimalField(max_digits=12, decimal_places=10, default=-1)
    bbox_min_lat = models.DecimalField(max_digits=12, decimal_places=10, default=-1)
    bbox_max_lng = models.DecimalField(max_digits=12, decimal_places=10, default=-1)
    bbox_max_lat = models.DecimalField(max_digits=12, decimal_places=10, default=-1)
    
    def save(self, *args, **kwargs):
    
        self.metadata_type = self.__class__.__name__

        super(GeographicMetadata, self).save(args, kwargs)
    
