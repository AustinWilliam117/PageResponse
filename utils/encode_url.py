import urllib.parse
import json

def encode_string(**kwargs):
    conditions_json = json.dumps(kwargs)
    kwargs["conditions"] = conditions_json
    encoded_params = urllib.parse.urlencode(kwargs)
    return encoded_params
