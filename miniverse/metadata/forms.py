from django import forms

from dataset.models import Dataset

from mock_token.models import DataverseToken
from metadata.models import GeographicMetadata
#token = models.CharField(max_length=255, blank=True, help_text = 'auto-filled on save', db_index=True)

class GeographicMetadataUpdateForm(forms.Form):
    dataset_id = forms.IntegerField()

    layer_name = forms.CharField()
    layer_link = forms.URLField()
    embed_map_link = forms.URLField(required=False)    
    worldmap_username = forms.CharField()

    #bbox_min_lng = forms.DecimalField()
    #bbox_min_lat = forms.DecimalField()
    #bbox_max_lng = forms.DecimalField()
    #bbox_max_lat = forms.DecimalField()


    def save_metadata(self):
        """
        If form is valid, save the metadata
        """
        if not self.is_valid():
            raise Exception('Attempt save metadata on invalid form')
        
        try:    
            dataset = Dataset.objects.get(pk=self.cleaned_data['dataset_id'])
        except Dataset.DoesNotExist:
            return False
        
        try:
            geo_meta = GeographicMetadata.objects.get(dataset=dataset\
                                            , layer_name=self.cleaned_data['layer_name'])
            return True
        except GeographicMetadata.DoesNotExist:
            pass
        
        clean_metadata = self.cleaned_data.copy()    
        
        geo_meta = GeographicMetadata(**clean_metadata)
        geo_meta.dataset = dataset
        geo_meta.save()
        return True
    
    
    """
    def get_dataverse_token(self, token_str):
        print 'token_str', token_str
        try:
            return DataverseToken.objects.get(token=token_str)
        except DataverseToken.DoesNotExist:
            return None

    
    def clean_dv_session_token(self):
        dv_session_token = self.cleaned_data.get('dv_session_token', None)
        
        dv_token_obj = self.get_dataverse_token(dv_session_token)
        if dv_token_obj is None:
            raise forms.ValidationError('Token not found')
            
        if dv_token_obj.has_token_expired():
            raise forms.ValidationError('The token has expired.')

        return dv_session_token
    """