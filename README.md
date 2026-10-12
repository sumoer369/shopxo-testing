# ShopXO 电商系统 功能测试与接口实践

> ⚠️ **声明**：本项目为个人自主实战项目，非企业实习项目。旨在完整演练软件测试全流程。

## 项目简介
对 ShopXO 电商系统（线上演示环境）进行功能测试，并基于本地 Flask Mock 接口完成接口、性能及自动化的基础实践。由于演示站接口有防护，因此本地搭建 Mock 环境进行深入实操。

## 测试工具
- **功能与数据校验**：Navicat (MySQL)、Linux命令 (grep、tail)
- **接口与抓包**：F12开发者工具 (抓取线上演示环境请求)、Postman (验证线上接口及本地Mock接口)
- **性能与自动化**：JMeter (本地Mock接口基础并发验证)、Python + Requests + Pytest + YAML

## 测试内容
- **功能测试**：设计32条用例，覆盖登录、搜索、购物车、订单，发现1个数据一致性缺陷（弹窗提示6件，实际5件，已跟踪并验证修复）。
- **抓包与接口测试**：使用F12开发者工具抓取线上演示环境登录请求，分析请求参数；使用Postman复现该线上接口请求，验证异常场景（如验证码过期返回 `{"code": -11}`），并本地Mock验证200/401状态码。
- **性能与自动化实操**：使用JMeter对本地Mock接口进行3并发基础验证（异常率0%）；编写Requests + Pytest + YAML基础脚本，实现数据驱动与断言。
- **数据库与日志**：使用Navicat编写SQL子查询及EXPLAIN验证索引，使用Linux命令（grep、tail）排查日志。

## 项目文件
- `api_automation/`：接口自动化测试脚本（含 `test_api.py`）。
- `mock_api.py`：本地 Flask Mock 接口服务，模拟登录返回 200/401。
- `api_data.yaml`：接口自动化测试的 YAML 数据文件（供 Pytest 实现数据驱动）。
- `testcases/`：测试用例与Bug记录（含数据一致性缺陷详情及复现步骤）。
- `Test_Report.md`：完整的测试报告。
- `Testing_Practice_Record.md`：各工具的详细实操记录与截图（F12抓包、Postman、JMeter、SQL校验等）。

## 项目截图验证（真实操作记录）

**1. 接口与抓包（F12 + Postman）**
<img width="1231" height="1114" alt="postman_api" src="https://github.com/user-attachments/assets/871b468e-b9c7-40bb-a99a-fc7b01db86fe" />
<img width="1097" height="322" alt="f12_capture1" src="https://github.com/user-attachments/assets/143cedae-57ee-4957-bd55-86f3a43e7cc9" />
<img width="1259" height="713" alt="f12_capture" src="https://github.com/user-attachments/assets/e77344e4-d23a-438d-974d-5858579380e5" />


**2. 数据库校验（Navicat SQL）**
<img width="701" height="566" alt="sql_subquery" src="https://github.com/user-attachments/assets/3d245b82-7917-4f8d-80bd-e7191e1f4d14" />
<img width="706" height="550" alt="sql_index" src="https://github.com/user-attachments/assets/eb40364d-60bd-4023-b4ba-4e69abedcc0e" />
<img width="680" height="533" alt="sql_first_step" src="https://github.com/user-attachments/assets/05e6d88b-2d32-4125-8cc1-2f32264aafd1" />


## 如何运行自动化脚本
```bash
# 安装依赖
pip install requests pytest pyyaml flask

# 启动本地 Mock 接口
python api_automation/mock_api.py

# 执行自动化测试
pytest api_automation/
