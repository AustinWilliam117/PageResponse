import requests
import json
import pytest
from utils.connect_redis import return_rediskey
from utils.encode_url import encode_string
from utils.requests_utils import RequestsUtils
from utils.yaml_utils import read_testcase_yaml


class TestRequests:
    #base_url = "http://10.54.0.30:19048/pbot/audio/iod/report/"
    list_url = "call_list"
    count_url = "call_count"
    token_url = return_rediskey("PBOT_PHX_4_3")

    params = {
        "conditions": {
            "call_time_start": "2024-03-15 00:00:00",
            "call_time_end": "2024-03-15 23:59:59",
            "entrance_id": "107"
        },
        "page_size": "20",
        "call_label": "",
        "date_start": "202403",
        "date_end": "202403",
        "flip": "",
        "min_id": "0",
        "max_id": "0",
        "chiasm": "home"
    }


    @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcase/testcase.yaml'))
    def test_call_list(self, caseinfo):
        RequestsUtils("base", "base_url").analysis_yaml(caseinfo)
  #      print(caseinfo)
    #     request_url = TestRequests.list_url + "/?" + encode_string(**TestRequests.params)
    #     Token = TestRequests.token_url
    #     response = RequestsUtils("base", "base_url").send_request(method="GET", request_url=request_url, headers={'Token': Token})
    #     response_time = response.elapsed
    #     print(response_time)
    #     pass
    #
    #
    # def test_call_count(self):
    #     request_url = TestRequests.count_url + "/?" + encode_string(**TestRequests.params)
    #     Token = TestRequests.token_url
    #     response = RequestsUtils("base", "base_url").send_request(method="GET", request_url=request_url, headers={'Token': Token})
    #     response_time = response.elapsed
    #     print(response_time)
    #     pass


if __name__ == '__main__':
    TestRequests.test_call_list()
