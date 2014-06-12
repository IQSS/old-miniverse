from django.db import models


"""
# from inspectdb
class Dvobject(models.Model):
    id = models.IntegerField(primary_key=True)
    dtype = models.CharField(max_length=31, blank=True)
    
    createdate = models.DateTimeField(blank=True, null=True)
    publicationdate = models.DateTimeField(blank=True, null=True)

    creator = models.ForeignKey(Dataverseuser, blank=True, null=True)

    owner = models.ForeignKey('self', blank=True, null=True)

    releaseuser = models.ForeignKey(Dataverseuser, blank=True, null=True)

    authority = models.CharField(max_length=255, blank=True)
    identifier = models.CharField(max_length=255, blank=True)
    protocol = models.CharField(max_length=255, blank=True)
    affiliation = models.CharField(max_length=255, blank=True)
    alias = models.CharField(max_length=255, blank=True)
    backgroundcolor = models.CharField(max_length=255, blank=True)

    contactemail = models.EmailField(max_length=255, blank=True)

    description = models.TextField(blank=True)

    facetroot = models.NullBooleanField()

    linkcolor = models.CharField(max_length=255, blank=True)
    linktext = models.CharField(max_length=255, blank=True)
    linkurl = models.CharField(max_length=255, blank=True)
    logo = models.CharField(max_length=255, blank=True)
    logoalignment = models.CharField(max_length=255, blank=True)
    logobackgroundcolor = models.CharField(max_length=255, blank=True)
    logoformat = models.CharField(max_length=255, blank=True)
    metadatablockroot = models.NullBooleanField()

    name = models.CharField(max_length=255, blank=True)
    permissionroot = models.NullBooleanField()
    tagline = models.CharField(max_length=255, blank=True)
    textcolor = models.CharField(max_length=255, blank=True)
    contenttype = models.CharField(max_length=255, blank=True)
    filesystemname = models.CharField(max_length=255, blank=True)
    ingeststatus = models.CharField(max_length=1, blank=True)
    md5 = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'dvobject'
"""
