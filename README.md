# ShopXO 电商系统 功能测试与接口实践

> ⚠️ **声明**：本项目为个人自主实战项目，非企业实习项目。旨在完整演练软件测试全流程。

## 项目简介
对 ShopXO 电商系统（线上演示环境）进行功能测试，并基于本地 Flask Mock 接口完成接口、性能及自动化的基础实践。由于演示站接口有防护，因此本地搭建 Mock 环境进行深入实操。

## 测试工具
- **功能与数据校验**：Navicat (MySQL)、Linux命令 (grep、tail)
- **接口与抓包**：Fiddler (抓取线上演示环境请求)、Postman (本地Mock接口验证)
- **性能与自动化**：JMeter (本地Mock接口基础并发验证)、Python + Requests + Pytest + YAML

## 测试内容
- **功能测试**：设计32条用例，覆盖登录、搜索、购物车、订单，发现1个数据一致性缺陷（弹窗提示6件，实际5件，已跟踪并验证修复）。
- **抓包分析**：使用Fiddler抓取线上演示环境登录请求，成功解码响应数据 `{"msg":"登录成功","code":0}`。
- **接口与性能实操（本地Mock）**：由于演示站接口有防护，本地搭建Flask Mock接口。使用Postman验证200/401场景，使用JMeter完成3并发基础验证（异常率0%）。
- **自动化入门**：基于本地Mock接口，编写Requests + Pytest + YAML基础脚本，实现数据驱动与断言。

## 项目文件
- `testcases/`：测试用例与Bug记录（含数据一致性缺陷详情及复现步骤）。
- `api_automation/`：接口自动化测试脚本（含 `mock_api.py`、`api_data.yaml`、`test_login.py` 等）。
- `Test_Report.md`：完整的测试报告。
- `Testing_Practice_Record.md`：各工具的详细实操记录与截图（HWUI掉帧、禅道Bug、SQL校验等）。

## 如何运行自动化脚本
```bash
# 安装依赖
pip install requests pytest pyyaml flask

# 启动本地 Mock 接口
python api_automation/mock_api.py

# 执行自动化测试
pytest api_automation/
