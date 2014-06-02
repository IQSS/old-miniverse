import json
from miniverse_util.json_util import get_json_err, get_json_success
from dataset.models import DataFile

class MetadataHelper:
    
    @staticmethod
    def get_singlefile_metadata(data_file, request, as_json=True):
        """
        Given DataFile object, return metadata in python dict or json format
        """
        if not type(data_file) == DataFile: 
            return get_json_err('Data file not found!')

        if not request:
            return get_json_err('Request object is missing')
            
        info_dict = data_file.get_dv_api_params(request)
        print info_dict
        """
        info_dict = { 'dataverse_name': data_file.dataset.dataverse.name\
               , 'dataset_name': data_file.dataset.name\
               ,'has_gis_data' : data_file.has_gis_data\
               ,'dataset_file_location' : request.build_absolute_uri(data_file.dataset_file.url)\
               ,'filename' : data_file.get_basename()\
               ,'filesize' : data_file.dataset_file.size\
               ,'create_time' : str(data_file.create_time)\
               ,'dv_username' : data_file.dataset.dataverse.owner.username
               }
        """
        return get_json_success(info_dict)
        #if as_json:
        #    try:
        #        return json.dumps(info_dict)
        #    except:
        #        raise Exception('Failed to convert dict to json')
        #return info_dict