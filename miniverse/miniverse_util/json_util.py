import json


def get_json_err(err_msg):
    d = {}
    d['status'] = 'fail'
    d['message'] = err_msg
    return json.dumps(d)
    
    
def get_json_success(dinfo):
    d = {}
    d['status'] = 'success'
    print d
    d.update(dinfo)
    try:
        return json.dumps(d)
    except:
        return get_json_err('Failed to convert dict to json')