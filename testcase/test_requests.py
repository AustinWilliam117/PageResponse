import pytest
from utils.requests_utils import RequestsUtils
from utils.yaml_utils import read_testcase_yaml
from utils.encode_url import write_file
from utils.log_manager import my_logger

class TestRequests:

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcase/testcase.yaml'))
    def test_page_response(self, caseinfo):
        response, casename, request_url = RequestsUtils().analysis_yaml(caseinfo)
        response_time = response.elapsed
        # print(f"测试用例: {casename}, 请求的参数是: {request_url}, 响应的时间是: {response_time}")
        my_logger.logger.info(f"测试用例: {casename}, 请求的参数是: {request_url}, 响应的时间是: {response_time}")
        # write_file('result.log', f"测试用例: {casename}, 请求的参数是: {request_url}, 响应的时间是: {response_time}")


if __name__ == '__main__':
    TestRequests.test_page_response()
