from hashlib import md5
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db import models
from datetime import date
from django.contrib.auth.models import User
import shutil

class Dataverse(models.Model):
    """Bare bones dataverse, just a name, owner, metadata text
    Simply for display, no checking, even for circular relationships, etc.
    """
    name = models.CharField(max_length=255)
    
    parent_dataverse = models.ForeignKey('self', blank=True, null=True)
    
    owner = models.ForeignKey(User)
    
    description = models.TextField(blank=True)
        
    md5 = models.CharField(max_length=40, blank=True, db_index=True, help_text='auto-filled on save')
    
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def get_dv_api_params(self):
        """
        Params to respond to API call from GeoConnect
        """
        if not self.id:
            return {}

        return { 'dv_id' : self.id\
                , 'dv_name' : self.name\
                , 'dv_user_id' : self.owner.id\
                , 'dv_user_email' : self.owner.email\
                , 'dv_username' : self.owner.username\
                }
        
    def breadcrumb(self):
        if not self.id or not self.parent_dataverse:
            return 'n/a'
        l = [self.name]
        
        parent = self.parent_dataverse
        while parent:
            l.append(parent.name)
            parent = parent.parent_dataverse
        l.reverse()
        return ' > '.join(l)
    breadcrumb.allow_tags = True
                      
        
    def save(self, *args, **kwargs):
        if Dataverse.is_parent_relationship_circular(self, self.parent_dataverse):
            raise Exception("Dataverse parent relationship is circular")
        
        if not self.id:
            super(Dataverse, self).save(*args, **kwargs)

        self.md5 = md5('%s%s' % (self.id, self.name)).hexdigest()
        super(Dataverse, self).save(*args, **kwargs)
        
        
    def __unicode__(self):
        return self.name
    
    @staticmethod
    def is_parent_relationship_circular(instance, new_parent):
        """
            Make sure parent relationship isn't circular
            e.g. you don't want parent relations such as below:

            "<-" = "parent of"

            ex 1/   red <- apple
                    apple <- red
            ex 2/   food <- fruit <- yellow <- banana
                    banana <- food
            etc.            
        """
        if new_parent and instance:
            if instance.id == new_parent.id:
                return True

        # This will be a new root
        if instance and new_parent is None:           
            return False

        # case: p1 -> p1    
        if instance == new_parent or instance == instance.parent_dataverse:
            return True

        parent = new_parent
        plist = [instance]
        while parent:
            if parent in plist:
                return True
            plist.append(parent)
            parent = parent.parent_dataverse     

        return False

        
    class Meta:
        ordering = ('name',  )
