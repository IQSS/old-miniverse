import json


def get_json_err(err_msg):
    d = {}
    d['status'] = 'fail'
    d['message'] = err_msg
    return json.dumps(d)
    
def get_json_success_msg(msg):
    d = { 'status' : 'success'\
        , 'message' : msg\
        }
    return json.dumps(d)
    
def get_json_success(data_dict):
    d = {}
    d['status'] = 'success'
    if type(data_dict) == dict:
        d['data'] = data_dict
    else:
        return get_json_err('Failed to convert data_dict. Found type: %s' % type(data_dict))
    #print d
    try:
        return json.dumps(d)
    except:
        return get_json_err('Failed to convert dict to json')