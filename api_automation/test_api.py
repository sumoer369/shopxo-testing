import requests
import pytest
import yaml
import os


def load_data():
    # 自动获取当前目录的上一级目录，拼出 yaml 文件的绝对路径
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "api_data.yaml")
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.mark.parametrize("case", load_data())
def test_login_api(case):
    # 发送 POST 请求
    response = requests.post(
        "http://127.0.0.1:5000/api/user/login",
        json={"username": case["username"], "password": case["password"]}
    )

    print(f"\n执行用例：{case['case_name']}")
    print(f"实际状态码：{response.status_code}")

    # 断言状态码
    assert response.status_code == case["expected_status"]
    print("测试通过！")


if __name__ == "__main__":
    pytest.main(["-s", "test_api.py"])