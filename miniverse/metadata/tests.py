from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from datetime import datetime, timedelta
from django.utils.timezone import utc

from miniverse_util.msg_util import *
from dataverse.models import Dataverse
from dataset.models import DataFile, Dataset

from metadata.forms import GeographicMetadataUpdateForm

from mock_token.models import ApplicationInfo, DataverseToken
# Create your tests here.

class TokenTestCase(TestCase):
    fixtures = [ 't1_dataverses.json'\
            ,   't1_test_user.json'\
            ,   't1_datasets.json'\
            ,   't1_applicationinfo.json'\
             ]
        
    def setUp(self):
        pass

    def test_form(self):
        """Animals that can speak are correctly identified"""
        for d in Dataset.objects.all():
            print d
        for app in ApplicationInfo.objects.all():
            print app

        dataset = Dataset.objects.get(pk=1)
        sf = DataFile(dataset=dataset\
                        , has_gis_data=False\
                        , dataset_file=SimpleUploadedFile('one_text.txt', 'these are the file contents!')\
                    )
        sf.save()
        
        # Make new token
        app_info = ApplicationInfo.objects.get(pk=1)
        dv_token = DataverseToken.get_new_token(user=sf.dataset.dataverse.owner\
                                            , application=app_info\
                                            , data_file=sf)
        
        metadata_upate_data = { 'dataset_id' : dataset.id\
        , "layer_link": "http://worldmap-test-server.edu/data/geonode:income_in_boston_gui_1_zip_v7e"\
        , "worldmap_username": "bari_user"\
        , "layer_name": "geonode:income_in_boston_gui_1_zip_v7e"\
        , "embed_map_link": "http://worldmap-test-server.edu/maps/embed/?layer=geonode:income_in_boston_gui_1_zip_v7e"\
        }
        
        
        f = GeographicMetadataUpdateForm(metadata_upate_data)
        self.assertEqual(f.is_valid(), True)

        print 'save_metadata', f.save_metadata()
        
        
        
        
        
        