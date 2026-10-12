# ShopXO 测试设计与工具实践记录

## 一、Postman 接口测试（真实接口与本地 Mock）
使用 Postman 对 ShopXO 线上演示环境接口进行异常场景验证，并对本地 Mock 接口进行 200/401 场景验证。

**ShopXO 线上真实接口测试（验证码过期场景，返回 code: -11）：**
<img width="1231" height="1114" alt="postman_api" src="https://github.com/user-attachments/assets/63602c15-7e05-4cd0-bccb-75cd3ed7cdfc" />


**本地 Mock 接口正常登录（200）：**
![postman_200](https://github.com/user-attachments/assets/c80597d8-9fbe-4498-b0e4-94f311ba6725)

**本地 Mock 接口密码错误（401）：**
![postman_401](https://github.com/user-attachments/assets/2d93501c-64f5-410d-83db-d2835af9ce39)

## 二、F12 抓包分析（线上真实请求）
使用 F12 开发者工具抓取 ShopXO 线上演示站的登录请求，分析前后端交互。

**抓包分析截图：**
![f12_capture](https://github.com/user-attachments/assets/aeb2bd49-a8ee-45e4-92cd-772fd4197053)

## 三、JMeter 性能测试（本地 Mock）
使用 JMeter 对本地 Mock 登录接口进行3并发基础验证，异常率0%。

**压测聚合报告：**
![jmeter_report](https://github.com/user-attachments/assets/241abb3b-4fd2-4cc7-8d6d-bc832ac22469)

## 四、SQL 校验与 Linux 日志排查
使用 Navicat 验证购物车数量数据一致性，编写子查询及验证索引；使用 Linux grep/tail 命令排查错误日志。

![sql_check](https://github.com/user-attachments/assets/049093b1-9701-46dd-b1cc-cad16c9804a9)
![linux_log](https://github.com/user-attachments/assets/c987de96-2e23-40c2-8e95-d377cb9c55bb)

## 五、缺陷记录
**BUG001：添加商品后弹窗提示数量与实际购物车数量不一致**
- **所属模块**：购物车
- **严重程度**：中
- **复现步骤**：登录商城 -> 打开商品详情页 -> 点击加入购物车 -> 观察弹窗提示件数 -> 进入购物车页面观察实际件数。
- **预期结果**：弹窗提示件数与购物车实际件数一致。
- **实际结果**：弹窗显示「购物车共 6 件商品」，实际只有 5 件。
- **缺陷分析**：前端弹窗取数逻辑有误，未与购物车列表实际数据保持一致。
