# ShopXO 商城系统 测试实战

## 项目简介
对 ShopXO 商城系统进行功能测试，覆盖登录、搜索、购物车、订单四大模块。

## 测试内容
- **黑盒测试**：等价类、边界值、场景法设计32条用例
- **SQL校验**：使用MySQL模拟数据库，验证数据一致性
- **日志排查**：使用Linux命令（grep、tail）分析模拟日志
- **缺陷管理**：提交并跟踪1个有效缺陷

## 项目结构
```text
shopxo-testing/
├── testcases/
│   ├── 测试用例.md            # 32条测试用例
│   └── Bug列表.md             # 缺陷记录
├── screenshots/
│   ├── BUG001_弹窗显示6件.png
│   ├── BUG001_购物车显示5件.png
│   ├── SQL校验.png
│   └── Linux日志.png
├── 测试报告.md
└── README.md