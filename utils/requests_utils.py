import requests
from utils.yaml_utils import read_yaml_file
import jsonpath
import json
import pytest
from utils.connect_redis import return_rediskey
from utils.yaml_utils import read_testcase_yaml
import urllib.parse

class RequestsUtils:
    session = requests.Session()

    def __init__(self, yaml_node, base_url_name):
        self.base_url = read_yaml_file(yaml_node, base_url_name)
        self.token = return_rediskey("PBOT_PHX_4_3")


    def encode_string(self, **kwargs):
        conditions_json = json.dumps(kwargs)
        kwargs["conditions"] = conditions_json
        encoded_params = urllib.parse.urlencode(kwargs)
        return encoded_params

    def send_request(self, method, request_url, headers, **kwargs):
        # 处理基础路径
        self.base_url = self.base_url + request_url
        # 发送请求
        res = RequestsUtils.session.request(method=method, url=self.base_url, headers=headers, **kwargs)
        return res

    def analysis_yaml(self, caseinfo):
        # 1.testcase.yaml 必须有四个一级关键字：name,base_url,request,validate
        caseinfo_keys = dict(caseinfo).keys()
        if "name" in caseinfo and "base_url" in caseinfo and "request" in caseinfo and "validate" in caseinfo:
            # 2.request一级关键字下必须有：method
            request_keys = dict(caseinfo["request"]).keys()
            if "method" in request_keys and "request_url" in request_keys:
                method = caseinfo["request"]["method"]
                params = caseinfo["request"]["params"]

                print(params)
                print(self.encode_string(**params))
               # request_url = caseinfo["request"]["request_url"] + "/?" + encode_string(**caseinfo["request"]["params"])
               # print(request_url)
        #         # 如果有上传文件的话，取出文件并删除字典中的key
        #         if jsonpath.jsonpath(caseinfo["request"]["files"]):
        #             files = [caseinfo["request"]["files"]]
        #             del caseinfo["request"]["files"]
        #
        #         self.send_request(method=method, request_url=request_url, headers=self.token)
        #     else:
        #         print("request一级关键字下必须有：method")
        # else:
        #     print("testcase.yaml 必须有四个一级关键字：name,base_url,request,validate")

