import urllib.parse
import json
import os

def encode_string(**kwargs):
    conditions_json = json.dumps(kwargs)
    kwargs["conditions"] = conditions_json
    encoded_params = urllib.parse.urlencode(kwargs)
    return encoded_params

def write_file(file_path, data):
    file_path = os.getcwd() + '/result_files/' + file_path
    print(file_path)
    with open(file_path, 'a+', encoding='utf-8') as f:
        f.write(data + '\n')

if __name__ == '__main__':
    write_file('1.txt', '111')