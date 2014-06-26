from django.db import models

from dataset.models import DataFile
from core.models import TimeStampedModel

# Create your models here.
class MetadataBase(TimeStampedModel):
    
    datafile = models.ForeignKey(DataFile)
        
    def __unicode__(self):
        return '%s' % self.datafile
        
    class Meta:
        abstract=True
        ordering = ('-modified', 'datafile')
        
       
        
class GeographicMetadata(MetadataBase):
    """
    Metadata regarding a related WorldMap Layer
    """
    layer_name = models.CharField(max_length=255, unique=True, db_index=True)
    layer_link = models.URLField()
    embed_map_link = models.URLField(blank=True)
    worldmap_username = models.CharField(max_length=255)
    
    bbox_min_lng = models.DecimalField(max_digits=14, decimal_places=7, default=0)
    bbox_min_lat = models.DecimalField(max_digits=14, decimal_places=7, default=0)
    bbox_max_lng = models.DecimalField(max_digits=14, decimal_places=7, default=0)
    bbox_max_lat = models.DecimalField(max_digits=14, decimal_places=7, default=0)
    
    links_working = models.BooleanField(default=True)
    #def save(self, *args, **kwargs):
    #    super(GeographicMetadata, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Geographic metadata'