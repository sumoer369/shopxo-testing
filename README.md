# ShopXO 电商系统 功能测试与接口实践

## 项目简介
对 ShopXO 电商系统（线上演示站）进行功能测试，并基于本地 Flask Mock 接口完成接口、性能及自动化的基础实践。

## 测试工具
- **功能与数据校验**：Navicat（MySQL）、Linux命令（grep、tail）
- **接口与抓包**：Fiddler（抓取线上真实请求）、Postman（本地Mock接口验证）
- **性能与自动化**：JMeter（本地Mock接口压测）、Python + Requests + Pytest + YAML

## 测试内容
- **功能测试**：设计32条用例，覆盖登录、搜索、购物车、订单，发现1个数据一致性缺陷。
- **抓包分析**：使用 Fiddler 抓取线上登录请求，成功解码响应数据 `{"msg":"登录成功","code":0}`。
- **接口与性能实操（本地Mock）**：由于演示站接口有防护，本地搭建 Flask Mock 接口。使用 Postman 验证 200/401 场景，使用 JMeter 完成3并发压测（异常率0%）。
- **自动化入门**：基于本地 Mock 接口，编写 Requests + Pytest + YAML 基础脚本，实现数据驱动与断言。

## 项目文件
- `testcases/`：测试用例与 Bug 记录。
- `api_automation/`：接口自动化测试脚本。
- `测试报告.md`：完整的测试报告。
- `测试设计与工具实践记录.md`：各工具的详细实操记录与截图。