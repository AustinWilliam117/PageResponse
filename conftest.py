import pytest, os

def get_object_path():
    return os.getcwd().split('utils')[0]

# 清理extract.yaml
@pytest.fixture(scope="class", autouse=True)
def clear_extract_file():
    with open(get_object_path() + "/extract.yaml", 'w', encoding='utf') as f:
        f.truncate()