import pytest
from utils.requests_utils import RequestsUtils
from utils.yaml_utils import read_testcase_yaml
from utils.encode_url import write_file
from utils.log_manager import my_logger
from utils.yaml_utils import *


class TestRequests:

    @pytest.mark.parametrize('caseinfo', read_testcase_yaml('/testcase/testcase.yaml'))
    def test_page_response(self, caseinfo, clear_extract_file):
        # 如果flip为down，则获取修改min_id、max_id和chiasm的值, min_id为last_id, max_id为'0'，chiasm为''
        try:
            if caseinfo['request']['params']['flip'] == 'down':
                _, last_id = read_extract_file()
                caseinfo['request']['params']['max_id'] = '0'
                caseinfo['request']['params']['min_id'] = last_id
                caseinfo['request']['params']['chiasm'] = ''
                my_logger.logger.debug(f"case flip为down, 已将min_id修改为{last_id}, chiasm修改为''")
            # 如果flip为up，则获取修改min_id、max_id和chiasm的值, max_id为first_id, min_id为'0'，chiasm为''
            if caseinfo['request']['params']['flip'] == 'up':
                first_id, _ = read_extract_file()
                caseinfo['request']['params']['max_id'] = first_id
                caseinfo['request']['params']['min_id'] = '0'
                caseinfo['request']['params']['chiasm'] = ''
                my_logger.logger.debug(f"case flip为up, 已将max_id修改为{first_id}, chiasm修改为''")
        except Exception as e:
            my_logger.logger.error(f"该页面为第一页或最后一页, 错误原因为：{e}")

        response, casename, request_url = RequestsUtils().analysis_yaml(caseinfo)
        response_time = response.elapsed
        my_logger.logger.info(f"测试用例: {casename}, 请求的参数是: {request_url}, 响应的时间是: {response_time}")
        # write_file('result.log', f"测试用例: {casename}, 请求的参数是: {request_url}, 响应的时间是: {response_time}")

        # 如果请求的是call_list记录第一条id和最后一条id存入extract.yaml中，翻页的时候调用id写入min_id/max_id
        if caseinfo['request']['request_url'] == 'call_list':
            # 解析response.text返回的json，提取第一条id和最后一条id
            id_dict = RequestsUtils().analysis_json(response.text)
            my_logger.logger.debug(f"第一个id的值为: {id_dict['first_id']}, 最后一个id的值为: {id_dict['last_id']}")
            # 将first_id和last_id写入extract.yaml中
            write_extract_file(id_dict)


if __name__ == '__main__':
    TestRequests.test_page_response()
