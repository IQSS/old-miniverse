from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from datetime import datetime, timedelta
from django.utils.timezone import utc

from miniverse.util.msg_util import *
from dataverse.models import Dataverse
from dataset.models import SingleFile, Dataset
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
        #self.dataset = Dataset.objects.get(pk=1)
        #self.single_file = SingleFile(dataset=dataset\
        #                    , has_gis_data=False\
        #                    , dataset_file=SimpleUploadedFile('one_text.txt', 'these are the file contents!')\
        #                    )
        #self.single_file.save()
        

    def test_elapsed_times(self):
        """Animals that can speak are correctly identified"""
        for d in Dataset.objects.all():
            print d
        for app in ApplicationInfo.objects.all():
            print app

        dataset = Dataset.objects.get(pk=1)
        sf = SingleFile(dataset=dataset\
                        , has_gis_data=False\
                        , dataset_file=SimpleUploadedFile('one_text.txt', 'these are the file contents!')\
                    )
        sf.save()
        
        # Make new token
        app_info = ApplicationInfo.objects.get(pk=1)
        dv_token = DataverseToken.get_new_token(user=sf.dataset.dataverse.owner\
                                            , application=app_info\
                                            , single_file=sf)
        
        #------------------------------------------
        msgt('token limit for application: [seconds:%s] [minutes:%s]' \
                    % (app_info.time_limit_seconds, app_info.time_limit_minutes))
        msgt('check 1 - fresh token, not elapsed')
        test_time = datetime.utcnow().replace(tzinfo=utc)
        msg('test time %s' % test_time)
        self.assertEqual(dv_token.has_token_expired(test_time), False)

        #------------------------------------------
        msgt('check 2 - fresh token, not elapsed, 20 minutes')
        twent_minutes_elapsed = test_time + timedelta(minutes=+20)
        msg('test time %s' % twent_minutes_elapsed)
        self.assertEqual(dv_token.has_token_expired(twent_minutes_elapsed), False)

        #------------------------------------------
        msgt('check 3 - fresh token, ELAPSED, 30 minutes + some milliseconds')
        thirty_min_elapsed = test_time + timedelta(minutes=+30)
        msg('test time %s' % thirty_min_elapsed)
        self.assertEqual(dv_token.has_token_expired(thirty_min_elapsed), True)
        
        #dv_token.last_refresh_time = twenty_minutes_ago.utcnow().replace(tzinfo=utc)
        
        #print 'Expired?', dv_token.has_token_expired(test_time)
        #print dv_token.get_elapsed_seconds(twenty_minutes_ago)
        #datetime_obj = datetime_obj.utcnow().replace(tzinfo=utc)
        
        #dv_token.last_refresh_time = 
        
        
        
        #self.single_file.save()
        #lion = Animal.objects.get(name="lion")
        #cat = Animal.objects.get(name="cat")
        #self.assertEqual(lion.speak(), 'The lion says "roar"')
        #self.assertEqual(cat.speak(), 'The cat says "meow"')