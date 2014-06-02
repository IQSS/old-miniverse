import json
from miniverse_util.json_util import get_json_err, get_json_success

class MetadataHelper:
    
    @staticmethod
    def get_singlefile_metadata(single_file, request, as_json=True):
        """
        Given SingleFile object, return metadata in python dict or json format
        """
        if single_file is None or not single_file.__class__.__name__=='SingleFile':
            return None
        
        
        info_dict = { 'dataverse_name': single_file.dataset.dataverse.name\
               , 'dataset_name': single_file.dataset.name\
               ,'has_gis_data' : single_file.has_gis_data\
               ,'dataset_file_location' : request.build_absolute_uri(single_file.dataset_file.url)\
               ,'filename' : single_file.get_basename()\
               ,'filesize' : single_file.dataset_file.size\
               ,'create_time' : str(single_file.create_time)\
               ,'dv_username' : single_file.dataset.dataverse.owner.username
               }
        
        return get_json_success(info_dict)
        #if as_json:
        #    try:
        #        return json.dumps(info_dict)
        #    except:
        #        raise Exception('Failed to convert dict to json')
        #return info_dict