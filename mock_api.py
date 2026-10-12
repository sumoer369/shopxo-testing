from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟 ShopXO 的登录接口
@app.route('/api/user/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == 'qqqqqq' and password == 'qqqqqq':
        return jsonify({"code": 200, "msg": "登录成功", "token": "mock_token_123"}), 200
    else:
        return jsonify({"code": 401, "msg": "账号或密码错误"}), 401

if __name__ == '__main__':
    app.run(port=5000)