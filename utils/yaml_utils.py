import os

import yaml

"""
    获取项目路径
    :return 返回utils路径的上一层
"""


def get_object_path():
    return os.getcwd().split('utils')[0]


"""
    用于读取config.yaml文件
    :return config.yaml的base_url
"""


def read_yaml_file(yaml_node_1, yaml_node_2):
    with open(get_object_path() + "/config.yaml", 'r', encoding='utf-8') as f:
        yaml_content = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_content[yaml_node_1][yaml_node_2]


"""
    读取testcase.yaml文件，该文件是测试用例
    :return testcase.yaml的node_name
"""


def read_testcase_yaml(yaml_path):
    with open(get_object_path() + yaml_path, 'r', encoding='utf-8') as f:
        yaml_content = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_content


"""
    写入extract.yaml文件
"""


def write_extract_file(*data):
    with open(get_object_path() + "/extract.yaml", 'a', encoding='utf-8') as f:
        all_data = list(data)
        yaml.dump(all_data, stream=f, allow_unicode=True)


"""
    读取extract.yaml文件
    并返回list中的字典值'first_id'和'last_id'
"""


def read_extract_file():
    with open(get_object_path() + "/extract.yaml", 'r', encoding='utf-8') as f:
        yaml_content = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_content[-1]['first_id'], yaml_content[-1]['last_id']

"""
    清空extract.yaml文件
"""
def clear_extract_file():
    with open(get_object_path() + "/extract.yaml", 'w', encoding='utf') as f:
        f.truncate()


if __name__ == '__main__':
    # print(os.getcwd())
    print(read_yaml_file("base", "base_url"))
