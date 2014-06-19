from tastypie.resources import ModelResource
from dataset.models import Dataset, DataFile


class DatasetResource(ModelResource):
    class Meta:
        queryset = Dataset.objects.all()
        resource_name = 'dataset'
        
    def dehydrate(self, bundle):
        dataset_obj = bundle.obj
        
        # Include the request IP in the bundle.
        bundle.data['request_ip'] = bundle.request.META.get('REMOTE_ADDR')
        #bundle.data['datafiles'] = DataFile.objects.filter(dataset=self.id)
        bundle.data['datafiles'] = DataFile.objects.filter(dataset=dataset_obj.id).values('dataset_file', 'id', 'file_checksum')
        return bundle
        