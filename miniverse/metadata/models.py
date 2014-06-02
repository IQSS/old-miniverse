from django.db import models

from dataset.models import Dataset
from core.models import TimeStampedModel

# Create your models here.
class MetadataBase(TimeStampedModel):
    
    dataset = models.ForeignKey(Dataset)
    
    metadata_type = models.CharField(max_length=255, blank=True, help_text='auto-filled on save')

    def get_type(self):
        return self.__class__.__name__
        
    def __unicode__(self):
        return '%s' % self.dataset
        
    class Meta:
        ordering = ('-modified', 'dataset')
        
       
        
class GeographicMetadata(MetadataBase):
    """
    Metadata regarding a related WorldMap Layer
    """
    layer_name = models.CharField(max_length=255, unique=True, db_index=True)
    layer_link = models.URLField()
    embed_map_link = models.URLField(blank=True)
    worldmap_username = models.CharField(max_length=255)
    
    bbox_min_lng = models.DecimalField(max_digits=12, decimal_places=7, default=0)
    bbox_min_lat = models.DecimalField(max_digits=12, decimal_places=7, default=0)
    bbox_max_lng = models.DecimalField(max_digits=12, decimal_places=7, default=0)
    bbox_max_lat = models.DecimalField(max_digits=12, decimal_places=7, default=0)
    
    def save(self, *args, **kwargs):
    
        self.metadata_type = self.__class__.__name__

        super(GeographicMetadata, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Geographic metadata'